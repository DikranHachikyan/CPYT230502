# 2 + 4 + ... + 98 + 100 = 2550
# print(f'name is:{__name__}')

if __name__ == '__main__':
    i = 1
    sum_n = 0

    while i <= 100:
        i += 1

        if  i == 10:
            break

        sum_n += i
    else:
        print('--- else ---')

    print(f'2 + 4 + ... + 98 + 100 = {sum_n}')
    print('---')