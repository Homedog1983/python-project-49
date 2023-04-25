from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(test_value) -> bool:
    return True if test_value % 2 == 0 else False


def get_question_answer() -> tuple:
    # parameters for function's tuning
    max_value = 100

    value = randint(1, max_value)
    question = f'{value}'
    right_answer = 'yes' if is_even(value) else 'no'
    return question, right_answer
