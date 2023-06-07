def print_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        # 3. обичайно решение
        raise
        # 2. още по-лоша идея
        # pass

        # 1. лоша идея
        # print(f'invalid key:{e}')

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
        print(f'connection object does not have ip key')
        # raise
    print('---')    