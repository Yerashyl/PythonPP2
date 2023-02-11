class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, number):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    return False
            return True
        return False

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_filter = PrimeFilter(numbers)
print(prime_filter.filter_primes())