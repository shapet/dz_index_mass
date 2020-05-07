        # Практика

a = int(input('Введите число : '))
b = int(input('Введите число : '))
c = int(input('Введите число : '))


if (a, b, c) == 0:
    print('Введены все нули')
if a != 0 and b != 0 and c !=0:
    print('Нет нулевых значений!!!')
z = a or b or c
print(z)
if a > (b + c):
    print(a - b - c)
elif a < (b + c):
    print(b + c - a)            
if a > 50 and  (b > a or c > a):
    print("Вася")
if a > 5 or (b == 7 and c == 7):      
    print('Петя')


    # ДЗ
a = int(input('Введите число : '))
b = int(input('Введите число : '))
c = int(input('Введите число : '))


g = (a == 0 and b == 0 and c == 0 and 'Введены все нули') or ""
print(g)
v = (a != 0 and b != 0  and c != 0) and 'Нет нулевых значений!!!' or ''
print(v)
z = a or b or c or ''
print(z)
if a > (b + c):
    print(a - b - c)
elif a < (b + c):
    print(b + c - a)            
if a > 50 and  (b > a or c > a):0
print("Вася")
if a > 5 or (b == 7 and c == 7):      
    print('Петя')