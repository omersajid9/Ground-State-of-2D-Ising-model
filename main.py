import numpy as np
import random
import copy

energylist = list()
lattice_list = list()

def initializeLattice(size, prob_positive):
    return [random.choices([-1, 1], [1- prob_positive, prob_positive], k=size) for i in range(size) ]

def latticePrint(lattice):
    for i in lattice:
        print(i)

def calculateEnergy(lattice, magenticField):
    energy = 0
    for i in range(len(lattice)):
        for j in range(len(lattice)):
            if i + 1 < len(lattice):
                energy -= lattice[i][j] * lattice[i+1][j] - magenticField * lattice[i][j]
            if i - 1 >= 0:
                energy -= lattice[i][j] * lattice[i-1][j] - magenticField * lattice[i][j]
            if j + 1 < len(lattice):
                energy -= lattice[i][j] * lattice[i][j+1] - magenticField * lattice[i][j]
            if j - 1 >= 0:
                energy -= lattice[i][j] * lattice[i][j-1] - magenticField * lattice[i][j]
    return energy


def isingModelMetropolis(lattice, iterations, magenticField):
    lattice_initial_copy = copy.deepcopy(lattice_initial)
    for i in range(iterations):
        index_x = np.random.randint(0, len(lattice_initial_copy))
        index_y = np.random.randint(0, len(lattice_initial_copy))


        energy_initial = calculateEnergy(lattice_initial_copy, magenticField)
        lattice_prop = copy.deepcopy(lattice_initial_copy)
        lattice_prop[index_x][index_y] *= -1
        energy_prop = calculateEnergy(lattice_prop, magenticField)
        energy_diff = energy_prop - energy_initial
        prob = np.exp( -1 * beta * energy_diff)
        prob_accept = min(1, prob)

        if prob_accept > np.random.random():
            lattice_initial_copy[index_x][index_y] = lattice_prop[index_x][index_y]
            lattice_list.append(lattice_prop)
            energylist.append(energy_prop)
        else:
            continue
    return lattice_initial_copy


#Variables
iterations = 22
dim = 5
magneticField = 1
beta = 1
prob_positive = 0.5

lattice_initial = initializeLattice(dim, prob_positive)
print("Initial Lattice: ")
latticePrint(lattice_initial)
print("Initial Energy: ")
print(calculateEnergy(lattice_initial, magneticField))
lattice_final = isingModelMetropolis(lattice_initial, iterations, magneticField)
print("Final Lattice: ")
latticePrint(lattice_final)
print("Final Energy: ")
print(calculateEnergy(lattice_final, magneticField))
