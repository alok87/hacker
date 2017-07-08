import random
import sys
import math


def biggest_no(arr):
    i = 0
    while i < len(arr) - 1:
        # print(arr)
        j = i + 1
        while j != 0:
            elem1 = arr[j]
            elem2 = arr[j-1]
            # print("elem1 and elem2 %d %d" % (elem1, elem2))
            diff = len(str(elem2)) - len(str(elem1))
            # print("diff is %d" % diff)
            if diff > 0:
                elem1 += elem1 * int(math.pow(10, diff))
            elif diff < 0:
                diff = diff * -1
                elem2 += elem2 * int(math.pow(10, diff))
            else:
                pass
            if elem2 > elem1:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
            j -= 1
        i += 1
    return arr[::-1]

if __name__ == '__main__':
    test_cases = []
    i = 0
    while i < 1:
        random_array = random.sample(range(0, 30), 10)
        test_cases.append(random_array)
        i += 1
    test_cases.append([1, 34, 3, 98, 9, 76, 45, 4])
    test_cases.append([54, 546, 548, 60])

    for test_case in test_cases:
        print("Array %s" % test_case)
        sys.stdout.write("Biggest no: ")
        for i in biggest_no(test_case):
            sys.stdout.write(str(i))
        print("\n")
