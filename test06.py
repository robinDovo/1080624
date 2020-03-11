import copy

# data = [10,20,30,40,50]

# data2 = copy.copy(data)

# data.append(100)

# print(data2)
# print(data)

students = [['John',90,60,30],['peter',60,100,60]]
print(students[0][0])
print('-'*30)
print(students[1][0])

for i in range(0,2):
	for x in range(0,4):
		print(students[i],[x])
print('-'*30)
for(name,man,eng,math)in students:
	print('%6s分數為:%d,%d,%d'%(name,man,eng,math))
