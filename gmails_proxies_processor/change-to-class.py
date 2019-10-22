import re
import csv

class csv_reader():
   def __init__(self): 
      self.colon = ':::'
      self.count = 0
      self.gmails = []
      self.passwords = []
      self.testv = 'b'

   def read_from_csv(self,inFile):
      with open(inFile) as csvfile:
         readCSV = csv.reader(csvfile, delimiter=',')
         
         for row in readCSV:
            if count == 0:
               # first column
               print(count) 
            else:
               self.gmail = row[0]
               self.password = row[1]
               print('')
               print(count)
               print(gmail + ' ' + password)
                  
               self.gmails.append(gmail)
               self.passwords.append(password)
            count += 1

   def get_gmails(self):
      return self.gmails

   def get_passwords(self):
      return self.passwords

if __name__ == "__main__":
      cr = csv_reader()
      print(cr.gmails)
   # DOCUMENTS_PATH = '/Users/Shane/Documents/'
   # path = DOCUMENTS_PATH + 'Vim_Workspace/proxyFiles/'

   # inCSV = path + "gm_test.csv"
   # read_from_csv(inCSV)

   # # TODO: remove print
   # print(get_gmails())
   # print(passwords)
   # print('work is done')

