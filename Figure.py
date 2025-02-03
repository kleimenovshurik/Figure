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
        return  float((8/2) ** 2 * 3.14)

    def count_angles(self):
        super().count_angles()
        print("Я круг, у меня нет углов")

    def radius(self):
        super().radius()
        print(self.diametr/2)


point = Point("4", "2")
point1 = Figure()
point.info()
point.area()
point1.area()

Ma = Polygon([1, 3, 4, 7, 5])
Ma.perimeter()
Ma.area([[3, 4], [5, 11], [12, 8], [9, 5], [5, 6]])
Ma.radius([[3, 4], [5, 11], [12, 8], [9, 5], [5, 6]])

# Ma.area([[4,3],[2,9],[7,8],[5,6],[2,2]])
# Ma.count_angles()

s1 = Square(4)
s1.area(9)
s1.count_angles()
s1.radius()

c1 = Circle(8)
c1.info()

print(c1.area())
c1.diametr

#MironovaTamaraKarlovna1@