#  __name__执行当前脚本的module名，直接执行该脚本的时候是main

if __name__ == '__main__':
    print('this is module code06_1')


def mul(*args):
    total = 1
    for num in args:
        total *= num
    return total


# 回文数判断,反转后，回文和之前的数相同
#  123
def is_hui(num):
    tmp = num
    total = 0
    while tmp > 0:
        remain = tmp % 10  # 123 余3
        tmp = tmp // 10  # 123 取整 12
        total = total * 10 + remain
    return num == total


print(is_hui(1221))

print('----------------')


def foo():
    b = 'hello'

    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()


def foo():
    aa = 200
    print(aa)  # 200


if __name__ == '__main__':
    aa = 100
    foo()
    print(aa)  # 100
