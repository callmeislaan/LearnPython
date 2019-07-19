import random

def sinhNgaunhien():
    while True:
        ran = random.randint(0, 10)
        if ran == 5:
            continue
        return ran
num = sinhNgaunhien()
print("so ngau nhien la: %d" % num)
