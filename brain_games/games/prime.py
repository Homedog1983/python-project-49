from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    max_div = round(sqrt(number))
    for div in range(2, max_div + 1):
        if number % div == 0:
            return False
    return True


def get_question_answer() -> tuple:
    number = randint(1, 200)
    question = f'{number}'
    right_answer = 'yes' if is_prime(number) else 'no'
    return question, right_answer
