"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
def problem_two():
    fib_values = [[1, False], [2, False]] 
    flip = 0
    result = 0  
    while not check_bound(fib_values):
       val_one = fib_values[0]
       val_two = fib_values[1]
       if flip == 2:
           flip = 0

       if val_one[0] % 2 == 0 and val_one[1] == False:
           result += val_one[0]
           val_one[1] = True
       
       if val_two[0] % 2 == 0 and val_two[1] == False:
           result += val_two[0]
           val_two[1] = True
       
       fib_values[flip] = [fib_values[0][0] + fib_values[1][0], False]
       flip += 1
    print result
                           
def check_bound(fib_values):
    if fib_values[0][0] >= 4000000 or fib_values[1][0] >= 4000000:
        return True
    return False 

if __name__ == '__main__':
    problem_two()
