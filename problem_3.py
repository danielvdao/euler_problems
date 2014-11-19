import math
"""
The prime factors of 13195 are 5, 7, 13, and 29
What is the largest prime factor of the number 600851475143?
"""
def problem_three(): 
    n = 600851475143
    result = 0
    primes = [2]

    if n % 2 == 0:
        if n % 2 == 1:
            return 2 
        else:
            n /= 2

    result = determine_primes(primes, n)
    print result


def determine_primes(primes, n):
    for i in xrange(3, n, 2):
        if is_prime(primes, i):
            pass
        else:    
            if n % i == 0:
                if n / i == 1:
                    return i
                else:
                    n /= i

def is_prime(primes , n):
    for num in primes:
        if n % num == 0:
            return True
    
    primes.append(n)
    return False


if __name__ == '__main__':
    problem_three()

