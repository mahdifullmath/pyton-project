import threading
import time
import matplotlib.pyplot as plt

def get_time(time_list,q):
    q[0]=int(input("Qatom zamani: \n"))
    
    if (q[0]==-10):
        return
    thread=threading.Thread(target=rr)
    thread.start() 
    while(1):
        time_list.append(int(input("zaman enfejar farayand:\n")))
        burst_time.append(time_list[-1])
        arival_time.append(t[0])
        end_time.append(0)
        rt.append(0)
        
        if(time_list[-1]==-10):
            break
    qwt=[]
    qwt.append(q[0])
    qwt.append(sum(rt)/len(rt)-sum(burst_time)/len(burst_time))
    awt.append(qwt) 
    burst_time.clear()
    end_time.clear()
    process_namelist.clear()
    arival_time.clear()
    rt.clear()
    time_list.clear()
    get_time(time_list,q)

def rr():
    while(1):
        for j in range(0,len(time_list)):
            for k in range(q[0]):
                if(time_list[j]<=0):
                    break
                print(f"\nP{j+1}\n")
                time.sleep(1)
                time_list[j]=time_list[j]-1
                t[0]+=1
            end_time[j]=t[0]
            rt[j]=end_time[j]-arival_time[j]
            if (max(time_list)==0):
                return

def show_plot():
    x=[]
    y=[]
    for i in awt:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x,y,'g')
    plt.show()
    return 
t=[0]
burst_time=[]
end_time=[]
process_namelist=[]
time_list=[]
arival_time=[]
awt=[]
rt=[] 
q=[1]

get_time(time_list,q)
show_plot()