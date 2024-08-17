class person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        print('person构造函数')

    def intro_self(self):
        print('my name is ', self._name, self._age)


class stu(person):  # 继承person
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        print('stu构造函数调用。。')
        self._grade = grade

    def study(self, class_name):
        print('%s正在学习%s' % (self._name, class_name))

    def intro_self(self):  # 重写父类方法
        print('学生名是', self._name, self._age)

    def intro_self2(self):
        print('2学生名是', self._name, self._age)


def main():
    s = stu('zjh', 33, 100)
    s.study('java')
    s.intro_self()
    s.intro_self2()


if __name__ == '__main__':
    main()
