# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:31:39 2021

@author: YJ-Dai
"""
import time
a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
a_print = a
b_print = b
# 可半者半之
n_2_in_a = 0
n_2_in_b = 0
while(a%2==0):
    n_2_in_a += 1
    a /= 2
    
while(b%2==0):
    n_2_in_b += 1
    b/=2

# 不可半者，副置分母、子之数
if(b>a):
    a, b = b, a
    
# 以少减多，更相减损，求其等也
c = a - b
while(c!=0):
    if(c > b):
        a, b = c, b
        c = a - b
    else:
        a, b = b, c
        c = a - b
# 最大公约数注意加上原来的2
GCD = a*2**min(n_2_in_a, n_2_in_b)
print("%d 和 %d 的最大公约数为 %d" % (a_print, b_print, GCD))

time.sleep(1)

# test
def GCD_minus(a,b):
    # 可半者半之
    n_2_in_a = 0
    n_2_in_b = 0
    while(a % 2 == 0):
        n_2_in_a += 1
        a /= 2

    while(b%2==0):
        n_2_in_b += 1
        b/=2

    # 不可半者，副置分母、子之数
    if(b>a):
        a, b = b, a
    
    # 以少减多，更相减损，求其等也
    c = a - b
    while(c!=0):
        if(c > b):
            a, b = c, b
            c = a - b
        else:
            a, b = b, c
            c = a - b
    # 最大公约数注意加上原来的2
    GCD = a*2**min(n_2_in_a, n_2_in_b)
    return GCD

def GCD_traverse(a,b):
    if(b > a):
        a, b = b, a
    for divider in range(b, 0, -1):
        if(a%divider==0 and b%divider==0):
            GCD = divider
            break
    return GCD

import random

a = [random.randint(1,1000) for i in range(10001)]
b = [random.randint(1,1000) for i in range(10001)]
start = time.time()
for i in range(10001):
    GCD_minus(a[i], b[i])
end = time.time()
print("It takes %f to loop 10000 times." % (end - start))