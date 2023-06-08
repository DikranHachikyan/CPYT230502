class KeyNotFoundError(Exception):
    pass

def print_key(key, **kwargs):
    
    if key not in kwargs:
        raise KeyNotFoundError(f'Missing key {key} in hash table')

    print(f'{key} => {kwargs[key]}')
    print('--- end of print_key ---')

if __name__ == '__main__':
    conn = {
        'host':'localhost',
        'port': 1521,
        'service':'oracle-xe'
    }

    try:
        print_key('host', **conn)
        print_key('ip', **conn)
    except KeyNotFoundError as e:
        print(f'{e}')
        # raise
    print('---')    