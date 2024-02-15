
import threading
import time
import matplotlib.pyplot as plt
t=0 
Qt=1

def insert_burst_times(burst_time):
    
    burst_time.append(int(input("insert burst time for process & -1 to next q :\n")))
    bt.append(burst_time[-1])
    waite_times.append(0)
    arival_times.append(t)
    response_time.append(0)
    ex_time.append(0)

    

def insert_burst_times_inf_loop(Burst_time):
    global Qt
    Qt=int(input("Quantum time & -1 to display plot:  "))
    if (Qt==-1):
        plt.plot(x,y,'y',marker='o')
        plt.show()
        return
    x.append(Qt)
    in_theread()
    while(1):
        insert_burst_times(Burst_time)
        if (burst_times[-1]==-1):
            burst_times.clear()
            burst_times.append(0)
            bt.clear()
            waite_times.clear()
            arival_times.clear()
            response_time.clear()
            ex_time.clear()
            break
    insert_burst_times_inf_loop(Burst_time)

def in_theread():
    thread=threading.Thread(target=round_robin,args=(burst_times,Qt))
    thread.start()

def round_robin(burst_times,Qt):
    global t
    while(1):
        for i in range(0,len(arival_times)):
            if(burst_times[i+1]>Qt):
                for t in range(0,Qt):  
                    burst_times[i+1]=burst_times[i+1]-1
                    print("process", end=" ")
                    print(i+1)
                    t+=1
                    time.sleep(1)
            elif (burst_times[i+1]>0):
                while(burst_times[i+1]>0):   
                    burst_times[i+1]=burst_times[i+1]-1
                    print("process",end=" ")
                    print(i+1)
                    t+=1
                    time.sleep(1)
                response_time[i]=t-arival_times[i]
                waite_times[i]=response_time[i]- bt[i]
        if(max(burst_times)<=0 and len(burst_times)>1):
            y.append(sum(waite_times)/len(waite_times))    
            return

burst_times=[0]
waite_times=[]
arival_times=[]
response_time=[]
ex_time=[]
bt=[]
x=[]
y=[]

insert_burst_times_inf_loop(burst_times)


