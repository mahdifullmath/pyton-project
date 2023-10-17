import threading
import tkinter
import time as t
import matplotlib.pyplot as plt
time1=0
Qt=1
#plot----------------------------------------------------------------------
def show_plot():
    x=[]
    y=[]
    for i in awt:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x,y,'g',marker='o')
    plt.show()
    return 
def roundrobin(M,Qt):
    global time1
    while(max(M)>0):
        for j in range(0,len(M)):
            if(M[j]>=Qt):
                for i in range(0,Qt):
                    M[j]=M[j]-1
                    box.insert(tkinter.INSERT,"process")
                    box.insert(tkinter.INSERT,j+1)
                    box.insert(tkinter.INSERT,"\n")
                    t.sleep(1)
                    time1+=1
       
            else:
                while(M[j]>0):
                    M[j]=M[j]-1
                    box.insert(tkinter.INSERT,"process")
                    box.insert(tkinter.INSERT,j+1)
                    box.insert(tkinter.INSERT,"\n")
                    t.sleep(1)
                    time1+=1
            if(M[j]==0 and in_end[j]!=1):
                end_time[j]=time1
                rt[j]=end_time[j]-arival_time[j]
                in_end[j]=1
    qwt=[]
    qwt.append(Qt)
    qwt.append(sum(rt)/len(rt)-sum(burst_time)/len(burst_time))
    awt.append(qwt) 
    return        

def inserti():
    global Qt
    Qt=int(input("Quantum time:  ")) 
    while(1):
        ptime.append(int(input("time of process ")))
        arival_time.append(time1)
        if (ptime[-1]==-1):
            break
        burst_time.append(ptime[-1])
        end_time.append(0)
        rt.append(0)
        in_end.append(0)
    burst_time.clear()
    end_time.clear()
    arival_time.clear()
    rt.clear()
    ptime.clear()
    return
    
def inserti_thread():
    t1=threading.Thread(target=inserti,args=())
    t1.start()

def ROUNDROBIN_thread():
    t2=threading.Thread(target=roundrobin ,args=(ptime,Qt))
    t2.start()

def plot_thread():
    t=threading.Thread(target=show_plot )
    t.start()


in_end=[]
ptime=[]
burst_time=[]
end_time=[]
arival_time=[]
awt=[]
rt=[]
root=tkinter.Tk()
root.minsize(width=500,height=300)
tkinter.Button(root, text="plot", command=plot_thread, width=20).pack(side="bottom" ,pady=10)
in_lable=tkinter.Label(text="round_robin")
in_lable.pack(side="top")

box=tkinter.Text(root)
box.pack()
botom=tkinter.Button(text="exe", command=ROUNDROBIN_thread)
botom.pack()
          
tkinter.Button(root, text="get Qt", command=inserti_thread, width=20).pack(side="bottom" ,pady=10)
root.mainloop()