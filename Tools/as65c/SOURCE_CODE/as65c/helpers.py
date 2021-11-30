###################################################
#   Helper functions for as65c and related tools
#      by MrL314
#
#        [ Aug.28, 2021 ]
###################################################



import os.path
from os import path
import hashlib
import time
import platform


PLTFRM = platform.system()



def get_time():

	'''
	if PLTFRM == "Windows":
		return time.clock()
	elif PLTFRM == "Linux":
		return time.perf_counter()
	elif PLTFRM == "Darwin":
		return time.perf_counter()
	else:
		return time.perf_counter()
	'''
	return time.perf_counter()



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




def flatten_set(L):
	"""Turns a nested list into a flattened set containing all sub elements"""

	return set(flatten_list(L))




# types of list objects
#             tuple     list      set
LIST_TYPES = {type(()), type([]), type(set())}



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

		return size_bytes










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

def load_hashes():
	global PARSED_HASHES

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
		for f in PARSED_HASHES:
			HASH_DAT = []

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
