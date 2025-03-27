import math
import random

DESCRIPTION = "Find the smallest common multiple of given numbers."


def nok(a, b):
    return abs(a * b) // math.gcd(a, b)


def nok_three(a, b, c):
    return nok(nok(a, b), c)


def generate_round():
    numbers = [random.randint(1, 30) for _ in range(3)]
    question = ' '.join(map(str, numbers))
    correct_answer = nok_three(*numbers)
    return question, correct_answer
