import random


if __name__ == '__main__':
    test_cases = []
    i = 0
    while i < 5:
        random_array = random.sample(range(0, 30), 10)
        test_cases.append(random_array)
        i += 1
