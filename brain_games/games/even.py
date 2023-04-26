from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_question_answer() -> tuple:
    number = randint(1, 100)
    question = f'{number}'
    right_answer = 'yes' if is_even(number) else 'no'
    return question, right_answer
