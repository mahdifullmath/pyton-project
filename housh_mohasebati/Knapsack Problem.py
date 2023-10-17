
from KP_Functions import *
import matplotlib.pyplot as plt

number_of_things = 10
number_of_genereation = 500
number_of_population = 20
number_of_parents = 10
W=15
best=[]
avrage=[]
crossover_probability = 0.9
mutation_probability = 0.1


things = creat_thing_list(number_of_things)
population = []
firstgene= creat_gene(number_of_things)
print(firstgene)
print(things)
# Initialization----------------------------------------------------------
for i in range(number_of_population):
    temp = []
    temp = creat_gene(number_of_things)
    fitness = fitnessFunction(temp,things,W)
    gene = Gene(temp, fitness)
    population.append(gene)
  

print(population)
best_av(population,best,avrage)
# Main Loop---------------------------------------------------------------------
for i in range(number_of_genereation):
    
    parents = parentSelection(population, number_of_parents)
    offsprings = Crossover(parents, crossover_probability,things,W)
    offsprings = mutation(offsprings, mutation_probability,things,W)
    population.extend(offsprings)
    population = survivorSelection(population, number_of_population)
    best_av(population,best,avrage)
    # print()

population.sort(key = lambda x: x.fitness)
print(population)
plt.plot(avrage,'r',best,'g')
plt.legend(['avrage', 'best'])
plt.xlabel('generation')
plt.ylabel('fitness')
plt.show()
