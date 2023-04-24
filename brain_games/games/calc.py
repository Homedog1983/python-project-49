from random import randint
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def eval():
    operators = {
        0: ['+', add],
        1: ['-', sub],
        2: ['*', mul]
    }
    random_n = randint(0, 2)
    max_value = 100
    a = randint(1, max_value)
    b = randint(1, max_value)
    question = f'{a} {operators[random_n][0]} {b}'
    right_answer = f'{operators[random_n][1](a, b)}'
    return question, right_answer
