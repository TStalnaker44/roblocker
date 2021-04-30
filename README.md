# Roblocker for Windows
 A simple python program that can be used in an academic setting to prevent students from playing Roblox.  The program silently listens in the background waiting for a Roblox window to be opened.  Once such a window is opened, the process is killed.  The user of the program can choose to exempt certain times from being effected by Roblocker.
 
 ## Installation Options
 Downloads for the python source code and a prepackaged executable are available in labeled folders.  
 ## Usage
 
 IMPORTANT - This version of Roblocker only works on Windows machines
 
 ### Python File
 
 #### Option 1 - Point and Click
 Double-click on the script to start it.
 
 #### Option 2 - Command Line
 Open a CMD window and navigate to the directory containing roblocker.pyw
 
 ```bash
 py roblocker.pyw
 ```
 
 ### Executable
 
 IMPORTANT - Do not separate the .exe file from the other files in the executable folder
 
 #### Option 1 - Point and Click
 Open the downloaded folder. Find the executable named roblocker.exe.  Double-click the executable.
 
 #### Option 2 - Command Line
Open a CMD window and navigate to the directory containing the executable files

```bash
roblocker.exe
```

## Stopping the Roblocker
If you want to stop the Roblocker, open a CMD window and type the following:

```bash
taskkill /im roblocker.exe /F
```

The process will end and the user will be able to start Roblox normally.

## Configuring Roblocker to Run at Startup
* Create a .bat file like the following:

```bat
start "" C:\Users\%USERPROFILE%\<path to roblocker file>\roblocker.exe
```

* Replace <path to roblocker file> with the path on the targeted machine.
    
* Hit Windows Key + R to open the run dialog
* Type 'shell:startup' and hit enter
* Drag your newly created .bat file into the opened directory

Note - with admin privileges you can set Roblocker to run during the startup process of all users.  To achieve this type 'shell:common startup' into the run dialog instead

## Disclaimer
The authors of this repository are not responsible for any issues or problems that arise while using Roblocker
 
## License
[MIT](https://choosealicense.com/licenses/mit/)
