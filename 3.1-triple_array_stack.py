import random

def pop(stack_num, test_arr):
    top = stack_pointers[stack_num]
    sub = 0
    if stack_num+1 in stack_pointers:
        sub = stack_pointers[stack_num+1]
    bottom = stack_num * len(test_arr) - sub
    print(bottom)
    popped = test_arr[pos]
    test_arr = test_arr[pos+1:]
    print("Popped %d from %s" % (popped, test_arr))


stack_pointers = {}
test_arr = random.sample(range(1, 100), 10)
print("Array is %s" % test_arr)
n = len(test_arr)

stack_1 = test_arr[0:n/3]
stack_pointers[0] = 0

stack_2 = test_arr[n/3:2*n]
stack_pointers[1] = n

stack_3 = test_arr[2*n:n]
stack_pointers[2] = 2*n

pop(0, test_arr)

#push(stack_pointers[1], test_arr)
#push(stack_pointers[2], test_arr)
#push(stack_pointers[3], test_arr)
