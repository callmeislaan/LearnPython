# giai bai toan x^2 - 4 = 0 với -5 <= x <= 5
# ham thich nghi: 100 - x^2 + 4 --> 100
import math
import numpy as np
import random

n_nst = 5
n_qt = 6

qt = np.zeros((n_qt, n_nst))
dtn = np.zeros(n_qt)

# tao quan the ban dau
def taoQuanTheBanDau():
    for i in range(n_qt):
        for j in range(n_nst):
            ran = random.randrange(0, 100)
            qt[i, j] = ran % 2
        dtn[i] = tinhDoThichNghi(qt[i])

def tinhDoThichNghi(nst):
    return int(1000 - chuyenSangCoSo10(nst)**2 + 4)

def chuyenSangCoSo10(nst):
    rs = 0
    hs = 1
    for k in range(1, n_nst + 1):
        rs += nst[-k] * hs
        hs *= 2
    return rs

def dotBien(nst):
    ran = random.randrange(0, n_nst)
    nst[ran] = 1 - nst[ran]

def laiGhep1(nst1, nst2):
    ran = random.randrange(1, n_nst - 1)
    nstc1 = nst1
    for i in range(0, ran):
        nstc1[i] = nst2[i]
    return nstc1

def laiGhep2(nst1, nst2):
    ran = random.randrange(1, n_nst - 1)
    nstc2 = nst2
    for i in range(0, ran):
        nstc2[i] = nst2[i]
    return nstc2

def chonLoc():
    tongDoThichNghi = sum(dtn)
    ran = random.randrange(0, tongDoThichNghi)
    r = 0
    for i in range(len(dtn)):
        r += dtn[i]
        if r >= ran:
            return i
    return len(dtn - 1)

if __name__ == '__main__':
    xs_laighep = 0.8
    xs_dotbien = 0.2
    # tao quan the ban dau
    taoQuanTheBanDau()
    # chay den khi nao co ket qua thi thoi
    while True:
        print(qt)
        print(dtn)
        # ktra dieu kien dung
        rs = 1000
        if rs in dtn:
            # lay ket qua
            kq = dtn.tolist()
            i = kq.index(rs)
            print('ket qua la: ', chuyenSangCoSo10(qt[i]))
            break
        
        # lua chon
        vt_nst1 = chonLoc()
        vt_nst2 = chonLoc()
        nst1 = qt[vt_nst1]
        nst2 = qt[vt_nst2]
        
        # lam viec voi nst con
        nstc1 = laiGhep1(nst1, nst2)
        nstc2 = laiGhep2(nst1, nst2)
        
        # dot bien con 1
        rand = random.random()
        if rand < xs_dotbien:
            dotBien(nstc1)

        # dot bien con 2
        rand = random.random()
        if rand < xs_dotbien:
            dotBien(nstc2)
        
        # cho hai nst con vao quan the: thay the vao 2 thang co dtn nho nhat
        # tim hai thang nho nhat
        dtn1 = []
        dtn1 = dtn.tolist()
        min1 = min(dtn1)
        vt_min1 = dtn1.index(min1)
        del dtn1[vt_min1]
        min2 = min(dtn1)
        vt_min2 = dtn1.index(min2)
        del dtn1
        qt[vt_min1] = nstc1
        qt[vt_min2] = nstc2
        dtn[vt_min1] = tinhDoThichNghi(nstc1)
        dtn[vt_min2] = tinhDoThichNghi(nstc2)
