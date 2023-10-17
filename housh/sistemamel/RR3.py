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

def RR(processlist,timelist):
    m=1
    while(1):
        for i in range(len(timelist)):
            for j in range(q):
                if(timelist[i]==0):
                    break
                text.insert(tkinter.INSERT,"p%d :\t%s\n" % (m,processlist[i]))
                time.sleep(1)
                timelist[i]=timelist[i]-1
                m+=1

def adding_thread(x):
    t1=threading.Thread(target=adding,args=(process.name,process.time))
    t1.start()

def RR_thread():
    t2=threading.Thread(target=RR ,args=(process.name,process.time))
    t2.start()
    
def qin_thread():
    t3=threading.Thread(target=qin )
    t3.start()
# gui--------------------------------------------------------------------

        
# q=int(input("time slice for your round robin? "))

processlist=[]
timelist=[]
process=p(processlist,timelist)  
#gui---------------------------------------------------
window=tkinter.Tk()
window.minsize(width=500,height=500)
#exit--------------------------------------------------------
tkinter.Button(window, text="Quit", command=exitt, width=20).pack(side="bottom")
#q------------------------------------------------------
q_lable=tkinter.Label(text="q").pack(side="left")
q_in=tkinter.Entry(width=2)
q_in.pack(side="left")
tkinter.Button(window, text="qin", command=qin_thread, width=2).pack(side="left")
#entery name & burst----------------------------------------------------
in_lable=tkinter.Label(text="input name:").pack(side="left")
in_name=tkinter.Entry(width=20)
in_name.pack(side="left")
in_lablet=tkinter.Label(text="input burst time:").pack(side="left")
in_burst=tkinter.Entry(width=20)
in_burst.pack(side="left")
window.bind('<Return>', adding_thread)

#output-----------------------------------------------------------
out_lable=tkinter.Label(text="output")
out_lable.pack(side="top")
text=tkinter.Text(window)
text.pack()
b=tkinter.Button(window, text="run", command=RR_thread,width=20)
b.pack()




window.mainloop()
