import numpy as np

# tao mang ban dau
width = 10
height = 10

first_data = np.ones((height, width), np.uint8)

# tao sum area-table
def create_sum_area_table(data):
    sat = np.zeros((height, width), np.uint8)
    # cho phan tu khoi dau
    sat[0, 0] = data[0, 0]

    # cho dong dau tien
    for i in range(1):
        for j in range(1, width):
            sat[i, j] = sat[i, j-1] + data[i, j]
    
    # cho cot dau tien
    for j in range(1):
        for i in range(1, height):
            sat[i, j] = sat[i-1, j] + data[i, j]

    # cac cac chi cho ben trong
        for i in range(1, height):
            for j in range(1, width):
                sat[i, j] = sat[i - 1, j] + sat[i, j - 1] - sat[i - 1, j - 1] + data[i, j]

    print(sat)
create_sum_area_table(first_data)