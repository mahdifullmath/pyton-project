import os
x= input("name the process=")
x="taskkill /IM "+x+".exe /F"
os.system(x)