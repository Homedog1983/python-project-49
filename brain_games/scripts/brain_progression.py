#!/usr/bin/env python3


import brain_games.cli as cli
import brain_games.game_engine as game_engine


def main():
    user_name = cli.welcome_user()
    game_name = 'progression'
    qty_of_questions = 3
    game_engine.game(user_name, game_name, qty_of_questions)


if __name__ == '__main__':
    main()
