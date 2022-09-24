anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
def calcular():
    area=altura*anchura
    perimetro=altura+anchura+altura+anchura
    print(area)
    print(perimetro)
    for i in range(altura):
        for j in range(anchura):
            print("* ", end="")
        print()

calcular()