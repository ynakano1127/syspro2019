# https://python.ms/sub/algorithm/prime/eratosthenes/#_2-%E9%AB%98%E9%80%9F%E7%89%88

import math

def is_sosu(target):
    dest = int(math.sqrt(target))
 
    for i in range(2,dest):
        if target % i == 0:
            return False
    return True

num = 10000
while True:
    if is_sosu(num):
        print(num)
    num = num + 1
