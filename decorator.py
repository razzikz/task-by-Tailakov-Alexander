def my_decorator(number):
    def wrapper(*x, **q):
        res = number(int(input('1: ')), int(input('2: ')))
        return res * 2
    return wrapper

@my_decorator
def number(a, b):
    return a+b


print(number())

def decorator(info):
    def wrapper(*x):
        print(f"Вызываю функцию {info.__name__} с аргументами {x}.")
        result = info(*x)
        print(f'function {info.__name__} returned {result}')
        return result
    return wrapper

@decorator
def info(a, b):
    return a*b


print(info(2,2))
