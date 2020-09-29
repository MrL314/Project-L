###################################################
#   Helper data and functions for as65c assembler
#      by MrL314
#
#        [ Aug.19, 2020 ]
###################################################









# standard imports
import os.path
from os import path
import hashlib

# local imports
import exceptions
global DATA_TYPES
import datatypes as DATA_TYPES




# global export variables
global BSR_CHAR
global BSL_CHAR
global BANK_CHAR
global OFFSET_CHAR
global HIGH_CHAR
global LOW_CHAR
global ARITHMETIC_SYMBOLS
global OPCODE_SYMBOLS
global REGA_SYMBOLS
global REGX_SYMBOLS
global REGY_SYMBOLS
global REGS_SYMBOLS
global REGISTER_SYMBOLS
global SEPARATOR_SYMBOLS
global TYPE_SYMBOLS
global GLOBAL_SYMBOLS
global EXTERNAL_SYMBOLS
global INCLUDE_SYMBOLS
global SECTION_SYMBOLS
global PSEG_SYMBOLS
global DSEG_SYMBOLS
global COMN_SYMBOLS
global GROUP_SYMBOLS
global ORG_SYMBOLS
global DBANK_SYMBOLS
global DPAGE_SYMBOLS
global END_SYMBOLS
global PROCESSOR_SYMBOLS
global EQU_SYMBOLS
global BYTE_SYMBOLS
global WORD_SYMBOLS
global LONG_SYMBOLS
global DATA_SYMBOLS
global STORAGE_DIRECTIVE_SYMBOLS
global MACRO_SYMBOLS
global END_MACRO_SYMBOLS
global OTHER_SYMBOLS
global PARSING_SYMBOLS
global RESERVED
global RESERVED_FLAT
global NONE






def flatten_list(L):
	"""Turns a nested list into a flattened list, ordered by nesting order."""

	if type(L) in LIST_TYPES:
		# is a list, can be nested or not

		flattened = []

		for elem in L:
			# for each element of the "nested" list...

			for item in flatten_list(elem):
				# (recursive step)
				# ... append the items of the flattened
				# out version of that element to the 
				# final flattened out list 

				flattened.append(item)


		# return the flattened out list
		return flattened


	else:
		# if not a list, but an item...
		# end recursion and return a list containing
		# only that element, for code clarity
		return [L]












# types of list objects
#             tuple     list
LIST_TYPES = (type(()), type([]))





# bit shift operation symbols
BSL_CHAR = "«"   # ALT + 174
BSR_CHAR = "»"   # ALT + 175

# bank/offset symbols
BANK_CHAR = "@"
OFFSET_CHAR = "`"
HIGH_CHAR = "{"
LOW_CHAR = "}"

# symbols used in simple arithmetic in code
ARITHMETIC_SYMBOLS = ("+", "-", "*", "/", "%", BSL_CHAR, BSR_CHAR, "|", "&", "^", "(", ")")

# symbols for separators
SEPARATOR_SYMBOLS = ("(", ")", "[", "]", ",")

# symbols for opcodes
OPCODE_SYMBOLS = ("adc", "ADC", "and", "AND", "asl", "ASL", "bcc", "BCC", "blt", "BLT", "bcs", "BCS", "bge", "BGE", "beq", "BEQ", "bit", "BIT", "bmi", "BMI", "bne", "BNE", "bpl", "BPL", "bra", "BRA", "brk", "BRK", "brl", "BRL", "bvc", "BVC", "bvs", "BVS", "clc", "CLC", "cld", "CLD", "cli", "CLI", "clv", "CLV", "cmp", "CMP", "cop", "COP", "cpx", "CPX", "cpy", "CPY", "dec", "DEC", "dea", "DEA", "dex", "DEX", "dey", "DEY", "eor", "EOR", "inc", "INC", "ina", "INA", "inx", "INX", "iny", "INY", "jmp", "JMP", "jml", "JML", "jsr", "JSR", "jsl", "JSL", "lda", "LDA", "ldx", "LDX", "ldy", "LDY", "lsr", "LSR", "mvn", "MVN", "mvp", "MVP", "nop", "NOP", "ora", "ORA", "pea", "PEA", "pei", "PEI", "per", "PER", "pha", "PHA", "phb", "PHB", "phd", "PHD", "phk", "PHK", "php", "PHP", "phx", "PHX", "phy", "PHY", "pla", "PLA", "plb", "PLB", "pld", "PLD", "plp", "PLP", "plx", "PLX", "ply", "PLY", "rep", "REP", "rol", "ROL", "ror", "ROR", "rti", "RTI", "rtl", "RTL", "rts", "RTS", "sbc", "SBC", "sec", "SEC", "sed", "SED", "sei", "SEI", "sep", "SEP", "sta", "STA", "stp", "STP", "stx", "STX", "sty", "STY", "stz", "STZ", "tax", "TAX", "tay", "TAY", "tcd", "TCD", "tcs", "TCS", "tdc", "TDC", "trb", "TRB", "tsb", "TSB", "tsc", "TSC", "tsx", "TSX", "txa", "TXA", "txs", "TXS", "txy", "TXY", "tya", "TYA", "tyx", "TYX", "wai", "WAI", "wdm", "WDM", "xba", "XBA", "xce", "XCE")
OPCODE_REGS = {
	"adc": "a", 
	"and": "a", 
	"asl": " ", 
	"bcc": " ", 
	"blt": " ", 
	"bcs": " ", 
	"bge": " ", 
	"beq": " ", 
	"bit": "a", 
	"bmi": " ", 
	"bne": " ", 
	"bpl": " ", 
	"bra": " ", 
	"brk": " ", 
	"brl": " ", 
	"bvc": " ", 
	"bvs": " ", 
	"clc": " ", 
	"cld": " ", 
	"cli": " ",
	"clv": " ", 
	"cmp": "a", 
	"cop": "p", 
	"cpx": "x", 
	"cpy": "y", 
	"dec": " ", 
	"dea": " ", 
	"dex": " ", 
	"dey": " ", 
	"eor": "a", 
	"inc": " ", 
	"ina": " ", 
	"inx": " ", 
	"iny": " ", 
	"jmp": " ", 
	"jml": " ", 
	"jsr": " ", 
	"jsl": " ", 
	"lda": "a", 
	"ldx": "x", 
	"ldy": "y", 
	"lsr": " ", 
	"mvn": " ", 
	"mvp": " ", 
	"nop": " ", 
	"ora": "a", 
	"pea": "s", 
	"pei": " ", 
	"per": " ", 
	"pha": " ", 
	"phb": " ", 
	"phd": " ", 
	"phk": " ",
	"php": " ", 
	"phx": " ", 
	"phy": " ", 
	"pla": " ", 
	"plb": " ", 
	"pld": " ", 
	"plp": " ", 
	"plx": " ", 
	"ply": " ", 
	"rep": "p", 
	"rol": " ", 
	"ror": " ", 
	"rti": " ", 
	"rtl": " ", 
	"rts": " ", 
	"sbc": "a", 
	"sec": " ", 
	"sed": " ", 
	"sei": " ", 
	"sep": "p", 
	"sta": " ", 
	"stp": " ", 
	"stx": " ", 
	"sty": " ", 
	"stz": " ", 
	"tax": " ", 
	"tay": " ", 
	"tcd": " ", 
	"tcs": " ", 
	"tdc": " ", 
	"trb": " ", 
	"tsb": " ", 
	"tsc": " ", 
	"tsx": " ", 
	"txa": " ", 
	"txs": " ", 
	"txy": " ", 
	"tya": " ", 
	"tyx": " ", 
	"wai": " ", 
	"wdm": " ", 
	"xba": " ", 
	"xce": " "}

# symbols for accumulator register
REGA_SYMBOLS = ("a", "acc", "accumulator", "accum", "A", "ACC", "ACCUMULATOR", "ACCUM")

# symbols for x register
REGX_SYMBOLS = ("x", "X")

# symbols for y register
REGY_SYMBOLS = ("y", "Y")

# symbols for stack register
REGS_SYMBOLS = ("s", "stack", "S", "STACK")

# symbols for registers
REGISTER_SYMBOLS = flatten_list((REGA_SYMBOLS, REGX_SYMBOLS, REGY_SYMBOLS, REGS_SYMBOLS))



# symbols for data types
TYPE_SYMBOLS = ("<", ">", "!", "#", BANK_CHAR, OFFSET_CHAR, HIGH_CHAR, LOW_CHAR, "$")


# symbols to declare global
GLOBAL_SYMBOLS = ("glb", "global", "glob", "GLB", "GLOBAL", "GLOB")

# symbols to declare external
EXTERNAL_SYMBOLS = ("ext", "external", "extern", "EXT", "EXTERNAL", "EXTERN")

# symbols to declare include file
INCLUDE_SYMBOLS = ("incl", "include", "INCL", "INCLUDE")



# symbols to declare section
SECTION_SYMBOLS = ("sect", "section", "SECT", "SECTION")

# symbols to declare program section
PSEG_SYMBOLS = ("prog", "program", "PROG", "PROGRAM")

# symbols to declare data section
DSEG_SYMBOLS = ("data", "DATA")

# symbols to declare common section
COMN_SYMBOLS = ("comn", "common", "COMN", "COMMON")

# symbols to declare group
GROUP_SYMBOLS = ("group", "grp", "GROUP", "GRP")

# symbols to declare org section
ORG_SYMBOLS = ("org", "ORG")



# symbols to declare data bank
DBANK_SYMBOLS = ("dbank", "databank", "DBANK", "DATABANK")

# symbols to declare data page
DPAGE_SYMBOLS = ("dpage", "datapage", "DPAGE", "DATAPAGE")


# symbols to declare end
END_SYMBOLS = ("end", "END")


# symbols for processor flags
PROCESSOR_SYMBOLS = ("mem8", "mem16", "idx8", "idx16", "MEM8", "MEM16", "IDX8", "IDX16")


# symbols to declare variable value
EQU_SYMBOLS = ("equ", "equal", "equals", "EQU", "EQUAL", "EQUALS")



# symbols to declare byte data
BYTE_SYMBOLS = ("byte", "bytes", "db", "ascii", "BYTE", "BYTES", "DB", "ASCII")

# symbols to declare word data
WORD_SYMBOLS = ("word", "words", "dw", "WORD", "WORDS", "DW")

# symbols to declare long data
LONG_SYMBOLS = ("long", "longs", "dl", "lword", "LONG", "LONGS", "DL", "LWORD")

# symbols to declare data
DATA_SYMBOLS = flatten_list((LONG_SYMBOLS, WORD_SYMBOLS, BYTE_SYMBOLS))



# symbols that affect compilation flow
CONDITIONAL_SYMBOLS = ("if", "endif", "IF", "ENDIF")

# symbols that signal storage directive
STORAGE_DIRECTIVE_SYMBOLS = ("ds", "DS")

# symbols that signal a macro
MACRO_SYMBOLS = ("macro", "MACRO")

# symbols that signal end of macro
END_MACRO_SYMBOLS = ("endm", "ENDM")

# symbols that arent compiled but I don't know what to do with them yet
OTHER_SYMBOLS = ("native", "extend", "list", "nolist", "rel", "NATIVE", "EXTEND", "LIST", "NOLIST", "REL")


# list of symbols used in parsing the data
PARSING_SYMBOLS = flatten_list((SEPARATOR_SYMBOLS, ARITHMETIC_SYMBOLS))

# list of reserved names
RESERVED = (
	REGISTER_SYMBOLS,    # register names
	PARSING_SYMBOLS,     # parsing
	OPCODE_SYMBOLS,      # opcode mnemonics
	TYPE_SYMBOLS,        # data types
	GLOBAL_SYMBOLS, EXTERNAL_SYMBOLS,               # global variables
	INCLUDE_SYMBOLS,                                # included files
	SECTION_SYMBOLS, GROUP_SYMBOLS, ORG_SYMBOLS,    # sections
	PSEG_SYMBOLS, DSEG_SYMBOLS, COMN_SYMBOLS,
	DBANK_SYMBOLS, DPAGE_SYMBOLS,                   # data bank/page
	END_SYMBOLS,               # end of sections
	PROCESSOR_SYMBOLS,         # processor flags
	EQU_SYMBOLS,               # variables
	DATA_SYMBOLS,              # data
	CONDITIONAL_SYMBOLS,       # assembler flow conditionals
	STORAGE_DIRECTIVE_SYMBOLS, # storage directive symbols
	MACRO_SYMBOLS,
	END_MACRO_SYMBOLS,
	OTHER_SYMBOLS              # other
	)



RESERVED_FLAT = flatten_list(RESERVED)


NONE = None












def size_to_bytes(size):
	"""Converts the number for a size into the REL format for size."""

	if size < 0x80:
		# if smaller than 0x80 bytes, set "small size" bit of size
		return [size | 0x80]

	else:
		# if larger than 0x80 bytes, convert into size_len+size format

		num_bytes = 0

		size_bytes = []

		while size != 0:
			size_bytes.append(size % 256)
			size = size // 256
			num_bytes += 1

		if num_bytes > 0x7f:
			raise 




def is_int(v):
	try:
		int(v)
		return True
	except:
		return False

def is_operator(t):
	if t in "+-/*%&|^" + BSL_CHAR + BSR_CHAR:
		return True


def get_precedence(t):

	if t == "*" or t == "/" or t == "%":
		return 6
	elif t == "+" or t == "-":
		return 5
	elif t == BSL_CHAR or t == BSR_CHAR:
		return 4
	elif t == "&": 
		return 3
	elif t == "^":
		return 2
	elif t == "|":
		return 1
	else:
		return 0




def evaluateExpression(EXP):

	E = EXP.replace("[", "(").replace("]", ")")
	E = " ".join(E.split()).split(" ")


	# convert infix to postfix via Shunting-yard algorithm
	output_queue = []
	operator_stack = []

	for tok in E:
		if is_int(tok):
			output_queue.append(tok)

		elif is_operator(tok):
			while operator_stack != []:
				if get_precedence(operator_stack[-1]) >= get_precedence(tok):
					if operator_stack[-1] != "(":
						output_queue.append(operator_stack.pop())
					else:
						break
				else:
					break

			operator_stack.append(tok)

		elif tok == "(":
			operator_stack.append(tok)

		elif tok == ")":
			while operator_stack != [] and operator_stack[-1] != "(":
				output_queue.append(operator_stack.pop())

			if operator_stack != []:
				if operator_stack[-1] == "(":
					operator_stack.pop()

	while operator_stack != []:
		output_queue.append(operator_stack.pop())


	# output_queue is now a postfix expression, which is easier to evaluate

	#print(output_queue, E)

	# postfix evaluation algorithm

	eval_stack = []

	for tok in output_queue:
		if is_int(tok):
			eval_stack.append(int(tok))

		elif is_operator(tok):

			right_arg = eval_stack.pop()
			left_arg = eval_stack.pop()

			if tok == "+":
				val = left_arg + right_arg
			elif tok == "-":
				val = left_arg - right_arg
			elif tok == "*":
				val = left_arg * right_arg
			elif tok == "/":
				val = left_arg // right_arg
			elif tok == "%":
				val = left_arg % right_arg
			elif tok == "&":
				val = left_arg & right_arg
			elif tok == "|":
				val = left_arg | right_arg
			elif tok == "^":
				val = left_arg ^ right_arg
			elif tok == BSL_CHAR:
				val = left_arg << right_arg
			elif tok == BSR_CHAR:
				val = left_arg >> right_arg
			else:
				raise Exception("Bad expression " + " ".join(E))

			eval_stack.append(val)

		else:
			raise Exception("Bad expression " + " ".join(E))


	if len(eval_stack) == 1:
		return eval_stack[0]
	else:
		raise Exception("Error evaluating " + " ".join(E))







def isValue(v):
	"""Returns true if the input is a type of value literal"""
	try:
		# if this works, the value is a decimal number
		int(v)
		return True
	except:
		pass
	
	try:
		if v[-1].lower() == "b":
			# if this works, the value is a binary number
			int("0b" + v[:-1], 2)
			return True
		elif v[-1].lower() == "h":
			# if this works, the value is a hex number
			int("0x" + v[:-1], 16)
			return True
		else:
			# ascii char check
			if v[0] == "\"" and v[-1] == "\"" and len(v) == 3:
				return True
			elif v[0] == "\'" and v[-1] == "\'" and len(v) == 3:
				return True
			else:
				return False
	except:
		pass

	return False



def parseValue(v):
	"""Converts different types of values from string form into in integer""" 

	try:
		# if this works, the value is a decimal number
		return int(v)
	except:
		pass
	
	try:
		if v[-1].lower() == "b":
			# if this works, the value is a binary number
			return int("0b" + v[:-1], 2)
		elif v[-1].lower() == "h":
			# if this works, the value is a hex number
			return int("0x" + v[:-1], 16)
		else:
			# ascii char parse
			if v[0] == "\"" and v[-1] == "\"" and len(v) == 3:
				ch = v[1]
				if ch == "\x01":
					ch = " "
				return ord(ch)
			elif v[0] == "\'" and v[-1] == "\'" and len(v) == 3:
				ch = v[1]
				if ch == "\x01":
					ch = " "
				return ord(ch)
			else:
				raise TypeError("Invalid value type: " + str(type(v)) + " " + str(v))
	except:
		pass

	raise TypeError("Invalid value type: " + str(type(v)) + " " + str(v))



def get_symbols(file):

	lines = []
	with open(file, "r") as f:

		for line in f:
			lines.append(line.replace("\n", ""))


	symbols = []

	for line in lines:
		parsed = line.split("   ")

		try:
			var = parsed[0]
			vartype = parsed[1]
			varval = int(parsed[2])

			symbols.append((var, vartype, varval))
		except IndexError as e:
			raise e



	return symbols




def set_symbols(symbols, file):

	with open(file, "w") as f:

		for var in symbols:
			#        var name             var type                     var value
			f.write(str(var) + "   " + str(symbols[var][0]) + "   " + str(symbols[var][1]) + "\n")




# file hashing for quick assembling

PARSED_HASHES = {}
HASH_SIZE = 32


if not path.exists("fhist.ahist"):
	open("fhist.ahist", "a").close() # will create an empty file if it doesnt exist




with open("fhist.ahist", "rb") as HASH_HISTORY:
	H_BYTES = HASH_HISTORY.read()

	for i in range(len(H_BYTES) // (HASH_SIZE*2)):
		CURR_HASH = H_BYTES[i*(HASH_SIZE*2):(i+1)*(HASH_SIZE*2)]
		file_hash = "".join([format(h, "02x") for h in CURR_HASH[:HASH_SIZE]])
		data_hash = "".join([format(h, "02x") for h in CURR_HASH[HASH_SIZE:]])

		PARSED_HASHES[file_hash] = data_hash






def add_hash(file_hash, data_hash):
	global PARSED_HASHES

	PARSED_HASHES[file_hash.hexdigest()] = data_hash.hexdigest()

	with open("fhist.ahist", "wb") as HASH_HISTORY:
		HASH_DAT = []
		for f in PARSED_HASHES:
			F = f
			D = PARSED_HASHES[f]

			#print(F, D)

			for i in range(HASH_SIZE):
				HASH_DAT.append(int("0x" + F[i*2:(i+1)*2], 16))

			for i in range(HASH_SIZE):
				HASH_DAT.append(int("0x" + D[i*2:(i+1)*2], 16))

			HASH_HISTORY.write(bytes(HASH_DAT))



def get_hash(file_hash):
	global PARSED_HASHES
	
	fh = file_hash.hexdigest() 
	if not (fh in PARSED_HASHES):
		return ""
	else:
		return PARSED_HASHES[fh]






if __name__ == "__main__":
	L = (1, ((2, 3, (4)), 5, (6), 7), 8, (9, (10)))

	print(flatten_list(L))

