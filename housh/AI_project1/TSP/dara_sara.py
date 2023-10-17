import numpy as np
def creat_list(number):
    citylist=[]
    for i in range(1,number):
        citylist.append(i)
    return citylist

def fitnessFunction(gene):
    fitness = 2
    x=[0]
    for i in (gene):
        if (i>max(x)):
            fitness +=1
        if (i<min(x)):
            fitness +=1
        x.append(i)
        
    
    return fitness

def parentSelection(population, number_of_parents):
    parents = []
    for i in range(0,number_of_parents,1):
        random_number = np.random.randint(0,len(population))
        parents.append(population[random_number])
    return parents

def Mateing(parents, MateProbability):
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
    return population[0:number_of_population]


class Gene:
    def __init__(self, chromosome, gene):
        self.chromosome = chromosome
        self.fitness = gene
    def __repr__(self):
        return "(" + str(self.chromosome) + "," + str(self.fitness) + ")\n"  





number_of_aroos = int(input())
number_of_genereation = 20
number_of_population =10
number_of_parents = number_of_population // 2


Mate_probability = 0.9
mutation_probability = 0.2


citylist = creat_list(number_of_aroos)
population = []
if number_of_aroos==1:
    print(2)
    exit()
# Initialization----------------------------------------------------------
for i in range(number_of_population):
    temp = []
    np.random.shuffle(citylist)
    temp = citylist
    fitness = fitnessFunction(temp)
    gene = Gene(temp, fitness)
    population.append(gene)
  





# Main Loop---------------------------------------------------------------------
for i in range(number_of_genereation):
    
    parents = parentSelection(population, number_of_parents)
    offsprings = Mateing(parents, Mate_probability)
    offsprings = mutation(offsprings, mutation_probability)
    population.extend(offsprings)
    population = survivorSelection(population, number_of_population)
    # print()
print(population)    
print(population[0].fitness)


