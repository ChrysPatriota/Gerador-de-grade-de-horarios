import numpy as np


def mutacao(individuo, probabilidadeMutacao):
    opcoes = [True, False]

    probabilidade = [probabilidadeMutacao, 1 - probabilidadeMutacao]

    escolhido = np.random.choice(opcoes, size=1, p=probabilidade)

    if escolhido[0]:
        semestre = np.random.randint(6)

        horario = np.random.choice(np.arange(len(individuo[0])), size=2, replace=False)

        parte_1 = individuo[semestre][horario[0]]
        parte_2 = individuo[semestre][horario[1]]

        parte_1, parte_2 = parte_2, parte_1

        individuo[semestre][horario[1]] = parte_2
        individuo[semestre][horario[0]] = parte_1
        # individuo[semestre][horario[1]],individuo[semestre][horario[3]] = individuo[semestre][horario[3]],
        # individuo[semestre][horario[1]]

    return individuo


'''
lista = [1,2,3,4,5]

print(mutacao(lista,1))
'''
