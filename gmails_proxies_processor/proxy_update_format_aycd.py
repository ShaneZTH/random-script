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

DOCUMENTS_PATH = '/Users/Shane/Documents/'
path = DOCUMENTS_PATH + 'Vim_Workspace/proxyFiles/'
#input = open(path + 'input.txt', 'r')
#output = open(path + 'output.txt', 'w')

with open(path+'input.txt','r') as inFile, open(path+'output.txt','w') as outFile:
	for line in inFile.readlines():
		print('gmail #', count)
		outFile.write(adder(line))
		
#print('\nret is ', adder(test))
