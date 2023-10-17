from timeproblem_functions import *
import numpy as np
import matplotlib.pyplot as plt
number_of_times = 10
number_of_genereation = 500
number_of_population = 100
number_of_parents = number_of_population // 2


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
    
    parents = parentSelection(population, number_of_parents)
    offsprings = Crossover(parents, crossover_probability)
    offsprings = mutation(offsprings, mutation_probability)
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