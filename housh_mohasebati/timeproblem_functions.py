import numpy as np
import random
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

def parentSelection(population, number_of_parents):
    parents = []
    for i in range(0,number_of_parents,1):

        random_number1 = np.random.randint(0,len(population))
        random_number2 = np.random.randint(0,len(population))
        if (population[random_number1].fitness >= population[random_number2].fitness):
            parents.append(population[random_number1])
        else:
            parents.append(population[random_number2])
    return parents

def Crossover(parents, MateProbability):
    offsprings = []
    Probability =[]
    for i in range(0,int(MateProbability*len(parents))):
        Probability.append(np.random.randint(0,len(parents)-1))
    for i in Probability:
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

def survivorSelection(population, number_of_population):
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    return population[0:number_of_population]

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
        for i in range (len(self.chromosome)):
            list_time.append((self.chromosome[i].kar,self.chromosome[i].time))
        return "(" + str(list_time) + "," + str(self.fitness) + ")\n"
