import numpy as np

'''
def elitismo(populacaoAntiga, fitnessAntiga, populacaoNova, fitnessNova, qtd):
    populacaoUnida = populacaoAntiga + populacaoNova
    fitnessUnida = fitnessAntiga + fitnessNova

    aux = list(np.arange(qtd * 2))

    zipped = zip(fitnessUnida, aux)

    fitnessElitismo = []
    populacaoElitismo = []

    for fitness, populacao in sorted(zipped):
        populacaoElitismo.append(populacaoUnida[populacao])
        fitnessElitismo.append(fitness)

    length = len(populacaoElitismo)
    middle_index = length // 2

    first_half = populacaoElitismo[:int((qtd*0.2))] + populacaoNova[int((qtd*0.2)):]
    first_half2 = fitnessElitismo[:int((qtd*0.2))] + fitnessNova[int((qtd*0.2)):]

    # first_half = populacaoElitismo[:middle_index]
    # first_half2 = fitnessElitismo[:middle_index]

    return first_half, first_half2
'''


def elitismo(populacaoAntiga, fitnessAntiga, populacaoNova, fitnessNova, qtd, porcentagem):
    aux = list(np.arange(qtd))
    populacaoAntigaZipped = zip(fitnessAntiga, aux)
    populacaoAntigaZipped = sorted(populacaoAntigaZipped)

    fitnessElitismo = []
    populacaoElitismo = []
    qtdElitismo = int(round(qtd * porcentagem))
    for i in range(qtdElitismo):
        fitnessElitismo.append(populacaoAntigaZipped[i][0])
        populacaoElitismo.append(populacaoAntiga[populacaoAntigaZipped[i][1]])

    return [populacaoElitismo + populacaoNova[qtdElitismo:qtd], fitnessElitismo + fitnessNova[qtdElitismo:qtd]]
