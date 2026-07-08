import datetime
import time
import os
import shutil


path = "/home/"
in1 = os.listdir(path)

sel = int(input("Select your choice(1 to move or 2 to delete): "))
if sel == 1:
    p1th = [in1]
    print(p1th)
    select = int(input("Select number (0 - infinity): "))
    targetfiles1 = in1[select]
    shutil.move(f"/home/lonex/Downloads/{targetfiles1}", "/home/lonex/Videos/")
elif sel == 2:
    p2th = [in1]
    print(p2th)
    print("Предупреждение: после выбора файл будет удален!")
    time.sleep(2)
    select = int(input("Select number (0 - infinity): "))

    targetfiles2 = in1[select]
    os.remove(f"/home/lonex/Downloads/{targetfiles2}")
    print("file deleted")
else:
    print("Please select a valid option")
