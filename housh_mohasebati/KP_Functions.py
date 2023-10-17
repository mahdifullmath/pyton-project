import numpy as np
import random
def creat_thing_list(number):
    thing_list=[]
    for i in range(0,number):
        thing_list.append(Thing(np.random.randint(1,15),np.random.randint(1,50)))
    return thing_list

def creat_gene(number):
    list=[]
    for i in range(0,number):
        list.append(np.random.randint(0,2))
    return list

def objf1(gene,things,W):
    Wsum=0
    for i in range(0,len(gene)):
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

def Crossover(parents, MateProbability,things,W):
    offsprings = []
    Probability =[]
    for i in range(0,int(MateProbability*len(parents))):
        Probability.append(random.randrange(0,len(parents),2))
    for i in Probability:
        parent1 = parents[i].chromosome
        parent2 = parents[i + 1].chromosome
        p = np.random.randint(0,len(parent1))
        offspring2 = list(parent1[0:p])
        offspring1 = list(parent2[0:p])

        for j in range(p,len(parent1),1):
            offspring1.append(parent1[j])
            
            offspring2.append(parent2[j])

        gene1 = Gene(np.array(offspring1), fitnessFunction(offspring1,things,W))
        gene2 = Gene(np.array(offspring2), fitnessFunction(offspring2,things,W))
        offsprings.append(gene1)
        offsprings.append(gene2)
    return offsprings

def mutation(offsprings, mutation_probability,things,W):
    t=np.random.randint(0,len(offsprings)-int(mutation_probability*len(offsprings)))
    for i in range(t,t+int(mutation_probability*len(offsprings))):
        random_number = np.random.randint(0,len(offsprings[0].chromosome))
        random_number2= np.random.randint(0,len(offsprings[0].chromosome))
        temp = offsprings[i].chromosome[random_number]
        offsprings[i].chromosome[random_number]=offsprings[i].chromosome[random_number2]
        offsprings[i].chromosome[random_number2]=temp

        gene = Gene(offsprings[i].chromosome,fitnessFunction(offsprings[i].chromosome,things,W))
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
