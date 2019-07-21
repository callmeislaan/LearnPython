# Đề bài: Assignment 2: Cho list data = [1, 2, 3, 4, 5, 6, 7, 8, 9]. 
# Các giá trị trong list thể hiện điểm số của mỗi phần tử.
# Phần tử đầu có điểm số nhỏ nhất là 1 và phần tử cuối có điểm số lớn nhất là 9.
# Yêu cầu đặt ra là chọn ngẫu nhiên 1000 phần tử từ list data, 
# và phần tử có điểm số lớn hơn nên được chọn nhiều hơn. 
# Các bạn hãy suy nghĩ và cài đặt chương trình thỏa mãn yêu cầu trên bằng nhiều cách nhất có thể.

# Cách 1 có thể là: Dựa vào điểm số để tính miền giá trị cho từng phần tử.
# Cụ thể miền giá trị của phần tử đầu tiên là 1 / N;
# trong đó N là tổng số điểm số. Phần tử thứ 2 là 2/N,…, và phần tử cuối là 9/N. 
# Tổng của các miền giá trị là 1. Sau đó, với mỗi số ngẫu nhiên r nằm trong đoạn [0,1], 
# xác định r nằm trong miền nào thì phần tử đó được chọn. Cuối cùng in số lần được chọn cho mỗi phần tử.

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

import numpy as np