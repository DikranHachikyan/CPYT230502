# Глобална променлива
port = 1521
# 1. дефиниция
def show():
    global port
    port = 3306
    print(f'local var port:{port}')

if __name__ == '__main__':

    print(f'(before) global var port:{port}')
    show()
    print(f'(after) global var port:{port}')

    print('---')