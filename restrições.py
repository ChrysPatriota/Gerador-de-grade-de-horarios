import numpy as np

pesos = [10 ** 0, 10 ** 1, 10 ** 2, 10 ** 3]


# Função para percorer cada aula de cada dia e semestre
def avaliar(individuo):
    fitness = 0
    for semestre in range(6):
        for horario in range(6):
            for dia in range(5):
                if individuo[semestre][dia + horario * 5]['disciplina'] is not None:
                    fitness += avaliarAula(semestre, dia, horario, individuo)
    fitness += ocorrenciaJanelas(individuo)
    # fitness += densidadeAulaDia(individuo)
    return np.around(fitness, 2)


# Função para avaliar a aula
def avaliarAula(semestre, dia, horario, individuo):
    fitness = 0

    fitness += choqueProfessor(semestre, dia, horario, individuo)
    fitness += horarioImpropio(horario)

    # fitness += disponibilidadeProfessor(semestre, dia , horario, individuo)

    if individuo[semestre][dia + horario * 5]['disciplina']['cargaHoraria'] != 30:
        fitness += aulasMesmoDia(semestre, dia, horario, individuo)
        # fitness += aulasMesmoHorario(semestre, dia, horario, individuo)
        fitness += aulasTurnosDiferente(semestre, dia, horario, individuo)
        if individuo[semestre][dia + horario * 5]['disciplina']['cargaHoraria'] != 90:
            fitness += aulasMesmoHorario(semestre, dia, horario, individuo)
            # fitness += aulasTurnosDiferente(semestre, dia, horario, individuo)
            if dia != 2:
                fitness += aulasDistantes(semestre, dia, horario, individuo)

    return fitness


# Função para verificar choque de horário de professor
def choqueProfessor(semestre, dia, horario, individuo):
    fitness = 0
    contador = 1

    professor = individuo[semestre][dia + horario * 5]['professor']['nome']

    disp = individuo[semestre][dia + horario * 5]['professor']['disponibilidade']

    for semestre_it in disp:

        if semestre_it != semestre and individuo[semestre_it][dia + horario * 5]['disciplina'] is not None:

            professor_it = individuo[semestre_it][dia + horario * 5]['professor']['nome']

            if professor == professor_it:
                contador += 1
                fitness += pesos[3]

    return fitness  # / contador


# Função para verificar a disponibilidade do professor no dia e hora selecionados
def disponibilidadeProfessor(semestre, dia, horario, individuo):
    fitness = 0

    disponibilidade = individuo[semestre][dia + horario * 5]['professor']['disponibilidade'][dia + horario * 5]

    if disponibilidade == 0:
        fitness = pesos[3]
    return fitness


# Ocorrencia de aulas vagas
def ocorrenciaJanelas(individuo):
    fitness = 0

    for semestre in range(6):
        for aula in range(5):

            aula_manha_primeira = individuo[semestre][aula]['disciplina']
            aula_manha_segunda = individuo[semestre][aula + 5]['disciplina']

            aula_tarde_primeira = individuo[semestre][aula + 10]['disciplina']
            aula_tarde_segunda = individuo[semestre][aula + 15]['disciplina']

            aula_noite_primeira = individuo[semestre][aula + 20]['disciplina']
            aula_noite_segunda = individuo[semestre][aula + 25]['disciplina']

            if aula_manha_primeira is None and aula_manha_segunda is not None:
                fitness += pesos[0]

            if aula_tarde_primeira is None and aula_tarde_segunda is not None:
                fitness += pesos[0]

            if aula_noite_primeira is None and aula_noite_segunda is not None:
                fitness += pesos[0]

    return fitness


# Ocorrencia de mais de uma aula
def aulasMesmoDia(semestre, dia, horario, individuo):
    disciplina = individuo[semestre][dia + horario * 5]['disciplina']['nome']
    turma = individuo[semestre][dia + horario * 5]['turma']
    fitness = 0
    contador = 1

    for horario_it in range(6):

        if horario_it != horario:

            aula = individuo[semestre][dia + horario_it * 5]

            if aula['disciplina'] is not None:
                disciplina_it = aula['disciplina']['nome']
                turma_it = aula['turma']

                if turma_it == turma and disciplina_it == disciplina:
                    fitness += pesos[2]
                    contador += 1

    return fitness  # / contador


def aulasTurnosDiferente(semestre, dia, horario, individuo):
    aula = individuo[semestre][dia + horario * 5]
    disciplina = aula['disciplina']['nome']
    turma = aula['turma']
    fitness = 0
    contador = 1

    for dia_it in range(5):

        if horario == 0 or horario == 1:

            for horario_it in range(2, 6):

                aula_it = individuo[semestre][dia_it + horario_it * 5]

                if aula_it['disciplina'] is not None:

                    disciplina_it = aula_it['disciplina']['nome']
                    turma_it = aula_it['turma']
                    if disciplina_it == disciplina and turma_it == turma:
                        fitness += pesos[2]
                        contador += 1

        elif horario == 2 or horario == 3:

            for horario_it in range(2):

                aula_it = individuo[semestre][dia_it + horario_it * 5]

                if aula_it['disciplina'] is not None:

                    disciplina_it = aula_it['disciplina']['nome']
                    turma_it = aula_it['turma']
                    if disciplina_it == disciplina and turma_it == turma:
                        fitness += pesos[2]
                        contador += 1

            for horario_it in range(4, 6):

                aula_it = individuo[semestre][dia_it + horario_it * 5]

                if aula_it['disciplina'] is not None:

                    disciplina_it = aula_it['disciplina']['nome']
                    turma_it = aula_it['turma']
                    if disciplina_it == disciplina and turma_it == turma:
                        fitness += pesos[2]
                        contador += 1

        else:
            for horario_it in range(4):

                aula_it = individuo[semestre][dia_it + horario_it * 5]

                if aula_it['disciplina'] is not None:

                    disciplina_it = aula_it['disciplina']['nome']
                    turma_it = aula_it['turma']
                    if disciplina_it == disciplina and turma_it == turma:
                        fitness += pesos[2]
                        contador += 1

    return fitness  # / contador


def aulasDistantes(semestre, dia, horario, individuo):
    aula = individuo[semestre][dia + horario * 5]
    disciplina = aula['disciplina']['nome']
    turma = aula['turma']
    fitness = 0
    contador = 1

    if dia == 0 or dia == 1:

        for dia_it in range(3, 5):

            for horario_it in range(6):

                aula_it = individuo[semestre][dia_it + horario_it * 5]

                if aula_it['disciplina'] is not None:

                    disciplina_it = aula_it['disciplina']['nome']
                    turma_it = aula_it['turma']

                    if disciplina_it == disciplina and turma_it == turma:
                        fitness += pesos[2]
                        contador += 1
    else:

        for dia_it in range(2):

            for horario_it in range(6):

                aula_it = individuo[semestre][dia_it + horario_it * 5]

                if aula_it['disciplina'] is not None:

                    disciplina_it = aula_it['disciplina']['nome']
                    turma_it = aula_it['turma']
                    if disciplina_it == disciplina and turma_it == turma:
                        fitness += pesos[2]
                        contador += 1

    return fitness  # / contador


def aulasMesmoHorario(semestre, dia, horario, individuo):
    aula = individuo[semestre][dia + horario * 5]
    disciplina = aula['disciplina']['nome']
    turma = aula['turma']
    fitness = 0
    contador = 1

    for dia_it in range(5):

        aula_it = individuo[semestre][dia_it + horario * 5]

        if dia != dia_it and aula_it['disciplina'] is not None:

            disciplina_it = aula_it['disciplina']['nome']
            turma_it = aula_it['turma']

            if disciplina_it == disciplina and turma_it == turma:
                fitness += pesos[1]
                contador += 1

    return fitness  # / contador


def densidadeAulaDia(individuo):
    fitness = 0

    for semestre in range(6):
        contador = 0
        for dia in range(5):
            for horario in range(4):
                aula = individuo[semestre][dia + horario * 5]
                if aula['disciplina'] is not None:
                    contador += 1

        densidade = np.ceil(contador / 5)
        for dia in range(5):
            contador = 0
            for horario in range(4):
                aula = individuo[semestre][dia + horario * 5]
                if aula['disciplina'] is not None:
                    contador += 1
            if contador > densidade:
                fitness += pesos[1]

    return fitness


def horarioImpropio(horario):
    fitness = 0
    if horario == 4 or horario == 5:
        fitness += pesos[3]

    return fitness
