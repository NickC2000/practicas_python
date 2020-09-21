import math

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def hallarDistancia(self,Punto):
        distancia = math.sqrt(((Punto.x-self.x)**2) + ((Punto.y-self.y)**2))
        return distancia

class Circulo:
    def __init__(self,punto,radio):
        self.radio = radio
        self.punto = punto
    def hallarArea(self):
        area = math.pi * (self.radio ** 2)
        return area
    def hallarPerimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

class Triangulo:
    def __init__(self,verticeA,verticeB,verticeC):
        self.verticeA = verticeA
        self.verticeB = verticeB
        self.verticeC = verticeC
    def hallarArea(self):
        ladoA = self.verticeA.hallarDistancia(self.verticeB)
        ladoB = self.verticeB.hallarDistancia(self.verticeC)
        ladoC = self.verticeC.hallarDistancia(self.verticeA)

        perimetro = ladoA + ladoB + ladoC
        s = perimetro/2
        area = math.sqrt(s*(s-ladoA)*(s-ladoB)*(s-ladoC))
        return area
    def hallarPerimetro(self):
        ladoA = self.verticeA.hallarDistancia(self.verticeB)
        ladoB = self.verticeB.hallarDistancia(self.verticeC)
        ladoC = self.verticeC.hallarDistancia(self.verticeA)

        perimetro = ladoA + ladoB + ladoC
        return perimetro
    def clasificacionTriangulo(self):
        ladoA = self.verticeA.hallarDistancia(self.verticeB)
        ladoB = self.verticeB.hallarDistancia(self.verticeC)
        ladoC = self.verticeC.hallarDistancia(self.verticeA)

        if (ladoA == ladoB) and (ladoB == ladoC) and (ladoC == ladoA):
            return "equilatero"
        elif ((ladoA == ladoB) and (ladoB != ladoC)) or ((ladoB == ladoC) and (ladoC == ladoA)) or ((ladoA == ladoC) and (ladoC == ladoB)):
            return "Isoceles"
        elif (ladoA != ladoB) and (ladoB != ladoC) and (ladoC != ladoA):
            return "Escaleno"
        return "Error"

class Rectangulo:
    def __init__(self,verticeA,verticeB,verticeC,verticeD):
        self.verticeA = verticeA
        self.verticeB = verticeB
        self.verticeC = verticeC
        self.verticeD = verticeD
    def hallarArea(self):
        area = (self.verticeA.hallarDistancia(self.verticeB))*(self.verticeB.hallarDistancia(self.verticeC))
        return area
    def hallarPerimetro(self):
        perimetro = (2*self.verticeA.hallarDistancia(self.verticeB))+(2*self.verticeB.hallarDistancia(self.verticeC))
        return perimetro

def main():
    print("Programa plano cartesiano")

    #PUNTO Y DISTANCIA ENTRE PUNTO

    p1 = Punto(-1,0)
    p2 = Punto(1,0)
    d = p1.hallarDistancia(p2)
    print("Distancia entre el punto 1 y 2 es: ",d)

    #CIRCULO, AREA Y PERIMETRO

    c = Circulo(Punto(0,0),1)
    areaCirculo = c.hallarArea()
    print("El area del circulo es: ", areaCirculo)
    perimetroCirculo = c.hallarPerimetro()
    print("El perimetro del circulo es: ", perimetroCirculo)

    #TRIANGULO, AREA, PERIMETRO Y CLASIFICACION
    t = Triangulo(Punto(0,4),Punto(0,0),Punto(3,0))
    areaTriangulo = t.hallarArea()
    print("El area del triangulo es: ",areaTriangulo)
    perimetroTriangulo = t.hallarPerimetro()
    print("El perimetro del triangulo es: ",perimetroTriangulo)
    clasificacion = t.clasificacionTriangulo()
    print("El triangulo es: ",clasificacion)

    #RECTANGULO, AREA Y PERIMETRO
    r = Rectangulo(Punto(0,2),Punto(0,0),Punto(3,0),Punto(3,2))
    areaRectangulo = r.hallarArea()
    print("El area del rectangulo es: ",areaRectangulo)
    perimetroTriangulo = r.hallarPerimetro()
    print("El perimetro del rectangulo es: ",perimetroTriangulo)

if __name__ == "__main__":
    main()