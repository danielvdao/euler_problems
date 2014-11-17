"""
Find the sum of all multiples of 3 or 5 below 1000 
"""
def problem_one():
    result = 0
    for i in xrange(1, 1000):
        if i % 3 == 0 and i % 5 != 0: 
            result += i
        elif i % 3 != 0 and i % 5 == 0:
            result += i
        elif i % 3 == 0 and i % 5 == 0:
            result += i
        else:
            pass
    print result 

if __name__ == '__main__':
    problem_one()
