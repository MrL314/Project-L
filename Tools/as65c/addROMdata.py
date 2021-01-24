




import os, sys
import argparse

os.chdir(os.getcwd())



DATA = []










written_ranges = []


def write_data(file, s_off, d_off, d_size, data):
	global DATA


	print("Writing 0x" + format(d_size, "04x") + " bytes from offset $" + format(s_off, "06x") + " in file " + str(file) + " to offset $" + format(d_off, "06x"))

	

		#print(format(len(data), "04x"))


	for i in range(d_size):
		if d_off + i + 2 > len(DATA):
			while len(DATA) < d_off + i + 1:
				DATA.append(0)
		try:
			DATA[d_off + i] = data[s_off + i]
		except IndexError:
			DATA[d_off + i] = 0



def overwrite_warning(file, start, end, o_start, o_end):
	d_size = (end - start) + 1

	print("[WARNING] Overwriting 0x" + format(d_size, "04x") + " bytes in file " + str(file) + " from $" + format(start, "06x") + " to $" + format(end, "06x"))
	print("          Overwrites data from this inserted block: [$" + format(o_start, "06x") + ", $" + format(o_end, "06x") + "]\n")




inputfile = "LINKED_OUTPUT.rom"
optionsfile = "ROM files.txt"
outputfile = "output.sfc"




parser = argparse.ArgumentParser(description="Add asset data to ROM file, to create .sfc file.")

parser.add_argument("inputfile", metavar="inputfile", type=str, help="Name of code ROM file.", default="")

parser.add_argument("optionsfile", metavar="optionsfile", type=str, help="Name of file containing instructions for asset assembly.", default="")

parser.add_argument("outputfile", metavar="outputfile", type=str, help="Name of output .sfc file to create.", default="")



ARGS = vars(parser.parse_args())



if ARGS["inputfile"] != "":
	inputfile = ARGS["inputfile"]

if ARGS["optionsfile"] != "":
	optionsfile = ARGS["optionsfile"]

if ARGS["outputfile"] != "":
	outputfile = ARGS["outputfile"]
	




with open(inputfile, "rb") as file:
	DATA = list(file.read())



with open(optionsfile, "r") as R:

	lines = []

	for line in R:
		if line.rstrip() != "":
			lines.append(line.split("#")[0])



	for line in lines:
		dat = line.split(",")

		if len(dat) == 4:

			file = dat[0].lstrip().rstrip()

			s_off = int("0x" + dat[1].lstrip().rstrip().replace("0x", ""), 16)
			d_off = int("0x" + dat[2].lstrip().rstrip().replace("0x", ""), 16)
			size  = int("0x" + dat[3].lstrip().rstrip().replace("0x", ""), 16)

			data = []

			with open(file, "rb") as FILE:
				data = FILE.read()

			if s_off + size > len(data):
				size = len(data) - s_off


			write_data(file, s_off, d_off, size, data)

			start = d_off
			end = d_off+size-1

			for o_file, o_start, o_end in written_ranges:

				r_start = min(start, o_start)
				r_end = max(end, o_end)

				if r_start == start and r_end == end:		# overwriting complete block
					overwrite_warning(o_file, o_start, o_end, o_start, o_end)
					break

				elif r_start == o_start and r_end == o_end:	# overwriting inside of block
					overwrite_warning(o_file, start, end, o_start, o_end)
					break

				elif r_start == start and r_end == o_end:	# new block possibly overwrites left side
					if min(end, o_start) == o_start:
						overwrite_warning(o_file, o_start, end, o_start, o_end)	# overwrites part of left side of block
						break
					elif min(end, o_start) == end:
						continue		# new is completely to the left of block, no overwrite 

				elif r_start == o_start and r_end == end:	# new block possibly overwrites right side
					if min(o_end, start) == start:
						overwrite_warning(o_file, start, o_end, o_start, o_end)	# overwrites part of right side of block
						break
					elif min(o_end, start) == o_end:
						continue		# new is completely to the right of block, no overwrite 
				




			written_ranges.append((file, start, end))


			






with open(outputfile, "wb") as OUT:
	OUT.write(bytes(DATA))