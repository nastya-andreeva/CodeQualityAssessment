import random

DESCRIPTION = "What number is missing in the progression?"


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(2, 5)
    length = 10
    progression = [start * (step ** i) for i in range(length)]
    hid_ind = random.randint(0, length - 1)
    hid_value = progression[hid_ind]
    progression[hid_ind] = '..'
    return progression, hid_value


def generate_round():
    progression, hid_value = generate_progression()
    question = ' '.join(map(str, progression))
    return question, hid_value
