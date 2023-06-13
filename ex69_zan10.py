# 2.
from draw.point import Point

def show():
    p = Point(x=1,y=2)
    print(f'show:{p} n instances:{Point.count}')

if __name__ == '__main__':
    
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата (представител на типа) от типа, който сме дефинирали
    print('--- begin ---')
    p1 = Point(x=15, y=20)
    p2 = Point(x=15, y=20)

    p2.draw()

    show()

    print(f'n instances of Point: {Point.count}')

    print('--- end ---')    