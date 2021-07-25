import numpy
from numpy import random as rd

import restrições


# criar populacao
def criarPopulacao(aulas, qtd):
    populacao = []
    fitness = []

    for _ in range(qtd):
        individuo = criarIndividuo(aulas)
        populacao.append(individuo[0])
        fitness.append(individuo[1])

    return populacao, fitness


# declaração de individuo
def criarIndividuo(aulas):
    individuo = []

    for semestre in range(6):
        individuo.append(criarSemestre(aulas, semestre + 1))

    fitness = restrições.avaliar(individuo)

    return individuo, fitness


# criar semestre individuais
def criarSemestre(aulas, semestre):
    gradeHoraria = numpy.full(30, fill_value={'disciplina': None})

    ID = 0
    for aula in aulas:

        professores = aula['professor']

        for professor in range(len(professores)):

            turma = professor

            aula_nova = {
                'disciplina': aula['disciplina'],
                'professor': professores[professor],
                'turma': turma
            }

            if aula['disciplina']['cargaHoraria'] == 60 and aula['disciplina']['semestre'] == semestre:

                while True:
                    horario = rd.randint(6)
                    dia = rd.randint(5)

                    if gradeHoraria[dia + horario * 5]['disciplina'] is None:
                        break

                aula_copy = aula_nova.copy()
                aula_copy['ID'] = ID

                gradeHoraria[dia + horario * 5] = aula_copy

                ID += 1

                while True:
                    horario = rd.randint(6)
                    dia = rd.randint(5)

                    if gradeHoraria[dia + horario * 5]['disciplina'] is None:
                        break

                aula_copy = aula_nova.copy()
                aula_copy['ID'] = ID

                gradeHoraria[dia + horario * 5] = aula_copy

                ID += 1

            elif aula['disciplina']['cargaHoraria'] == 90 and aula['disciplina']['semestre'] == semestre:

                while True:
                    horario = rd.randint(6)
                    dia = rd.randint(5)

                    if gradeHoraria[dia + horario * 5]['disciplina'] is None:
                        break

                aula_copy = aula_nova.copy()
                aula_copy['ID'] = ID

                gradeHoraria[dia + horario * 5] = aula_copy

                ID += 1

                while True:
                    horario = rd.randint(6)
                    dia = rd.randint(5)

                    if gradeHoraria[dia + horario * 5]['disciplina'] is None:
                        break

                aula_copy = aula_nova.copy()
                aula_copy['ID'] = ID

                gradeHoraria[dia + horario * 5] = aula_copy

                ID += 1

                while True:
                    horario = rd.randint(6)
                    dia = rd.randint(5)

                    if gradeHoraria[dia + horario * 5]['disciplina'] is None:
                        break

                aula_copy = aula_nova.copy()
                aula_copy['ID'] = ID

                gradeHoraria[dia + horario * 5] = aula_copy

                ID += 1

            elif aula['disciplina']['cargaHoraria'] == 30 and aula['disciplina']['semestre'] == semestre:

                while True:
                    horario = rd.randint(6)
                    dia = rd.randint(5)

                    if gradeHoraria[dia + horario * 5]['disciplina'] is None:
                        break

                aula_copy = aula_nova.copy()
                aula_copy['ID'] = ID

                gradeHoraria[dia + horario * 5] = aula_copy

                ID += 1

    for restID in range(30):
        if gradeHoraria[restID]['disciplina'] is None:
            copy = gradeHoraria[restID].copy()
            copy['ID'] = ID
            gradeHoraria[restID] = copy
            ID += 1

    return gradeHoraria
