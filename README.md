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

## Exempting Times
There may be times when you want your students or other computer users to have access to Roblox.  You can whitelist specific times in the time_exemptions.csv file.  The first row denotes the day of the week, the second the start time of the exemption, and the third the end time of the exemption.

Example:

```csv
Monday,8:00,9:00
Friday,14:30,15:00
```

The above will give users access to Roblox only on Monday between 8 and 9 AM and on Friday between 2:30 and 3 PM.  Note that times are provided in the 24 hour format.

## Configuring Roblocker to Run at Startup
* Create a .bat file like the following:

```bat
start "" C:\Users\%USERPROFILE%\<path to roblocker file>\roblocker.exe
```

* Replace &lt;path to roblocker file&gt; with the path on the targeted machine.
    
* Hit Windows Key + R to open the run dialog.
* Type 'shell:startup' and hit enter.
* Drag your newly created .bat file into the opened directory.

Note - with admin privileges you can set Roblocker to run during the startup process of all users.  To achieve this type 'shell:common startup' into the run dialog instead.

## Disclaimer
The authors of this repository are not responsible for any issues or problems that arise while using Roblocker.
 
## License
[MIT](https://choosealicense.com/licenses/mit/)
