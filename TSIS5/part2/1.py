import os
f1 = os.getcwd()
f2 = os.getcwd()
ls = ""
while True:
    if os.path.isfile(f1):
        print("it is file")
        print("\nChoose option")
        choose = input()
        
        if choose == "delete":
            os.remove(f1)
            f1 = f1[:f1.find(ls)]
        
        elif choose == "rename":
            name = input()
            os.rename(f1, name)
            f1 = os.path.join(f1[:len(f1) - len(ls)] + name)
        
        elif choose == "add":
            text = input()
            with open (f1, "a") as f:
                f.write(text)
        
        elif choose == "back":
            f1 = f1[::-1]
            if f1[f1.find("\\") + 1] != ":" :
                f1 = f1[f1.find("\\") + 1:]
                f1 = f1[::-1]
                print("done")
    else:
        print("it is directories")
        print("\nChoose option")
        choose = input()
        
        if choose == "rename":
            dir1 = [i for i in os.listdir(f1) if os.path.isdir(i)]
            while True:
                name = input()
                os.rename(f1, name)
                f1 = f1[:len(f1) - f1[::-1].find("\\")]
                f1 = os.fath.join(f1[:f1.find(ls)], name) 

        elif choose == "dirs":
            cnt = 0
            l = []
            for i in os.listdir(f1):
                if os.path.isdir(i):
                    l.append(i)
                    cnt += 1 
            if cnt == 0:
                print('There is no directory here.')
            else:
                print('\nList of directories:')
                print(*l, sep='\n')
                print('Total amount of directories:', cnt)
        
        elif choose == "content":  
            cnt = 0
            l = []
            for i in os.listdir(f1):
                l.append(i)
                cnt += 1
            if cnt == 0:
                print('This directory is empty.')
            else:
                print('\nList of files and directories:')
                print(*l)
                print('Total amount of files and directories:', len(os.listdir(f1)))    
        
        elif choose == "mkfile":
            files = [i for i in os.listdir(f1) if os.path.isfile(i)]
            while True:
                name = input()
                if name in files:
                    print("Error")
                else:
                    break
            os.chdir(f1)
            with open(name, "w") as f:
                f.write("")

        elif choose == "mkdir":
            dirs = [i for i in os.listdir(f1) if os.path.isdir(i)]
            while True:
                name  = input() 
                if name in dirs:
                    print("Error") 
                else:
                    break
            os.chdir(f1)
            os.mkdir(name)

        elif choose == "open":
            os.chdir(f1)
            files = [i for i in os.listdir() if os.path.isfile(i)]
            dirs = [i for i in os.listdir() if os.path.isdir(i)]
            a = 1
            if len(files) == 0 and len(dirs) == 0:
                print("nothing to open")
                a = 0
            while a == 1:
                if (len(files) == 0):
                    print("no files") 
                else:
                    print(*files, sep = "\n")
                if (len(dirs) == 0):
                    print("no directories") 
                else:
                    print(*dirs, sep = "\n")
                name = input()
                if name not in files and name not in dirs:
                    print("Error")
                else:
                    break
            if a == 1:
                if name in files:
                    f1 = os.path.join(f1, name)
                else:
                    f1 = os.path.join(f1, name) 
                ls = name

        elif choose == "back":
            f1 = f1[::-1]
            if f1[f1.find("\\") + 1] != ":" :
                f1 = f1[f1.find("\\") + 1:]
                f1 = f1[::-1]
            else:
                print("Error")

        elif choose == "stop":
            break
        else:
            print("Error") 

