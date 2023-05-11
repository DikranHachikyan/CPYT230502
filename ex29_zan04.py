# port - глобална променлива
port = 1521
# 1. дефиниция
def sum_numbers(a, b, d=0):
    # c - локална променлива
    c = a + b + d
    return c

if __name__ == '__main__':
    
    # 2. извикване на функцията
    res = sum_numbers(5, 6)
    print(f'res={res}')
    
    x, y, z = 10, 20, 25
    res = sum_numbers(x, y, z)

    print(f'{x} + {y} + {z} = {res}')


    print('---')