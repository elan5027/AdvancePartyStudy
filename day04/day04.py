import json

# JSON 문자열
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# JSON 문자열을 Python 객체로 변환
data = json.loads(json_data)

# Python 객체 출력
# print(data)
# print(type(data))




# with open('sub_movies.json', 'w', encoding="utf-8") as make_file:
# json.dump(mylist, make_file, ensure_ascii=False, indent="\t")

# json_data = open('sub_movies.json', 'r', encoding = 'utf-8')
# data1 = json.load(json_data)

# sample : https://jsonplaceholder.typicode.com/posts

import requests

# response = requests.get('https://jsonplaceholder.typicode.com/posts')

data = {'title':'homework', 'body':'parkjohong', 'userId':1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)

# 방법1. 전송한 데이터 그대로 Json형태로 넣기
if response.status_code == 201:
    # with open('result.text', 'w') as test_file:
    #      json.dump(data, test_file, indent='\t')
         
# 방법2. 별도의 값으로 받아와서 별도 저장
    title, body, userId = data.values()
    f = open('result.text', 'w')
    f.write(f"title={title}\n")
    f.write(f"body={body}\n")
    f.write(f"userId={userId}\n")
    f.close()

    





