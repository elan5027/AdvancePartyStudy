
def test(n, result=0):
    if n != 1:
        result += n*test(n-1)
        return result
    return 1


count = 0

def fibo(n):
    global count
    _cur, _next = 0, 1
    for i in range(n):
        count += 1
        print(f'for loop[{i}] _cur: {_cur}, _next: {_next}, count: {count}')
        _cur, _next = _next, _cur + _next
    return _cur

def fibo2(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo2(n - 1) + fibo2(n - 2)
    
    


#숙제 파스칼의 삼각형

# 1번째 줄에는 1을 사용
# 2. n번째 줄 (n >= 2) 줄을 만들때 n-1 번째 줄의 왼쪽 숫자와 오른쪽 숫자를 더한다.
#    n-1번째 줄의 왼쪽 숫자 혹은 오른쪽 숫자 중 하나가 없을 경우 존재하는 수만 더한다.
# 트리구조? 

# 파스칼의 삼각형 
n = 8 

def pascal(n):
    parscal_list = [[1]]
    if n == 1:
        return parscal_list[0]
    
    for x in range(1, n+1):
        tmp = [1]
        for y in range(1, x):
            if y != x-1 and y != 0:
                tmp.append(parscal_list[x-1][y-1]+parscal_list[x-1][y])
        tmp.append(1)
        parscal_list.append(tmp)
    return parscal_list[n]

# for i in range(1, 9):
#     print(pascal(i))

def pascal2(n):
    if n == 1:
        return [[1]]
    else:
        result = pascal2(n-1)
        num_array = [1]
        for i in range(len(result[-1])-1):
            num_array.append(result[-1][i] + result[-1][i+1])
        num_array.append(1)
        result.append(num_array)
        return result

for i in range(1, 9):
    print(pascal2(i)[i-1])
