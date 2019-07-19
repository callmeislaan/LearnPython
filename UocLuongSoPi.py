import random
import math

sum_point = 1000000

def uocLuongPi():
    # lay hai so ngau nhien tu -1 den 1
    count_inside_cicle = 0
    for _ in range(sum_point):
        num1 = random.random()*2 - 1
        num2 = random.random()*2 - 1
        x1 = num1 * num1
        x2 = num2 * num2
        if math.sqrt(x1 + x2) <= 1:
            count_inside_cicle = count_inside_cicle + 1
    pi = 4 * count_inside_cicle / sum_point
    return pi
print("pi = ", uocLuongPi())
