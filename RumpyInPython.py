import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.zeros(3)
print(b)

c = np.ones(4)
print(c)

d = np.zeros_like(c)
print(d)

# mang cap so cong
cc = np.arange(3)
print(cc)

dd = np.arange(2, 8)
print(dd)

ee = np.arange(0, 1, 0.2)
print(ee)

#Xây dựng mảng các luỹ thừa của 2 nhỏ hơn 1025, bao gồm cả 1 = 2**0.
#Gợi ý: Nếu a là một mảng và b là một số thì b**a sẽ trả về một mảng
#cùng kích thước với a mà phần tử có chỉ số i bằng b**a[i], 
# với ** là toán tử luỹ thừa.

a = np.arange(11)
b = 2
c = b**a
print(c)

#Xây dựng mảng gồm 10 phần tử, trong đó 9 phần tử đầu bằng 3, phần tử cuối cùng bằng 1.5.

a = np.ones(10)*3
a[9] /= 2
print(a)

#Lấy chiều dài: 

len = a.shape
print(len)
print(len[0])

#Cho trước một số tự nhiên n.
#Tạo một mảng có n phần tử mà các phần tử có chỉ số chẵn (bắt đầu từ 0)
#là một cấp số cộng bắt đầu từ 2, công sai bằng -0.5; 
#các phần tử có chỉ số lẻ bằng -1.

n = int(input("n = "))

a = np.ones(n)*-1
a[0] = 2
i = 2
t = 2
while(i < n):
    t += -0.5
    a[i] = t
    i += 2
    
print(a)

# Cho một mảng 1 chiều x, 
# tính mảng y và z sao cho y[i] = pi/2 - x[i] và z[i] = cos(x[i]) - sin(x[i]).
# Sau đó trả về tổng các phần tử của z

import math
x = np.arange(10)
print("x: ", x)

y = math.pi/2 - x
print("y: ", y)

z = np.cos(x) - np.sin(x)
print("z: ", z)
print("sum_z: ", np.sum(z))

# gia tri tuyet doi

print(np.abs(z))
print(np.sum(np.abs(z)))

def softmax_funtion(data):
    sm = []
    mau = np.sum(np.exp(data))
    print("mau: ", mau)
    for i in data:
        tu = np.exp(data[i])
        smi = tu / mau
        print("tu: ", tu)
        sm.append(smi)
    return sm

data = np.arange(10)
print("softmax_data: ", softmax_funtion(data))

print('.T and not')
a = np.array([1, 2])
print(a)
b = np.array([[1, 2], [3, 4]])
print(b)
c = np.array([1, 2]).T
print(c)
d = np.array([[1, 2, 3, 4], ['a', 'b', 'c', 'd']]).T
print(d)