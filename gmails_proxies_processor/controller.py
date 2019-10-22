import re
import aycd_proxy_formatter as pf
import read_from_csv as rc
import read_from_txt as rt
 

if __name__ == "__main__":
   rc.read_from_csv(
      "/Users/Shane/Documents/Vim_Workspace/proxyFiles/gm_test.csv")
   pf.set_gmails(rc.get_gmails())
   pf.set_passwords(rc.get_passwords())
   proxies = rt.readProxies('newProxies.txt')
   pf.set_proxies(proxies)

   print('---------------')
   pf.test_print()
   print(rc.testv)
   print(pf.testv)
   
    

