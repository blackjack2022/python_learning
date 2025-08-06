import json


def create_file():
    try:
        with open("README.md", "rb") as f1, open("tempfile/readme.txt", "xb") as f2:
            data = f1.read(10)
            while data:
                f2.write(data)
                data = f1.read(10)
    except FileNotFoundError:
        print("file not found")
    except IOError:
        print("read file error")


create_file()


def json_read():
    my_dict = {
        'name': '骆昊',
        'age': 40,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BMW', 'max_speed': 240},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 280}
        ]
    }
    with open('tempfile/data.json', 'w') as file:
        json.dump(my_dict, file)

    with open('tempfile/data.json', 'r') as file:
        data = json.loads(file.read())
        print(data)


json_read()

import requests

resp = requests.get('http://apis.tianapi.com/guonei/?key=APIKey&num=10')
if resp.status_code == 200:
    data_model = resp.json()
    print(data_model)
    # for news in data_model['newslist']:
    #     print(news['title'])
    #     print(news['url'])
    #     print('-' * 60)
else:
    print(resp.status_code)

import csv
import random

with open('tempfile/scores.csv', 'r+') as file:
    if len(file.read()) == 0:
        writer = csv.writer(file)
        writer.writerow(['姓名', '语文', '数学', '英语'])
        names = ['关羽', '张飞', '赵云', '马超', '黄忠']
        for name in names:
            scores = [random.randrange(50, 101) for _ in range(3)]
            scores.insert(0, name)
            writer.writerow(scores)

with open('tempfile/scores.csv', 'r') as file:
    print(file.read())
