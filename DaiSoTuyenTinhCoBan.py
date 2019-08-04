# cong hai vector
def congHaiVector(vector1, vector2):
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

# tru hai vector
def truHaiVector(vector1, vector2):
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

# nhan vector voi mot so
def nhanVectorVoiMotSo(k, vector):
    return [k*v for v in vector]

# tich vo huong hai vector
def tinhTichVoHuongHaiVector(vector1, vector2):
    return sum([v1*v2 for v1, v2 in zip(vector1, vector2)])

# do dai vector
def tinhDoDaiVector(vector):
    return sum(v**2 for v in vector)**0.5

# cosine similarity: tính độ giống nhau giữa hai vector
def cosine_similarity(vector1, vector2):
    tu = tinhTichVoHuongHaiVector(vector1, vector2)
    mau1 = tinhDoDaiVector(vector1)
    mau2 = tinhDoDaiVector(vector2)
    mau = mau1 * mau2
    return tu / mau

# test vector
# vector1 = [1, 2, 3]
# vector2 = [4, 5, 6]
# print('v1 + v2 = ', congHaiVector(vector1, vector2))
# print('v1 - v2 = ', truHaiVector(vector1, vector2))
# print('v1 . v2 = ', tinhTichVoHuongHaiVector(vector1, vector2))
# print('|v1| = ', tinhDoDaiVector(vector1))
# print('|v2| = ', tinhDoDaiVector(vector2))
# print('consie_similarity(v1, v2) = ', cosine_similarity(vector1, vector2))

# cong hai ma tran
def congHaiMaTran(matrix1, matrix2):
    nrows = len(matrix1)
    ncols = len(matrix1[0])
    rs = [[0]*ncols for _ in range(nrows)]
    for i in range(nrows):
        for j in range(ncols):
            rs[i][j] = matrix1[i][j] + matrix2[i][j]
    return rs

# tru hai ma tran
def truHaiMaTran(matrix1, matrix2):
    nrows = len(matrix1)
    ncols = len(matrix1[0])
    rs = [[0]*ncols for _ in range(nrows)]
    for i in range(nrows):
        for j in range(ncols):
            rs[i][j] = matrix1[i][j] - matrix2[i][j]
    return rs

# nhan hai ma tran
def nhanHaiMaTran(matrix1, matrix2):
    nrows1 = len(matrix1)
    nrows2 = len(matrix2)
    ncols2 = len(matrix2[0])
    rs = [[0]*ncols2 for _ in range(nrows1)]
    for i in range(nrows1):
        for j in range(ncols2):
            for k in range(nrows2):
                rs[i][j] += matrix1[i][k] * matrix2[k][j]
    return rs

# vector chuyen vi
def chuyenVi(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    rs = [[0]*nrows for _ in range(ncols)]
    for i in range(nrows):
        for j in range(ncols):
            rs[j][i] = matrix[i][j]
    return rs

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 1, 2, 1], [1, 2, 1, 1], [1, 1, 1, 2]]
print('m1 * m2 = ', nhanHaiMaTran(matrix1, matrix2))
print('m1T = ', chuyenVi(matrix1))
