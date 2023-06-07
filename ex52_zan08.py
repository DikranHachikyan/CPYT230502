# 1
# import time
# print(f'now is:{time.time()}')

# 1.1
# import time as ts
# print(f'now is:{ts.time()}')

# 2
# from time import time, sleep
# print(f'now is:{time()}')

# 2.1
# from time import time as now, sleep
# print(f'now is:{now()}')

from functools import wraps

# 1. дефиниция на декоратора
def to_upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper 



if __name__ == '__main__':
    users = ['anna', 'maria', 'markus', 'jorg']

    print(*users)
    # прилагаме декоратор към функция от стандартната библиотека
    print = to_upper(print)

    print(*users)

    # премахваме декоратора
    print = print.__original

    print(*users)

    print('---')    