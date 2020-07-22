import copy
import os
import random
import tsplib95
from plot_graphs import plot_path


def random_state(problem):
    nodes = list(problem.get_nodes())
    return random.sample(nodes, len(nodes))


def swap_positions(state, pos1, pos2):
    state[pos1], state[pos2] = state[pos2], state[pos1]


def swap_neighbours(state, problem):
    best_distance = calc_distance_of_state(state, problem)
    best_solution = copy.deepcopy(state)

    for i in range(len(state)-1):
        swap_positions(state, i, i+1)
        actual_value = calc_distance_of_state(state, problem)
        if actual_value < best_distance:
            best_distance = actual_value
            best_solution = copy.deepcopy(state)
        swap_positions(state, i, i + 1)

    return best_distance, best_solution


def calc_distance_of_state(state, problem):
    distance = 0
    for i in range(len(state)-1):
        distance += problem.get_weight(state[i], state[i+1])
    return distance


def index(file_name):
    cities = tsplib95.load(os.path.join(os.getcwd(), '../data/' + file_name))

    initial_state = random_state(cities)
    distance_initial_state = calc_distance_of_state(initial_state, cities)

    best_distance, best_solution = swap_neighbours(initial_state, cities)

    print(initial_state)
    plot_path(cities, initial_state, distance_initial_state, 'Estado Inicial')
    print('initial: {}'.format(distance_initial_state))

    print(best_solution)
    plot_path(cities, best_solution, best_distance, 'Melhor Solução')
    print('best: {}'.format(best_distance))
    print('difference: {}'.format(distance_initial_state - best_distance))
