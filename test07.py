dict1 = {1:'first',2:'second'}

dict2 = dict(a ='apple',b ='beer',c ='car')

dict3 = dict([['a','apple'],['b','beer']])

print(dict1[2])
print(dict2['a'])
print(dict3['a'])

data = {'car':'BR-123','apple':'蘋果'}
print(data['car'])
print(data.get('apple'))
print(data.get('banana'))