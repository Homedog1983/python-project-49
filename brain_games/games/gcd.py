from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def eval():
    rnd_stop_min = 10
    rnd_stop_max = 30
    a = randint(1, rnd_stop_min) * randint(1, rnd_stop_min)
    b = randint(1, rnd_stop_min) * randint(1, rnd_stop_max)
    question = str(a) + ' ' + str(b)
    right_answer = str(gcd(a, b))
    return question, right_answer
