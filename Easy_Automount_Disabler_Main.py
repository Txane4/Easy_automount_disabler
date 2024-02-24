from os import system

def disable():
    system("echo automount scrub > %temp%\EAD_dis.tmp && echo automount disable >> %temp%\EAD_dis.tmp") #Creates tmp fle with diskpart commands
    system("diskpart /s %temp%\EAD_dis.tmp")#Executes previous commands in diskpart
    system("del %temp%\EAD_dis.tmp")#deletes commands
    print("Automontado Disabled")

def enable():
    system("mountvol /e") #Enables automount without using diskpart
    print("Automontado activated")

def main():
    print("Easy Automount Disabler v.1.0")
    print("This software is free to use, but be very carefull about the things you do with it, if you use it, will be on you responsability. Also be carefull around encrypted disks.")
    print("What do you want to do? \n 1) Disable automount \n 2) Enable automount \n exit) To exit")
    question=str(input("Select the option: "))

    while question != '1' or question != '2' or question == exit:
        if question =='2':
            enable()
            break
        elif question =='1' :
            disable()
            break
        elif question == 'exit':
            break
        question=int(input( "Select the option: "))

   
if __name__ == "__main__":
    main()