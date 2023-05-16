# 1. дефиниция
def show(title, ver='1.4.3', *args, **kwargs):
    
    print(f'title (positional):{title}')

    print(f'ver (optional):{ver}')

    print('args:')
    for i in args:
        print(i, end=' ')
    print()

    print('kwargs:')
    params = {
        'color': kwargs.get('color', 'black'),
        'font':  kwargs.get('font', 'sans-serif')
    }

    print(f'color:{params["color"]} font:{params["font"]}')

if __name__ == '__main__':
    
    arr = [1,2,3,4,5]

    settings = {
        'font':'serif',
        'bold':True,
        'color':'red',
        'margins': [10, 5, 10, 5]
    }
    # 2. извикване на функцията
    # 1.
    show('Text Editor', *arr)

    # 2.
    show('Text Editor', '1.4.5', *arr, **settings)
    
    
    

    print('---')