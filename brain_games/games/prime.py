from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(test_value) -> bool:
    if test_value <= 2:
        return True
    max_div = round(sqrt(test_value))
    for div in range(2, max_div + 1):
        if test_value % div == 0:
            return False
    else:
        return True


def get_question_answer() -> tuple:
    # parameters for function's tuning
    max_value = 200

    value = randint(1, max_value)
    question = f'{value}'
    right_answer = 'yes' if is_prime(value) else 'no'
    return question, right_answer
