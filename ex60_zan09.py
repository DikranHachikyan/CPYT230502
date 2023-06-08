# 1. Дефиниция на класа

class Point:
    
    def __init__(self):
        print('--- init Point ---')
        # данни на обекта
        self.x = 10
        self.y = 20

    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == '__main__':
    
    # 2. декларация на променлива от типа Point
    # клас - типа, който сме дефинирали (Point)
    # обект - променливата (представител на типа) от типа, който сме дефинирали
    print('--- begin ---')
    p = Point()

    print(f'type of p is:{type(p)}, point at ({p.x}, {p.y}) ')

    p.x = 12
    p.y = 23

    p.draw()
    p.move_to(-5, 8)
    p.draw()

    print('--- end ---')    