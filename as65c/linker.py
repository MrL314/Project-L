
import rel_to_class as RTC
import argparse


import os, sys

os.chdir(os.getcwd())

FILES = []


OFFSETS = {}
START_OFFS = {}

#OFFSET_VARS_TEST = "prog=808000"
#OFFSET_VARS_TEST = "prog=0ff70,bank80=08000,objprog=0b900,objdata=18000,objinit=5dc00,bank81=1e000,bank83=3f000,bank84=4d500,bank85=58000,SFXDOS=9c000,editer=88000,comn=0"


def make_offset_vars(VARS):

	global OFFSETS
	global START_OFFS

	vals = VARS.split(",")

	for v in vals:
		var,val = tuple(v.split("="))

		OFFSETS[var.upper()] = int("0x" + val, 16)


	for O in OFFSETS:
		START_OFFS[O] = OFFSETS[O]


# delete later
def get_rel_files(f):
	global FILES
	with open(f, "r") as file:
		for line in file:
			FILES.append(line.replace("\\", "").replace("\n", ""))




def get_file_path(p):
	basepath = os.path.dirname(__file__)
	for f in p.split("/"):
		basepath = os.path.abspath(os.path.join(basepath, f))
	return basepath



inputfile = "linked rel files.txt"
outputfile = "LINKED_OUTPUT.rom"
optionsfile = "rel options.txt"


if __name__ == "__main__":


	parser = argparse.ArgumentParser(description="Link .rel files into a code ROM.")

	parser.add_argument("inputfile", metavar="inputfile", type=str, help="Name of file containing locations of .rel files to link.", default="")

	parser.add_argument("optionsfile", metavar="optionsfile", type=str, help="Name of file containing linker options.", default="")

	parser.add_argument("outputfile", metavar="outputfile", type=str, help="Name of output ROM file to create.", default="")

	parser.add_argument("--rom_size", dest="rom_size", default=512, type=int, help="Set output rom size (in KB)")



	ARGS = vars(parser.parse_args())



	if ARGS["inputfile"] != "":
		inputfile = ARGS["inputfile"]

	if ARGS["optionsfile"] != "":
		optionsfile = ARGS["optionsfile"]

	if ARGS["outputfile"] != "":
		outputfile = ARGS["outputfile"]

	ROM_SIZE = ARGS["rom_size"]

	








	REL_FILES = []
	GLOBALS = {}


	with open(optionsfile, "r") as r:
		lines = []
		for line in r:
			lines.append(line.replace("\n", ""))

		make_offset_vars(lines[0])


	get_rel_files(inputfile)



	for F in FILES:
		with open(get_file_path(F), "rb") as f:
			try:
				RF = RTC.REL_FILE(f.read())
				f = RF._file_name.replace(".asm", "")


				REL_FILES.append((f, RF))
			except Exception as e:
				print(str(e))

				raise Exception("error from " + F) 







	# step 1: section offsets
	for f_name, R in REL_FILES:

		for S in R._sections[1:]:
			NAME = S["sec_group"].replace(f_name, "").upper()
			if NAME != "COMN":
				if S["sec_addr"] == -1:
					if not NAME in OFFSETS:
						OFFSETS[NAME] = 0
					R.get_section(S["sec_name"])["sec_addr"] = OFFSETS[NAME]

					size = 0
					for c in S["code_data"]:
						size += c["size"]

					R.get_section(S["sec_name"])["sec_size"] = size
					OFFSETS[NAME] += size




	# step 2: set global vars
	for f_name, R in REL_FILES:
		for G in R._global_vars[1:]:
			if G["value"] == -1:
				GLOBALS[G["name"]] = R.get_section(G["section"])["sec_addr"] + G["offset"]
			else:
				GLOBALS[G["name"]] = G["value"]



	# step 3: get local offsets and external values 
	for f_name, R in REL_FILES:
		for S in R._sections[1:]:
			ind = 0
			for c in S["code_data"]:

				'''
				if c["type"] == RTC.CODE_TYPE_SECTION_OFFSET:
					try:
						value = R.get_section(c["section"])["sec_addr"] + c["offset"]

						l = 0
						list_data = []
						while l < c["size"]:
							list_data.append(value%256)
							value = value // 256
							l += 1
					except:
						list_data = [0 for b in range(c["size"])]

					R.get_section(S["sec_name"])["code_data"][ind] = {"type": RTC.CODE_TYPE_FINALIZED_BYTES, "size": c["size"], "data": list_data}
				elif c["type"] == RTC.CODE_TYPE_EXTERNAL_VAR:
					try:

						value = GLOBALS[R._all_globals[c["var_num"]]["name"]]

						l = 0
						list_data = []
						while l < c["size"]:
							list_data.append(value%256)
							value = value // 256
							l += 1
					except:
						list_data = [0 for b in range(c["size"])]

					R.get_section(S["sec_name"])["code_data"][ind] = {"type": RTC.CODE_TYPE_FINALIZED_BYTES, "size": c["size"], "data": list_data}

				elif c["type"] == RTC.CODE_TYPE_BANK_VAL:
					value = R.get_section(c["section"])["sec_addr"] + c["offset"]
					

					list_data = [(value & 0xff0000) >> 16]
					

					R.get_section(S["sec_name"])["code_data"][ind] = {"type": RTC.CODE_TYPE_FINALIZED_BYTES, "size": c["size"], "data": list_data}

				elif c["type"] == RTC.CODE_TYPE_OFFSET_VAL:
					value = R.get_section(c["section"])["sec_addr"] + c["offset"]
					

					list_data = [value & 0xff, (value & 0xff00) >> 8]
					

					R.get_section(S["sec_name"])["code_data"][ind] = {"type": RTC.CODE_TYPE_FINALIZED_BYTES, "size": c["size"], "data": list_data}

				'''


				if c["type"] == RTC.CODE_TYPE_VARIABLE:
					try:
						val = 0

						if c["local"]:
							# local variable offset
							val = R.get_section(c["section"])["sec_addr"] + c["offset"]
						else:
							# global variable offset
							val = GLOBALS[R._all_globals[c["var_num"]]["name"]]
							val += c["offset"] # just in case

						list_data = [0, 0, 0]

						if c["addr_type"] == RTC.ADDR_TYPE_NONE or c["addr_type"] == RTC.ADDR_TYPE_OFFSET:
							list_data = [val & 0xff, (val & 0xff00) >> 8, (val & 0xff0000) >> 16]

						elif c["addr_type"] == RTC.ADDR_TYPE_BANK:
							list_data = [(val & 0xff0000) >> 16]

							while len(list_data) < c["size"]:
								list_data.append(0)

						elif c["addr_type"] == RTC.ADDR_TYPE_HIGH:
							list_data = [(val & 0xff00) >> 8]

							while len(list_data) < c["size"]:
								list_data.append(0)

						elif c["addr_type"] == RTC.ADDR_TYPE_LOW:
							list_data = [(val & 0xff)]

							while len(list_data) < c["size"]:
								list_data.append(0)
						

						R.get_section(S["sec_name"])["code_data"][ind] = {"type": RTC.CODE_TYPE_FINALIZED_BYTES, "size": c["size"], "data": list_data[:c["size"]]}
					except Exception as e:
						raise Exception(f_name + "::" + S["sec_name"] + str(c))



				ind += 1



	def fresh_data(ind):
		if ind % 0x40 > 0x1f:
			return 0x00
		else:
			return 0xff



	HEX_DATA = [fresh_data(b) for b in range(0x1000000)]



	with open("out.map", "w") as F:

		f_ind = 0
		for f_name, R in REL_FILES:
			for S in R._sections[1:]:
				if S["sec_size"] > 0:
					ind = S["sec_addr"]

					start_addr = format(ind, "06x")
					end_addr = format(ind + S["sec_size"] - 1, "06x")
					F_NAME = FILES[f_ind]




					sect_name =  S["sec_name"].replace(f_name, "")
					if sect_name == "P": sect_name = "PSEG"
					if sect_name == "D": sect_name = "DSEG"

					try:
						if sect_name[0] == "A" and int(sect_name[1]) > 0: sect_name = "ASEG"
					except:
						pass


					
					F.write(" ".join([F_NAME.ljust(30), f_name.ljust(30), sect_name.ljust(15), start_addr[:2] + ":" + start_addr[2:] + "\t",  end_addr[:2] + ":" + end_addr[2:] + "\t", format(S["sec_size"], "04x")]) + "\n")
					

					try:
						for c in S["code_data"]:
							if c["type"] != RTC.CODE_TYPE_FINALIZED_BYTES:
								raise TypeError("Code did not all convert, in " + f_name + " @ byte " + format(ind, "04x"))

							for b in range(c["size"]):
								offset = ind & 0x0fffff
								for DB in range(len(HEX_DATA) // 0x100000):
									HEX_DATA[offset + 0x100000*DB] = c["data"][b]
								ind += 1
					except Exception as e:
						print(e)

						raise Exception("Section = " + f_name + "::" + S["sec_name"] + ", " + str(c))

			f_ind += 1



	"""
	ROM_DATA = []

	ROM_TYPE = "LoROM"


	if ROM_TYPE == "LoROM":
		'''
		HEADER = HEX_DATA[0xff70:0x10000]
		for i in range(0x10000 - 0xff70):
			HEX_DATA[0x80ff70+i] = HEADER[i]
		'''

		for i in range(0x80000):
			ROM_DATA.append(HEX_DATA[0x800000 + i])

	elif ROM_TYPE == "HiROM":
		pass
	"""






	with open(outputfile, "wb") as outf:
		outf.write(bytes(HEX_DATA[:ROM_SIZE * 0x400]))