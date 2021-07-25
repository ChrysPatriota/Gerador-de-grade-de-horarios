def repair(individual):
    individual = windowRepair(individual)

    return individual


def windowRepair(individual):
    for period, timetable in enumerate(individual):
        individual[period] = windowRepairPeriod(timetable)

    return individual


def windowRepairPeriod(period):
    class30hr = []

    for schedule, classes in enumerate(period):
        if classes['disciplina'] is not None:
            if classes['disciplina']['cargaHoraria'] == 30:
                if schedule < 5:
                    if period[schedule + 5]['disciplina'] is None:
                        class30hr.append(schedule)
                elif 10 <= schedule < 15:
                    if period[schedule + 5]['disciplina'] is None:
                        class30hr.append(schedule)
                elif 20 <= schedule < 25:
                    if period[schedule + 5]['disciplina'] is None:
                        class30hr.append(schedule)

    if class30hr:
        for schedule, classes in enumerate(period):
            if classes['disciplina'] is not None:
                if 5 <= schedule < 10:
                    if period[schedule - 5]['disciplina'] is None:
                        period[schedule - 5], period[class30hr[0]] = period[class30hr[0]], period[schedule - 5]
                        del class30hr[0]
                elif 15 <= schedule < 20:
                    if period[schedule - 5]['disciplina'] is None:
                        period[schedule - 5], period[class30hr[0]] = period[class30hr[0]], period[schedule - 5]
                        del class30hr[0]
                elif 25 <= schedule < 30:
                    if period[schedule - 5]['disciplina'] is None:
                        period[schedule - 5], period[class30hr[0]] = period[class30hr[0]], period[schedule - 5]
                        del class30hr[0]
            if not class30hr:
                break

    return period
