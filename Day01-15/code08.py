class stu:
    def __init__(self, name, age):
        print('构造函数调用。。')
        print('my name is', name, 'age is ', age)
        self.name = name
        self.age = age
        self.__name = name  # 私有变量通过在变量名前面加2个下划线

    def study(self, class_name):
        print('%s正在学习%s' % (self.__name, class_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能看熊出没' % self.name)
        else:
            print('%s可以看岛国爱情动作大片' % self.name)


def main():
    s1 = stu('zjh', 29)
    print(s1.__name)  # 没有此字段
    print(s1.age)
    s1.study('python教程')
    s1.watch_movie()


if __name__ == '__main__':
    main()
