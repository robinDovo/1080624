# fruits = {'a':'apple','b':'banana','c':'crerry'}

# fruits['b'] = 'beer'
# fruits['d'] = 'duran'
# print(fruits)

# del fruits['a']
# print(fruits)

# fruits.clear()
# print(fruits)
# while name != '-1':
fruits = {'apple':'蘋果','banana':'香蕉','cherry':'櫻桃','orang':'橘子'}

while True:
	number = int(input('選項:1/2'))
	if number == 1:
		name = input('請輸入英文的水果名稱:')
		if fruits.get(name) == None:
			print('本店沒賣')
		else:
				print('水果為:',fruits[name])
	elif number == 2:
		name = input('輸入想刪除的水果名稱:')
		del fruits['name']
		print(fruits)

