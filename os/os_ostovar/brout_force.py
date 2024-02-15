
n=int(input("n="))
W=int(input("W="))
w=[]
p=[]
inc=[]
majmu=[]
profit=0
weight=0
maxprofit=0
for i in range(n):
    w.append(int(input("w=")))
    p.append(int(input("p=")))
    inc.append(i)
for i in range (n):
    if [inc[i]] not in majmu :
        majmu.append([inc[i]])
    if list(inc[i:n]) not in majmu :
        majmu.append(list(inc[i:n]))
    if inc[0:n-i] not in majmu :
        majmu.append(list(inc[0:n-i]))
    if inc[i:i+2] not in majmu :
        majmu.append(list(inc[i:i+2]))
majmu.append([0,2])    
for x in majmu:
    profit=0
    weight=0
    for i in x:
        print("w",i,end=" , ")
        profit+=p[i]
        weight+=w[i]
    print("profit=",profit,end=" ")
    if weight>W:
        print(">>not include this",end=" ")
        profit=0
    if (profit>maxprofit):
        maxprofit=profit
    print()
print("maxprofit=",maxprofit)