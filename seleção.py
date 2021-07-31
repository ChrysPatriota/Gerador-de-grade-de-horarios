import numpy as np


def selecao(populacao, fitness, qtd):
    probabilidade = probabilityVector(fitness, qtd)

    populacaoIndex = np.arange(qtd)

    escolhidos = np.random.choice(populacaoIndex, size=2, replace=False, p=probabilidade)

    retorno = []

    for i in range(2):
        index = escolhidos[i]
        retorno.append(populacao[index])

    return retorno


'''
def probabilityVector(fitness, qtd):
    soma = np.sum(fitness)

    if soma == 0:
        return 'break'

    fitness_copy = []

    for i in range(qtd):
        fitness_copy.append(soma - fitness[i])

    soma = np.sum(fitness_copy)

    for i in range(qtd):
        ajuda = (fitness_copy[i] / soma)
        fitness_copy[i] = ajuda

    return fitness_copy
'''


def probabilityVector(fitness, qtd):
    selecaoScore = []

    for i in range(qtd):
        score = 1 / (1 + fitness[i])
        selecaoScore.append(score)

    probabillityList = []

    for i in range(qtd):
        probability = selecaoScore[i] / np.sum(selecaoScore)
        probabillityList.append(probability)

    return probabillityList
