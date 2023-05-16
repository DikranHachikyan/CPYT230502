# 1. дефиниция
def show(title, *, ver='1.4.3', **kwargs):
    
    print(f'title (positional):{title}')

    print(f'ver (optional keyword-only):{ver}')

    print('kwargs:')
    params = {
        'color': kwargs.get('color', 'black'),
        'font':  kwargs.get('font', 'sans-serif')
    }

    print(f'color:{params["color"]} font:{params["font"]}')

if __name__ == '__main__':

    settings = {
        'font':'serif',
        'bold':True,
        'color':'red',
        'margins': [10, 5, 10, 5]
    }
    # 2. извикване на функцията
    # 1.
    show('Text Editor')

    # 2.
    show('Text Editor', ver='1.4.5', **settings)
    
    
    

    print('---')