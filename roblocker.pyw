import os, time, subprocess

def main():
    targets = ("RobloxPlayerLauncher.exe","RobloxPlayerBeta.exe")
    CREATE_NO_WINDOW = 0x08000000

    while True:
        lines = os.popen("tasklist").readlines()
        for line in lines:
            task = line.split()
            task = task[0] if len(task) > 0 else ""
            if task in targets:
                subprocess.call('taskkill /im %s' % (task,),
                          creationflags=CREATE_NO_WINDOW)
                break
        time.sleep(.25)

if __name__ == "__main__":
    main()

    
