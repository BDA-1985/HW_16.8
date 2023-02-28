from main import Rectangle, Square, Circle

# Для проверки создаём два прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

# Выводим на печать площадь прямоугольника

print(rect_1.get_area())
print(rect_2.get_area())

# Для проверки создаём два квадрата

square_1 = Square(5)
square_2 = Square(10)

# Выводим на печать площадь квадрата

print(square_1.get_area_square())
print(square_2.get_area_square())

# Для провеврки создаем два круга

сircle_1 = Circle(6)
сircle_2 = Circle(14)

# Выводим на печать площадь круга
print(сircle_1.get_area_circle())
print(сircle_2.get_area_circle())
