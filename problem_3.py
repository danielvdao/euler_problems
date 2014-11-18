import math
"""
The prime factors of 13195 are 5, 7, 13, and 29
What is the largest prime factor of the number 600851475143?
"""
def problem_three(): 
    n = int(math.sqrt(600851475143))
    result = 0
    while n > 3:
        if is_prime(n) and 600851475143 % n == 0:
            result = n 
            break
        n -= 1
    print result

def is_prime(n):
    for i in xrange(3, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    problem_three()

