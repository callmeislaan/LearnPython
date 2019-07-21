# thực hiện các thao tác trên list trong python
data = [1, 2, 3, 4, 5, 6, 7]

# in ra danh sách
print(data)

# truy cập danh sách xuôi vd truy cập phần tử thứ 2
print(data[1])

# truy cập danh sách ngược
print(data[-2])

# listslicing
print(data[2:5])
print(data[:3])
print(data[3:])

# thay đổi giá trị của phần tử
data[0] = 0
print(data)

# thêm phần tử mới vào cuối danh sách
data.append(1)
print(data)

# nối hai danh sách
data1 = [1, 2, 3]
data2 = [4, 5, 6]
data3 = data1 + data2
print(data3)

# lặp lại danh sách n lần
print(data1*3)

# chèn một phần tử vào một vị trí danh sách)
data.insert(1, 10)
print(data)

# trả về vị trí xuất hiện đầu tiên của phần tử x
print(data.index(5))

# trả về số lần phần tử xuất hiện
data.append(5)
print(data.count(5))

# sắp xếp danh sách theo chiều tăng dần
data.sort()
print(data)

# sắp xếp danh sách theo chiều giảm dần
data.sort(reverse = True)
print(data)

# đảo ngược danh sách
data.reverse()
print(data)

# copy sang một danh sách khác
new_data = data.copy()
new_data.append(11)
print("data: ", data)
print("new_data: ", new_data)

# xóa một phần tử ở vị trí i
del data[1]
print(data)

# xóa nhiều phần tử từ i -> j
del data[2:4]
print(data)

# xóa một phần tử đầu tiên có giá trị là x
data.remove(5)
print(data)

# xóa toàn bộ danh sách
data.clear()
print(data)

# mảng 2 chiều
data2 = [[1, 2, 3], [4, 5]]

print(data2)
print(data2[0])
print(data2[0][0])
print(data2[1])
print(data2[0][1])
print(data2[1][0])

# tinh tong
s = 0
for i in data2:
    for j in i:
      s += j
print(s)  
