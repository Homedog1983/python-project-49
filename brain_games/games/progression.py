from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_answer() -> tuple:
    # parameters for function's tuning
    n_start = 5
    n_stop = 15
    max_start = 20
    max_step = 5

    progression_start = randint(1, max_start)
    progression_step = randint(1, max_step)
    progression_n = randint(n_start, n_stop)
    progression = list(progression_start + i * progression_step for i in range(progression_n))  # noqa: E501
    question_i = randint(0, progression_n - 1)  # index for replace to '..'
    right_answer = f'{progression[question_i]}'
    progression[question_i] = '..'
    question = ' '.join(str(item) for item in progression)
    return question, right_answer
