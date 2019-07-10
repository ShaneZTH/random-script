import re

input = open('./proxyFiles/input.txt', 'r')
output = open('./proxyFiles/output.txt', 'w')

colon = ':::'

def adder(str):
	print('input is ', str)
	
	ret = re.split(':{3}', str)

	return (ret[0]+colon+ret[1]+colon+colon+ret[2]);

#####

test = 'torres.earlene@gmail.com:::Stevie24082408:::181.214.238.165:65045 '

print('\nret is ', adder(test))


	





