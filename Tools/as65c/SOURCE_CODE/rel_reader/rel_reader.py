########################
#   REL file debugger  #
#       by MrL314      #
#                      #
#     Jun 15, 2021     #
########################


import argparse



FILE = ""







if __name__ == "__main__":


	parser = argparse.ArgumentParser(description="Create human-readable format for the .rel file.")

	parser.add_argument("inputfile", metavar="inputfile", type=str, help="Name of rel file.", default="")
	parser.add_argument("--hideops", action="store_true", help="Hides assumed opcode mnemonics, and instead shows raw byte value. Default shows mnemonics.")
	parser.add_argument("--ws", action="store_true", help="Shows whitespace lines where there is no code in the code output.")
	parser.add_argument("--header", action="store_true", help="Displays only the header data for the rel file.")
	parser.add_argument("--legacy_off", action="store_true", help="Disables concatenation of 0D 0A pairs. Old REL format requires that 0D 0A be shortened to 0A when parsing.")


	args = parser.parse_args()

	HIDE_OPS = False
	if args.hideops:
		HIDE_OPS = True

	CONDENSE = True
	if args.ws:
		CONDENSE = False

	HEADER_ONLY = False
	if args.header:
		HEADER_ONLY = True

	LEGACY_MODE = True
	if args.legacy_off:
		LEGACY_MODE = False

	ARGS = vars(args)



	if ARGS["inputfile"] != "":
		inputfile = ARGS["inputfile"]





	H_DATA = []



	with open(inputfile, "rb") as file:
		H_DATA = file.read()



	'''
	def byte_buffer(buf):
		global BUF_IDX
		# helper to easily access data from a buffer via a generator

		BUF_IDX = 0

		while BUF_IDX < len(buf):
			yield buf[BUF_IDX]
			BUF_IDX += 1
	'''


	def clean_buffer(buf):

		# MAKE SURE THAT THIS IS ***ALWAYS*** THE CASE, AND NOT A
		# SPECIAL CASE WHERE ONLY THE LAST BYTE IS 0D
		out_buf = []

		i = 0
		while i < len(buf):
			if i < len(buf)-1:
				if buf[i] == 0x0D and buf[i+1] == 0x0A:
					i += 1

			out_buf.append(buf[i])
			i += 1

		return out_buf
		


	def get_bytes(buf, n, reverse=False, force_list=False):

		out_buf = []
		out_n = 0
		read_size = 0
		
		while out_n < n and read_size < len(buf):
			if LEGACY_MODE:
				if buf[read_size] == 0x0d:
					if read_size < len(buf)-1 and buf[read_size+1] == 0x0a:
						read_size += 1
			out_buf.append(buf[read_size])
			out_n += 1
			read_size += 1

		if out_n < n:
			raise IndexError("Cannot read past end of buffer.")
		

		if n == 1 and (not force_list):
			out_buf = int(out_buf[0])
		else:
			out_buf = bytes(out_buf)

		return buf[read_size:], out_buf






	def list_to_string(l):
		return " ".join([format(int(h), "02x") for h in list(l)])


	def list_to_text(l):
		return "".join([chr(h) for h in list(l)])


	def list_to_int(l, reverse=False):

		v = 0
		LIST = [b for b in list(l)]

		if not reverse: # as in opposite endian
			LIST = [b for b in reversed(LIST)]

		for i in range(len(LIST)):
			v += LIST[i] * (256**i)

		return v

	#dat = H_DATA[0xd1:]

	SECTIONS = [""]

	GLOBALVARS = ["", ]
	LABELS = {}
	PROC_LABELS = {}


	opcodes = {
		'00':{'name':'BRK', 'size':2},
		'01':{'name':'ORA', 'size':2},
		'02':{'name':'COP', 'size':2},
		'03':{'name':'ORA', 'size':2},
		'04':{'name':'TSB', 'size':2},
		'05':{'name':'ORA', 'size':2},
		'06':{'name':'ASL', 'size':2},
		'07':{'name':'ORA', 'size':2},
		'08':{'name':'PHP', 'size':1},
		'09':{'name':'ORA', 'size':2},
		'0A':{'name':'ASL', 'size':1},
		'0B':{'name':'PHD', 'size':1},
		'0C':{'name':'TSB', 'size':3},
		'0D':{'name':'ORA', 'size':3},
		'0E':{'name':'ASL', 'size':3},
		'0F':{'name':'ORA', 'size':4},
		'10':{'name':'BPL', 'size':2},
		'11':{'name':'ORA', 'size':2},
		'12':{'name':'ORA', 'size':2},
		'13':{'name':'ORA', 'size':2},
		'14':{'name':'TRB', 'size':2},
		'15':{'name':'ORA', 'size':2},
		'16':{'name':'ASL', 'size':2},
		'17':{'name':'ORA', 'size':2},
		'18':{'name':'CLC', 'size':1},
		'19':{'name':'ORA', 'size':3},
		'1A':{'name':'INA', 'size':1},
		'1B':{'name':'TCS', 'size':1},
		'1C':{'name':'TRB', 'size':3},
		'1D':{'name':'ORA', 'size':3},
		'1E':{'name':'ASL', 'size':3},
		'1F':{'name':'ORA', 'size':4},
		'20':{'name':'JSR', 'size':3},
		'21':{'name':'AND', 'size':2},
		'22':{'name':'JSL', 'size':4},
		'23':{'name':'AND', 'size':2},
		'24':{'name':'BIT', 'size':2},
		'25':{'name':'AND', 'size':2},
		'26':{'name':'ROL', 'size':2},
		'27':{'name':'AND', 'size':2},
		'28':{'name':'PLP', 'size':1},
		'29':{'name':'AND', 'size':2},
		'2A':{'name':'ROL', 'size':1},
		'2B':{'name':'PLD', 'size':1},
		'2C':{'name':'BIT', 'size':3},
		'2D':{'name':'AND', 'size':3},
		'2E':{'name':'ROL', 'size':3},
		'2F':{'name':'AND', 'size':4},
		'30':{'name':'BMI', 'size':2},
		'31':{'name':'AND', 'size':2},
		'32':{'name':'AND', 'size':2},
		'33':{'name':'AND', 'size':2},
		'34':{'name':'BIT', 'size':2},
		'35':{'name':'AND', 'size':2},
		'36':{'name':'ROL', 'size':2},
		'37':{'name':'AND', 'size':2},
		'38':{'name':'SEC', 'size':1},
		'39':{'name':'AND', 'size':3},
		'3A':{'name':'DEA', 'size':1},
		'3B':{'name':'TSC', 'size':1},
		'3C':{'name':'BIT', 'size':3},
		'3D':{'name':'AND', 'size':3},
		'3E':{'name':'ROL', 'size':3},
		'3F':{'name':'AND', 'size':4},
		'40':{'name':'RTI', 'size':1},
		'41':{'name':'EOR', 'size':2},
		'42':{'name':'WDM', 'size':2},
		'43':{'name':'EOR', 'size':2},
		'44':{'name':'MVP', 'size':3},
		'45':{'name':'EOR', 'size':2},
		'46':{'name':'LSR', 'size':2},
		'47':{'name':'EOR', 'size':2},
		'48':{'name':'PHA', 'size':1},
		'49':{'name':'EOR', 'size':2},
		'4A':{'name':'LSR', 'size':1},
		'4B':{'name':'PHK', 'size':1},
		'4C':{'name':'JMP', 'size':3},
		'4D':{'name':'EOR', 'size':3},
		'4E':{'name':'LSR', 'size':3},
		'4F':{'name':'EOR', 'size':4},
		'50':{'name':'BVC', 'size':2},
		'51':{'name':'EOR', 'size':2},
		'52':{'name':'EOR', 'size':2},
		'53':{'name':'EOR', 'size':2},
		'54':{'name':'MVN', 'size':3},
		'55':{'name':'EOR', 'size':2},
		'56':{'name':'LSR', 'size':2},
		'57':{'name':'EOR', 'size':2},
		'58':{'name':'CLI', 'size':1},
		'59':{'name':'EOR', 'size':3},
		'5A':{'name':'PHY', 'size':1},
		'5B':{'name':'TCD', 'size':1},
		'5C':{'name':'JML', 'size':4},
		'5D':{'name':'EOR', 'size':3},
		'5E':{'name':'LSR', 'size':3},
		'5F':{'name':'EOR', 'size':4},
		'60':{'name':'RTS', 'size':1},
		'61':{'name':'ADC', 'size':2},
		'62':{'name':'PER', 'size':3},
		'63':{'name':'ADC', 'size':2},
		'64':{'name':'STZ', 'size':2},
		'65':{'name':'ADC', 'size':2},
		'66':{'name':'ROR', 'size':2},
		'67':{'name':'ADC', 'size':2},
		'68':{'name':'PLA', 'size':1},
		'69':{'name':'ADC', 'size':2},
		'6A':{'name':'ROR', 'size':1},
		'6B':{'name':'RTL', 'size':1},
		'6C':{'name':'JMP', 'size':3},
		'6D':{'name':'ADC', 'size':3},
		'6E':{'name':'ROR', 'size':3},
		'6F':{'name':'ADC', 'size':4},
		'70':{'name':'BVS', 'size':2},
		'71':{'name':'ADC', 'size':2},
		'72':{'name':'ADC', 'size':2},
		'73':{'name':'ADC', 'size':2},
		'74':{'name':'STZ', 'size':2},
		'75':{'name':'ADC', 'size':2},
		'76':{'name':'ROR', 'size':2},
		'77':{'name':'ADC', 'size':2},
		'78':{'name':'SEI', 'size':1},
		'79':{'name':'ADC', 'size':3},
		'7A':{'name':'PLY', 'size':1},
		'7B':{'name':'TDC', 'size':1},
		'7C':{'name':'JMP', 'size':3},
		'7D':{'name':'ADC', 'size':3},
		'7E':{'name':'ROR', 'size':3},
		'7F':{'name':'ADC', 'size':4},
		'80':{'name':'BRA', 'size':2},
		'81':{'name':'STA', 'size':2},
		'82':{'name':'BRL', 'size':3},
		'83':{'name':'STA', 'size':2},
		'84':{'name':'STY', 'size':2},
		'85':{'name':'STA', 'size':2},
		'86':{'name':'STX', 'size':2},
		'87':{'name':'STA', 'size':2},
		'88':{'name':'DEY', 'size':1},
		'89':{'name':'BIT', 'size':2},
		'8A':{'name':'TXA', 'size':1},
		'8B':{'name':'PHB', 'size':1},
		'8C':{'name':'STY', 'size':3},
		'8D':{'name':'STA', 'size':3},
		'8E':{'name':'STX', 'size':3},
		'8F':{'name':'STA', 'size':4},
		'90':{'name':'BLT', 'size':2},
		'91':{'name':'STA', 'size':2},
		'92':{'name':'STA', 'size':2},
		'93':{'name':'STA', 'size':2},
		'94':{'name':'STY', 'size':2},
		'95':{'name':'STA', 'size':2},
		'96':{'name':'STX', 'size':2},
		'97':{'name':'STA', 'size':2},
		'98':{'name':'TYA', 'size':1},
		'99':{'name':'STA', 'size':3},
		'9A':{'name':'TXS', 'size':1},
		'9B':{'name':'TXY', 'size':1},
		'9C':{'name':'STZ', 'size':3},
		'9D':{'name':'STA', 'size':3},
		'9E':{'name':'STZ', 'size':3},
		'9F':{'name':'STA', 'size':4},
		'A0':{'name':'LDY', 'size':2},
		'A1':{'name':'LDA', 'size':2},
		'A2':{'name':'LDX', 'size':2},
		'A3':{'name':'LDA', 'size':2},
		'A4':{'name':'LDY', 'size':2},
		'A5':{'name':'LDA', 'size':2},
		'A6':{'name':'LDX', 'size':2},
		'A7':{'name':'LDA', 'size':2},
		'A8':{'name':'TAY', 'size':1},
		'A9':{'name':'LDA', 'size':2},
		'AA':{'name':'TAX', 'size':1},
		'AB':{'name':'PLB', 'size':1},
		'AC':{'name':'LDY', 'size':3},
		'AD':{'name':'LDA', 'size':3},
		'AE':{'name':'LDX', 'size':3},
		'AF':{'name':'LDA', 'size':4},
		'B0':{'name':'BGE', 'size':2},
		'B1':{'name':'LDA', 'size':2},
		'B2':{'name':'LDA', 'size':2},
		'B3':{'name':'LDA', 'size':2},
		'B4':{'name':'LDY', 'size':2},
		'B5':{'name':'LDA', 'size':2},
		'B6':{'name':'LDX', 'size':2},
		'B7':{'name':'LDA', 'size':2},
		'B8':{'name':'CLV', 'size':1},
		'B9':{'name':'LDA', 'size':3},
		'BA':{'name':'TSX', 'size':1},
		'BB':{'name':'TYX', 'size':1},
		'BC':{'name':'LDY', 'size':3},
		'BD':{'name':'LDA', 'size':3},
		'BE':{'name':'LDX', 'size':3},
		'BF':{'name':'LDA', 'size':4},
		'C0':{'name':'CPY', 'size':2},
		'C1':{'name':'CMP', 'size':2},
		'C2':{'name':'REP', 'size':2},
		'C3':{'name':'CMP', 'size':2},
		'C4':{'name':'CPY', 'size':2},
		'C5':{'name':'CMP', 'size':2},
		'C6':{'name':'DEC', 'size':2},
		'C7':{'name':'CMP', 'size':2},
		'C8':{'name':'INY', 'size':1},
		'C9':{'name':'CMP', 'size':2},
		'CA':{'name':'DEX', 'size':1},
		'CB':{'name':'WAI', 'size':1},
		'CC':{'name':'CPY', 'size':3},
		'CD':{'name':'CMP', 'size':3},
		'CE':{'name':'DEC', 'size':3},
		'CF':{'name':'CMP', 'size':4},
		'D0':{'name':'BNE', 'size':2},
		'D1':{'name':'CMP', 'size':2},
		'D2':{'name':'CMP', 'size':2},
		'D3':{'name':'CMP', 'size':2},
		'D4':{'name':'PEI', 'size':2},
		'D5':{'name':'CMP', 'size':2},
		'D6':{'name':'DEC', 'size':2},
		'D7':{'name':'CMP', 'size':2},
		'D8':{'name':'CLD', 'size':1},
		'D9':{'name':'CMP', 'size':3},
		'DA':{'name':'PHX', 'size':1},
		'DB':{'name':'STP', 'size':1},
		'DC':{'name':'JML', 'size':3},
		'DD':{'name':'CMP', 'size':3},
		'DE':{'name':'DEC', 'size':3},
		'DF':{'name':'CMP', 'size':4},
		'E0':{'name':'CPX', 'size':2},
		'E1':{'name':'SBC', 'size':2},
		'E2':{'name':'SEP', 'size':2},
		'E3':{'name':'SBC', 'size':2},
		'E4':{'name':'CPX', 'size':2},
		'E5':{'name':'SBC', 'size':2},
		'E6':{'name':'INC', 'size':2},
		'E7':{'name':'SBC', 'size':2},
		'E8':{'name':'INX', 'size':1},
		'E9':{'name':'SBC', 'size':2},
		'EA':{'name':'NOP', 'size':1},
		'EB':{'name':'XBA', 'size':1},
		'EC':{'name':'CPX', 'size':3},
		'ED':{'name':'SBC', 'size':3},
		'EE':{'name':'INC', 'size':3},
		'EF':{'name':'SBC', 'size':4},
		'F0':{'name':'BEQ', 'size':2},
		'F1':{'name':'SBC', 'size':2},
		'F2':{'name':'SBC', 'size':2},
		'F3':{'name':'SBC', 'size':2},
		'F4':{'name':'PEA', 'size':3},
		'F5':{'name':'SBC', 'size':2},
		'F6':{'name':'INC', 'size':2},
		'F7':{'name':'SBC', 'size':2},
		'F8':{'name':'SED', 'size':1},
		'F9':{'name':'SBC', 'size':3},
		'FA':{'name':'PLX', 'size':1},
		'FB':{'name':'XCE', 'size':1},
		'FC':{'name':'JSR', 'size':3},
		'FD':{'name':'SBC', 'size':3},
		'FE':{'name':'INC', 'size':3},
		'FF':{'name':'SBC', 'size':4}
	}


	def get_section_name(section):
		

		rev = [x for x in reversed(list(section[-2:]))]
		s_num = 0
		for i in range(len(rev)):
			s_num += rev[i] * (256**i)

		try:
			return SECTIONS[s_num]
		except IndexError:
			print(s_num)
			print(section)
			raise IndexError()
			return ""




	def decode_opcode(op):
		return opcodes[format(op, "02x").upper()]['name']



	processor_flags = ["     ", "idx8 ", "idx16", "mem8 ", "mem16"]


	def processor_status_data_decode(dat):
		global PROC_LABELS

		

		while len(dat) > 1 and not (dat[0] == 0 and dat[1] == 0):

			# are the other flags not used??

			# 04 = mem16
			# 03 = mem8
			# 02 = idx16
			# 01 = idx8

			dat, _flag = get_bytes(dat, 2)
			flag = processor_flags[list_to_int(_flag)]
			
			'''
			data1 = dat[2:3]  # 01 to tell what type of data this is?
			section = dat[3:7]
			offset = dat[7:11]
			'''

			dat, data1   = get_bytes(dat, 1, force_list=True)  # 01 to tell what type of data this is?
			dat, section = get_bytes(dat, 4)
			dat, offset  = get_bytes(dat, 4)

			offset_str = list_to_string(offset).replace(" ", "")
			location = get_section_name(section) + "::" + format(int("0x"+offset_str, 16), "06x").upper()

			'''
			if location in PROC_LABELS:
				PROC_LABELS[location].append(flag)
			else:
				PROC_LABELS[location] = [flag]
			'''

			print(flag,  " @  ", get_section_name(section) + "::" + offset_str)
			#print(list_to_string(dat[:11]))
			#dat = dat[11:]

		#print(list_to_string(dat[:2]).replace(" ", ""))
		try:
			if dat[0] == 0 and dat[1] == 0:
				print("; 00 00") #last 2 bytes 00
				dat = dat[2:]
		except:
			pass

		return dat









	def rel_name_decode(dat):
		global GLOBALVARS
		global LABELS
		#print(" ".join([format(x, "02x") for x in dat]))
		#ind = 0


		while len(dat) > 0:

			if dat[0] == 0:
				break

			dat, LEN = get_bytes(dat, 1)
			#ind += 1

			dat, _NAME = get_bytes(dat, LEN, force_list=True)
			NAME = list_to_text(_NAME)
			#ind += LEN

			dat, TYPE = get_bytes(dat, 1)
			#ind += 1

			#print(str(LEN), NAME, str(TYPE))
			#print(str(LEN), NAME)
			#print(NAME)


			if TYPE == 0:
				print(NAME)
				raise KeyError("hit 00 instruction")
				break

			elif TYPE == 1:
				dat, section = get_bytes(dat, 4)
				#ind += 4

				dat, offset = get_bytes(dat, 4)
				#ind += 4

				#print("GLB value:\n   data1: " + list_to_string(data1) + "\n   offset: " + list_to_string(offset).replace(" ","")) 
				print("label ", NAME.ljust(25), "; " + get_section_name(section) + "::" + list_to_string(offset[1:]).replace(" ","").upper())

				label_name = get_section_name(section) + "::" + list_to_string(offset[1:]).replace(" ","").upper()

				if label_name in LABELS:
					LABELS[label_name].append(NAME)
				else:
					LABELS[label_name] = [NAME]


			elif TYPE == 2:
				#exact value

				dat, _txt = get_bytes(dat, 8)

				#print("Exact Value: " + list_to_string(dat[ind:ind+8]).replace(" ", ""))
				print(NAME.ljust(20), "  EQU  ", list_to_string(_txt).replace(" ", "")[-6:])
				#ind += 8


			elif TYPE == 3:
				raise KeyError("hit 03 instruction")
				break

			elif TYPE == 4:
				#external

				#print("External Value   " + list_to_string(dat[ind:ind+8]).replace(" ", ""))
				print("EXT   ", NAME.ljust(20), end="")

				GLOBALVARS.append(NAME)

				dat, _txt = get_bytes(dat, 8)
				print("      ;  data : ", list_to_string(_txt))

				#ind += 8


			elif TYPE == 5:
				#global value

				dat, section = get_bytes(dat, 4)
				#ind += 4

				dat, offset = get_bytes(dat, 4)
				#ind += 4


				#print("GLB value:\n   data1: " + list_to_string(data1) + "\n   offset: " + list_to_string(offset).replace(" ","")) 
				print("GLB   ", NAME.ljust(20), "     ; ", get_section_name(section) + "::" + list_to_string(offset).replace(" ",""))
				GLOBALVARS.append(NAME)

				label_name = get_section_name(section) + "::" + list_to_string(offset).replace(" ","")[-6:].upper()

				if label_name in LABELS:
					LABELS[label_name].append(NAME)
				else:
					LABELS[label_name] = [NAME]




			elif TYPE == 6:
				#global exact

				dat, _txt = get_bytes(dat, 8)

				#print("External Value   " + list_to_string(dat[ind:ind+8]).replace(" ", ""))
				print("GLB   ", NAME.ljust(20), "     ; = ", list_to_string(_txt).replace(" ", "")[-6:])
				GLOBALVARS.append(NAME)
				#ind += 8


			else:
				print(NAME)
				raise KeyError("HIT UNEVALUATED " + format(TYPE, "02x") + " INSTRUCTION")
				break


			#print("")

		if len(dat) > 0:
			if dat[0] == 0:
				print("; 00")
				dat = dat[1:]

		for loc in PROC_LABELS:
			for proc_flag in PROC_LABELS[loc]:
				if loc in LABELS:
					LABELS[loc].append(proc_flag)
				else:
					LABELS[loc] = [proc_flag]

		return dat





	def parse_chunk_size(DATA):
		DATA, size_of_length = get_bytes(DATA, 1)



		if size_of_length & 0x80 != 0:
			section_len = size_of_length & 0x7f
			#print("SL", format(section_len, "02x"))
			return (section_len, DATA)
		else:
			DATA, section_len = get_bytes(DATA, size_of_length, force_list=True)
			section_len = list_to_int(section_len, reverse=False)
			#print("SL", format(section_len, "02x"))

			'''
			for i in range(size_of_length):
				power = (size_of_length-i)-1
				section_len += DATA[i] * (256 ** power)
			'''


			return (section_len, DATA)





	def section_data_decode(dat):
		global SECTIONS
		

		while dat != [] and dat[0] != 0:

			dat, name_len = get_bytes(dat, 1)
			dat, _name = get_bytes(dat, name_len, force_list=True)
			name = list_to_text(_name)
			#dat = dat[name_len+1:]

			dat, TYPE = get_bytes(dat, 1)
			#dat = dat[1:]

			SECTIONS.append(name)


			if TYPE == 1:
				dat, data1    = get_bytes(dat, 8)
				dat, _        = get_bytes(dat, 1)
				dat, _        = get_bytes(dat, 18)
				dat, location = get_bytes(dat, 4)
				dat, offset   = get_bytes(dat, 4)

				#dat = dat[35:]

				#print("sect", name.ljust(15), list_to_string(data1), "  {weird 18 thing}  ; ", "offset ", list_to_string(offset).replace(" ", ""))
				print("sect", name.ljust(15), list_to_string(data1), " ; ", "size =", list_to_string(offset).replace(" ", ""))

			elif TYPE == 2:
				'''
				data1 = dat[:8]
				#data2 = dat[8:33]
				location = dat[29:31]
				offset = dat[32:35]
				'''
				dat, data1    = get_bytes(dat, 8)
				dat, _        = get_bytes(dat, 1)
				dat, _        = get_bytes(dat, 18)
				dat, location = get_bytes(dat, 4)
				dat, offset   = get_bytes(dat, 4)

				#dat = dat[35:]

				print("org ", name.ljust(15), list_to_string(data1), "  addr ", list_to_string(location).replace(" ", "") , "     ; size =", list_to_string(offset).replace(" ", ""))


			elif TYPE == 0:
				#data1 = dat[:8]
				#data2 = dat[8:33]
				#offset = dat[33:35]

				dat, data1    = get_bytes(dat, 8)
				dat, _        = get_bytes(dat, 1)
				dat, _        = get_bytes(dat, 18)
				dat, location = get_bytes(dat, 4)
				dat, offset   = get_bytes(dat, 4)

				#dat = dat[35:]

				#print("comn", name.ljust(15), list_to_string(data1), "  {weird 18 thing}  ; ", "offset ", list_to_string(offset).replace(" ", ""))

				print("comn", name.ljust(15), list_to_string(data1), " ; ", "size =", list_to_string(offset).replace(" ", ""))

			else:
				print(TYPE)
				raise KeyError("type " + str(TYPE) + " encountered")
				break

		if dat[0] == 0:
			print("; 00")
			dat = dat[1:]

		return dat





	LINE_BUFFER = ""

	def ADD_TO_BUFF(s, end=""):
		global LINE_BUFFER
		LINE_BUFFER += s + end


	def decode_code(dat):
		global LABELS
		global LINE_BUFFER
		prev_line = -1
		new_line = True
		is_list = False

		curr_section = None

		byte_count = 0
		p_byte_count = -1
		repeat_labels = 0
		did_start = False
		p_line_num = -1

		NEW_SECTION = True

		spacer = "".ljust(30)

		#dat = clean_buffer(dat)


		


		while dat != [] and not (dat[0] == 0 and dat[1] == 0):

			dat, TYPE = get_bytes(dat, 1)

			if TYPE == 1:
				#section starter
				dat, section = get_bytes(dat, 2)
				section_name = get_section_name(section)

				#dat = dat[3:]
				#ADD_TO_BUFF("SECTION  " + section_name)
				print("\n\nSECTION  " + section_name, end="")
				new_line = True
				is_list = False
				byte_count = 0
				p_byte_count = -1
				did_start = False
				LINE_BUFFER = ""


				NEW_SECTION = True


			elif TYPE == 0x57:
				#new line of code
				dat, LN = get_bytes(dat, 2)
				line_num = list_to_string(LN).replace(" ", "")

				new_line = True
				is_list = False

				t_byte_count = byte_count

				#print(byte_count)
				if not did_start:
					byte_count = 0
					did_start = True


				line_int = int("0x" + line_num, 16)
				
				if byte_count != 0:
					if not CONDENSE:
						if line_int > p_line_num + 1:
							for i in range(p_line_num + 1, line_int):
								print("\n" + format(i, "04x") + ": ", end="")

					if LINE_BUFFER != spacer and LINE_BUFFER != "":
						print("\n" + line_num + ": " + LINE_BUFFER, end="")
					LINE_BUFFER = ""
				#ADD_TO_BUFF("")
				#ADD_TO_BUFF(line_num + ": ", end="")


				not_label = True

				line_name = section_name + "::" + format(byte_count, "06x").upper()
				if p_byte_count != byte_count:
					repeat_labels = 0

				if line_name in LABELS:
					if repeat_labels < len(LABELS[line_name]):
						if byte_count == 0:
							T_BUFF = LINE_BUFFER
							LINE_BUFFER = ""
							ADD_TO_BUFF(LABELS[line_name][repeat_labels].ljust(30) + T_BUFF, end="")
						else:
							ADD_TO_BUFF(LABELS[line_name][repeat_labels].ljust(30), end="")
							not_label = False
					repeat_labels += 1
					


				if byte_count == 0:
					if LINE_BUFFER != spacer and LINE_BUFFER != "":
						print("\n" + line_num + ": " + LINE_BUFFER, end="")
					LINE_BUFFER = ""

				if not_label:
					ADD_TO_BUFF(spacer, end="")


				
				
				#if byte_count == 0:
				#	ADD_TO_BUFF("")
				#	ADD_TO_BUFF(line_num + ": ", end="")

				#if not did_start:


				'''
				if byte_count == 0:
					if did_start:
						dat = dat[3:]
					else:
						did_start = True
				else:
					dat = dat[3:]
				'''

				#dat = dat[2:]

				byte_count = t_byte_count
				

				p_byte_count = byte_count

				p_line_num = line_int

			elif TYPE == 0x10:
				# storage directive

				dat, _size = get_bytes(dat, 1) 
				size = _size & 0x7f

				#dat = dat[2:]

				ADD_TO_BUFF("00 " * size, end="") 
				new_line = False
				is_list = True

				byte_count += size

			elif TYPE == 0x11:
				#finalized bytes

				dat, b1 = get_bytes(dat, 1)

				if b1 & 0x80 > 0:

					num_finalized = b1 & 0x7f

					dat, finalized_bytes = get_bytes(dat, num_finalized, force_list=True)

					max_size = 0

					if finalized_bytes != []:
						opcode = format(finalized_bytes[0], "02x").upper()

						max_size = opcodes[opcode]['size']


					if new_line and len(finalized_bytes) <= max_size+1:
						try:
							opcode = finalized_bytes[0]
						except IndexError:
							print(b1)
							raise IndexError()

						if HIDE_OPS:
							cmd = format(opcode, "02x")
						else:
							cmd = decode_opcode(opcode).lower()

						if len(finalized_bytes) > 1:
							ADD_TO_BUFF(cmd + " " + list_to_string(finalized_bytes[1:]) + " ", end="")
						else:
							ADD_TO_BUFF(cmd + " ", end="")
					else:
						ADD_TO_BUFF(list_to_string(finalized_bytes) + " ", end="")

					#dat = dat[2+num_finalized:]

					byte_count += num_finalized

				else:
					num_len = b1
					dat, _size = get_bytes(dat, num_len, force_list=True)
					size = list_to_int(_size)

					ADD_TO_BUFF("DATA FOR " + format(size, "06x") + " BYTES")

					#dat = dat[2+num_len+size]

					byte_count += size


				new_line = False

				

				is_list = False



			elif TYPE == 0x12:
				#variable data

				dat, variable_type = get_bytes(dat, 1)
				#dat = dat[2:]

				dat, section = get_bytes(dat, 3)
				#dat = dat[3:]
				dat, offset = get_bytes(dat, 4)
				#dat = dat[4:]

				is_external = False

				if is_list:
					ADD_TO_BUFF(", ", end="")


				#if section[0] & 0xf > 0:
				if section[0] & 0x7 > 0:
					#section with offset

					line_name = get_section_name(section) + "::" + list_to_string(offset[1:]).replace(" ", "").upper()
					if line_name in LABELS:
						line_name = LABELS[line_name][0]

					ADD_TO_BUFF(line_name, end="")

				else:
					#external variable
					is_external = True
					ADD_TO_BUFF("EXT::" + GLOBALVARS[list_to_int(section[1:])], end="")



				if section[0] & 0x78 != 0:
					if section[0] & 0x78 == 0x48:
						#bank of variable
						ADD_TO_BUFF(".BANK", end="")
					elif section[0] & 0x78 == 0x60:
						#offset of variable
						ADD_TO_BUFF(".OFFSET", end="")
					elif section[0] & 0x78 == 0x40:
						#high byte of variable
						ADD_TO_BUFF(".HIGH", end="")
					elif section[0] & 0x78 == 0x38:
						#low byte of variable
						ADD_TO_BUFF(".LOW", end="")

					#ADD_TO_BUFF("(BITS ARE " + format(section[0], "02x") + ")", end="")


				if variable_type == 0x11:
					ADD_TO_BUFF(".B ", end="")
					byte_count += 1
				elif variable_type == 0x12:
					ADD_TO_BUFF(".W ", end="")
					byte_count += 2
				elif variable_type == 0x13:
					ADD_TO_BUFF(".L ", end="")
					byte_count += 3
				else:
					ADD_TO_BUFF(" ", end="")
					raise TypeError("HEY WHAT IS THIS? NO LENGTH SPECIFIED")   # REMOVE LATER

				if is_external:
					offs = list_to_int(offset)

					if offs >= 0x80000000: offs = offs - 0x100000000

					if offs != 0:
						if offs < 0:
							ADD_TO_BUFF("- " + hex(offs)[3:] + "h ", end="")
						else:
							ADD_TO_BUFF("+ " + hex(offs)[2:] + "h ", end="")

				is_list = True

			else:
				ADD_TO_BUFF("")
				raise KeyError("Unintentionally hit " + format(TYPE, "02x"))
				break

		if LINE_BUFFER != "":
			print("\n" + format(int(line_num, 16) + 1, "04x") + ": " + LINE_BUFFER, end="")

		if dat[0] == 0 and dat[1] == 0:
			print("\n; 00 00")
			dat = dat[2:]

		return dat




	MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]




	def decode_header(dat):
		#global dat

		#dat = [d for d in data]



		dat, header_bytes = get_bytes(dat, 5)
		print("HEADER: " + list_to_string(header_bytes) + "\n")
		
		'''
		dat, null_bytes = get_bytes(dat, 2)
		print("RELNULL: " + list_to_string(null_bytes))
		'''


		# date of assembly
		#date_bytes = dat[:4]
		dat, YEAR    = get_bytes(dat, 1)
		dat, MONTH   = get_bytes(dat, 1)
		dat, DAY     = get_bytes(dat, 1)
		dat, WEEKDAY = get_bytes(dat, 1)
		try:
			print("ASSEMBLY DATE: " + WEEKDAYS[WEEKDAY] + " " + MONTHS[MONTH] + " " + format(DAY, "02d") + ", XX" + str(YEAR))
		except:
			print("INVALID ASSEMBLY DATE DATA:" + "\n\tWEEKDAY: " + format(WEEKDAY, "02x") + "\n\tMONTH:   " + format(MONTH, "02x") + "\n\tDAY:     " + format(DAY, "02x") + "\n\tYEAR:    " + format(YEAR, "02x"))
		#dat = dat[4:]



		# time of assembly
		#time_bytes = dat[:3]
		dat, HOUR = get_bytes(dat, 1)
		dat, MIN  = get_bytes(dat, 1)
		dat, SEC  = get_bytes(dat, 1)
		print("ASSEMBLY TIME: " + format(HOUR, "02d") + ":" + format(MIN, "02d") + ":" + format(SEC, "02d"))
		#dat = dat[3:]


		

		


		
		# assembler name
		dat, name_len = get_bytes(dat, 1)
		#dat = dat[1:]

		dat, name = get_bytes(dat, name_len)
		print("ASSEMBLER VERSION: " + list_to_text(name))
		dat, sec_size_raw = get_bytes(dat, 8)
		sec_size = list_to_int(sec_size_raw)
		#print(list_to_string(dat[:8]))
		#dat = dat[8:]

		print("")



		while dat[0] != 0:

			dat, name_len = get_bytes(dat, 1)
			#dat = dat[1:]

			dat, name = get_bytes(dat, name_len)
			#dat = dat[name_len:]

			print(list_to_text(name))
			dat, _data = get_bytes(dat, 8)
			print(list_to_string(_data))
			#dat = dat[8:]

			'''
			while dat[0] != 0:
				dat, _ = dat[1:]
			'''
			if dat[0] != 0:
				raise ValueError("NOT ZERO HERE")

			dat = dat[1:]


		'''
		# PROG block
		prog_name_len = dat[0]
		dat = dat[1:]

		prog_name = dat[:prog_name_len]
		dat = dat[prog_name_len:]
		print(list_to_text(prog_name))
		print(list_to_string(dat[:8]))
		dat = dat[8:]
		print("; end PROG block data,", list_to_string(dat[:1]))
		dat = dat[1:]


		# dat block
		data_name_len = dat[0]
		dat = dat[1:]

		data_name = dat[:data_name_len]
		dat = dat[data_name_len:]
		print(list_to_text(data_name))
		print(list_to_string(dat[:8]))
		dat = dat[8:]
		print("; end dat block data,", list_to_string(dat[:1]))
		dat = dat[1:]
		'''


		# end header ??
		if dat[0] == 0:
			dat, _data = get_bytes(dat, 1)
			print(";", list_to_string([_data]))
			#dat = dat[1:]

		else:
			if len(dat) == 1:
				dat, _data = get_bytes(dat, 1)
				print(";", list_to_string([_data]))
				#dat = dat[1:]


			if len(dat) > 0:
				print("; EXTRA DATA, ", list_to_string(dat))

		return dat







	def print_rel_data(DATA):

		#section 0
		print("\n---------HEADER DATA-----------\n")

		#DATA = clean_buffer(DATA)

		DATA = decode_header(DATA)


		#DATA = DATA[0x3e:]

		#return


		#input("")

		if HEADER_ONLY: return


		#section 1
		print("\n---------SECTION DATA-----------\n")
		section_len, DATA = parse_chunk_size(DATA)
		#dat = DATA[:section_len]
		#DATA = DATA[section_len:]

		DATA = section_data_decode(DATA)

		#input("")




		#section 2
		print("\n---------GLOBAL VAR DATA-----------\n")
		section_len, DATA = parse_chunk_size(DATA)
		#dat = DATA[:section_len]
		#DATA = DATA[section_len:]

		DATA = rel_name_decode(DATA)

		#input("")

		#section 3
		print("\n---------PROCESSOR STATUS DATA-----------\n")
		section_len, DATA = parse_chunk_size(DATA)
		#dat = DATA[:section_len]
		#DATA = DATA[section_len:]

		DATA = processor_status_data_decode(DATA)
		
		#input("")




		#section 4 ASM file name
		print("\n---------ASM FILE NAME-----------\n")
		DATA, LEN   = get_bytes(DATA, 1)
		DATA, _NAME = get_bytes(DATA, LEN, force_list=True)
		ASCII_NAME  = list_to_text(_NAME)

		#DATA = DATA[LEN+1:]

		print(ASCII_NAME)


		#input("")

		#section 5
		print("\n---------LOCAL VAR DATA-----------\n")
		section_len, DATA = parse_chunk_size(DATA)
		#dat = DATA[:section_len]
		#DATA = DATA[section_len:]

		DATA = rel_name_decode(DATA)

		#input("")




		#section 6 CODE
		print("\n---------CODE-----------\n")
		

		DATA = decode_code(DATA)



		if len(DATA) > 0:
			print("; LEFTOVER DATA:")
			for x in DATA:
				print(format(x, "02x").upper(), end=" ")



















	#print_rel_data(H_DATA[0xd0:])
	#print_rel_data(H_DATA[0x3e:])
	print("\n\nReading " + inputfile)
	print_rel_data(H_DATA)