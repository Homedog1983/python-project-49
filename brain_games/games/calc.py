from random import randint
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def get_question_answer() -> tuple:
    # parameters for function's tuning
    max_value = 100

    operations = {'+': add, '-': sub, '*': mul}
    random_n = randint(0, 2)
    random_operator = list(operations.keys())[random_n]
    a = randint(1, max_value)
    b = randint(1, max_value)
    question = f'{a} {random_operator} {b}'
    right_answer = f'{operations[random_operator](a, b)}'
    return question, right_answer
