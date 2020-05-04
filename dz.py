a = float(input('Введите ваш вес: '))
b = float(input('Введите ваш рост: '))
b = (b / 100)
c = (a / float(b**2))
print('Ваш индекс массы тела: ', int(c))
f = ('10' + "=" * int((c)- 10)) + "|" + '=' * (50 - int(c)) +'50'
print(f)