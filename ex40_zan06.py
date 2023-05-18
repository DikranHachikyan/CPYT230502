# 1. дефиниция

def foo( a=[], b={}):
    print(f'a={a}, b={b}')

    print('-' * 20)
    n = len(a)
    a.append(n)

    b[n] = n
    

if __name__ == '__main__':

    foo()

    foo([2,5,3], {'Z':20})

    foo()

    foo([12,51,23, 4], {'Z':20, 'X':1})

    foo()
    print('---')    