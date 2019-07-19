# ước lượng số e
# cho trước e = 2.718281828
# công thức ước lượng: e≈1+1/1!+1/2!+…+1/n!
import math

sum_number = input("input sum number: ")

def tinhGiaiThua(n):
    giaiThua = 1
    for i in range(1, n):
        giaiThua = giaiThua * i
    return giaiThua

def uocLuongE():
    e = 0
    for i in range(1, 100):
        e = e + 1 / tinhGiaiThua(i)
    return e
print("e = ", uocLuongE())