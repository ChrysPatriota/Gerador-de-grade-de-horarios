import time

import matplotlib.pyplot as plt

from aulas import aula
from crossover import crossOverIndividuo as crossOver
from elitismo import elitismo
from individuo import criarPopulacao
from mutação import mutacao
from planilha import criarPlanilha
from restrições import avaliar
from seleção import selecao

inicio = time.time()

qtd = 100
geracoes = 2000
probabilidadeMutacao = 0.1
porcentagemElitismo = 0.05

populacao, fitness = criarPopulacao(aula, qtd)

media = []
menor = []

for geracao in range(geracoes):
    if fitness[0] != 0:
        populacaoNova = []
        fitnessNova = []

        for _ in range(qtd):
            pais = selecao(populacao, fitness, qtd)

            filho_1 = crossOver(pais[0], pais[1])

            filho_1 = mutacao(filho_1, probabilidadeMutacao)

            populacaoNova.append(filho_1)
            fitnessNova.append(avaliar(filho_1))

        populacao, fitness = elitismo(populacao, fitness, populacaoNova, fitnessNova, qtd, porcentagemElitismo)
        print(geracao)
        print(fitness)
        media.append(sum(fitness) / qtd)
        menor.append(min(fitness))
    else:
        break

winner = populacao[0]
'''
for semestre in range(6):
    print('Semestre ', semestre + 1)
    for dia in range(5):
        print()
        print('dia ', dia + 1)
        print()
        for horario in range(4):
            if winner[semestre][dia + horario * 5]['disciplina'] is None:
                print('Vaga', end=' ')
                print('ID: ', winner[semestre][dia + horario * 5]['ID'])
            else:
                print('Aula: ' + winner[semestre][dia + horario * 5]['disciplina']['nome'], end=' ')
                print('Turma: ', winner[semestre][dia + horario * 5]['turma'], end=' ')
                print('ID: ', winner[semestre][dia + horario * 5]['ID'])

    print('--------------------------------')'''

final = time.time()
print('Tempo de execução: ', (final - inicio) // 60, ' minutos')

criarPlanilha(winner)
plt.xlabel('Gerações')
plt.ylabel('Aptidão')
plt.plot(media)
plt.plot(menor, 'g')
plt.show()

'''
for individuo in range(10):
    print(ind.fitnessFunction(populacao[individuo]))



for semestre in range(3):
    for dia in range(5):
        for horario in range(4):
            if(populacao[0][semestre][dia + horario*5] is None):
                print(None)
            else:
                print(populacao[0][semestre][dia + horario*5]['disciplina']['nome'], end=' ')
                print(populacao[0][semestre][dia + horario*5]['id'])
    print('--------------------------------')

for semestre in range(3):
    for dia in range(5):
        for horario in range(4):
            if(populacao[1][semestre][dia + horario*5] is None):
                print(None)
            else:
                print(populacao[1][semestre][dia + horario*5]['disciplina']['nome'], end=' ')
                print(populacao[1][semestre][dia + horario*5]['id'])
    print('--------------------------------')

filhos = crossOver(populacao[0],populacao[0])


for semestre in range(3):
    for dia in range(5):
        for horario in range(4):
            if(filhos[0][semestre][dia + horario*5] is None):
                print(None)
            else:
                print(filhos[0][semestre][dia + horario*5]['disciplina']['nome'], end=' ')
                print(filhos[0][semestre][dia + horario*5]['id'])
    print('--------------------------------')

for semestre in range(3):
    for dia in range(5):
        for horario in range(4):
            if(filhos[1][semestre][dia + horario*5] is None):
                print(None)
            else:
                print(filhos[1][semestre][dia + horario*5]['disciplina']['nome'], end=' ')
                print(filhos[1][semestre][dia + horario*5]['id'])
    print('--------------------------------')
 

print(ind.fitnessFunction(populacao[0]))
print(ind.fitnessFunction(populacao[1]))
print(ind.fitnessFunction(filhos[0]))
print(ind.fitnessFunction(filhos[1]))
'''
