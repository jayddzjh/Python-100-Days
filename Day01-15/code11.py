import json

import requests


def read_test():
    try:
        f = open('read.txat', 'r', encoding='utf-8')
        txt = f.read()
        print(txt)
    except FileNotFoundError as e:
        print('找不到指定文件：', e)
    finally:
        if 'f' in locals():
            print('close file.')
            f.close()


def read_test2():
    try:  # 可能发生异常的代码
        with open(file='read.txt', mode='r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError as e:  # 处理特定异常
        print('找不到指定文件：', e)
    else:  # 不发生异常则执行
        print('no except...')
    finally:  # 不管是否异常都会执行
        print('finally...')


def write_test():
    my_dict = {
        "name": "zjh",
        "age": 12.3,
        "food": ['胡辣汤', '水煎包'],
        'company': [
            {'name': "xdf", 'salary': 30},
            {'name': "bd", 'salary': 30}
        ]
    }
    try:
        with open(file='write.txt', mode='a', encoding='utf-8') as fs:
            # json.dump(my_dict, fs)  # json.dump序列化到文件中
            js = json.dumps(my_dict)
            # fs.writelines(js)
            fs.write(js + '\n')
    except IOError as e:
        print('io err', e)
    finally:
        print('finally...')


def req():
    resp = requests.get('https://apis.tianapi.com/duoyinzi/index?key=fb7e66e8dab4f67b1ffb499cf125da81&word=乐')
    data_model = json.loads(resp.text)
    if resp.status_code == 200:
        print('请求成功：', data_model)
    else:
        print('请求失败:', resp.status_code)


if __name__ == '__main__':
    # read_test2()
    # write_test()
    req()
