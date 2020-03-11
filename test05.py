import copy

data = [10,20,30,40]

print(data[0])
print(data[1:3])

data2 = list(data)
data2[0] = 100
data = tuple(data2)
data3 = copy.copy(data)
print(data)
print(data3)
