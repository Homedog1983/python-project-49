from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def eval():
    random_stop = 100
    value = randint(1, random_stop)
    question = str(value)
    right_answer = 'yes' if value % 2 == 0 else 'no'
    return question, right_answer
