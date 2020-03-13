from os import listdir
from os.path import isfile, join

mypath = "/media/eshan/OS/Users/Eshan/Documents/Kitti/data/2011_09_26/2011_09_26_drive_0001_sync/velodyne_points/data"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
items = len(onlyfiles)
traincount = int(items*(60/100))
valcount = int(items*(20/100))
testcount = items - traincount - valcount
trainitems = onlyfiles[:traincount]
valitems = onlyfiles[traincount:traincount+valcount]
testitems = onlyfiles[traincount+valcount:]
f= open("train.txt","w+")
for i in trainitems:
    f.write(f"{i.replace('.bin', '')}\n")
f.close()
f= open("val.txt","w+")
for i in valitems:
    f.write(f"{i.replace('.bin', '')}\n")
f.close()
f= open("test.txt","w+")
for i in testitems:
    f.write(f"{i.replace('.bin', '')}\n")
f.close()