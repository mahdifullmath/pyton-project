import numpy as np
import matplotlib.pyplot as plt
import random
def creat_city_list(number):
    citylist=[]
    for i in range(0,number):
        citylist.append( City(np.random.randint(0,100),np.random.randint(0,100)))
    return citylist

def objectivefunction(gene):
    fitness = 0
    for i in range(len(gene)-1):
        fitness += gene[i].distance(gene[i+1])
    fitness += gene[len(gene)-1].distance(gene[0])
    return fitness

def fitnessFunction(gene):
    return 1/(objectivefunction(gene)+1)

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

def Mateing(parents, MateProbability):
    offsprings = []
    Probability =[]
    for i in range(0,int(MateProbability*len(parents))):
        Probability.append(random.randrange(0,len(parents),2))
    for i in Probability:
        parent1 = parents[i].chromosome
        parent2 = parents[i + 1].chromosome
        a = np.random.randint(0,len(parent1)-1)
        b = np.random.randint(a,len(parent1))
        offspring1 = list(parent1[a:b])
        offspring2 = list(parent2[a:b])

        for j in range(len(parent1)):
            if parent1[j] not in offspring1:
                offspring1.append(parent1[j])
            if parent2[j] not in offspring2:
                offspring2.append(parent2[j])

        gene1 = Gene(offspring1, fitnessFunction(offspring1))
        gene2 = Gene(offspring2, fitnessFunction(offspring2))
        offsprings.append(gene1)
        offsprings.append(gene2)
    return offsprings

def mutation(offsprings, mutation_probability):
    t=np.random.randint(0,len(offsprings)-int(mutation_probability*len(offsprings)))
    for i in range(t,t+int(mutation_probability*len(offsprings))):
        h = np.random.randint(0,len(offsprings[0].chromosome)-1)
        k = np.random.randint(h+1,len(offsprings[0].chromosome))
        
        offsprings[i].chromosome[h:k]=offsprings[i].chromosome[h:k][::-1]
        # print()
        gene = Gene(offsprings[i].chromosome,fitnessFunction(offsprings[i].chromosome))
        offsprings[i] = gene
    return offsprings

def survivorSelection(population, offsprings):
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    for i in range(1,len(offsprings),1):
        population[i]=offsprings[i]
    return population
    # new_population = []
    # population.sort(key = lambda x: x.fitness)
    # for i in range(number_of_population):
    #     random_number = np.random.randint(0,len(population),(8,1))
    #     new_population.append(population[int(max(random_number))])
    # return new_population

def best_av(population,best,avrage):
    population.sort(key = lambda x: x.fitness)
    population.reverse()
    best.append(population[0].fitness)
    sumfit=0
    for i in population:
        sumfit=sumfit+i.fitness
    avrage.append(sumfit/len(population))

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"  

class Gene:
    def __init__(self, chromosome, gene):
        self.chromosome = chromosome
        self.fitness = gene
    def __repr__(self):
        return "(" + str(self.chromosome) + "," + str(self.fitness) + ")\n" 


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