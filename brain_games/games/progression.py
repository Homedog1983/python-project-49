from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_answer() -> tuple:
    progression_start = randint(1, 5)
    progression_step = randint(1, 5)
    progression_n = randint(5, 15)
    progression_end = progression_start + progression_n * progression_step
    progression_options = progression_start, progression_end, progression_step
    progression = list(range(*progression_options))
    random_index = randint(0, progression_n - 1)  # index for replace to '..'
    right_answer = f'{progression[random_index]}'
    progression[random_index] = '..'
    question = ' '.join(str(item) for item in progression)
    return question, right_answer
