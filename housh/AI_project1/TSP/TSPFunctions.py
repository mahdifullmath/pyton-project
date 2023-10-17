import numpy as np
import matplotlib.pyplot as plt
def creat_city_list(number):
    citylist=[]
    for i in range(0,number):
        citylist.append( City(np.random.randint(0,100),np.random.randint(0,100)))
    return citylist

def fitnessFunction(gene):
    fitness = 0
    for i in range(len(gene)-1):
        fitness += gene[i].distance(gene[i+1])
    fitness += gene[len(gene)-1].distance(gene[0])
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

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
     

class Gene:
    def __init__(self, chromosome, gene):
        self.chromosome = chromosome
        self.fitness = gene


def display_plot(population,plt2,t):
    chromosomef=population[0].chromosome
    # X=[i.x for i in chromosomef]
    # Y=[i.y for i in chromosomef]
    # X.append(X[0])
    # Y.append(Y[0])
    # plt.scatter(X,Y,'.-r')
    X=[]
    Y=[]
    for i in chromosomef :
        
        X.append(i.x)
        Y.append(i.y)
        plt2[t].plot(X,Y,'g',marker='o')
        plt.pause(0.50)

    X.append(X[0])
    Y.append(Y[0])
    plt2[t].plot(X,Y,color='g',marker='o')
    plt.pause(0.50)
