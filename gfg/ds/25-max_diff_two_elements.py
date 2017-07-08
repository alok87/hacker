import random


def max_diff_1(arr):
    """Returns a max diff in an array with largest no having higher index
       T = O(n^2)
    """
    i = 0
    max_diff = arr[1] -arr[0]
    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr) - 1:
            if arr[j] - arr[i] > max_diff:
                max_diff = arr[j] - arr[i]
            j += 1
        i += 1
    return max_diff


def max_diff_2(arr):
    """Better algo to return max diff T = O(n)
    """
    i = 0
    min_elem = arr[0]
    max_diff = arr[1] - arr[0]
    while i < len(arr) - 1:
        if arr[i] < min_elem:
            min_elem = arr[i]
        diff = arr[i] - min_elem
        if diff > max_diff:
            max_diff = diff
        i += 1
    return max_diff


if __name__ == '__main__':
    test_cases = [[2, 3, 10, 6, 4, 8, 1]]
    i = 0
    while i < 5:
        random_array = random.sample(range(0, 30), 10)
        test_cases.append(random_array)
        i += 1

    for test_case in test_cases:
        print("Max diff for list[O(n^2)] %s is %d" % (test_case, max_diff_1(test_case)))
        print("Max diff for list[O(n)] %s is %d\n" % (test_case, max_diff_2(test_case)))
