# 1. Дефиниция на класа

class Point:
    
    def __init__(self, *, x = 0, y = 0, visible=True, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        self.set_x(x)
        self.set_y(y)
        self.set_visible(visible)

    def draw(self):
        print(f'draw point at ({self.get_x()}, {self.get_y()})')

    def move_to(self, dx, dy):
        self.set_x( self.get_x() + dx)
        self.set_y( self.get_y() + dy)

    # методи за достъп до данните (класически подход)
    def set_x(self, x):
        assert x >= 0, f'x must be positive number (x={x})'
        self.__x = x

    def set_y(self, y):
        assert y >= 0, f'y must be positive number (y={y})'
        self.__y = y

    def set_visible(self, visible):
        self.__visible = visible

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def is_visible(self):
        return self.__visible 

if __name__ == '__main__':
    
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата (представител на типа) от типа, който сме дефинирали
    print('--- begin ---')
    p1 = Point()
    p2 = Point(x=15, y=20)

    if p1.is_visible():
        p1.draw()

    p1.set_x(30)
    p1.set_y(20)
    p1.draw()

    p1.set_x(-2)    
    
    print('--- end ---')    