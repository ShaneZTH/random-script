import re

colon = ':::'
count = 0
proxy = [50]


def readProxies():
	#if(str == '\n'): return ''

	index = 1
	with open(path + 'newProxies.txt', 'r') as newProxies:
		for line in newProxies.readlines():
			print('proxy is ', line)
			global proxy
			if line is None:
				print('line is null\n')
			else:
				print('index is ', index)
				#proxy[index] = line
				proxy.append(line)
				index+=1
	
	return True;


def changer(str):
    if(str == '\n'): return ''
   
    print('input is ', str)
    global count
    count += 1
    ret = re.split(':{3}', str)

    return (ret[0]+colon+ret[1]+colon+colon+proxy[count+1])

#####

path = '../../Vim_Workspace/proxyFiles/'
#input = open(path + 'input.txt', 'r')
#newProxies = open(path + 'newProxies.txt', 'r');
#output = open(path + 'output.txt', 'a')

if(readProxies()):
	with open(path+'input.txt','r') as inFile, open(path+'output.txt','w') as outFile:
		for line in inFile.readlines():
			print('gmail #', count)
			outFile.write(changer(line))

#print('\nret is ', adder(test))




