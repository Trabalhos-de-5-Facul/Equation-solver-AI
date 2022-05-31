import random
import sys
import numpy as np

population_size = 1000
default_variation = 100
bests_sample_size = 10
bests_sample_use_size = 3
start_sample = [0.]
results = []
qnt_results = 2
max_repetitive_tries = 5
MAX_GENERATIONS = 200

# Resolve a equação com o valor de x passado e retorna o resultados
def equation(x):
    return eval(equacao)


# Define a recompença a ser recebida baseada na proximidade com o resultado esperado
def equation_reward(x):
    # resolve a equação com o valor de x parametrizado
    ans = equation(x)
    # Se a resposta for 0, significa que é uma raiz
    if ans == 0:
        return sys.maxint
    # Senão, retorna uma recompensa baseada na resposta encontrada: quanto melhor a resposta, maior a recompensa
    else:
        return abs(1 / ans)


# Gera uma população de amostra
def generate_population_sample(x_variation, subject):
    # Criando uma lista de amostras vazia
    sample = []
    # Loop para popular a lista de amostras
    for _ in range(population_size):
        # Cria as amostras baseadas em um sujeito base, criando amostras com valores que "orbitam" o
        # valor do sujeito base, com uma distancia de até x_variation
        sample.append((subject[0] + random.uniform(-x_variation, x_variation)))
    # Retornando a lista de amostras
    return sample

# Gera uma nova geração baseada no valor x_variation e um sujeito a ser mutado
def create_new_generation(x_variation, mutated_subject):
    # Criando amostra populacional baseada nos parametros passados
    sample = generate_population_sample(x_variation, mutated_subject)
    # Criando uma lista vazia dos resultados da população
    population_results = []
    # Para cada sujeito na lista de amostras
    for subject in sample:
        # Registra os resultados do valor da amostra, utilizando a função equation_reward
        # para definir a proximidade com uma raiz da equação
        population_results.append((equation_reward(subject), subject))
    # Ordena os resultados
    population_results.sort()
    # Reverte a ordenação, pois recompensar maiores representam amostras melhores
    population_results.reverse()
    # retorna os resultados
    return population_results


# Gera novas amostras que são derivadas das melhores amostras da população anterior
def mutate_best_samples(population_results):
    # Recolhe as melhores amostras
    bests_sample = population_results[0:bests_sample_size]
    # Recolhe as melhores amostras que podem devem ser reutilizadas
    bests_sample_use = population_results[0:bests_sample_use_size]
    # Cria variações mutadas das melhores amostras
    variations = mutate_variations(bests_sample)
    # Retorna as variações mutadas e as melhores amostras
    return variations, bests_sample_use

# Muta as variações
def mutate_variations(bests_sample):
    # Cria uma lista vazia de elementos X
    x_elements = []
    # Para cada um em na lista de melhores amostras
    for subject in bests_sample:
        x_elements.append(subject[1])

    x_variation = default_variation
    if default_variation > np.var(x_elements):
        x_variation = np.var(x_elements)

    return [x_variation]

# iniciando o algoritmo na geração 0
generation_number = 0
# recolhendo a equação que deve ser resolvida
equacao = input("Digite o polinômio desejado\n")
# Enquanto ainda não forem encontrado o numero de raizes esperado
while len(results) < qnt_results:
    # Cria a geração 0 a partir da variação definida inicialmente e o valor inicial 0
    gen0 = create_new_generation(default_variation, start_sample)
    # Cria as mutações da geração 0
    mutations = mutate_best_samples(gen0)
    # Inicializa repetições com 0
    repetition = 0
    # Faz MAX_GENERATIONS repetições
    for _ in range(MAX_GENERATIONS):
        # Cria uma lista vazia de melhores soluções
        best_equations = []
        # Para cada elemento de mutations[1]
        for element in mutations[1]:
            # Anexa o valor de element[1] (sujeito que alcançou o resultado)
            best_equations.append(element[1])
        # Para toda geração que não é a primeira
        if generation_number != 0:
            # Se a recompensa conseguida pela melhor equação não for igual ao melhor resultado anterior
            if best_equations[0] != last_best_result:
                # Printa o melhor resultado e atualiza o melhor resultado como sendo o novo melhor
                print(f'==== RESULT {len(results) + 1} GENERATION {generation_number} ====')
                print(f'BEST SAMPLE RESULT = {best_equations[0]}\n\n\n')
                last_best_result = best_equations[0]
            # Senão (best_equations[0] == last_best_result)
            else:
                # Soma um em repetition
                repetition = repetition + 1
                # Se repetition alcançar o numero maximo de tentativas
                if repetition == max_repetitive_tries:
                    # Para cada resultado em results
                    for result in results:
                        # Se a variação entre o resultado e o melhor resultado anterior for maior que -0.1
                        if 0.1 > result - last_best_result > -0.1:
                            # Printa essa variação
                            print(result - last_best_result)
                            # Reseta o melhor resultado anterior com um valor exorbitante
                            last_best_result = 999999999999999
                    # Se o melhor resultado anterior for diferente de um valor exorbitante
                    if last_best_result != 999999999999999:
                        # Reseta o contador repetições
                        repetition = 0
                        # Anexa o melhor valor anterior na lista de resultados
                        results.append(last_best_result)
                        # Reseta a geração para a primeira
                        generation_number = 0
                    break
        # Para a primeira geração
        else:
            # Inicia o melhor valor anterior como sendo o melhor valor alcançado pelas amostras
            last_best_result = best_equations[0]

        # Cria uma lista vazia de novas gerações
        new_generations = []
        # Repete um numero de vezes igual ao numero de melhores equações
        for i in range(len(best_equations)):
            # Cria novas gerações com a x_variation baseada na mutação gerada
            new_generations = new_generations + create_new_generation(mutations[0][0],
                                                                      best_equations)
        new_generations.sort()
        new_generations.reverse()
        if generation_number >= MAX_GENERATIONS-1:
            print("TRY CHANGING THE PARAMETERS")
            print("The best values for x are: ", results)
            print(f'==== BEST RESULT {len(results) + 1} IN GENERATION {generation_number} ====')
            print(f'BEST SAMPLE RESULT = {last_best_result}\n\n\n')
            exit(1)
        mutations = mutate_best_samples(new_generations)
        generation_number = generation_number + 1
    if generation_number >= MAX_GENERATIONS:
            print("TRY CHANGING THE PARAMETERS")
            print("The best values for x are: ", results)
            print(f'==== BEST RESULT {len(results) + 1} IN GENERATION {generation_number} ====')
            print(f'BEST SAMPLE RESULT = {last_best_result}\n\n\n')
            exit(1)
best_equations = []
for element in mutations[1]:
    best_equations.append(element[1])

print("The best values for x are: " , results)