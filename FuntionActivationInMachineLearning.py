import math

# Hàm sigmoid
def sigmoid_funtion(data):
    result = []
    for d in data:
        result.append(1 / (1 + math.exp(-d)))
    return result

# hàm tanh
def tanh_funtion(data):
    result = []
    for d in data:
        result.append(2 / (1 + math.exp(-2 * d)) - 1)
    return result

# hàm ReLU
def ReLU_funtion(data):
    result = []
    for d in data:
        if d < 0:
            result.append(0)
        else:
            result.append(d)
    return result

# hàm PReLU
def PReLU_funtion(data, alpha):
    result = []
    for d in data:
        if d < 0:
            result.append(alpha * d)
        else:
            result.append(d)
    return result

# hàm ELU
def ELU_funtion(data, alpha):
    result = []
    for d in data:
        if d < 0:
            result.append(alpha * (math.exp(d) - 1))
        else:
            result.append(d)
    return result

# hàm SoftPlus
def SoftPlus_funtion(data):
    result = []
    for d in data:
        result.append(math.log(1 + math.e**d))
    return result

data = [1, 5, -4, 3, -2]
print("sigmoid: ", sigmoid_funtion(data))
print("tanh: ", tanh_funtion(data))
print("ReLU: ", ReLU_funtion(data))
print("PReLU: ", PReLU_funtion(data, 0.1))
print("ELU: ", ELU_funtion(data, 0.1))
print("SoffPlus: ", SoftPlus_funtion(data))
