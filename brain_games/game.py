from prompt import string


def engine(game_module):
    quest_qty = 3  # quantity of questions
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(game_module.DESCRIPTION)
    for _ in range(quest_qty):
        question, right_answer = game_module.eval()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer != right_answer:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
        else:
            print('Correct!')
    else:
        print(f"Congratulations, {user_name}!")
