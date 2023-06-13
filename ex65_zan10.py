# 1. Дефиниция на класа

class Point:
    '''Class Point'''
    
    def __init__(self, *, x = 0, y = 0, visible=True, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        self.x = x
        self.y = y
        self.is_visible = visible

    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

    # методи за достъп до данните (класически подход)
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, x):
        assert x >= 0, f'x must be positive number (x={x})'
        self.__x = x

    @y.setter
    def y(self, y):
        assert y >= 0, f'y must be positive number (y={y})'
        self.__y = y

    @property
    def is_visible(self):
        return self.__visible 
    
    @is_visible.setter
    def is_visible(self, visible):
        self.__visible = visible



if __name__ == '__main__':
    
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата (представител на типа) от типа, който сме дефинирали
    print('--- begin ---')
    p1 = Point()
    p2 = Point(x=15, y=20)

    print(f'Point ({p2.x},{p2.y}) is visible:{p2.is_visible}')

    p1.x = 20
    p1.y = 12
    p1.draw()

    # AssertionError
    # p2.x = -1
    print('--- end ---')    