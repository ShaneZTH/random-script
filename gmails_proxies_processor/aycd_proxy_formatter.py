import re

COLON = ':::'
proxies = []
gmails = []
passwords = []
results = []

def set_gmails(g):
   global gmails
   gmails = g

def set_passwords(p):
   global passwords
   gmails = p

def set_proxies(p):
   global proxies
   proxies = p

def pair_gmails_proxies():
   # Check for valid inputs
   if proxies is None or gmails is None:
      print('Error in inputs')
      return

   p_ratio = 1
   # if rotatation is needed  
   if len(proxies) < len(gmails):
      p_ratio = ceil(len(gmails)/len(proxies))
   
   p_count = 1
   p_index = 0
   # pair up
   for i in range(len(gmails)):
      results.append(gmails[i]
                     +COLON+passwords[i]
                     +COLON+COLON
                     +proxies[p_index])
      
      p_count += 1
      if p_count == p_ratio:
         p_count = 1
         p_index += 1

# write results to file
def write_to_files(filename):
   DOCUMENTS_PATH = '/Users/Shane/Documents/'
   path = DOCUMENTS_PATH + 'Vim_Workspace/proxyFiles/'
   file_path = path + filename

   with open(file_path,'w') as out:
      for r in results:
         if (r is not None or r != '\n'):
            out.write(r)
            print("write: " + r)
      out.close      


# testing before import to other files
# TODO: testing with generated data
# if __name__ == "__main__":
#     gmails = ['JoFavcela234@gmail.com ', 
#                'CloraMecsvtas743@gmail.com ']
#     passwords = ['ShaneGM03', 
#                   'ShaneGM04']
#    #  proxies = 

#     set_gmails(gmails)
#     set_passwords(passwords)
#     set_proxies(proxies)
#     pass