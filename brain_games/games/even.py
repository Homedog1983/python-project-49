from random import randint


random_stop = 100


def greeting():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def eval():
    value = randint(1, random_stop)
    is_even = value % 2 == 0
    question = str(value)
    right_answer = 'yes' if is_even else 'no'
    return question, right_answer
