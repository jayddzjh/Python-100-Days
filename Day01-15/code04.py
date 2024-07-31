import random

num = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    inputNum = int(input('请输入数字：'))
    if inputNum == num:
        print('恭喜，答对了。你猜了%d次' % counter)
        break
    elif inputNum < num:
        print('猜小了')
    else:
        print('猜大了')

print('游戏完毕。')
