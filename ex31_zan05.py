# port - глобална променлива
port = 1521
# 1. дефиниция
def sum_numbers(a, b, *args):
    # c - локална променлива
    print(f'type of args:{type(args)} args:{args}')
    c = a + b
    for i in args:
        c += i 
    return c

if __name__ == '__main__':
    
    # 2. извикване на функцията
    res = sum_numbers(5, 6)
    print(f'res={res}')
    
    x, y, z, s = 10, 20, 25, 14
    res = sum_numbers(x, y, z, s)

    print(f'{x} + {y} + {z} + {s} = {res}')

    arr = [1, 2, 3, 4, 5]

    res = sum_numbers(x, y, *arr)

    print(f'{x} + {y} + {" + ".join(map(str, arr)) } = {res}')
    print('---')