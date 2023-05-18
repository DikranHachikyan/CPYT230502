# 1. дефиниция

def foo( values, n):
    n = n ** 2
    print(f'inside foo n={n}')

    values.sort()

    print(f'inside foo values:{values}')

if __name__ == '__main__':

    # mutable
    numbers = [5, 4, 6, 3, 7, 8, 9]
    # immutable
    a = 10

    foo(numbers, a)

    print(f'numbers:{numbers} a={a}')
    
    print('---')    