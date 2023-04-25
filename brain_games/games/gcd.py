from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_answer() -> tuple:
    # parameters for function's tuning
    min_value = 10
    max_value = 30

    a = randint(1, min_value) * randint(1, min_value)
    b = randint(1, min_value) * randint(1, max_value)
    question = f'{a} {b}'
    right_answer = f'{gcd(a, b)}'
    return question, right_answer
