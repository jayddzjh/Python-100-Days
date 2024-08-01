# 水仙花数
for num in range(100, 1000):  # 100-999
    low = num % 10
    mid = num // 10 % 10
    hig = num // 100
    if low ** 3 + mid ** 3 + hig ** 3 == num:
        print('找到一个水仙花数：%d' % num)

# 整数反转
num = int(input('请输入一个整数：'))
reversed_num = 0
while num > 0:
    remain = num % 10  # 整数对10求余，可得最后一位
    num = num // 10  # 对10取整，可排除最后一位后的数字
    reversed_num = reversed_num * 10 + remain
print('reversed_num:%d' % reversed_num)

# 百钱百鸡问题
# 100元买多少只5元的鸡，多少只3元的，多少只1元3只的鸡，刚好买100只

for x in range(0, 19):  # 最多买19只5元的
    for y in range(0, 34):  # 最多33只3元的
        z = 100 - x - y  # z只1元的
        if x * 5 + y * 3 + z / 3 == 100:
            print('x:%d y:%d z:%d' % (x, y, z))
