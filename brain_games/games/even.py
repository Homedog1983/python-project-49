from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_answer(test_value):
    return 'yes' if test_value % 2 == 0 else 'no'


def eval():
    max_value = 100
    value = randint(1, max_value)
    question = f'{value}'
    right_answer = is_even_answer(value)
    return question, right_answer
