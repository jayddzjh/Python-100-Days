a = 12
b = 121.1212
c = "zjh"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
# type()函数，看类型

a = int(input("请输入数字a："))
b = int(input("请输入数字b："))

print("%d+%d=%d" % (a, b, a + b))
print("%d/%d=%f" % (a, b, a / b))

# 位运算
a = 10
res = ~a
print("原始数字:", a)
print("二进制表示:", bin(a))
print("按位取反后的结果:", res)
print("按位取反后的二进制表示:", bin(res))

# $C=(F - 32) \div 1.8$。
f = int(input("请输入华氏温度："))
c = (f - 32) / 1.8
print("%.1f华氏度 = %.1f摄氏度'" % (f, c))

s = "zjh"
print(s[1])
flag = True or False
print(flag)