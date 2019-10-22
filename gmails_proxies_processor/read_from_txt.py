import re

def readProxies(inFile):
   # global path
   # index = 0
   proxies = []
   with open(inFile, 'r', newline='') as newProxies:
      for line in newProxies.readlines():
         # print('proxy is ', line)
         if line is not None:
            # print('line is null\n')
            # print('index is ', index)
            proxies.append(line.strip('\n'))
            # index+=1
   return proxies
