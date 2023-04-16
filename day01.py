# 1일차 타입별 메서드 및 프로세스, 스레딩 개념 익히기

park_list = ["apple", "banana", "cherry"]
park_text = "Hello, World"
park_text2 = ','.join(park_list)


def park_count(text=park_text):
    parkjihong_count = text.count("l")
    # 문자열 내에서 문자의 갯수를 반환한다.
    print(parkjihong_count)


def park_find(text=park_text):
    parkjihong_position = text.find("World")
    # 문자열 내에서 특정문자열의 시작 인덱스를 반환한다. 찾지 못하면 -1 ( False )를 반환함
    print(parkjihong_position)


def park_index(text=park_text):
    try:
        parkjihong_position = text.index("World")
        # find와 기능적으로 같은 기능을 하지만 반환값이 존재하지 않다면 ValueError를 발생시킨다.
        print(parkjihong_position)
    except ValueError:
        print("문자열이 존재하지 않습니다.")


def park_join(text=park_list):
    park_join = ",1 ".join(text)
    # 특정 문자열을 기준으로 다른 문자열들을 합쳐준다. " " 안의 문자를 리스트의 인덱스 사이에 추가해주는 개념
    print(park_join)


def park_uppper_lower(text=park_text):
    park_upper = text.upper()
    # 문자열 내의 소문자를 대문자로 바꿔준다.
    print(park_upper)
    park_lower = text.lower()
    # 문자열 내의 대문자를 소문자로 바꿔준다.
    print(park_lower)


def park_replace(text=park_text):
    park_replace = text.replace("World", "Python")
    # 문자열내의 첫번째 값을 (world)를 두번쨰 값으로 (python) 로 바꿔준다.
    print(park_replace)


def park_split(text=park_text2):
    park_fruits = text.split(',')
    # 특정 문자열을 기준으로 나눠준다 결과는 리스트형태로 반환된다.
    # 나눠지는 결과값이 3개일때
    # a, b, c = text.split(',') 형식으로 사용하면 첫번째 리스트는 a에 2번째는 b에  3번째는 c에 담기게 된다.
    print(park_fruits)


def park_len(text=park_list):
    # len은 리스트의 길이값을 반환해준다.
    print(len(text))


def park_del(text=park_list):
    del text[2]
    # 리스트의 특정 요소를 삭제한다 (위에서는 2번째 인덱스가 제거된다.)
    # ["apple", "banana", "cherry"] => ['apple', 'banana']
    print(text)


def park_append(text=park_list):
    text.append("grape")
    # 리스트의 맨 뒤에 새로운 요소를 추가한다.
    # ["apple", "banana", "cherry"] => ['apple', 'banana', 'cherry', 'grape']
    print(text)


def park_sort(text=park_list):
    numbers = [3, 2, 1, 6, 4, 8]
    # 리스트를 오름차순으로 정렬한다.
    # reverse=true 사용시 역순 정렬
    numbers.sort()
    print(numbers)


def park_reverse(text=park_list):
    numbers = [3, 2, 1, 6, 4, 8]
    # 리스트의 요소의 순서를 반대로 뒤집어준다
    # 정렬과는 다른개념 단순히 앞뒤를 뒤집는다.
    numbers.reverse()
    print(numbers)


def park_list_index(text=park_list):
    # 리스트의 특정 요소의 인덱스를 반환해준다.
    print(text.index('banana'))


def park_insert(text=park_list):
    text.insert(2, "TEST")
    # 리스트의 특정 인덱스에 요소를 삽입한다.
    print(text)


def park_remove(text=park_list):
    text.remove("banana")
    # 리스트의 특정 요소를 제거한다 (인덱스가 아니라 값을 사용한다)
    print(text)


def park_pop(text=park_list):
    text.pop(1)
    # 해당 부분 설명 오류 존재함.
    # 인자값이 없다면 리스트의 마지막요소를 뺀뒤 해당 요소를 삭제한다.
    # 인자값으로 인덱스를 사용 할 수 있으며 이때 해당 인덱스를 빼낸 뒤 삭제한다.
    print(text)


def park_count(text=park_list):
    print(text.count("banana"))
    # 리스트에서 특정 요소의 개수를 반환한다.


def park_extend(text=park_list):
    text.extend(["TA", "TB", "TC"])
    # 리스트를 확장하여 새로운 요소를 추가한다.
    print(text)


def park_listadd(text=park_list):
    text += ["TA", "TB", "TC"]
    # 리스트를 확장하여 새로운 요소를 추가한다.
    print(text)


empty_dic = {}
# 빈 딕셔너라 생성

park_dict = {"apple": 1, "banana": 2, "orange": 3}
# 키로 apple, banana, orange 생성 해당 키에 대해 :값 형태로 붙게된다.


def park_dic_add(text=park_dict):
    text["grape"] = 4
    # 딕셔너리 쌍을 추가한다.
    print(text)


def park_dic_del(text=park_dict):
    del text["apple"]
    # 딕셔너리에 특정 요소를 삭제한다.
    print(text)


def park_dic_getvalue(text=park_dict):
    print(text["banana"])
    # 딕셔너리에서 특정 Key에 대한 Value를 얻어온다.
    # 딕셔너리에 Key가 존재하지않는 경우 KeyError 를 발생시킨다.


def park_dic_getkeys(text=park_dict):
    keylist = list(text.keys())
    # 딕셔너리 내에서 모든 Key를 리스트형태로 반환받는다
    print(keylist)


def park_dic_getvalues(text=park_dict):
    value_list = list(text.values())
    # 딕셔너리 내에서 모든 Value를 dict_values 형태 [튜플 형태의 리스트] 로 반환 받는다.
    # 해당 값을 사용하기 위해 list 형태로 변환하여 반환 받는게 일반적이다.
    print(value_list)


park_dict2 = {'name': 'John', 'age': 30, 'gender': 'male'}


def park_dic_getitems(text=park_dict2):
    items = text.items()
    # 딕셔너리 내의 모든 키와 값을 튜플 형태의 리스트로 반환받는다.
    # 해당 값은 for 문에서 유용하게 사용된다 for key, value in items 와 같은 형식.
    print(items)


def park_dic_clear(text=park_dict2):
    text.clear()
    # 딕셔너리의 모든 요소를 삭제한다.
    print(text)


def park_dic_get(text=park_dict2):
    name = text.get('name')
    print(name)

    email = text.get('email')
    print(email)

    email = text.get('email', 'unknown')
    # 기본값을 설정할 수 있다. 데이터가 없다면 본래 None 이 출려되지만 설정하면 unknown이 출력된다.
    print(email)


def park_dic_in(text=park_dict2):
    print('name' in text)
    # 해당 키가 딕셔너리 안에 존재하는지 확인한다. 반환값은 Boolrean 형태이다.
    print('email' in text)





