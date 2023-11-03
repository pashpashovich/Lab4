class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) * 0.5
        return area

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def is_right_method(self):
        return self.a + self.b + self.c

    @classmethod
    def is_right_triangle(cls, a, b, c):
        sides = [a, b, c]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

    @staticmethod
    def is_equilateral(a, b, c):
        return a == b == c

    @staticmethod
    def get_triangle_sides_from_user():
        try:
            a = float(input("Введите длину стороны a: "))
            b = float(input("Введите длину стороны b: "))
            c = float(input("Введите длину стороны c: "))
            return a, b, c
        except ValueError:
            print("Неверный ввод...")
            return 0, 0, 0


a, b, c = Triangle.get_triangle_sides_from_user()

if a + b > c and a + c > b and b + c > a:
    triangle = Triangle(a, b, c)
    print("Периметр треугольника:", triangle.calculate_perimeter())
    print("Площадь треугольника:", triangle.calculate_area())
    if Triangle.is_right_triangle(a, b, c):
        print("Это прямоугольный треугольник")
    elif Triangle.is_equilateral(a, b, c):
        print("Это правильный треугольник")
    else:
        print("Это обычный треугольник")
else:
    print("Неверное значение сторон. Они не образуют треугольник.")