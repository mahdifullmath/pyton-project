import threading
import time
import tkinter
class p:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def adding(name, time):
    process.name.append( input("insert process name:"))
    if(process.name[-1]=="exit"):
        exit()
    process.time.append(int(input("insert process time:")))

def adding_plus(process):
    while(1):
        adding(process)

def adding_thread():
    t1=threading.Thread(target=adding,args=(process))
    t1.start()
def RR_thread():
    t2=threading.Thread(target=RR ,args=(process,q,text))
    t2.start()

def RR(process,q,text):
    m=1
    while(1):
        for i in range(len(process.name)):
            for j in range(q):
                if(process.time[i]<=0):
                    break
                text.insert(tkinter.INSERT,"p%d :\t%s\n" % (m,process.name[i]))
                # print("p%d :\t%s" % (m,processlist[i]))
                time.sleep(1)
                process.time[i]=process.time[i]-1
                m+=1
# gui--------------------------------------------------------------------
q=int(input("time slice for your round robin? ")) 
processnamelist=[]
timelist=[]
process=p(processnamelist,timelist)  
window=tkinter.Tk()
window.minsize(width=500,height=500)
in_lable=tkinter.Label(text="output")
in_lable.pack(side="top")

text=tkinter.Text(window)
text.pack()
b=tkinter.Button(text="run", command=RR_thread)
b.pack()

          


t3=threading.Thread(target=adding_plus,args=(process))
t3.start()
window.mainloop()