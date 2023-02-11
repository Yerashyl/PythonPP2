def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False
def filter_prime(lst):
    for i in lst:
        if isPrime(i):
            print(i, end=" ")
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_prime(numbers)