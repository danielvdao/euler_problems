def problem_four():
    max_product = 0 
    
    for i in xrange(100, 1000):
        for j in xrange(i, 1000):
            cur = i * j
            if is_palindrome(cur) and cur > max_product:
                max_product = cur

    print max_product

def is_palindrome(num):
    str_num = str(num)
    beg = 0
    end = len(str_num) - 1

    while beg <= end:
        if str_num[beg] != str_num[end]:
            return False
        beg += 1
        end -= 1

    return True

if __name__ == '__main__':
    problem_four()
