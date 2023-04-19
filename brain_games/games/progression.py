from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def eval():
    n_rnd_stop = 15
    n_rnd_start = 5
    max_rnd_start = 20
    max_rnd_step = 5
    # 'pr' : 'progression', 'q' : 'question', 'i' : 'index of list'
    pr_start = randint(1, max_rnd_start)
    pr_step = randint(1, max_rnd_step)
    pr_n = randint(n_rnd_start, n_rnd_stop)
    pr_list = list(pr_start + _ * pr_step for _ in range(pr_n))
    pr_q_i = randint(0, pr_n - 1)
    right_answer = str(pr_list[pr_q_i])
    pr_str_list = list(map(str, pr_list))
    pr_str_list[pr_q_i] = '..'
    question = ' '.join(pr_str_list)
    return question, right_answer
