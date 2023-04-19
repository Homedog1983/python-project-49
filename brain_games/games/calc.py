from random import randint
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def eval():
    random_stop = 100
    operators = [' + ', ' - ', ' * ', add, sub, mul]
    rnd_op_num = randint(0, 2)
    a = randint(1, random_stop)
    b = randint(1, random_stop)
    question = str(a) + operators[rnd_op_num] + str(b)
    right_answer = str(operators[rnd_op_num + 3](a, b))
    return question, right_answer
