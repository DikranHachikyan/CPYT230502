# 1 + 2 + 3 + ... + 99 + 100 = 5050
# print(f'name is:{__name__}')

if __name__ == '__main__':
    i = 1
    sum_n = 0

    while i <= 100:
        # sum_n = sum_n + i
        sum_n += i
        # !! inf loop !!
        i += 1
    else:
        print('--- else ---')

    print(f'1 + 2 + ... + 99 + 100 = {sum_n}')
    print('---')