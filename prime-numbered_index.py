'''
In this Kata, you will be given an integer array and your task
    is to return the sum of elements occupying prime-numbered indices.
'''

def total(arr):
    total = 0
    for i in range(2, len(arr)):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            total += arr[i]
    return total

def total(arr):
    return sum(arr[i] for i in range(len(arr)) if is_prime(i))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    print(total([1,2,3,4]))
    print(total([1,2,3,4,5,6]))
    print(total([1,2,3,4,5,6,7,8]))
    print(total([1,2,3,4,5,6,7,8,9,10,11]))
    print(total([1,2,3,4,5,6,7,8,9,10,11,12,13]))
    print(total([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

if __name__ == "__main__":
    main()