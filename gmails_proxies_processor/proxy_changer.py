import re

colon = ':::'
count = 0
proxy = [50]
gmail = [50]
password = 'ShaneGM'


# read gmails from given txt file
#
def readGmails():
	index = 0
	with open(path + 'gmails.txt', 'r') as gmails:
		for line in gmails.readlines():
			print('gmail is ', line)
			global gmail
			if line is None:
				print('line is null\n')
			else: 
				print('index is ', index)
				gmail.append(line)
				index+=1
	return True


# read proxies from given txt file
#
def readProxies():
	index = 0
	with open(path + 'newProxies.txt', 'r') as newProxies:
		for line in newProxies.readlines():
			print('proxy is ', line)
			global proxy
			if line is None:
				print('line is null\n')
			else:
				print('index is ', index)
				proxy.append(line)
				index+=1
	
	return True


# Update proxies in AYCD's format
#
def updater(str):
    if(str == '\n'): return ''
   
    print('input is ', str)
    global count
    count += 1
    ret = re.split(':{3}', str)

    return (ret[0]+colon+ret[1]+colon+colon+proxy[count+1])

#####
# Main func
####

path = '../../Vim_Workspace/proxyFiles/'
output = open(path + 'output.txt', 'a')

if(readProxies()):
	with open(path+'input.txt','r') as inFile, open(path+'output.txt','w') as outFile:
		for line in inFile.readlines():
			if(line != '\n'):
				print('gmail #', count)
				res = updater(line)
				print('output is ', res)
				print(' ----------- \n')
				outFile.write(res)



# TODO: this file is objective to be deleted



