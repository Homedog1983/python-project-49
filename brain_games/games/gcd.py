from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_answer() -> tuple:
    a = randint(1, 10) * randint(1, 10)
    b = randint(1, 30) * randint(10, 30)
    question = f'{a} {b}'
    right_answer = f'{gcd(a, b)}'
    return question, right_answer
