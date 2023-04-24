from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_answer(test_value):
    if test_value <= 2:
        return 'yes'
    max_div = round(sqrt(test_value))
    for div in range(2, max_div + 1):
        if test_value % div == 0:
            return 'no'
    else:
        return 'yes'


def eval():
    max_value = 200
    value = randint(1, max_value)
    question = f'{value}'
    right_answer = is_prime_answer(value)
    return question, right_answer
