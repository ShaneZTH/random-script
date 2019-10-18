import re
from aycd_proxy_formatter import *
from read_from_csv import *
from read_from_txt import *


if __name__ == "__main__":
    read_from_csv(
       "/Users/Shane/Documents/Vim_Workspace/proxyFiles/gm_test.csv")
    g = get_gmails()
    p = get_passwords()
    print('---------------')
    print(g)
    print(p)