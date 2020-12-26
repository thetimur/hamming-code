from util import *

s = 'Hello, world!'

blocks = get_block_array(s)

coded_blocks = [code_block(matrix(x)) for x in blocks]

res = get_string_by_block_array(coded_blocks)


# Меняем бит в каждом блоке с вероятностью 20 процентов.
for beaten_block in range(0, len(coded_blocks)):
	if (random.randint(1, 99) <= 20):
		coded_blocks[beaten_block] = change_random_bit(coded_blocks[beaten_block])

broken_res = get_string_by_block_array(coded_blocks)
print('Input string = ' + res)
print('Broken string = ' + broken_res)

checksum_blocks = [get_checksum(x) for x in coded_blocks]
restored_blocks = [restore(coded_blocks[i], get_error_bit(checksum_blocks[i])) for i in range(len(coded_blocks))]
restored_string = get_string_by_block_array(restored_blocks)

print('Restored string = ' + restored_string)