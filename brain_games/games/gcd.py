from random import randint
from math import gcd

# 'rnd' : 'random'

rnd_stop_min = 10
rnd_stop_max = 30


def greeting():
    print('Find the greatest common divisor of given numbers.')


def eval():
    # for user's interest I'll partially simulate a, b
    a = randint(1, rnd_stop_min) * randint(1, rnd_stop_min)
    b = randint(1, rnd_stop_min) * randint(1, rnd_stop_max)
    question = str(a) + ' ' + str(b)
    right_answer = str(gcd(a, b))
    return question, right_answer
