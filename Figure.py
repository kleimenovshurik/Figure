import math
class Figure():

    def __init__(self):
        pass

    def info(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def count_angles(self):
        pass

    def radius(self):
        pass


class Point(Figure):
    def __init__(self, locationX: str, locationY: str):
        super().__init__()
        self.locationX = locationX
        self.locationY = locationY

    def info(self):
        super().info()
        print("Я точка с координатами: " + "х:" + self.locationX + " у:" + self.locationY)

    def area(self):
        super().area()
        print("Я точка, у меня нет площади")

    def perimeter(self):
        super().perimeter()
        print("Я точка, у меня нет периметра")

    def count_angles(self):
        super().count_angles()
        print("Я точка, у меня нет углов")

    def radius(self):
        super().radius()
        print("Я точка, мой радиус равен нулю")


class Polygon(Figure):
    A = 0
    B = 0

    def __init__(self, qs):
        super().__init__()
        self.qs = qs

    def info(self):
        super().info()
        print("Я многоугольник со сторонами: ", end=' ')
        for i in range(len(self.qs)):
            print(str(self.qs[i]) + ", ", end=' ')
            # печать с той же строки python

    # расчёт площади по методу Гаусса
    def area(self, coord: [[]]):
        super().area()
        sum = 0
        resedual = 0
        self.coord = coord
        end = coord[len(coord) - 1][0] * coord[0][1]
        itog = 0
        for i in range(len(coord) - 1):
            sum = sum + coord[i][0] * coord[i + 1][1]
        sum += end

        end2 = coord[0][0] * coord[len(coord) - 1][1]

        for i in range(len(coord) - 1):
            resedual = resedual + coord[i + 1][0] * coord[i][1]
        resedual += end2
        itog = int(0.5 * abs(sum - resedual))
        self.A = itog
        # print(itog)
        return itog

    # количество углов равняется количеству сторон
    def count_angles(self):
        super().count_angles()
        print("Количество углов: " + str(len(self.qs)))

    def perimeter(self):
        P = 0
        super().perimeter()
        for i in range(len(self.qs)):
            P = P + self.qs[i]
        self.B = P
        print(P)

    # радиус вписанной окружности
    def radius(self, coord):
        super().radius()
        self.coord = coord
        self.area(coord)
        delimoe = self.A
        delitel = self.B * 0.5
        chasnoe = delimoe / delitel
        print("Радиус вписанной окружности: " + str(chasnoe))


# четырехугольник - квадрат
class Square(Figure):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def info(self):
        super().info()
        print("Привет, я квадрат со стороной: " + str(self.side))

    def area(self, sidesize):
        super().area()
        self.sidesize = sidesize
        print(self.sidesize ** 2)

    # def perimeter(self):

    def count_angles(self):
        super().count_angles()
        print("Привет, я квадрат, у меня четыре угла.")

    # радиус вписанной окружности
    def radius(self):
        super().radius()
        rad = 0.5 * self.side
        print(rad)


class Circle(Figure):
    def __init__(self, diametr):
        super().__init__()
        self.diametr = diametr

    def info(self):
        super().info()
        print("Привет, я круг с диаметорм: " + str(self.diametr))

    def area(self):
        super().area()
        return float((self.diametr / 2) ** 2 * 3.14)

    def count_angles(self):
        super().count_angles()
        print("Я круг, у меня нет углов")

    def radius(self):
        super().radius()
        print(self.diametr / 2)


# прямоугольник
class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        super().__init__()
        self.a = a
        self.b = b

    def info(self):
        super().info()
        print("Я прямоугольник со сторонами:" + str(self.a) + " и " + str(self.b))

    def area(self):
        super().area()
        return int(self.a * self.b)

    def perimeter(self):
        super().perimeter()
        return int(2 * (self.a + self.b))

    def count_angles(self):
        super().count_angles()
        print("Я прямоугольник, у меня четыре угла")

    # радиус описанной окружности
    def radius(self):
        super().radius()
        return (((self.a * self.a + self.b * self.b) ** 0.5) / 2)


class Ellipse(Figure):
    def __init__(self, semi_major_axis, minor_axis, fi):
        super().__init__()
        self.semi_major_axis = semi_major_axis
        self.minor_axis = minor_axis
        self.fi = fi

    def info(self):
        super().info()
        print("Привет, я эллипс с большой полуосью: " + str(self.semi_major_axis) + " с малой полуосью: " + str(
            self.minor_axis) + " углом фи: " + str(self.fi) + " градусов")

    def area(self):
        super().area()
        return float(3.14 * self.semi_major_axis * self.minor_axis)

    # приближенная формула вычисления периметра эллипса
    def perimeter(self):
        super().perimeter()
        numerator = float(3.14 * self.semi_major_axis * self.minor_axis + (self.semi_major_axis - self.minor_axis) ** 2)
        denominator = self.semi_major_axis + self.minor_axis
        return float(4 * numerator / denominator)

    def count_angles(self):
        super().count_angles()
        print("Привет, я эллипс, у меня нет углов")

    def radius(self):
        super().radius()
        numerator = self.semi_major_axis * self.minor_axis
        denominator1 = float(self.minor_axis ** 2 * math.cos(self.fi) ** 2)
        denominator2 = float(self.semi_major_axis ** 2 * math.sin(self.fi) ** 2)
        preresult = (denominator1 + denominator2) ** 0.5
        result = numerator / preresult
        return result


class Square(Figure):
    def __init__(self, sideA):
        super().__init__()
        self.sideA = sideA

    def info(self):
        super().info()
        print("Привет, я квадрат со стороной: " + str(self.sideA))

    def area(self):
        super().area()
        return self.sideA ** 2

    def perimeter(self):
        super().perimeter()
        return self.sideA * 2

    def count_angles(self):
        super().count_angles()
        print("Привет, я квадрат, у меня четыре угла")

    # радиус вписанной окружности
    def radius(self):
        super().radius()
        radius = self.sideA / 2
        return radius

    # Треугольник


class Triangle(Figure):
    def __init__(self, basis: int, sideB: int, sideC: int, height: int):
        super().__init__()
        self.basis = basis
        self.sideB = sideB
        self.sideC = sideC
        self.height = height

    def info(self):
        super().info()
        print("Привет, я треугольник с основанием: " + str(self.basis))

    def area(self):
        super().area()
        return self.basis * self.height * 0.5

    def perimeter(self):
        super().perimeter()
        perimeter = self.basis + self.sideC + self.sideC
        return perimeter

    def count_angles(self):
        super().count_angles()
        print("Привет, я треугольник, у меня 3 угла")

    # радиус окуружности, вписанной в треугольник
    def radius(self):
        super().radius()
        self.area() / (self.perimeter() * 0.5)


class RegularTriangle(Figure):
    def __init__(self, OneSide: int):
        super().__init__()
        self.sside = OneSide

    def info(self):
        super().info()
        print("Привет, я правильный треугольник со строной:" + self.sside)

    def area(self):
        super().area()
        return (self.sside ** 2 * math.sqrt(3)) / 4

    def perimeter(self):
        super().perimeter()
        perimeter = 3 * self.sside
        return perimeter

    def count_angles(self):
        super().count_angles()
        print("Привет, я треугольник, у меня 3 угла")

    # радиус окружности, описанной около треугольника
    def radius(self):
        super().radius()
        radius = self.sside / math.sqrt(3)
        return radius


class Sphere(Figure):
    def __init__(self, radius, height):
        super().__init__()
        self.radius = radius
        self.height = height

    def info(self):
        super().info()
        print("Привет, я сфера")

    def area(self):
        super().area()
        area = 4 * 3.14 * (self.radius ** 2)
        return area

    def Volume(self):
        volume = 4 / 3 * 3.14 * (self.radius ** 2)
        return volume

    # площадь верхней поверхности сегмента сферы
    # area of the upper surface of a segment of a sphere
    def AUSSS(self, HeightofSegment):
        self.HeightofSegment = HeightofSegment
        AUSSS = 2 * 3.14 * self.radius * self.HeightofSegment


class Parallelogram(Figure):
    def __init__(self, bigside, smallside, height):
        super().__init__()
        self.bigside = bigside
        self.smallside = smallside
        self.height = height

    def info(self):
        super().info()
        print("Привет, я параллелограмм со стронами" + str(self.bigside) + str(self.smallside))

    def area(self):
        super().area()
        area = self.bigside * self.height
        return area

    def perimeter(self):
        super().perimeter()
        perimeter = ( self.bigside + self.smallside ) * 2
        return perimeter
    
    def count_angles(self):
        super().count_angles()
        print("Я параллелограммм, у меня четыре угла")

    def radius(self):
        super().radius()






























