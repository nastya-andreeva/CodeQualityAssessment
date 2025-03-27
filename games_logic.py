def play_game(game):
    print("Welcome to the Brain Games!")

    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)

    rounds = 3
    for _ in range(rounds):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")

        user_answer = input("Your answer: ")

        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct "
                  f"answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
