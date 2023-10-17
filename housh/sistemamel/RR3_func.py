import threading
import time
import tkinter
import os 
q=1
class p:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def qin():
    global q
    q=int(q_in.get())

def adding(processlist,timelist):
    processlist.append( in_name.get())
    if (processlist[-1]=="exit"):
        window.destroy()
        os._exit(0)
    timelist.append(int(in_burst.get()))
    

def exitt():
    window.destroy()
    os._exit(0)

def RR(processlist,timelist,q):
    m=1
    while(1):
        for i in range(len(timelist)):
            for j in range(q):
                if(timelist[i]<=0):
                    break
                text.insert(tkinter.INSERT,"p%d :\t%s\n" % (m,processlist[i]))
                # print("p%d :\t%s" % (m,processlist[i]))
                time.sleep(1)
                timelist[i]=timelist[i]-1
                m+=1

def adding_thread(x):
    t1=threading.Thread(target=adding,args=(process.name,process.time))
    t1.start()

def RR_thread():
    t2=threading.Thread(target=RR ,args=(process.name,process.time,q))
    t2.start()
    
def qin_thread():
    t3=threading.Thread(target=qin )
    t3.start()