from random import randint


random_stop = 100


def greeting():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def eval():
    value = randint(1, random_stop)
    question = str(value)
    right_answer = 'yes' if value % 2 == 0 else 'no'
    return question, right_answer
