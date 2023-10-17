import numpy as np
import matplotlib.pyplot as plt
def creat_thing_list(number):
    thing_list=[]
    for i in range(0,number,1):
        thing_list.append(Thing(np.random.randint(1,15),np.random.randint(1,50)))
    return thing_list

def creat_gene(number):
    list=[]
    for i in range(0,number):
        list.append(np.random.randint(0,2))
    return list

def objf1(gene,things,W):
    Wsum=0
    for i in range(0,len(gene),1):
        if (gene[i]==1):
            Wsum=Wsum+things[i].w
    if (Wsum>W):
        return 0
    else:
        return 1

def objf2(gene,things):
    vsum=0
    sum=0
    for i in range(0,len(gene)):
        if (gene[i]==1):
            vsum=vsum+things[i].v
        sum=sum+things[i].v
    vsum=vsum/sum
    return vsum

def fitnessFunction(gene,things,W):
    fitness = 0.5*objf1(gene,things,W) + 0.5*objf2(gene,things)
    return fitness

def parentSelection(population, crossover_probability):
    parents = []
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    for i in range(0,int(crossover_probability*len(population)),1):
        parents.append(population[i])
    return parents

def Crossover(parents,things,W):
    offsprings = []
    for i in range(0,len(parents),2):
        parent1 = parents[i].chromosome
        parent2 = parents[i + 1].chromosome
        p = np.random.randint(0,len(parent1))
        offspring2 = list(parent1[0:p])
        offspring1 = list(parent2[0:p])

        for j in range(p,len(parent1),1):
            offspring1.append(parent1[j])
            
            offspring2.append(parent2[j])

        gene1 = Gene(offspring1, fitnessFunction(offspring1,things,W))
        gene2 = Gene(offspring2, fitnessFunction(offspring2,things,W))
        offsprings.append(gene1)
        offsprings.append(gene2)
    return offsprings

def mutation(offsprings, mutation_probability,things,W):
    
    for i in range(0,len(offsprings)):
        t=np.random.random(1)
        if t<mutation_probability:
            random_number = np.random.randint(0,len(offsprings[0].chromosome))
            if offsprings[i].chromosome[random_number]==0:
                offsprings[i].chromosome[random_number]=1
            else:
                offsprings[i].chromosome[random_number]=0
        
            gene = Gene(offsprings[i].chromosome,fitnessFunction(offsprings[i].chromosome,things,W))
            offsprings[i] = gene
    return offsprings

def survivorSelection(population, offsprings):
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    for i in range(1,len(offsprings),1):
        population[i]=offsprings[i]
    return population

def avrage_and_best_creator(population,best,avrage):
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    best.append(population[0].fitness)
    sumfit=0
    for i in population:
        sumfit=sumfit+i.fitness
    avrage.append(sumfit/len(population))

class Thing:
    def __init__(self, w, v):
        self.w = w
        self.v = v
    def __repr__(self):
        return "(" + str(self.w) + "," + str(self.v) + ")\t"  

     

class Gene:
    def __init__(self, chromosome, fitness):
        self.chromosome = chromosome
        self.fitness = fitness
    def __repr__(self):
        str1=[]
        for i in range(0,len(self.chromosome)):
            if self.chromosome[i]==1:
                str1.append ('t'+str(i+1))
        return "(" + str(str1) + "," + str(self.fitness) + ")\n"



#mian
tedad_ashya = 10
number_of_population = 20
number_of_genereation = 500
W=15
best=[]
avrage=[]
crossover_probability = 0.9
mutation_probability = 0.1


things = creat_thing_list(tedad_ashya)
population = []
firstgene= creat_gene(tedad_ashya)
print(firstgene)
print(things)
# Initialization----------------------------------------------------------
for i in range(0,number_of_population,1):
    temp = []
    temp = creat_gene(tedad_ashya)
    fitness = fitnessFunction(temp,things,W)
    gene = Gene(temp, fitness)
    population.append(gene)
  

print(population)
avrage_and_best_creator(population,best,avrage)
# generation Loop---------------------------------------------------------------------
for i in range(0,number_of_genereation,1):
    parents = parentSelection(population, crossover_probability)
    offsprings = Crossover(parents,things,W)
    offsprings = mutation(offsprings, mutation_probability,things,W)
    population = survivorSelection(population, offsprings)
    avrage_and_best_creator(population,best,avrage)
    # print()

population.sort(key = lambda x: x.fitness)
print(population)

fig,plots=plt.subplots(2)        

plots[0].plot(avrage)
plots[0].legend(['avrage'])
plots[1].plot(best)
plots[1].legend(['best'])
plt.xlabel('generation')
plt.ylabel('fitness')
plt.show()