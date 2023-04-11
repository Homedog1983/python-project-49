import random


def even_game(user_name: str, qty: int, rand_stop: int) -> bool:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    result = True
    for i in range(qty):
        value = random.randint(1, rand_stop)
        is_even = value % 2 == 0
        right_answer = 'yes' if is_even else 'no'
        print(f"Question: {value}")
        answer = input("Your answer: ")
        correct_answers = ['yes', 'no']
        if answer not in correct_answers:
            result = False
            break
        elif answer != right_answer:
            result = False
            break
        print('Correct!')
    if result:
        print(f"Congratulations, {user_name}!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(.", end=' ')
        print(f"Correct answer was '{right_answer}'.")
        print(f"Let's try again, {user_name}!")
        return False
