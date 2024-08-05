import os
import random
import sys
import time

s1 = 'hello, world!'
s2 = "hello, world!"
s3 = """
hello, 
  world!
"""
print(s1, s2, s3)

str2 = 'abc123456'
print(str2[:3])  # abc
print(str2[1:2])  # b
print(str2[::1])

f = [e for e in range(1, 10)]
print(f)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

f = [x + y for x in 'ABCDE' for y in '12345']
print(f)

f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


# 生成code_len长度的验证码
def auth_code(code_len):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    idx = len(all_chars) - 1
    code = ""
    for x in range(0, code_len):
        index = random.randint(0, idx)
        code += all_chars[index]
    return code


def get_suffix(file_name):
    split = file_name.split('.')
    return split[-1]


def main():
    # for val in fib(20):
    #     print(val)
    print(fib(3))
    print(auth_code(5))
    print(get_suffix(''))


if __name__ == '__main__':
    main()
