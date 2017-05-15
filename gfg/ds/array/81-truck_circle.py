import random

class PetrolPump:
    def __init__(self, petrol, kms):
        self.petrol = petrol
        self.kms = kms


def truck_circle(pumps):
    n = len(pumps)
    mileage = 1
    start = 0
    end = 1
    curr_petrol = pumps[0].petrol - (pumps[0].kms/mileage)

    # Keep checking till we are able to complete a round trip(start=end)
    # and we have petrol also left(>=0) after the trip
    while start != end or curr_petrol < 0:
        while curr_petrol < 0 and start != end:
            # Remove the starting petrol pump considered
            curr_petrol = curr_petrol - (pumps[start].petrol - (pumps[start].kms/mileage))
            # Consider a new starting petrol pump
            start = (start + 1) % n
            if start == 0:
                return -1
        print("Considering starting petrol-pump:%d" % start)
        curr_petrol = curr_petrol + (pumps[end].petrol - pumps[end].kms/mileage)
        # Incrementing end in a circular track
        end = (end + 1) % n
        print('Petrol after travelling start(%d) to end(%d) = %d' % (start, end, curr_petrol))
    return start


if __name__ == '__main__':
    test_cases = []
    j = 0
    while j < 3:
        pumps = []
        i = 0
        while i < 3:
            pumps.append(PetrolPump(random.randint(2, 10), random.randint(2, 10)))
            i += 1
        test_cases.append(pumps)
        j += 1
    test_cases.append([PetrolPump(6,4), PetrolPump(3,6), PetrolPump(7,3)])
    for test_case in test_cases:
        print("Evaluating case ----")
        k = 0
        for t in test_case:
            print("Petrolpump:%d \t lts: %d\t next_kms: %d" % (k, t.petrol, t.kms))
            k += 1
        result = truck_circle(test_case)
        if result ==  -1:
            print('No soultion\n')
        else:
            print('Starting from petrol pump %d we can complete the circle with petrol in hand\n' % result)
