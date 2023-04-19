import asyncio


def test01():
    def my_coroutine():
        while True:
            value = yield
            print('Received value:', value)
    # 코루틴 객체 생성
    co = my_coroutine()

    # 코루틴 실행 준비
    next(co)
    # 값을 보내기
    co.send(10)
    co.send(20)
    co.send(30)


def test02():
    def my_generator():
        yield 1
        yield 2
        yield 3

    gen = my_generator()
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3


def test3():
    phone_book = {"John": "123-4567", "Jane": "234-5678", "Max": "345-6789"}

    def search():
        name = yield
        while True:
            if name in phone_book:
                phone_number = phone_book[name]
            else:
                phone_number = "Cannot find the name in the phone book"
            name = yield phone_number
    search_coroutine = search()
    next(search_coroutine)

    result = search_coroutine.send("John")
    print(result)

    result = search_coroutine.send("Jane")
    print(result)

    result = search_coroutine.send("Sarah")
    print(result)


def test4():
    async def my_coroutine():
        print("Start app")
        await asyncio.sleep(1)
        print("End app")

    async def main():
        print("Before call")
        await my_coroutine()
        print("After Call")

    asyncio.run(main())


def test5():
    import random
    async def fetch_data():
        print("Load Data ...")
        await asyncio.sleep(1)
        return random.randint(1, 100)

    async def main():
        data = await fetch_data()
        print(f"가져온 데이터: {data}")

    asyncio.run(main())


test5()

# asyncio 참고 링크
# https://docs.python.org/ko/3/library/asyncio-task.html
# https://brownbears.tistory.com/540


# 의존성 관리. requirements 자제
# pipenv / Poetry 
# Poetry 사용법 참고링크
# https://blog.gyus.me/2020/introduce-poetry/