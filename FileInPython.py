# Các thao tác trên file trong Python

# doc file HelloWorld.txt
filePath = 'FileDemo/HelloWorld.txt'
fielHandle = open(filePath, 'r')
data = fielHandle.read()
print(type(data))
print('-------------------')
print(data)
fielHandle.close()

# ghi file

filePath = 'FileDemo/MyFile.txt'
fielHandle = open(filePath, 'w')

text1 = 'writing line 1 \n'
fielHandle.write(text1)

text2 = 'writing line2 \n'
fielHandle.write(text2)

fielHandle.close()

# Hàm os.path.exlsts: kiểm tra file có tồn tại không
import os

filePath1 = 'FileDemo/myFile.txt'
check1 = os.path.exists(filePath1)
print('myFile.txt có tồn tại không?', check1)

filePath2 = 'FileDemo/nonExistenceFile'
check2 = os.path.exists(filePath2)
print('nonExistenceFile có tồn tại không?', check2)

# hàm split: cắt chuỗi

filePathStudent = 'FileDemo/Student.txt'
# fileHandleStudent = open(filePathStudent, 'a')
# fileHandleStudent.write('001,john,12-06-1999\n')
# fileHandleStudent.write('002,lena,13-07-1999\n')
# fileHandleStudent.write('003,adam,11-11-1998\n')
# fileHandleStudent.close()

fileReadStudent = open(filePathStudent, 'r')
line = []
for i in fileReadStudent:
    line.append(i)
fileReadStudent.close()
print(line) 
for i in range(len(line)):
    infor = line[i].split(',')
    print(infor[1])

# thực hành
# in ra muoi dong dau tien: tat ca bo qua id va header
data = []
filePath = 'FileDemo/Iris.csv'
fileHandle = open(filePath, 'r')
lines = fileHandle.readlines()
for i in range(1, len(lines)):
    string = lines[i].split(',')
    sepal_length = float(string[1].strip())
    sepal_width = float(string[2].strip())
    pendal_length = float(string[3].strip())
    pendal_width = float(string[4].strip())
    species = 0
    if string[5].strip() == 'Iris-cersicolor':
        species = 1
    elif string[5].strip() == 'Iris-virginica':
        species = 2
    data.append([sepal_length, sepal_width, 
    pendal_length, pendal_width, species])
fileHandle.close()
print(data[0])
print(data[1])
print(data[2])

# tính min, mean, max and standard deviation của 4 cột đặc trưng

sepal_length = []
sepal_width = []
pendal_length = []
pendal_width = []
for d in data:
    sepal_length.append(d[0])
    sepal_width.append(d[1])
    pendal_length.append(d[2])
    pendal_width.append(d[3])

import BasicStatistics as bs
print('min(sepal_length) = ', bs.calculate_mean(sepal_length))
print('min(sepal_width) = ', bs.calculate_mean(sepal_width))
print('min(pendal_length) = ', bs.calculate_mean(pendal_length))
print('min(pendal_width) = ', bs.calculate_mean(pendal_width))
# đếm số mẫu cho từng loài hoa
