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

@to_upper
def concat(*args, **kwargs):
    '''Concatenate args with separator sep'''
    sep = kwargs.get('sep', ';')
    return sep.join(args)

if __name__ == '__main__':
    users = ['anna', 'maria', 'markus', 'jorg']

    print(f'users 1:{concat(*users)}')
    print(f'users 2:{concat(*users, sep=", ")}')

    values = [11, 23, 45, 77, 88, 94]
    print(f'values:{concat(*values, sep="|")}')

    concat = concat.__original
    print(f'users 3:{concat(*users)}')

    print('---')    