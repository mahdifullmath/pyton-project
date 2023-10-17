import numpy as np
n=3

#tabe---------------------------------------------------
def getmoraba():
    global n
    n=int (input("how meny ?"))
    morabalist=[]
    for i in range(n**2):
        morabalist.append(i+1)

    return morabalist

def objectiveFunc(morabalist):
    global n
    moraba1=[]
    moraba=[]
    moraba1=morabalist[:]
    for i in range (0,n**2,n):
        moraba.append(moraba1[i:i+n])
    counter = 0
 # for rows
    for i in range(n):
        if sum(moraba[i]) != n*(n**2+1)/2:
            counter += 1
    # for cols
    c1, c2, c3 = 0, 0, 0

    for i in moraba:
        c1 += i[0]
        c2 += i[1]
        c3 += i[2]
    if c1 != n*(n**2+1)/2:
        counter += 1
    if c3 != n*(n**2+1)/2:
        counter += 1
    if c2 != n*(n**2+1)/2:
        counter += 1
    # for Oblique
    if (moraba[0][0] + moraba[1][1] + moraba[2][2]) != n*(n**2+1)/2:
        counter += 1
    if (moraba[0][2] + moraba[1][1] + moraba[2][0]) != n*(n**2+1)/2:
       counter += 1
    return counter

def entekhab_valed(jameat, tedad_valed):
    valedlist = []
    for i in range(0,tedad_valed):

        random_number1 = np.random.randint(0,len(jameat))
        random_number2 = np.random.randint(0,len(jameat))
        if (jameat[random_number1].fitness <= jameat[random_number2].fitness):
            valedlist.append(jameat[random_number1])
        else:
            valedlist.append(jameat[random_number2])
    
    return valedlist

def tolid_mesl(valedlist):
    bachehalist = []
    for i in range(0, len(valedlist), 2):
        valed1 = valedlist[i].chromosome
        valed2 = valedlist[i + 1].chromosome
        p = np.random.randint(0,len(valed1)-1)
        x = np.random.randint(p,len(valed1))
        bache1 = list(valed1[p:x])
        bache2 = list(valed2[p:x])

        for j in range(0,len(valed1)):
            if valed1[j] not in bache2:
                bache2.append(valed1[j])
            if valed2[j] not in bache1:
                bache1.append(valed2[j])

        gene1 = Gene(bache2, fitnessFunc(bache2))
        gene2 = Gene(bache1, fitnessFunc(bache1))
        bachehalist.append(gene1)
        bachehalist.append(gene2)
    return bachehalist

def jahesh(bachehalist):
    for i in range(len(bachehalist)):
        
        h = np.random.randint(0,len(bachehalist[0].chromosome)-1)
        k = np.random.randint(h+1,len(bachehalist[0].chromosome))
        for j in range(h,k):
            t=bachehalist[i].chromosome[k-j]
            bachehalist[i].chromosome[k-j]= bachehalist[i].chromosome[j]
            bachehalist[i].chromosome[j]=t

        gene = Gene(bachehalist[i].chromosome,fitnessFunc(bachehalist[i].chromosome))
        bachehalist[i] = gene
    return bachehalist

def entekhabe_bazmande(jameatlist, tedad_jameat):
    jameatlist.sort(key = lambda x: x.fitness)
    return jameatlist[0:tedad_jameat]



class Gene:
    def __init__(self, chromosome, gene):
        self.chromosome = chromosome
        self.fitness = gene

    def __repr__(self):
        return "(" + str(self.chromosome) + "," + str(self.fitness) + ")\n"  



tedad_jameat = 700
tedad_ijad = 10000
tedad_valed = tedad_jameat // 2
# Ijad----------------------------------------------------------
morabalist = getmoraba()
jameatlist = []
for i in range(0,tedad_jameat):
    t = []
    x=morabalist[:]
    np.random.shuffle(x)
    t = x
    fitness = fitnessFunc(t)
    gene = Gene(t, fitness)
    jameatlist.append(gene)
    
print(jameatlist)



# halghe asli---------------------------------------------------------------------
for i in range(tedad_ijad):
    
    valedlist = entekhab_valed(jameatlist, tedad_valed)
    bachelist = tolid_mesl(valedlist)
    bachelist = jahesh(bachelist)
    jameatlist.extend(bachelist)
    jameatlist = entekhabe_bazmande(jameatlist, tedad_jameat)
    if (jameatlist[0].fitness==0):
        print(jameatlist[0])
        print ("\n")
        break
    
print(jameatlist)