import re

DOCUMENTS_PATH = '/Users/Shane/Documents/'
path = DOCUMENTS_PATH + 'Vim_Workspace/proxyFiles/'


def readProxies():
   global path
   index = 0
   proxies = []
   with open(path + 'newProxies.txt', 'r', newline='') as newProxies:
      for line in newProxies.readlines():
         print('proxy is ', line)
         if line is None:
            print('line is null\n')
         else:
            # print('index is ', index)
            proxies.append(line.strip('\n'))
            index+=1
   return proxies


# print(readProxies())