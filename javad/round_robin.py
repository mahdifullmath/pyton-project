

def round_robin(burst_times,q):
    while(max(burst_times)>0):
        for i in range(0,len(burst_times)):
            if(burst_times[i]>q):
                for x in range(0,q):  
                    burst_times[i]=burst_times[i]-1
                    print("process", i+1)
                    
                   
                    
            elif (burst_times[i]>0):
                while(burst_times[i]>0):   
                    burst_times[i]=burst_times[i]-1
                    print("process",i+1)
                    
burst_times=[]
n=int(input("tedad= "))
q=int (input("q= "))
while(n>0):
    burst_times.append(int(input("burst time= ")))
    n-=1
round_robin(burst_times,q)