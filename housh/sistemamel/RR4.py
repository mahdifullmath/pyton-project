import threading
import time
import tkinter
import os
import matplotlib.pyplot as plt 
from tkinter.ttk import * 
q=1
time1=0
#plot----------------------------------------------------------------------
def show_plot():
    x=[]
    y=[]
    #awt.sort(key=lambda x:x.[1])
    for i in awt:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x,y,'g',marker='o')
    plt.show()
    return
#q in-----------------------------------------------------------------------
def qin():
    progressbar['value']=0
    global q
    timelist.clear()
    q=int(q_in.get())
    burst_time.clear()
    end_time.clear()
    process_namelist.clear()
    arival_time.clear()
    rt.clear()
#awt clculate----------------------------------------------------------------------
def add_awt():
    qwt=[]
    qwt.append(q)
    qwt.append(sum(rt)/len(rt)-sum(burst_time)/len(burst_time))
    awt.append(qwt) 
    return  


#get process and burst------------------------------------------------------------
def adding():
    global time1
    process_namelist.append( in_name.get())
    if (process_namelist[-1]=="exit"):
        window.destroy()
        os._exit(0)
    timelist.append(int(in_burst.get()))
    burst_time.append(int(in_burst.get()))
    #arival_time.append(time.time())
    arival_time.append(time1)
    end_time.append(0)
    rt.append(0)
    progressbar['value']=progressbar['value']-timelist[-1]
    
#exit--------------------------------------------------------------------------------
def exitt():
    window.destroy()
    os._exit(0)
#roundrobin--------------------------------------------------------------------------
def RR():
    m=1
    global time1
    progressbar['value']=0
    while(0<max(timelist)):
        for i in range(len(timelist)):
            if(timelist[i]!=0):
                for j in range(q):
                    if(timelist[i]==0):
                        #end_time[i]=time.time()
                        break
                    text.insert(tkinter.INSERT,"p%d :\t%s\n" % (m,process_namelist[i]))
                    time.sleep(2)
                    timelist[i]=timelist[i]-1
                    m+=1
                    progressbar['value']=progressbar['value']+3
                    time1+=1
                end_time[i]=time1
                rt[i]=end_time[i]-arival_time[i]
    progressbar['value']=100
    add_awt()
    text.insert(tkinter.INSERT,"q=%d , AWt=%f\n" %(q,awt[-1][1]))
    return
#threads----------------------------------------------------------------
def adding_thread(x):
    t1=threading.Thread(target=adding,args=())
    t1.start()

def RR_thread():
    t2=threading.Thread(target=RR ,args=())
    t2.start()
    
def qin_thread():
    t3=threading.Thread(target=qin )
    t3.start()
def plot_thread():
    t4=threading.Thread(target=show_plot )
    t4.start()
# gui--------------------------------------------------------------------

        
burst_time=[]
end_time=[]
process_namelist=[]
timelist=[]
arival_time=[]
awt=[]
rt=[]
#process=p(processlist,timelist,burst_time,end_time,arival_time)  

#gui---------------------------------------------------
window=tkinter.Tk()
window.minsize(width=1200,height=600)
#exit--------------------------------------------------------

tkinter.Button(window, text="Quit", command=exitt, width=20).pack(side="bottom")
#plot------------------------------------------------------------------------------------
tkinter.Button(window, text="plot", command=plot_thread, width=20).pack(side="bottom" ,pady=10)
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
progressbar = Progressbar(window, orient = "horizontal",length = 600, mode = 'determinate')
progressbar.pack(pady = 10)
b=tkinter.Button(window, text="run", command=RR_thread,width=20)
b.pack()



window.mainloop()
