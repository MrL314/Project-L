




import os, sys
import argparse

os.chdir(os.getcwd())



DATA = []













def write_data(file, s_off, d_off, d_size):
	global DATA

	data = []

	print("Writing 0x" + format(d_size, "04x") + " bytes from file " + str(file) + " from offset $" + format(s_off, "06x") + " to offset $" + format(d_off, "06x"))

	with open(file, "rb") as FILE:
		data = FILE.read()

		#print(format(len(data), "04x"))


	for i in range(d_size):
		if d_off + i + 2 > len(DATA):
			while len(DATA) < d_off + i + 1:
				DATA.append(0)
		try:
			DATA[d_off + i] = data[s_off + i]
		except IndexError:
			DATA[d_off + i] = 0





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


			write_data(file, s_off, d_off, size)






with open(outputfile, "wb") as OUT:
	OUT.write(bytes(DATA))