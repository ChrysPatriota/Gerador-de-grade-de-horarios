import time

import matplotlib.pyplot as plt

from aulas_TI import aula_TI
from crossover import crossOverIndividuo as crossOver
from elitismo import elitismo
from individuo import criarPopulacao
from mutação import mutacao
from planilha import criarPlanilha
from reparador import repair
from restrições import avaliar
from seleção import selecao

inicio = time.time()

qtd = 20
geracoes = 5000
probabilidadeMutacao = 0.1
porcentagemElitismo = 0.1

populacao, fitness = criarPopulacao(aula_TI, qtd)

media = []
menor = []

for geracao in range(geracoes):

    if fitness[0] == 0:
        break

    populacaoNova = []
    fitnessNova = []

    for _ in range(qtd):
        pais = selecao(populacao, fitness, qtd)

        filho_1 = crossOver(pais[0], pais[1])

        filho_1 = mutacao(filho_1, probabilidadeMutacao)

        filho_1 = repair(filho_1)

        populacaoNova.append(filho_1)
        fitnessNova.append(avaliar(filho_1))

    populacao, fitness = elitismo(populacao, fitness, populacaoNova, fitnessNova, qtd, porcentagemElitismo)
    print(geracao)
    print(fitness)
    media.append(sum(fitness) / qtd)
    menor.append(min(fitness))

winner = populacao[0]

final = time.time()
print('Tempo de execução: ', (final - inicio) // 60, ' minutos')

criarPlanilha(winner)
plt.xlabel('Gerações')
plt.ylabel('Aptidão')
plt.plot(media)
plt.plot(menor, 'g')
plt.show()
