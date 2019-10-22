import re
import aycd_proxy_formatter as pf
import read_from_csv as rc
import read_from_txt as rt
 

if __name__ == "__main__":
   PATH = './testFiles/'
   rc.read_from_csv(PATH + 'gm.csv')
   pf.set_gmails(rc.get_gmails())
   pf.set_passwords(rc.get_passwords())
   proxies = rt.readProxies(PATH + 'newProxies.txt')
   pf.set_proxies(proxies)
   pf.pair_gmails_proxies()


   print('---------------')
   # pf.test_print()

   pf.pair_gmails_proxies()
   print(pf.get_results())

   pf.write_to_files(PATH + 'aycd_input.txt')
   print('---------------')
   print('proxies controller created by @shaneZTH')

   
    

