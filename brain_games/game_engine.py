import brain_games.games.even as even
import brain_games.games.calc as calc
import brain_games.games.gcd as gcd
import brain_games.games.progression as progression
import brain_games.games.prime as prime

# 'u' : 'user', 'g' : 'game', 'q' : 'question', 'qty' : 'quantity'

g_funcs = {
    'even': [even.greeting, even.eval],
    'calc': [calc.greeting, calc.eval],
    'gcd': [gcd.greeting, gcd.eval],
    'progression': [progression.greeting, progression.eval],
    'prime': [prime.greeting, prime.eval],
}


def game(u_name: str, g_name: str, q_qty: int) -> bool:
    g_funcs[g_name][0]()
    result = True
    for i in range(q_qty):
        question, right_answer = g_funcs[g_name][1]()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer != right_answer:
            result = False
            break
        print('Correct!')
    if result:
        print(f"Congratulations, {u_name}!")
    else:
        print(f"'{answer}' is wrong answer ;(.", end=' ')
        print(f"Correct answer was '{right_answer}'.")
        print(f"Let's try again, {u_name}!")
