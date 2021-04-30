import os, time, csv, subprocess, datetime, calendar

def main():
    targets = ("RobloxPlayerLauncher.exe","RobloxPlayerBeta.exe")
    CREATE_NO_WINDOW = 0x08000000
    
    exemptions = readExemptionsFromFile() 
          
    while True:
        lines = os.popen("tasklist").readlines()
        for line in lines:
            task = line.split()
            task = task[0] if len(task) > 0 else ""
            if task in targets:
                today = datetime.datetime.today()
                weekday = today.weekday()
                for e in exemptions:
                    if e[0] == weekday:
                        if e[1] < today.time() < e[2]:
                            break
                else:
                    subprocess.call('taskkill /im %s' % (task,),
                              creationflags=CREATE_NO_WINDOW)
                    break
        time.sleep(.25)

def readExemptionsFromFile():
    path = os.path.dirname(os.path.realpath(__file__))
    fileName = "time_exemptions.csv"
    with open(os.path.join(path, fileName)) as file:
        reader = csv.reader(file, delimiter=",")
        exemptions = []
        for i, row in enumerate(reader):
            if i > 0:
                day = list(calendar.day_name).index(row[0].title())
                start = "0" + row[1] if len(row[1]) == 4 else row[1]
                start = datetime.datetime.strptime(start, "%H:%M").time()
                end = "0" + row[2] if len(row[2]) == 4 else row[2]
                end = datetime.datetime.strptime(end, "%H:%M").time()
                exemptions.append((day, start, end))
    return exemptions

if __name__ == "__main__":
    main()

    
