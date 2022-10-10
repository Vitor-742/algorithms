def study_schedule(permanence_period, target_time):
    if not target_time and target_time != 0:
        return None
    count = 0
    for aluno in permanence_period:
        if type(aluno[0]) is not int or type(aluno[1]) is not int:
            return None
        if aluno[0] <= target_time <= aluno[1]:
            count += 1
    return count
