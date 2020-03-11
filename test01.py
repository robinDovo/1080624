for i in range(2,101):
	count = 0
	for x in range(2,i+1):
		if i%x == 0:
			count += 1
	if count == 1:
		print(i,end=',')

number = int(input(""))

for i in range(number,0,-1):
	for x in range(1,i):
		print(x,end='')
	print()
	# else:
	# 	print(i)