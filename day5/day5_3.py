"""
输出100以内的全部素数
素数是只能被1和他自己整除的数
例如：1，3，5

Version = 0.1
Author = St
"""
import math
for num in range(1, 101):#2-99range(2,100)
    is_prime = True
    for factor in range(2, int(math.sqrt(num) + 1)):
        if num % factor == 0:
            is_prime = False
            continue #break
    if is_prime:
        print(num)#print(num, end = ' ')
