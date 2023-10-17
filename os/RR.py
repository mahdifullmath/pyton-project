import threading
import time
import tkinter

def adding(processlist,timelist):
    processlist.append( input("insert process name:"))
    if(processlist[-1]=="exit"):
        exit()
    timelist.append(int(input("insert process time:")))
def adding_plus(processlist,timelist):
    while(1):
        adding(processlist,timelist)
def adding_thread():
    t1=threading.Thread(target=adding,args=(processlist,timelist))
    t1.start()
def RR_thread():
    t2=threading.Thread(target=RR ,args=(processlist,timelist,q,text))
    t2.start()

def RR(processlist,timelist,q,text):
    m=1
    while(1):
        for i in range(len(processlist)):
            for j in range(q):
                if(timelist[i]<=0):
                    break
                text.insert(tkinter.INSERT,"p%d :\t%s\n" % (m,processlist[i]))
                # print("p%d :\t%s" % (m,processlist[i]))
                time.sleep(1)
                timelist[i]=timelist[i]-1
                m+=1
# gui--------------------------------------------------------------------
q=int(input("time slice for your round robin? ")) 
processlist=[]
timelist=[]  
window=tkinter.Tk()
window.minsize(width=500,height=500)
in_lable=tkinter.Label(text="output")
in_lable.pack(side="top")

text=tkinter.Text(window)
text.pack()
b=tkinter.Button(text="run", command=RR_thread)
b.pack()

          


t3=threading.Thread(target=adding_plus,args=(processlist,timelist))
t3.start()
window.mainloop()