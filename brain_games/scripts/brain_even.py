#!/usr/bin/env python3


from brain_games.games.even import eval, DESCRIPTION
from brain_games.game import engine


def main():
    # 'q_qty' : 'quantity of questions'
    q_qty = 3
    engine(eval, DESCRIPTION, q_qty)


if __name__ == '__main__':
    main()
