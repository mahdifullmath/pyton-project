import threading
import time
import tkinter
import os
class p:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def adding(processlist,timelist):
    processlist.append( input("insert process name:"))
    if (processlist[-1]=="exit"):
        window.destroy()
        os._exit(0)
    timelist.append(int(input("insert process time:")))
def adding_plus(processlist,timelist):
    while(1):
        adding(processlist,timelist)
def exitt():
    window.destroy()
    os._exit(0)
def RR(processlist,timelist,q,text):
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



def RR_thread():
    t2=threading.Thread(target=RR ,args=(process.name,process.time,q,text))
    t2.start()


# gui--------------------------------------------------------------------

q=int(input("time slice for your round robin? ")) 
processlist=[]
timelist=[]
process=p(processlist,timelist)  

window=tkinter.Tk()
window.minsize(width=500,height=500)
in_lable=tkinter.Label(text="output")
in_lable.pack(side="top")

text=tkinter.Text(window)
text.pack()
b=tkinter.Button(window, text="run", command=RR_thread,width=20)
b.pack()
tkinter.Button(window, text="Quit", command=exitt, width=20).pack()
          


t1=threading.Thread(target=adding_plus,args=(process.name,process.time))
t1.start()
window.mainloop()
