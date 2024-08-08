import json

# Python 字典类型转换为 JSON 对象
data_dict = {
    'no': 1,
    'name': 'Runoob',
    'url': 'https://www.runoob.com',
    "point": 1.21
}

json_str = json.dumps(data_dict)
print("JSON 字符串：", json_str)
print("Python 原始数据：", repr(data_dict))
print('反序列化变量：', json.loads(json_str)['name'])

# list
data_list = [1, 3, 4, 5, 3]
dumps = json.dumps(data_list)
print('json字符串：', dumps)
print('python原始数据：', repr(data_list))
print('反序列化变量：', json.loads(dumps))

s = "{'no': 21, 'name': 'zjh', 'url': 'https://www.runoob.com', 'point': 3.1421}"
# python中json字符串必须双引号
json_string = s.replace("'", '"')
print("json_string", json_string)
ss = json.loads(json_string)
print(ss)
