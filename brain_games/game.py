from prompt import string
# 'q_qty' : 'quantity of questions'


def engine(game_eval, description, q_qty):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(description)
    result = True
    for i in range(q_qty):
        question, right_answer = game_eval()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer != right_answer:
            result = False
            break
        print('Correct!')
    if result:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"'{answer}' is wrong answer ;(.", end=' ')
        print(f"Correct answer was '{right_answer}'.")
        print(f"Let's try again, {user_name}!")
