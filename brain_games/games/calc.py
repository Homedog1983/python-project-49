from random import randint
from operator import add, sub, mul

# 'op' : 'operator'

op_names = [' + ', ' - ', ' * ']
op_funcs = [add, sub, mul]
random_stop = 100


def greeting():
    print('What is the result of the expression?')


def eval():
    op_num = randint(0, 2)
    a = randint(1, random_stop)
    b = randint(1, random_stop)
    question = str(a) + op_names[op_num] + str(b)
    right_answer = str(op_funcs[op_num](a, b))
    return question, right_answer
