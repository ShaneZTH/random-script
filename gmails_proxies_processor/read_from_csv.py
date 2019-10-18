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

def get_gmails():
   return gmails

def get_passwords():
   return passwords

# DOCUMENTS_PATH = '/Users/Shane/Documents/'
# path = DOCUMENTS_PATH + 'Vim_Workspace/proxyFiles/'

# inCSV = path + "gm_test.csv"
# read_from_csv(inCSV)

# # TODO: remove print
# print(get_gmails())
# print(passwords)
# print('work is done')

