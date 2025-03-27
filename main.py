import games.nok as nok
import games.progression as progression
from games_logic import play_game

GAMES = [nok, progression]


def main():
    print("Choose a game:")
    print("1 - Least Common Multiple")
    print("2 - Geometric Progression")

    try:
        choice = int(input("Enter the number of a game: "))
        play_game(GAMES[choice - 1])
    except Exception:
        print("Incorrect choice!")


if __name__ == "__main__":
    main()
