from random import randint
from math import gcd


def greeting():
    print('Find the greatest common divisor of given numbers.')


def eval():
    # for user's interest I'll partially simulate a, b
    a = randint(1, 10) * randint(1, 10)
    b = randint(1, 10) * randint(1, 30)
    question = str(a) + ' ' + str(b)
    right_answer = str(gcd(a, b))
    return question, right_answer
