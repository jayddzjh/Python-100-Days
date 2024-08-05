import code06_1 as module6_1

print('this is module 06')

mul = module6_1.mul(1, 2, 3)
print('mul:%d' % mul)


# 参数默认值
def max_num(num1=0, num2=0):
    if num1 >= num2:
        return num1
    else:
        return num2


mm = max_num(1)  # 1传给了num1变量
print(mm)
m = max_num(num2=13)  # 可以指定特定参数赋值
print(m)

mmm = max_num(121, 3)
print(mmm)


#  可变参数
def add_num(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add_num())
print(add_num(1))
print(add_num(1, 2))
