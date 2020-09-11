
import argparse










FILE = ""







if __name__ == "__main__":


	parser = argparse.ArgumentParser(description="Add asset data to ROM file, to create .sfc file.")

	parser.add_argument("inputfile", metavar="inputfile", type=str, help="Name of code ROM file.", default="")



	ARGS = vars(parser.parse_args())



	if ARGS["inputfile"] != "":
		inputfile = ARGS["inputfile"]





	H_DATA = []



	with open(inputfile, "rb") as file:
		H_DATA = file.read()





	def list_to_string(l):
		return " ".join([format(h, "02x") for h in l])


	def list_to_text(l):
		return "".join([chr(h) for h in l])


	def list_to_int(l, reverse=False):

		v = 0
		LIST = [b for b in l]

		if not reverse: # as in opposite endian
			LIST = [b for b in reversed(LIST)]

		for i in range(len(LIST)):
			v += LIST[i] * (256**i)

		return v


	SECTIONS = [""]

	GLOBALVARS = ["", ]


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

		#return list_to_string(section[-1:]).replace(" ", "")
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


		while not (dat[0] == 0 and dat[1] == 0):

			# 04 = mem16
			# 03 = mem8
			# 02 = idx16
			# 01 = idx8

			flag = processor_flags[dat[0]*256 + dat[1]]

			data1 = dat[2:3]  # 01 to tell what type of data this is?
			section = dat[3:7]
			offset = dat[7:11]


			print(flag,  " @  ", get_section_name(section), ", offset", list_to_string(offset).replace(" ", ""))

			dat = dat[11:]


		print("; end processor data 00 00") #last 2 bytes 00









	def rel_name_decode(dat):
		global GLOBALVARS
		#print(" ".join([format(x, "02x") for x in dat]))
		ind = 0

		while ind < len(dat):

			if dat[ind] == 0:
				break

			LEN = dat[ind]
			ind += 1

			NAME = list_to_text(dat[ind:ind+LEN])
			ind += LEN

			TYPE = dat[ind]
			ind += 1

			#print(str(LEN), NAME, str(TYPE))
			#print(str(LEN), NAME)
			#print(NAME)


			if TYPE == 0:
				print(NAME)
				raise KeyError("hit 00 instruction")
				break

			elif TYPE == 1:
				section = dat[ind:ind+4]
				ind += 4

				offset = dat[ind:ind+4]
				ind += 4

				print("label ", NAME.ljust(25), "; " + get_section_name(section) + "::" + list_to_string(offset[1:]).replace(" ","").upper())


			elif TYPE == 2:
				#exact value

				print(NAME.ljust(20), "  EQU  ", list_to_string(dat[ind:ind+8]).replace(" ", "")[-6:])
				ind += 8


			elif TYPE == 3:
				raise KeyError("hit 03 instruction")
				break

			elif TYPE == 4:
				#external

				print("EXT   ", NAME.ljust(20), end="")

				GLOBALVARS.append(NAME)

				print("     ; data : ", list_to_string(dat[ind:ind+8]))

				ind += 8


			elif TYPE == 5:
				#global value

				section = dat[ind:ind+4]
				ind += 4

				offset = dat[ind:ind+4]
				ind += 4


				print("GLB   ", NAME.ljust(20), "     ; ", get_section_name(section) + "::" + list_to_string(offset).replace(" ",""))
				GLOBALVARS.append(NAME)

			elif TYPE == 6:
				#global exact

				print("GLB   ", NAME, ";  value ", list_to_string(dat[ind:ind+8]).replace(" ", "")[-6:])
				GLOBALVARS.append(NAME)
				ind += 8


			else:
				print(NAME)
				raise KeyError("HIT UNEVALUATED " + format(TYPE, "02x") + " INSTRUCTION")
				break



		if dat[ind] == 0:
			print("; end data, 00")





	def parse_chunk_size(DATA):
		size_of_length = DATA[0]

		if size_of_length & 0x80 != 0:
			section_len = size_of_length & 0x7f
			return (section_len, DATA[1:])
		else:
			section_len = 0

			for i in range(size_of_length):
				power = (size_of_length-i)-1
				section_len += DATA[i+1] * (256 ** power)


			return (section_len, DATA[size_of_length+1:])





	def section_data_decode(dat):
		global SECTIONS
		
		while dat != [] and dat[0] != 0:
			name_len = dat[0]
			name = list_to_text(dat[1:name_len+1])
			dat = dat[name_len+1:]

			TYPE = dat[0]
			dat = dat[1:]

			SECTIONS.append(name)


			if TYPE == 1:
				data1 = dat[:8]
				data2 = dat[8:33]
				offset = dat[33:35]

				dat = dat[35:]
				
				
				print("sect", name.ljust(15), list_to_string(data1), " ; ", "size =", list_to_string(offset).replace(" ", ""))

			elif TYPE == 2:
				data1 = dat[:8]
				#data2 = dat[8:33]
				location = dat[29:31]
				offset = dat[32:35]

				dat = dat[35:]

				print("org ", name.ljust(15), list_to_string(data1), "  addr ", list_to_string(location).replace(" ", "") , "     ; size =", list_to_string(offset).replace(" ", ""))


			elif TYPE == 0:
				data1 = dat[:8]
				data2 = dat[8:33]
				offset = dat[33:35]

				dat = dat[35:]

				

				print("comn", name.ljust(15), list_to_string(data1), " ; ", "offset ", list_to_string(offset).replace(" ", ""))

			else:
				print(TYPE)
				raise KeyError("type " + str(TYPE) + " encountered")
				break

		if dat[0] == 0:
			print("; end of section data, 00")

		







	def decode_code(dat):

		new_line = True
		is_list = False

		curr_section = None

		while dat != [] and dat[0] != 0:



			if dat[0] == 1:
				#section starter
				section = dat[:3]
				section_name = get_section_name(section)

				dat = dat[3:]
				print("\n")
				print("SECTION ", section_name)
				new_line = True
				is_list = False

			elif dat[0] == 0x57:
				#new line of code
				line_num = list_to_string(dat[1:3]).replace(" ", "")
				dat = dat[3:]

				print("")
				print(line_num + ": ", end="")
				new_line = True
				is_list = False

			elif dat[0] == 0x10:
				# storage directive

				size = dat[1] & 0x7f

				dat = dat[2:]

				print("STORAGE FOR " + str(size) + " BYTES", end="") 
				new_line = False
				is_list = True

			elif dat[0] == 0x11:
				#finalized bytes

				if dat[1] & 0x80 > 0:

					num_finalized = dat[1] & 0x7f

					finalized_bytes = dat[2:2+num_finalized]

					max_size = 0

					if finalized_bytes != []:
						opcode = format(finalized_bytes[0], "02x").upper()

						max_size = opcodes[opcode]['size']


					if new_line and len(finalized_bytes) <= max_size+1:
						try:
							opcode = finalized_bytes[0]
						except IndexError:
							print(dat[1])
							raise IndexError()
						cmd = decode_opcode(opcode).lower()

						if len(finalized_bytes) > 1:
							print(cmd + " " + list_to_string(finalized_bytes[1:]) + " ", end="")
						else:
							print(cmd + " ", end="")
					else:
						print(list_to_string(finalized_bytes) + " ", end="")

					dat = dat[2+num_finalized:]

				else:
					num_len = dat[1]
					size = list_to_int(dat[2:2+num_len])

					print("DATA FOR " + format(size, "06x") + " BYTES")

					dat = dat[2+num_len+size]


				new_line = False

				

				is_list = False



			elif dat[0] == 0x12:
				#variable data

				variable_type = dat[1]
				dat = dat[2:]

				section = dat[:3]
				dat = dat[3:]
				offset = dat[:4]
				dat = dat[4:]

				is_external = False

				if is_list:
					print(", ", end="")


				if section[0] & 0xf > 0:
					#section with offset
					print(get_section_name(section) + "::" + list_to_string(offset[1:]).replace(" ", "").upper(), end="")

				else:
					#external variable
					is_external = True
					print("EXT::" + GLOBALVARS[list_to_int(section[1:])], end="")



				if section[0] & 0x78 != 0:
					if section[0] & 0x78 == 0x48:
						#bank of variable
						print(".BANK", end="")
					elif section[0] & 0x78 == 0x60:
						#offset of variable
						print(".OFFSET", end="")
					elif section[0] & 0x78 == 0x40:
						#high byte of variable
						print(".HIGH", end="")
					elif section[0] & 0x78 == 0x38:
						#low byte of variable
						print(".LOW", end="")

					


				if variable_type == 0x11:
					print(".B ", end="")
				elif variable_type == 0x12:
					print(".W ", end="")
				elif variable_type == 0x13:
					print(".L ", end="")
				else:
					print(" ", end="")

				if is_external:
					print("+ " + hex(list_to_int(offset))[2:] + "h ", end="")

				is_list = True

			else:
				print("")
				raise KeyError("Unintentionally hit " + format(dat[0], "02x"))
				break

		if dat[0] == 0:
			print("\n; end of code segment, 00 00")






	def decode_header(dat):


		DATA = [b for b in dat]


		header_bytes = DATA[:3]
		DATA = DATA[3:]

		null_bytes = DATA[:2]
		DATA = DATA[2:]

		# date of compilation
		date_bytes = DATA[:3]
		print("DATE: " + "/".join([format(int(b), "02d") for b in date_bytes]))
		DATA = DATA[3:]

		# time of compilation
		time_bytes = DATA[:3]
		print("TIME: " + ":".join([format(int(b), "02d") for b in time_bytes]))
		DATA = DATA[3:]

		# extra time byte???
		data_byte = DATA[:1]
		
		DATA = DATA[1:]



		
		# compiler name
		name_len = DATA[0]
		DATA = DATA[1:]

		name = DATA[:name_len]
		DATA = DATA[name_len:]
		print(list_to_text(name))
		sec_size = list_to_int(DATA[:8])
		#print(list_to_string(DATA[:8]))
		DATA = DATA[8:]


		while DATA[0] != 0:

			name_len = DATA[0]
			DATA = DATA[1:]

			name = DATA[:name_len]
			DATA = DATA[name_len:]

			print(list_to_text(name))
			print(list_to_string(DATA[:8]))
			DATA = DATA[8:]

			while DATA[0] != 0:
				DATA = DATA[1:]

			DATA = DATA[1:]


		


		# end header ??
		if DATA[0] == 0:
			print("; end header data,", list_to_string(DATA[:1]))
			DATA = DATA[1:]

		else:
			if len(DATA) == 1:
				print("; end header data,", list_to_string(DATA[:1]))
				DATA = DATA[1:]


			if len(DATA) > 0:
				print("  ; EXTRA DATA, ", list_to_string(DATA))

		return DATA







	def print_rel_data(DATA):

		#section 0
		print("\n---------HEADER DATA-----------\n")

		DATA = decode_header(DATA)


		


		input("") # slow down print for ease of viewing




		#section 1
		print("\n---------SECTION DATA-----------\n")
		section_len, DATA = parse_chunk_size(DATA)
		dat = DATA[:section_len]
		DATA = DATA[section_len:]

		section_data_decode(dat)

		input("") # slow down print for ease of viewing




		#section 2
		print("\n---------GLOBAL VAR DATA-----------\n")
		section_len, DATA = parse_chunk_size(DATA)
		dat = DATA[:section_len]
		DATA = DATA[section_len:]

		rel_name_decode(dat)

		input("") # slow down print for ease of viewing

		#section 3
		print("\n---------PROCESSOR STATUS DATA-----------\n")
		section_len, DATA = parse_chunk_size(DATA)
		dat = DATA[:section_len]
		DATA = DATA[section_len:]

		processor_status_data_decode(dat)
		
		input("") # slow down print for ease of viewing




		#section 4 ASM file name
		print("\n---------file name-----------\n")
		LEN = DATA[0]
		ASCII_NAME = list_to_text(DATA[1:1+LEN])
		DATA = DATA[LEN+1:]

		print(ASCII_NAME)


		input("") # slow down print for ease of viewing

		#section 5
		print("\n---------LOCAL VAR DATA-----------\n")
		section_len, DATA = parse_chunk_size(DATA)
		dat = DATA[:section_len]
		DATA = DATA[section_len:]

		rel_name_decode(dat)

		input("") # slow down print for ease of viewing




		#section 6 CODE
		print("\n---------CODE-----------\n")


		decode_code(DATA)










	print_rel_data(H_DATA)
