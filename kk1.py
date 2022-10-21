
import os
import time
import sys


All="""


"""



s=os.system("clear")



os.system("clear")

print('''\033[91m
           __  __           _   _   _            _
          |  \/  | __ _  __| | | | | | __ _  ___| | ___ __
          | |\/| |/ _` |/ _` | | |_| |/ _` |/ __| |/ / '__|
          | |  | | (_| | (_| | |  _  | (_| | (__|   <| |
          |_|  |_|\__,_|\__,_| |_| |_|\__,_|\___|_|\_\_|
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[95m
            +--------------------------------------+
            | This Tool Install All Basic Packages |
            +--------------------------------------+
            | Coded By Mad Hackr | version :  2.0  |
            +--------------------------------------+''')

slowprint(''' \033[93m
[01] python
[02] python2
[03] python-dev
[04] python3
[05] php
[06] java
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] openssl
[13] openssh
[14] wget
[15] clang
[16] nmap
[17] w3m
[18] hydra
[19] ruby
[20] macchanger
[21] host
[22] dnsutils
[23] coreutils ''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [N/Y] : ")
if choice == 'N' : os.system ("exit")
if choice == 'Y' : os.system ("python kk.py")





