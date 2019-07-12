import re

colon = ':::'
count = 0;

def adder(str):
	if(str == '\n'): return ''
	
	print('input is ', str)
	global count
	count += 1
	ret = re.split(':{3}', str)

	return (ret[0]+colon+ret[1]+colon+colon+ret[2]);

#####

path = '../../Vim_Workspace/proxyFiles/'
#input = open(path + 'input.txt', 'r')
#output = open(path + 'output.txt', 'w')

with open(path+'input.txt','r') as inFile, open(path+'output.txt','w') as outFile:
	for line in inFile.readlines():
		print('gmail #', count)
		outFile.write(adder(line))
		


test = 'torres.earlene@gmail.com:::Stevie24082408:::181.214.238.165:65045 '

#print('\nret is ', adder(test))


	





