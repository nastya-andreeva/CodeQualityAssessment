import random


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(2, 5)
    length = 10
    progression = [start * (step ** i) for i in range(length)]
    hid_ind = random.randint(0, length - 1)
    hid_value = progression[hid_ind]

    progression[hid_ind] = '..'

    return progression, hid_value


def brain_game():
    print("Welcome to the Brain Games!")

    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    print("What number is missing in the progression?")

    rounds = 3
    for _ in range(rounds):
        progression, hid_value = generate_progression()

        print(f"Question: {' '.join(map(str, progression))}")

        user_answer = int(input("Your answer: "))

        if user_answer == hid_value:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer "
                  f"was '{hid_value}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


brain_game()
