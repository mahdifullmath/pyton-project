import numpy as np
import matplotlib.pyplot as plt
n=3

#tabe---------------------------------------------------
def getmoraba():
    global n
    n=int (input("input n for n*n square :"))
    morabalist=[]
    for i in range(n**2):
        morabalist.append(i+1)

    return morabalist

def roulette_wheel(population):
    population.sort(key = lambda x: x.fitness)
    wheel=[]
    wheel.append(int(population[0].fitness*100))
    for i in range(1,len(population)):
        wheel.append(wheel[i-1]+int(population[i].fitness*100))
    return wheel

def objectiveFunc(morabalist):
    global n
    counter=0
 # for rows
    for i in range(0,n**2,n):
        if sum(morabalist[i:i+n]) != n*(n**2+1)/2:
            counter += 1
 # for cols
    for i in range(0,n):
        sumcol=0
        for j in range(i,n**2,n):
            sumcol=sumcol+morabalist[j]
        if sumcol != n*(n**2+1)/2:
            counter += 1
    # for Oblique
    sumobli=0
    for i in range(0,n**2,n+1):
        sumobli = sumobli + morabalist[i] 
    if sumobli != n*(n**2+1)/2:
            counter += 1
    sumobli=0
    for i in range(n-1,n**2-1,n-1):
        sumobli = sumobli + morabalist[i] 
    if sumobli != n*(n**2+1)/2:
            counter += 1
    return counter
def fitnessFunc(morabalist):
    return 1/(objectiveFunc(morabalist)+1)

def entekhab_valed(population, tedad_valed):
    wheel=roulette_wheel(population)
    valedlist=[]
    for i in range(tedad_valed):
        random=np.random.randint(0,max(wheel))
        j=0
        while (random>=wheel[j]):
            j+=1
        valedlist.append(population[j])
    
    return valedlist

def tolid_mesl(valedlist,probability):

    bachehalist = []
    for i in range(0, len(valedlist), 2):
        if probability>=np.random.random():
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

def jahesh(bachehalist,probability):
    for i in range(len(bachehalist)):
        if probability>=np.random.random():
            h = np.random.randint(0,len(bachehalist[0].chromosome)-1)
            k = np.random.randint(h+1,len(bachehalist[0].chromosome))
            for j in range(h,k):
                t=bachehalist[i].chromosome[k-j]
                bachehalist[i].chromosome[k-j]= bachehalist[i].chromosome[j]
                bachehalist[i].chromosome[j]=t

            gene = Gene(bachehalist[i].chromosome,fitnessFunc(bachehalist[i].chromosome))
            bachehalist[i] = gene
    return bachehalist

def entekhabe_bazmande(population, offsprings):
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    for i in range(2,len(offsprings),1):
        population[i]=offsprings[i]
    return population
    # wheel=roulette_wheel(population)
    # new_population=[]
    # for i in range(tedad_jameat):
    #     random=np.random.randint(0,max(wheel))
    #     j=0
    #     while (random>=wheel[j]):
    #         j+=1
    #     new_population.append(population[j])
                
    
    # return new_population
    

class Gene:
    def __init__(self, chromosome, gene):
        self.chromosome = chromosome
        self.fitness = gene

    def __repr__(self):
        sq=[]
        for i in range(0,n**2,n):
            sq.append(self.chromosome[i:i+n])
        return  "("+str(sq)+"," + str(self.fitness) + ")\n"  

def best_av(population,best,avrage):
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    best.append(population[0].fitness)
    sumfit=0
    for i in population:
        sumfit=sumfit+i.fitness
    avrage.append(sumfit/len(population))

tedad_jameat = 20*n
tedad_ijad = 500
tedad_valed = tedad_jameat // 2
crossover_probability = 0.9
mutation_probability = 0.1
best=[]
avrage=[]
# Ijad----------------------------------------------------------
morabalist = getmoraba()
population = []
for i in range(0,tedad_jameat):
    t = []
    x=morabalist[:]
    np.random.shuffle(x)
    t = x
    fitness = fitnessFunc(t)
    gene = Gene(t, fitness)
    population.append(gene)
    
print(population)
print ("\n")


# halghe asli---------------------------------------------------------------------
for i in range(tedad_ijad):
    
    valedlist = entekhab_valed(population, tedad_valed)
    offsprings = tolid_mesl(valedlist,crossover_probability)
    offsprings = jahesh(offsprings,mutation_probability)
    population = entekhabe_bazmande(population, offsprings)
    best_av(population,best,avrage)
    if (population[0].fitness==1):
        print("\n"+str(population[0]))
        print ("\n")
        break
print ("\n")    
print(population)
plt.plot(avrage,'r',best,'g')
plt.legend(['avrage', 'best'])
plt.xlabel('generation')
plt.ylabel('fitness')
plt.show()
