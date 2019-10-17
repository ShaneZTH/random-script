import re
import csv

colon = ':::'
count = 0
gmails = []
passwords = []
# password = 'ShaneGM'

def read_from_csv(inFile):
   with open(inFile) as csvfile:
      readCSV = csv.reader(csvfile, delimiter=',')
      global count
      global gmails
      global passwords
      for row in readCSV:
         if count == 0:
              # first column
              print(count) 
         else:
            gmail = row[0]
            password = row[1]
            print('')
            print(count)
            print(gmail + ' ' + password)
                 

            gmails.append(gmail)
            passwords.append(password)
         
         count += 1

      print()
      print(gmails)
      print(passwords)





path = '../../Vim_Workspace/proxyFiles/'
# output = open(path + 'output.txt', 'a')

inCSV = path + "gm_test.csv"
read_from_csv(inCSV)
print('work is done')

#Account	New Password	Password	Proxy	Recovery Email	
#JuleBedcell743@gmail.com	MDSAMRAT_1	MDSAMRAT_1	181.214.238.244:65045		
#ChantalcMehl743@gmail.com	MDSAMRAT_2	MDSAMRAT_2	181.214.238.245:65045		