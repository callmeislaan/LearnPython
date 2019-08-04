# bài toán fibonacci: in ra 10 số fibonacci đầu tiên
# cách 1: dùng vòng for
def fibonacci_for(n):
    fib = []
    after = 1
    bellow = 0
    for _ in range(n):
        rs = after + bellow
        fib.append(rs)
        after = bellow
        bellow = rs
    return fib

print("10 so fibonacci dau tien dung for: ", fibonacci_for(10))

def fibonacci_deQuy(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_deQuy(n - 1) + fibonacci_deQuy(n - 2)

fib = []
for i in range(10):
    fib.append(fibonacci_deQuy(i))
print("10 so fibonacci dung de quy: ", fib)

# Sử dụng quy hoạch động

def fibonacci_quyHoachDong(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]

print(fibonacci_quyHoachDong(10))

#Viết 3 hàm tính tổng của các số trong 1 dãy cho trước sử dụng for-loop, while-loop, và để quy.
def sum_use_for(data):
    sum_data = 0
    for i in data:
        sum_data += i
    return sum_data

def sum_use_while(data):
    sum_data = 0
    i = 0
    while(i < len(data)):
        sum_data += data[i]
        i += 1
    return sum_data

def sum_use_recursive(data, n):
    if n == 0:
        return data[n]
    else:
        return data[n] + sum_use_recursive(data, n - 1)


data = [1, 3, 5, 7, 9]

print("sum_use_for: ", sum_use_for(data))
print("sum_use_while: ", sum_use_while(data))
print("sum_use_recursive: ", sum_use_recursive(data, len(data) - 1))

#Viết 1 hàm kết hợp 2 dãy bằng cách xen kẽ các phần tử, 
# Ví dụ: cho 2 dãy [a, b, c] và [1, 2, 3], hàm trả về [a, 1, b, 2, c, 3].

def xenKe(x, y):
    n = len(x)
    z = []
    for i in range(n):
        z.append(x[i])
        z.append(y[i])
    return z

x = ["a", "b", "c"]
y = [1, 2, 3]
print("xen kẽ: ", xenKe(x, y))

#Viết 1 hàm nhận vào 1 dãy các số nguyên không âm, 
# sắp xếp chúng sao cho hợp thành 1 số lớn nhất có thể. 
# Ví dụ nhận vào dãy [40, 1, 99, 12], hàm trả về 9940121.

# [40, 1, 99, 12, 98, 9, 8, 934, 34, 32, 3]

def kiemTraHaiSo(x):
    return x[1]

def sapXep(data):
    data.sort(key = kiemTraHaiSo)
    return data

data = [40, 1, 99, 12]

print(sapXep(data))

print("end")


