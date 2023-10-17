import time
def get_time(timei,t):
    while(t>0):
        timei.append(int(input("zaman enfejar farayand:\n")))
        t-=1

q=int(input("Qatom zamani: \n")) 
n=int(input("tedad farayand: \n")) 
time_list=[]
get_time(time_list,n)
for i in range (max(time_list)):
    for j in range(len(time_list)):
        for k in range(q):
            if(time_list[j]<=0):
                break
            print(f"\nP{j+1}\n")
            time.sleep(1)
            time_list[j]=time_list[j]-1