# 1. дефиниция
def show(title, ver='1.4.3', *args, **kwargs):
    
    print(f'title (positional):{title}')

    print(f'ver (optional):{ver}')

    print('args:')
    for i in args:
        print(i, end=' ')
    print()

    if 'color' in kwargs and 'font' in kwargs:
        col = kwargs['color']
        fnt = kwargs['font']
        print(f'color:{col} font:{fnt}')

if __name__ == '__main__':
    
    # 2. извикване на функцията
    # 1.
    # show('Text Editor')

    # 2.
    # show('Text Editor', '1.4.5')
    
    # 3.
    show('Text Editor', '1.4.5', 1, 2, 3, 4, 5)

    # 4.
    show('Text Editor', '1.4.5', 1, 2, 3, 4, 5, font='monospace', color='red', size=10)
    

    print('---')