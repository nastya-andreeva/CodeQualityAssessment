import math
import random


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_three(a, b, c):
    return lcm(lcm(a, b), c)


def brain_game():
    print("Welcome to the Brain Games!")

    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    print("Find the smallest common multiple of given numbers.")


    rounds = 3
    for _ in range(rounds):
        numbers = [random.randint(1, 20) for _ in range(3)]

        print(f"Question: {' '.join(map(str, numbers))}")

        user_answer = int(input("Your answer: "))

        correct_answer = lcm_three(numbers[0], numbers[1], numbers[2])

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    brain_game()
