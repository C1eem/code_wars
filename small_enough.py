'''
You will be given an array and a limit value.
You must check that all values in the array are below or equal to the limit value.
If they are, return true. Else, return false.

You can assume all values in the array are numbers.
'''

def small_enough(array, limit):
    for i in array:
        if i > limit:
            return False
    return True

def small_enough_2(array, limit):
    return max(array)<=limit

def small_enough_3(array, limit):
    return all(a <= limit for a in array)

def main():
    print(small_enough([1, 2, 3, 4], 4))
    print(small_enough([1, 2, 3, 4], 3))

if __name__ == "__main__":
    main()