import datetime
import time
import os
import shutil



in1 = input("select files path:")
in2 = os.listdir(in1)
def print_logo():
    logo = """
                                             #**+===+*##                                        
                                 ##+=-*%#+:... ............:=#                          
                             #+=:..+%%*-......................:+                        
                           #-...:*%%%=...........................-#                     
                          #-...*@%%#+=:....::..:===+==-:...........-                    
                          *:.=%%%%%%#*+-:=##%%%%%%%%%%%%%%#=.........=                  
                          +.+%%%%%%%%%##%%%%%%%%#+-::.....:*%%=........*                
                          +*%%%%%%%%%%%%%%%%*-...............-#%=.... ..=               
                          *%%%%%%%%%%%%%%+:..........  ........=%#:.....:*              
                                       #-. =%%%*-......=*%%%*-....#%:.....+             
                                     #-...=%%%%%%  ...=%%%%%%%+....%%.....+             
                                     ....+%%%%%%%%....+%%%%%%%%....:%+....*             
                                    -. .  №%%%%%%......#%%%%%%+.....*%...:#             
                                    .......-#%%*-.......-#%%*-......+%=--=              
                                    .................. ........  ..*%**##              
                                  #%%-...............................#                  
                             #+++==#%#.........................:.....                 
                             #-:...=%%+.....:--:.. . ..............                    
                             #-.....=#%+..........................:#                    
                             #-.......=%*......................-%##                   
                              *. .......#%+: ..................-#%+-=*#                 
                               #.........:*%%=.............:=#%%=...:+                  
                                 -.....  . .-*%%%*=----=*%%%%+: ....+                   
                                  #:.............-=+++++=-........:*                    
                                    #:...........................=#                     
                                        +:......................-*                      
                                           #=:.............:=+#                         
                                           #**#%%%%%%%%%%%%%%%**#                       
                                             #+-...::::::..:=#                          
                                               #*=:....:=*#                             
                                                   ##

    """
    print(logo)
print_logo()
sel = int(input("Select your choice(1 to move or 2 to delete): "))
if sel == 1:
    sel2 = int(input("Select your choice(1 to move file or 2 to move whole directory with all files): "))
    timee = datetime.datetime.now()
    datee = timee.strftime("%y/%m/%d/ %H:%M")
    print(datee)
    if sel2 == 1:
        p1th = [in2]
        print(p1th)
        select = int(input("Select number (0 - infinity): "))
        targetfiles1 = in2[select]
        dst = input("Enter destination path: ")
        src = in1
        final_destination = os.path.join(dst, targetfiles1)
        shutil.move(os.path.join(src, targetfiles1), final_destination)
        print("file moved")
    elif sel2 == 2:
        directory = input("please input the directory path:")
        des = input("please input the destination path:")
        shutil.copytree(directory,des)
        shutil.rmtree(directory)
    else:
        print("Please select a valid option")
elif sel == 2:
    timee2 = datetime.datetime.now()
    datee2 = timee2.strftime("%y/%m/%d/ %H:%M")
    print(datee2)
    p2th = [in2]
    print(p2th)
    time.sleep(1)
    target11111 = input("please input the file path:")
    check = input("Are you sure? y/n")
    if check == "y":
        os.remove(target11111)
        print("file deleted")
    elif check == "n":
        print("Canceled")
    else:
        print("Please select a valid option")
else:
    print("Please select a valid option")
