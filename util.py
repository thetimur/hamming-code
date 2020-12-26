import numpy as np
import random

G = np.array([
	[1, 0, 1, 1],
	[1, 1, 0, 1],
	[0, 0, 0, 1],
	[1, 1, 1, 0],
	[0, 0, 1, 0],
	[0, 1, 0, 0],
	[1, 0, 0, 0]], 
	dtype = np.int)

H = np.array([
	[0, 0, 0, 1, 1, 1, 1],
	[0, 1, 1, 0, 0, 1, 1],
	[1, 0, 1, 0, 1, 0, 1]],
	dtype = np.int)

def decompose_into_F_2(block):
	res = block
	for i in range(block.shape[0]):
		for j in range(block.shape[1]):
			res[i][j] = block[i][j] % 2
	return res

def matrix(string):
	return np.array([
		[int(string[0])],
		[int(string[1])],
		[int(string[2])],
		[int(string[3])]],
		dtype = np.int)

def code_block(block):
	return decompose_into_F_2(G.dot(block))

def get_checksum(block):
	return decompose_into_F_2(H.dot(block))

def get_error_bit(block):
	return block[0][0] * 4 + block[1][0] * 2 + block[2][0]

def complain(string):
	add = (8 - (len(string) % 8)) % 8
	return ('0' * add) + string

def get_block_array(string):
	line = ''.join(complain(format(ord(x), 'b')) for x in string)
	return [line[i:i+4] for i in range(0, len(line), 4)]

def change_random_bit(block):
	block[random.randint(0, 6)][0] ^= 1
	return block

def restore(block, pos):
	if pos > 0:
		block[pos - 1][0] ^= 1
	return block

def get_string_by_block(block):
	return ''.join(str(block[i][0]) for i in [6, 5, 4, 2])

def get_string_by_block_array(blocks_array):
	res = ''.join(get_string_by_block(blocks_array[i]) for i in range(len(blocks_array)))
	parsed = [res[i:i+8] for i in range(0, len(res), 8)]
	return ''.join(str(chr(int('0b' + x, 2))) for x in parsed)