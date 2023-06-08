# 1. Дефиниция на класа

class Point:
    
    def __init__(self, *, x = 0, y = 0, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        self.__x = x
        self.__y = y

    def draw(self):
        print(f'draw point at ({self.__x}, {self.__y})')

    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy

if __name__ == '__main__':
    
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата (представител на типа) от типа, който сме дефинирали
    print('--- begin ---')
    p1 = Point()
    p2 = Point(x=15, y=20)

    
    # p1.__x = -100
    # print(f'p1 y is {p1.y}, p2 y is {p2.y}')
    # print(f'p1 __x is {p1.__x}, p2 __x is {p2.__x}')
    # AttributeError: 'Point' object has no attribute '__x'
    # print(f'p1 x coord is {p1.__x}')

    p1.draw()
    p2.draw()

    p1.move_to(30, 40)
    p1.draw()
    
    print('--- end ---')    