#!/usr/bin/env python3


import brain_games.cli as cli
import brain_games.even_game as even_game


def main():
    user_name = cli.welcome_user()
    even_game.even_game(user_name, 3, 100)


if __name__ == '__main__':
    main()
