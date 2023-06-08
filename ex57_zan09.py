def print_key(key, **kwargs):
    
    if key not in kwargs:
        raise KeyError(f'Missing key {key} in hash table')

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
    except KeyError as e:
        print(f'Invalid key: {e}')
        # raise
    print('---')    