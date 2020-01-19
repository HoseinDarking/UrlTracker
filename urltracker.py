import os

import urllib

import pyfiglet

from colorama import *

from bs4 import *

os.system("clear")

ascii_banner = pyfiglet.figlet_format("Url Tracker")

print Fore.RED + ascii_banner

print Fore.BLUE+ "Code By @Hosein_Darking"

url = raw_input (Fore.GREEN + "\nEnter The URL --> : ")

t = urllib.urlopen (url).read ()

s = BeautifulSoup (t,"html.parser")

for i in s.find_all ("a"):

    link = i.get ("href")

    print link
    print ("=======================================")
