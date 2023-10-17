import numpy as np
from TSPF1 import *
import matplotlib.pyplot as plt

number_of_citys = 10
number_of_genereation = 500
number_of_population = 100
number_of_parents = number_of_population // 2


Mate_probability = 0.9
mutation_probability = 0.3

best=[]
avrage=[]

citylist = creat_city_list(number_of_citys)
population = []


# Initialization----------------------------------------------------------
for i in range(number_of_population):
    temp = []
    np.random.shuffle(citylist)
    temp = citylist
    fitness = fitnessFunction(temp)
    gene = Gene(temp, fitness)
    population.append(gene)
  



fig, plots=plt.subplots(2)
plt.get_current_fig_manager().set_window_title('genetic algorithm (Travelling salesman problem)')
fig.suptitle("Travelling salesman problem")
display_plot(population,plots,0)

# Main Loop---------------------------------------------------------------------
for i in range(number_of_genereation):
    
    parents = parentSelection(population, number_of_parents)
    offsprings = Mateing(parents, Mate_probability)
    offsprings = mutation(offsprings, mutation_probability)
    population = survivorSelection(population, offsprings)
    best_av(population,best,avrage)
    print()
    
population.sort(key = lambda x: x.fitness)
population.reverse()
display_plot(population,plots,1)

plt.show()

plt.plot(avrage,'r',best,'g')
plt.legend(['avrage', 'best'])
plt.xlabel('generation')
plt.ylabel('fitness')
plt.show()