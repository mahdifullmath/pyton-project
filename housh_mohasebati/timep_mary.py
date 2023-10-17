import numpy as np
import random
import matplotlib.pyplot as plt
def creat_time_list(number):
    time_list=[]
    for i in range(0,number):
        t=random.randrange(1,50)
        time_list.append(t)
    print()
    return time_list
def creat_chromosome(number,time_list):
    chrom_list=[]
    for i in range(1,number+1):
        chrom_list.append(kar(i,time_list[i-1]))
    return chrom_list

def objf(times):
    bsum=[]
    bsum.append(0)
    for i in range(0,len(times)-1):
        bsum.append(int(bsum[i]+times[i].time))
    return sum(bsum)   

def fitnessFunction(times):
    fitness = 1/objf(times)+1
    return fitness

def parentSelection(population, crossover_probability):
    parents = []
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    for i in range(0,int(crossover_probability*len(population)),1):
        parents.append(population[i])
    return parents

def Crossover(parents):
    offsprings = []
    for i in range (0,len(parents),2):
        parent1 = parents[i].chromosome
        parent2 = parents[i + 1].chromosome
        p = np.random.randint(0,len(parent1))
        offspring2 = list(parent1[0:p])
        offspring1 = list(parent2[0:p])

        for j in range(0,len(parent1),1):
            if parent1[j] not in offspring1:
                offspring1.append(parent1[j])
            if parent2[j] not in offspring2:
                offspring2.append(parent2[j])

        gene1 = Gene(np.array(offspring1), fitnessFunction(offspring1))
        gene2 = Gene(np.array(offspring2), fitnessFunction(offspring2))
        offsprings.append(gene1)
        offsprings.append(gene2)
    return offsprings

def mutation(offsprings, mutation_probability):
    t=np.random.randint(0,len(offsprings)-int(mutation_probability*len(offsprings)))
    for i in range(t,t+int(mutation_probability*len(offsprings))):
        random_numbers = np.random.randint(0,len(offsprings[0].chromosome),(2,1))
        h = random_numbers[0]
        k = random_numbers[1]

        temp = offsprings[i].chromosome[h[0]]
        offsprings[i].chromosome[h[0]] = offsprings[i].chromosome[k[0]]
        offsprings[i].chromosome[k[0]] = temp

        gene = Gene(offsprings[i].chromosome,fitnessFunction(offsprings[i].chromosome))
        offsprings[i] = gene
    return offsprings

def survivorSelection(population):
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    for i in range(1,len(offsprings),1):
        population[i]=offsprings[i]
    return population
def best_av(population,best,avrage):
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    best.append(population[0].fitness)
    sumfit=0
    for i in population:
        sumfit=sumfit+i.fitness
    avrage.append(sumfit/len(population))

class kar:
    def __init__(self, kar, time):
        self.kar = kar
        self.time = time   
class Gene:
    def __init__(self, chromosome, gene):
        self.chromosome = chromosome
        self.fitness = gene
    def __repr__(self):
        list_time=[]
        list_kar=[]
        for i in range (len(self.chromosome)):
            list_time.append(self.chromosome[i].time)
            list_kar.append(self.chromosome[i].kar)
        return "(" + str(list_time) + "," + str(list_kar) +"," + str(self.fitness) + ")\n"



number_of_times = 10
number_of_genereation = 500
number_of_population = 100


crossover_probability = 0.9
mutation_probability = 0.1
best=[]
avrage=[]

times = creat_time_list(number_of_times)
chro_list=creat_chromosome(number_of_times,times)
population = []
print(times)
# Initialization----------------------------------------------------------
for i in range(number_of_population):
    temp = []
    

    np.random.shuffle(chro_list)
    temp = chro_list
    fitness = fitnessFunction(temp)
    gene = Gene(temp, fitness)
    population.append(gene)
  

print(population)
# Main Loop---------------------------------------------------------------------
for i in range(number_of_genereation):
    
    parents = parentSelection(population, crossover_probability)
    offsprings = Crossover(parents)
    offsprings = mutation(offsprings, mutation_probability)
    population = survivorSelection(population)
    best_av(population,best,avrage)
    # print()
    
population.sort(key = lambda x: x.fitness)
print(population)

plt.plot(avrage,'r',best,'g')
plt.legend(['avrage', 'best'])
plt.xlabel('generation')
plt.ylabel('fitness')
plt.show()