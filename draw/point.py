
# 1. Дефиниция на класа

# print(f'property name is {__name__}')

class Point:
    '''Class Point'''

    # Данни на класа
    # "Глобални" за обектите от тип Point
    count = 0

    def __init__(self, *, x = 0, y = 0, visible=True, **kwargs):
        print('--- init Point ---')
        # данни на обекта
        self.x = x
        self.y = y
        self.is_visible = visible
        Point.count +=1

    def draw(self):
        print(f'draw point at ({self.x}, {self.y}) n instances:{Point.count}')

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

    # Специални методи 
    # Предефиниране на методи (function overriding)
    # 
    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, right):
        if not isinstance(right, Point):
            raise NotImplementedError(f'Not yet implemented')
        return self.x == right.x and self.y == right.y
    
    def __add__(self, right):
        new_x, new_y = 0,0
        if isinstance(right, Point):
            new_x = self.x + right.x
            new_y = self.y + right.y
        elif isinstance(right, (float,int) ):
            new_x = self.x + right
            new_y = self.y + right
        else:
            raise NotImplementedError('Not yet implemented')
        return Point(x = new_x, y = new_y)
    
    def __del__(self):
        Point.count -= 1
        print(f'destroy object:{self}')

if __name__ == '__main__':
    p = Point(x=100, y=100)

    p.draw()