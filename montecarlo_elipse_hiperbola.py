import math
import random


def pedir_positivo(mensaje):
  
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("  El valor debe ser mayor que cero.")
        except ValueError:
            print("  Ingrese un número válido.")


def pedir_entero_positivo(mensaje):
    
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("  La cantidad debe ser mayor que cero.")
        except ValueError:
            print("  Ingrese un número entero válido.")


def esta_en_elipse(x, y, a, b):
   
    return (x ** 2) / (a ** 2) + (y ** 2) / (b ** 2) <= 1


def esta_en_hiperbola(x, y, c, d):
    
    return (x ** 2) / (c ** 2) - (y ** 2) / (d ** 2) >= 1


def simular(a, b, c, d, cantidad):
   
    puntos_elipse = 0
    puntos_interseccion = 0

    for _ in range(cantidad):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        if esta_en_elipse(x, y, a, b):
            puntos_elipse += 1
            if esta_en_hiperbola(x, y, c, d):
                puntos_interseccion += 1

    return puntos_elipse, puntos_interseccion


def main():
    print("=" * 60)
    print(" Área de intersección elipse-hipérbola (Montecarlo)")
    print("=" * 60)

    a = pedir_positivo("Ingrese a (semieje horizontal de la elipse): ")
    b = pedir_positivo("Ingrese b (semieje vertical de la elipse): ")
    c = pedir_positivo("Ingrese c (constante x de la hipérbola): ")
    d = pedir_positivo("Ingrese d (constante y de la hipérbola): ")
    cantidad = pedir_entero_positivo("Ingrese la cantidad de puntos aleatorios: ")

    puntos_elipse, puntos_interseccion = simular(a, b, c, d, cantidad)

    area_elipse = math.pi * a * b

    if puntos_elipse > 0:
        area_interseccion = (puntos_interseccion / puntos_elipse) * area_elipse
    else:
        area_interseccion = 0.0

    print("\n" + "-" * 60)
    print(" RESULTADOS")
    print("-" * 60)
    print(f" Puntos generados                          : {cantidad}")
    print(f" Puntos que cayeron dentro de la elipse    : {puntos_elipse}")
    print(f" Puntos en la intersección elipse-hipérbola: {puntos_interseccion}")
    print(f" Área de la elipse (fórmula π·a·b)         : {area_elipse:.4f}")
    print(f" Área aproximada de la intersección        : {area_interseccion:.4f}")
    print("-" * 60)


if __name__ == "__main__":
    main()
