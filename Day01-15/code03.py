#  相同缩紧并且连续的代码行是属于一个代码块
a = 3
b = 1
if a == 1 and b == 1:
    print('ok')
elif a > 1 or b < 1:
    print('no')
    if a < 10 and b > -10:
        print('no1')
    else:
        print('no2')
else:
    print('other')
print('done')

# 循环
suma = 0
for x in range(1, 101):  # 1-100
    print('x=%d' % x)
    suma += x
print(suma)
