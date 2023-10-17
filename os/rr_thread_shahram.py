import threading
import time

def get_time(timei,t):
    while(1):
        timei.append(int(input("zaman enfejar farayand:\n")))


q=int(input("Qatom zamani: \n")) 
time_list=[] 
thread=threading.Thread(target=get_time,args=(time_list,0))
thread.start()
while(1):
    
    for j in range(len(time_list)):
        for k in range(q):
            if(time_list[j]<=0):
                break
            print(f"\nP{j+1}\n")
            time.sleep(1)
            time_list[j]=time_list[j]-1
            


