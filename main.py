import random
import sys
import numpy as np

population_size = 1000
default_variation = 1000
bests_sample_size = 10
bests_sample_use_size = 3
start_sample = [0.]
results = []
qnt_results = 2
max_repetitive_tries = 5
MAX_GENERATIONS = 200

def equation(x):
    return eval(equacao)


def equation_reward(x):
    ans = equation(x)
    if ans == 0:
        return sys.maxint
    else:
        return abs(1 / ans)


def generate_population_sample(x_variation, subject):
    sample = []
    for _ in range(population_size):
        sample.append((subject[0] + random.uniform(-x_variation, x_variation)))
    return sample


def create_new_generation(x_variation, mutated_subject):
    sample = generate_population_sample(x_variation, mutated_subject)
    population_results = []

    for subject in sample:
        population_results.append((equation_reward(subject), subject))

    population_results.sort()
    population_results.reverse()
    return population_results


def mutate_best_samples(population_results):
    bests_sample = population_results[0:bests_sample_size]
    bests_sample_use = population_results[0:bests_sample_use_size]
    variations = mutate_variations(bests_sample)
    return variations, bests_sample_use


def mutate_variations(bests_sample):
    x_elements = []
    for subject in bests_sample:
        x_elements.append(subject[1])

    x_variation = default_variation
    if default_variation > np.var(x_elements):
        x_variation = np.var(x_elements)

    return [x_variation]


generation_number = 0
equacao = input("Digite o polinômio desejado\n")
while len(results) < qnt_results:
    gen0 = create_new_generation(default_variation, start_sample)
    mutations = mutate_best_samples(gen0)

    repetition = 0

    for _ in range(100):
        best_equations = []
        for element in mutations[1]:
            best_equations.append(element[1])
        if generation_number != 0:
            if best_equations[0] != last_best_result:
                print(f'==== RESULT {len(results) + 1} GENERATION {generation_number} ====')
                print(f'BEST SAMPLE RESULT = {best_equations[0]}\n\n\n')
                last_best_result = best_equations[0]
            else:
                repetition = repetition + 1
                if repetition == max_repetitive_tries:
                    for result in results:
                        if 0.1 > result - last_best_result > -0.1:
                            print(result - last_best_result)
                            last_best_result = 999999999999999
                    if last_best_result != 999999999999999:
                        repetition = 0
                        results.append(last_best_result)
                        generation_number = 0
                    break
        else:
            last_best_result = best_equations[0]
        new_generations = []
        for i in range(len(best_equations)):
            new_generations = new_generations + create_new_generation(mutations[0][0],
                                                                      best_equations)
        new_generations.sort()
        new_generations.reverse()
        if generation_number >= MAX_GENERATIONS:
            print("TRY CHANGING THE PARAMETERS")
            print("The best values for x are: " + results)
            print(f'==== BEST RESULT {len(results) + 1} IN GENERATION {generation_number} ====')
            print(f'BEST SAMPLE RESULT = {last_best_result}\n\n\n')
            exit(1)
        mutations = mutate_best_samples(new_generations)
        generation_number = generation_number + 1

best_equations = []
for element in mutations[1]:
    best_equations.append(element[1])

print("The best values for x are: " + results)