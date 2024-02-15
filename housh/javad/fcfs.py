

burst_times=[]
n=int(input("tedad= "))
while(n>0):
    burst_times.append(int(input("burst time= ")))
    n-=1
for i in range (len(burst_times)):
    for x in range (burst_times[i]):
        print("p",i+1)