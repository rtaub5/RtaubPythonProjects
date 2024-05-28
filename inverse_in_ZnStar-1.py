# Author: Rocki Taub
# Assignment: PA01
# Date: February 14, 2024
# This program calculates the inverses in Zn*, and also checks for numbers with no inverses

def inverse(base, num):
    # put in a check for base to be rp to num
    gcf = gcd(base, num)
    if (gcf != 1):
        raise Exception("Sorry, these two numbers are not relatively prime and will not have an inverse.")
    else:
        product = num
        for power in range(1, base):
            if product == 1:
                break
            else:
                product = num * power
                product %= base
        answer = power - 1
    return answer


# finds the gcd using Euclidean's algorithm
def gcd(a, b):
    if (a == b):
        answer = a
    else:
        bigger_num = (a if a >= b else b)
        smaller_num = (b if b != bigger_num else a)
        while (smaller_num != 0):
            remainder = bigger_num % smaller_num
            bigger_num = smaller_num
            smaller_num = remainder
        answer = bigger_num
    return answer
              
        
    
    


max_base = 30
 
for base in range(10,max_base):
    for num in range(1, base):
        try:
            print(f"base: {base} num: {num}")
            print(f"inverse of {num} base {base} = {inverse(base, num)}")
        except:
            print(f"skipping {num}")
 

                          
