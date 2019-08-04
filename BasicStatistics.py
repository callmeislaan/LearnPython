# Số liệu thống kê cơ bản
import time
from collections import Counter

# mean - giá trị trung bình
# hàm tính trung bình của dãy 
# 100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200
def calculate_mean(data):
    s = sum(data)
    n = len(data)
    mean = s / n
    return mean

start = time.time()
data = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
mean_value = calculate_mean(data)
print("Mean = ", mean_value)
print("time for calculate funtion calculate_mean = ", (time.time() - start)*1000)

# median - số trung vị: đứng ở giữa dãy nếu dãy lẻ
#                       trung bình 2 giá trị giữa dãy nếu dãy chẵn
def calculate_median(data):
    data.sort()
    n = len(data)
    m1 = int(n/2 + 1)
    m1 = m1 - 1
    if n % 2 != 0:
        median = data[m1]
    else:
        m2 = int(n/2)
        m2 = m2 - 1
        median = (data[m1] + data[m2])/2
    return median

print("Median = ", calculate_median(data))

# mode: phần tử xuất hiện nhiều nhất
def calculate_mode(points):
    c = Counter(points)
    mode = c.most_common()
    max_count = mode[0][1]
    modes = []
    for m in mode:
        if m[1] == max_count:
            modes.append(m[0])
    return modes
points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10, 6, 6]
print("most: ", calculate_mode(points))

# range of data - độ phân tán dữ liệu
def find_range(points):
    lowest = min(points)
    highest = max(points)
    r = highest - lowest
    print("lowest: {0}\thighest: {1}\trange: {2}".format(lowest, highest, r))
find_range(points)        

def caculate_variance(data):
    mean = calculate_mean(data)
    diff = []
    for d in data:
        diff.append(d-mean)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(data)
    return variance

del points[-1]
del points[-1]
print("Phương sai của dãy số: ", caculate_variance(points))
print("Độ lệch chuẩn của dãy số là: ", caculate_variance(points)**0.5)

# correlation coeffecient: Hệ số tương quan
def find_corr_x_y(x, y):
    n = len(x)
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi*yi)

    sum_prod_x_y = sum(prod)
    
    sum_x = sum(x)
    sum_y = sum(y)

    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2

    x_square = []
    for xi in x:
        x_square.append(xi**2)
    x_square_sum = sum(x_square)

    y_square = []
    for yi in y:
        y_square.append(yi**2)
    y_square_sum = sum(y_square)

    # thay lần lượt vào công thức
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator / denominator

    return correlation

x = [7, 18, 29, 2, 10, 9, 9]
y = [1, 6, 12, 8, 6, 21, 10]

print("Hệ số tương quan tuyến tính giữa hai biến x, y: ", find_corr_x_y(x, y))

# Dựa trên công thức tính hệ số tương quan chứng minh
# p(x, y) = p(x, y * a + b)

a = 2
b = 6
z = []
for i in y:
    i = i * a + b
    z.append(i)
corr_x_y = find_corr_x_y(x, y)
corr_x_z = find_corr_x_y(x, z)

print("corr_x_y = ", corr_x_y)
print("corr_x_z = ", corr_x_z)

# Tính hệ số tương quan giữa hai ảnh

import numpy as np
from PIL import Image

image1 = Image.open("Images/img1.png")
image2 = Image.open("Images/img2.png")
image3 = Image.open("Images/img3.png")
image4 = Image.open("Images/img4.png")

image1_list = np.asarray(image1).flatten().tolist()
image2_list = np.asarray(image2).flatten().tolist()
image3_list = np.asarray(image3).flatten().tolist()
image4_list = np.asarray(image4).flatten().tolist()

corr_1_2 = find_corr_x_y(image1_list, image2_list)
corr_1_3 = find_corr_x_y(image1_list, image3_list)
corr_1_4 = find_corr_x_y(image1_list, image4_list)

print("corr_1_2: ", corr_1_2)
print("corr_1_3: ", corr_1_3)
print("corr_1_4: ", corr_1_4)
