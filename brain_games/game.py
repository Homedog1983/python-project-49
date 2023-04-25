from prompt import string


QUEST_QTY = 3  # question's quantity


def start(game):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(game.DESCRIPTION)
    for _ in range(QUEST_QTY):
        question, right_answer = game.get_question_answer()
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
