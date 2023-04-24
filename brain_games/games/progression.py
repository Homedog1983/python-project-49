from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def eval():
    n_start = 5
    n_stop = 15
    max_start = 20
    max_step = 5
    # 'progr' : 'progression'
    progr_start = randint(1, max_start)
    progr_step = randint(1, max_step)
    progr_n = randint(n_start, n_stop)
    progression = list(progr_start + i * progr_step for i in range(progr_n))
    # quest_i : index of progression to replace by '..' for question
    quest_i = randint(0, progr_n - 1)
    right_answer = f'{progression[quest_i]}'
    progression[quest_i] = '..'
    question = ' '.join(str(item) for item in progression)
    return question, right_answer
