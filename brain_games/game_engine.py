import brain_games.games.even as even
import brain_games.games.calc as calc


# 'u' : 'user', 'g' : 'game', 'q' : 'question', 'qty' : 'quantity'
g_names = ['even', 'calc', ]
g_funcs = [
    [even.greeting, even.eval],
    [calc.greeting, calc.eval]
]


def game(u_name: str, g_name: str, q_qty: int) -> bool:
    g_num = g_names.index(g_name)
    g_funcs[g_num][0]()
    result = True
    for i in range(q_qty):
        question, right_answer = g_funcs[g_num][1]()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer != right_answer:
            result = False
            break
        print('Correct!')
    if result:
        print(f"Congratulations, {u_name}!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(.", end=' ')
        print(f"Correct answer was '{right_answer}'.")
        print(f"Let's try again, {u_name}!")
        return False
