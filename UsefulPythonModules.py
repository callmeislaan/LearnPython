# một số mô đun sử dụng phổ biến trong python

# module os
import os
# os.getcwd() tra ve thu muc hien hanh
print(os.getcwd())
# os.path.join(): noi string
print(os.path.join('/images/', 'img1.png'))
# split(): tach path va filename
pathName = 'Users/Phuoc/images/logo.png'
(dir_name, file_name) = os.path.split(pathName)
print(dir_name)
print(file_name)

# module glob
import glob
# lay tat ca path cac file co duoi la .jpg
list_of_path = glob.glob('E:/Images/*.png')
print(len(list_of_path))

# module gzip
import gzip
# tao file gzip
data = 'Large content'
f = gzip.open('FileDemo/file.txt.gz', 'wb')
f.write(data.encode())
f.close()
# doc file gzip
f = gzip.open('FileDemo/file.txt.gz', 'rb')
file_data = f.read()
print(file_data.decode())
f.close()

# numpy
import numpy as np
# tao mot numpy array co 1 chieu
a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[1] = 7
print(a)
# tao 1 numpt array co 2 chieu
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])
# tao mot numpt co 2 chieu
# kieu unsigened int 8 bit (chua gia tri tu 0 den 255)
width = 300
height = 250
image = np.zeros((width, height), np.uint8)
print(image)

# python imaging library
from PIL import Image
# doc file anh
im = Image.open('Images/Sydney-Opera-House.jpg')
# in cac thuoc tinh cua anh
print(im.format, im.size, im.mode)
# chuyen sang anh grayscale
im = im.convert("L")
# resize anh
im = im.resize((128, 128))
# rotate anh 45 do
im = im.rotate(45)
# hien thi anh
#im.show()

# Matplotlib
import matplotlib.pyplot as plt
x_data = [0, 1, 2, 3]
y_data = [1, 3, 4, 2]
# plt.plot(x_data, y_data)
# plt.ylabel('y values')
# plt.xlabel('x values')
#plt.show()
# ham linear_space: sinh so trong khoang start -> stop
def linear_space(start, stop, num = 10):
    num = int(num)
    start = start * 1
    stop = stop * 1
    assert num > 1, 'num should be greater than 1'
    step = (stop - start) / num
    result = []
    for i in range(num):
        result.append(start + step*i)
    return result
print(linear_space(1, 10, 4))
# plot ham tanh dung ham linear_space()
import math
def tanh_function(data):
    return [(math.exp(x)-math.exp(-x)) / (math.exp(x) + math.exp(-x)) for x in data]
def tanh_function1(data):
    return [(2 / (1 + math.exp(-2 * x))) - 1 for x in data]
# calculate plot points
data = linear_space(-5., 5., 100)
# print(tanh_function(data))
# print(tanh_function1(data))
data_tanh = tanh_function1(data)
# dao ham cua tanh
def tanh_derivative(data):
    return [1 - x**2 for x in data]
data_dtanh = tanh_derivative(data)
# chinh la 4 truc
fig, ax = plt.subplots(figsize = (10, 5))
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# create and show plot
ax.plot(data, data_tanh, color="#d35400", linewidth = 3, label = 'tanh')
ax.plot(data, data_dtanh, color="#1abd15", linewidth = 3, label = 'derivative')
ax.legend(loc = 'upper left', frameon = False)
fig.show()