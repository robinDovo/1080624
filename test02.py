# data = [100,80,60,89,70,30,45]
# data.sort()
# print(data)

data = list()
number = 0
while number != -1:

	number = int(input('請輸入隨意數字:'))
	if number != -1:
		data.append(number)
	print(data)
	data.sort()#小到大排序
	print(data)
	data.sort(reverse = True)#大到小排序
	print(data)


