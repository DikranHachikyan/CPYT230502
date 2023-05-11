

if __name__ == '__main__':
    
    tpl = 11, 23, 12, 45, 67

    for item in enumerate(tpl, start=5):
        key, value = item
        print(f'key = {key} value = {value}')

    print('---')