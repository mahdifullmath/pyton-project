import threading
import time
import tkinter
import os
import matplotlib.pyplot as plt  
awt=((1,2),(3,3),(4,7))
def show_plot():
    x=[]
    y=[]
    for i in awt:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x,y,'g',marker='o')
    plt.show()

show_plot()