import time
import math
import mpmath
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import os


# FUNCIONES
def alturamaxima():  # Funcion altura maxima
    print("\nCalculadora de Altura Maxima:")
    g = 9.81

    while True:
        try:
            # Entrada para velocidad inicial
            v0 = float(input("Velocidad Inicial: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la velocidad inicial.")
            continue

    while True:
        try:
            angulo = float(input("Valor ángulo: "))  # Entrada para el angulo
            break
        except ValueError:
            print("Error: Ingrese un número válido para el ángulo.")
            continue

    angulo_radians = math.radians(angulo)
    hmax = ((v0**2) * ((math.sin(angulo_radians)) ** 2)) / (2 * g)
    return hmax  # Retorno del calculo de altura maxima


def pendiente():  # Funcion pendiente
    print("\nCalculadora de Pendiente:")

    while True:
        try:
            px1 = float(input("Punto x1: "))  # Entrada para punto x1
            break
        except ValueError:
            print("Error: Ingrese un número válido para Punto x1.")

    while True:
        try:
            px2 = float(input("Punto x2: "))  # Entrada para punto x2
            break
        except ValueError:
            print("Error: Ingrese un número válido para Punto x2.")

    while True:
        try:
            py1 = float(input("Punto y1: "))  # Entrada para punto y1
            break
        except ValueError:
            print("Error: Ingrese un número válido para Punto y1.")

    while True:
        try:
            py2 = float(input("Punto y2: "))  # Entrada para punto y2
            break
        except ValueError:
            print("Error: Ingrese un número válido para Punto y2.")

    pendiente_val = (py2 - py1) / (px2 - px1)
    return pendiente_val  # Retorno del calculo de la pendiente


def aceleracionpromedio():  # Funcion aceleracion promedio
    print("\nCalculadora de Aceleración Promedio:")

    while True:
        try:
            # Entrada para tiempo inicial
            t0 = float(input("Tiempo Inicial: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para el Tiempo Inicial.")

    while True:
        try:
            # Entrada para velocidad inicial
            v0 = float(input("Velocidad Inicial: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Velocidad Inicial.")

    while True:
        try:
            t1 = float(input("Tiempo Final: "))  # Entrada para tiempo final
            break
        except ValueError:
            print("Error: Ingrese un número válido para el Tiempo Final.")

    while True:
        try:
            # Entrada para velocidad final
            v1 = float(input("Velocidad Final: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Velocidad Final.")

    aceleracionpromedio_val = (v1 - v0) / (t1 - t0)
    return aceleracionpromedio_val  # Retorno de la aceleracion promedio


def desplazamiento(v0, a, t):
    desplazamiento = (v0 * t) + (0.5 * a * (t**2))
    return desplazamiento  # Retorno del desplazamiento


def rango(angulo, velocidadinicial):
    g = 9.81
    angulo = math.radians(angulo)
    rango = ((velocidadinicial**2) * (math.sin(2 * angulo))) / g
    return rango  # Retorno del rango


def velocidadpromedio():
    print("\nCalculadora de Velocidad Promedio:")

    while True:
        try:
            # Entrada para tiempo inicial
            t0 = float(input("Tiempo Inicial: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para el Tiempo Inicial.")

    while True:
        try:
            # Entrada para posicion inicial
            s0 = float(input("Posición Inicial: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Posición Inicial.")

    while True:
        try:
            t1 = float(input("Tiempo Final: "))  # Entrada para tiempo final
            break
        except ValueError:
            print("Error: Ingrese un número válido para el Tiempo Final.")

    while True:
        try:
            # Entrada para posicion final
            s1 = float(input("Posición Final: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Posición Final.")

    velocidadpromedio_val = (s1 - s0) / (t1 - t0)
    return velocidadpromedio_val  # Retorno de velocidad promedio


def velocidad_inicial():
    print("\nCalculadora de Velocidad Inicial:")

    while True:
        try:
            # Entrada para velocidad final
            v1 = float(input("Velocidad Final: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Velocidad Final.")

    while True:
        try:
            a = float(input("Aceleración: "))  # Entrada para aceleracion
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Aceleración.")

    while True:
        try:
            t = float(input("Tiempo: "))  # Entrada para tiempo
            break
        except ValueError:
            print("Error: Ingrese un número válido para el Tiempo.")

    velocidad_inicial_val = v1 - a * t
    return velocidad_inicial_val  # Retorno de velocidad inicial


def velocidadfinal(v1, a, s):
    velocidadfinal = math.sqrt(v1**2 + 2 * a * s)
    return velocidadfinal


def aceleracion():
    print("\nCalculadora de Aceleración:")

    while True:
        try:
            # Entrada para velocidad inicial
            vi = float(input("Velocidad Inicial: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Velocidad Inicial.")

    while True:
        try:
            # Entrada para velocidad final
            vf = float(input("Velocidad Final: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Velocidad Final.")

    while True:
        try:
            t = float(input("Tiempo: "))  # Entrada para tiempo
            break
        except ValueError:
            print("Error: Ingrese un número válido para el Tiempo.")

    aceleracion_val = (vf - vi) / t
    return aceleracion_val  # Retorno de aceleracion


def tiempo(vi, vf, s):
    t = (2 * s) / (vf + vi)
    return t


def proyectiles():
    print("\nCalculadora de Proyectiles:")

    while True:
        try:
            # Entrada para velocidad inicial
            vi = float(input("Velocidad Inicial: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Velocidad Inicial.")

    while True:
        try:
            ang = float(
                input("Angulo de lanzamiento: ")
            )  # Entrada para angulo de lanzamiento
            break
        except ValueError:
            print("Error: Ingrese un número válido para el Ángulo de lanzamiento.")

    ax = 0
    ay = -9.81
    ang_rad = math.radians(ang)
    r = rango(ang, vi)
    vix = vi * math.cos(ang_rad)
    vfx = velocidadfinal(vix, ax, r)
    t = tiempo(vix, vfx, r)
    viy = vi * math.sin(ang_rad)
    sy = desplazamiento(viy, ay, t)
    vfy = velocidadfinal(viy, ay, sy)

    print("\nParametros en x")  # Despliega parametros en x
    print(f"Desplazamiento: {r:.4f}")  # Despliega parametros el desplazamiento
    print(f"Velocidad Inicial: {vix:.4f}")  # Despliega velocidad inicial
    print(f"Velocidad Final: {vfx:.4f}")  # Despliega velocidad final
    print(f"Aceleracion: {ax:.4f}")  # Despliega aceleracion
    print(f"Tiempo: {t:.4f}")  # Despliega tiempo
    print("\nParametros en y")  # Despliega parametros en y
    print(f"Desplazamiento: {sy:.4f}")  # Despliega desplazamiento
    print(f"Velocidad Inicial: {viy:.4f}")  # Despliega velocidad inicial
    print(f"Velocidad Final: {vfy:.4f}")  # Despliega velocidad final
    print(f"Aceleracion: {ay:.4f}")  # Despliega aceleracion
    print(f"Tiempo: {t:.4f}")  # Despliega tiempo


def angulos():
    print("\nCalculadora de Ángulos:")

    while True:
        try:
            x = float(input("Valor de x: "))  # Entrada para valor de x
            break
        except ValueError:
            print("Error: Ingrese un número válido para el Valor de x.")

    while True:
        try:
            y = float(input("Valor de y: "))  # Entrada para valor de y
            break
        except ValueError:
            print("Error: Ingrese un número válido para el Valor de y.")

    ang_r = math.atan(y / x)
    ang_d = math.degrees(ang_r)
    return ang_d  # Retorno de angulo


def posicion_x():
    print("\nCalculadora de posición en x:")

    while True:
        try:
            # Entrada para posicion inicial
            xi = float(input("Posición Inicial: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Posición Inicial.")

    while True:
        try:
            v = float(input("Velocidad: "))  # Entrada para velocidad
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Velocidad.")

    while True:
        try:
            t = float(input("Tiempo: "))  # Entrada para tiempo
            break
        except ValueError:
            print("Error: Ingrese un número válido para el Tiempo.")

    xt = xi + (v * t)
    return xt  # Retorno de posicion en x


def tiempo_choque():
    print("\nCalculadora de tiempo donde chocan dos objetos:")
    print(
        "\nEsta simulación se realizará suponiendo que el primer objeto empieza en el origen (0,0)."
    )

    while True:
        try:
            d = float(
                input("Distancia entre los dos objetos: ")
            )  # Entrada para distancia entre dos objetos
            break
        except ValueError:
            print(
                "Error: Ingrese un número válido para la Distancia entre los dos objetos."
            )

    while True:
        try:
            v1 = float(
                input("Velocidad del primer objeto: ")
            )  # Entrada para velocidad del primer objeto
            break
        except ValueError:
            print(
                "Error: Ingrese un número válido para la Velocidad del primer objeto."
            )

    while True:
        try:
            print("Recuerda que una de las dos velocidades debe ser negativa!")
            v2 = float(
                input("Velocidad del segundo objeto: ")
            )  # Entrada para velocidad del segundo objeto
            break
        except ValueError:
            print(
                "Error: Ingrese un número válido para la Velocidad del segundo objeto."
            )

    while True:
        try:
            a1 = float(
                input("Aceleración del primer objeto: ")
            )  # Entrada para aceleracion del primer objeto
            break
        except ValueError:
            print(
                "Error: Ingrese un número válido para la Aceleración del primer objeto."
            )

    while True:
        try:
            a2 = float(
                input("Aceleración del segundo objeto: ")
            )  # Entrada para aceleracion del segundo objeto
            break
        except ValueError:
            print(
                "Error: Ingrese un número válido para la Aceleración del segundo objeto."
            )

    t = sym.Symbol("t")
    xf1 = v1 * t + 0.5 * a1 * (t**2)
    xf2 = v2 * t + 0.5 * a2 * (t**2) + d
    tf = sym.Eq(xf1, xf2)
    tiempo = sym.solve(tf, t)
    return tiempo  # Retorno del tiempo cuando dos objetos chocan


def masa_resorte():  # Funcion ecuacion de movimiento (masa resorte)
    print("\nCalculadora de Sistemas Masa/Resorte:")

    while True:
        try:
            f = float(input("Fuerza: "))  # Entrada para fuerza
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Fuerza.")

    while True:
        try:
            m = float(input("Masa: "))  # Entrada para masa
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Masa.")

    while True:
        try:
            s = float(input("Distancia: "))  # Entrada para distancia
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Distancia.")

    while True:
        try:
            # Entrada para posicion inicial
            xi = float(input("Posicion Inicial: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Posición Inicial.")

    while True:
        try:
            # Entrada para velocidad inicial
            vi = float(input("Velocidad Inicial: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la Velocidad Inicial.")

    k = f / s
    w = math.sqrt(k / m)
    c1 = xi
    c2 = vi / w

    print(f"Constante k: {k:.4f}")  # Despliega la constante k
    print(f"Frecuencia circular: {w:.4f}")  # Despliega la frecuencia circular
    print(
        f"Ecuación del movimiento: \nx(t) = {c1:.4f}cos({w:.4f}t) + {c2:.4f}sin({w:.4f}t)"
    )  # Despliega la ecuacion del movimiento


# GRAFICADORA
def graficadora():  # Funcion para graficar
    print("\nGraficadora\n")

    while True:
        valores_y = []
        # Menu de graficas
        funcion = input("""\nEscoge que deseas graficar
1. Velocidad vs tiempo
2. Posición vs tiempo
3. Graficación libre
"""
        )

        match funcion:
            case "1":  # Grafica para velocidad vs tiempo
                while True:
                    try:
                        v1 = float(
                            input("\nVelocidad Inicial: ")
                        )  # Entrada para velocidad inicial
                        break
                    except ValueError:
                        print(
                            "Error: Ingrese un número válido para la Velocidad Inicial."
                        )

                while True:
                    try:
                        # Entrada para aceleracion
                        a = float(input("Aceleración: "))
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para la Aceleración.")

                while True:
                    try:
                        ti = float(
                            input(f"Escribe el valor inicial de tiempo: ")
                        )  # Entrada para tiempo inicial
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para el tiempo inicial.")

                while True:
                    try:
                        tf = float(
                            input(f"Escribe el valor final de tiempo: ")
                        )  # Entrada para tiempo final
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para el tiempo final.")

                t = np.arange(ti, tf, 0.1)
                y = v1 + a * t
                for i in t:
                    y2 = v1 + a * i
                    valores_y.append(y2)

                valor_max = max(valores_y)
                valor_min = min(valores_y)

                print(
                    f"\nv(t)= {a}t + {v1}"
                )  # Despliega la ecuacion de la velocidad final
                print(
                    f"\nEl valor minimo en el eje de las y es {valor_min}"
                )  # Despliega el valor minimo en el eje de las y
                print(
                    f"El valor máximo en el eje de las y es {valor_max}"
                )  # Despliega el valor maximo en el eje de las y

                # Se grafica la grafica velocidad vs tiempo
                plt.plot(t, y, "r--")
                plt.title("Velocidad")
                plt.xlabel("Tiempo (s)")
                plt.ylabel("Velocidad (m/s)")
                plt.show()

                salida = input(
                    "\nEscribe SALIR si deseas volver al menú principal. Cualquier otra tecla para volver a graficar: "
                ).upper()
                if salida == "SALIR":
                    break
                else:
                    continue

            case "2":  # Grafica para posicion vs tiempo
                while True:
                    try:
                        x1 = float(
                            input("\nPosición Inicial: ")
                        )  # Entrada para velocidad final
                        break
                    except ValueError:
                        print(
                            "Error: Ingrese un número válido para la posición final."
                        )

                while True:
                    try:
                        v1 = float(
                            input("Velocidad Inicial: ")
                        )  # Entrada para velocidad inicial
                        break
                    except ValueError:
                        print(
                            "Error: Ingrese un número válido para la velocidad inicial."
                        )

                while True:
                    try:
                        # Entrada para aceleracion
                        a = float(input("Aceleración: "))
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para la aceleración.")

                while True:
                    try:
                        ti = float(
                            input(f"Escribe el valor inicial de tiempo: ")
                        )  # Entrada para tiempo inicial
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para el tiempo inicial.")

                while True:
                    try:
                        tf = float(
                            input(f"Escribe el valor final de tiempo: ")
                        )  # Entrada para tiempo final
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para el tiempo final.")

                t = np.arange(ti, tf, 0.1)
                y = x1 + (v1 * t) + (0.5 * a * t**2)
                for i in t:
                    y2 = x1 + (v1 * i) + (0.5 * a * i**2)
                    valores_y.append(y2)

                valor_max = max(valores_y)
                valor_min = min(valores_y)

                print(
                    f"\ns(t)= {0.5*a}t^2 + {v1}t + {x1}"
                )  # Despliega la ecuacion de la posicion final
                print(
                    f"\nEl valor minimo en el eje de las y es {valor_min}"
                )  # Despliega el valor minimo en el eje de las y
                print(
                    f"El valor máximo en el eje de las y es {valor_max}"
                )  # Despliega el valor maximo en el eje de las y

                # Se grafica la grafica posicion vs tiempo
                plt.plot(t, y, "r--")
                plt.title("Posición")
                plt.xlabel("Tiempo (s)")
                plt.ylabel("Posición (m)")
                plt.show()

                salida = input(
                    "\nEscribe SALIR si deseas volver al menú principal. Cualquier otra tecla para volver a graficar: "
                ).upper()
                if salida == "SALIR":
                    break
                else:
                    continue

            case "3":  # Grafica libre
                eje_y = input(
                    "\nEscribe lo que deseas graficar en respecto al tiempo (Este sera el nombre del eje de las y): "
                )  # Entrada para definir que se quiere graficar
                titulo = input(
                    "Elije un titulo: "
                )  # Entrada para establecer titulo de la grafica

                while True:
                    try:
                        ti = float(
                            input(f"Escribe el valor inicial de tiempo: ")
                        )  # Entrada para tiempo inicial
                        break
                    except ValueError:
                        print(
                            "Error: Ingrese un número válido para el valor inicial de tiempo."
                        )

                while True:
                    try:
                        tf = float(
                            input(f"Escribe el valor final de tiempo: ")
                        )  # Entrada para tiempo final
                        break
                    except ValueError:
                        print(
                            "Error: Ingrese un número válido para el valor final de tiempo."
                        )

                t = np.arange(ti, tf, 0.1)

                grado = int(
                    input("Introduce el grado de la función (límite de 3):")
                )  # Entrada para definir de que grado es la funcion a graficar

                while True:
                    if grado == 1:
                        a = float(
                            input("Introduce el valor del coeficiente de grado 1: ")
                        )  # Entrada para el coeficiente de grado 1
                        k = float(input("Introduce el valor constante: "))
                        y = a * t + k
                        break
                    elif grado == 2:
                        a = float(
                            input("Introduce el valor del coeficiente de grado 2: ")
                        )  # Entrada para el coeficiente de grado 2
                        b = float(
                            input("Introduce el valor del coeficiente de grado 1: ")
                        )  # Entrada para el coeficiente de grado 1
                        k = float(input("Introduce el valor constante: "))
                        y = (a * t**2) + (b * t) + k
                        break
                    elif grado == 3:
                        a = float(
                            input("Introduce el valor del coeficiente de grado 3: ")
                        )  # Entrada para el coeficiente de grado 3
                        b = float(
                            input("Introduce el valor del coeficiente de grado 2: ")
                        )  # Entrada para el coeficiente de grado 2
                        c = float(
                            input("Introduce el valor del coeficiente de grado 1: ")
                        )  # Entrada para el coeficiente de grado 1
                        k = float(input("Introduce el valor constante: ")) # Entrada para el valor constante
                        y = (a * t**3) + (b * t**2) + (c * t) + k
                        break
                    else:
                        print("Valor no válido") 

                for i in t:
                    if grado == 1:
                        y2 = a * i + k
                    elif grado == 2:
                        y2 = (a * i**2) + (b * i) + k
                    elif grado == 3:
                        y2 = (a * i**3) + (b * i**2) + (c * i) + k
                    valores_y.append(y2)

                valor_max = max(valores_y)
                valor_min = min(valores_y)

                print(f"\nEl valor minimo en el eje de las y es {valor_min}")  # Despliega el valor minimo en el eje de las y 
                print(f"El valor máximo en el eje de las y es {valor_max}")  # Despliega el valor maximo en el eje de las y

                # Grafica la graficacion libre
                plt.plot(t, y, "r--")
                plt.title(titulo)
                plt.xlabel("Tiempo")
                plt.ylabel(eje_y)
                plt.show()

                salida = input(
                    "\nEscribe SALIR si deseas volver al menú principal. Cualquier otra tecla para volver a graficar: "
                ).upper()
                if salida == "SALIR":
                    break
                else:
                    continue
            case _:
                print("Opción no válida. Volver a intentar")
    main()


# MENU CALCULADORA
def calculadora_uf():  # Funcion que despliega las funciones de los calculos y contiene el menu de funciones
    print(
        "Bienvenido a la sección de calculadoras! Por favor, elije el número de calculadora que desees usar:"
    )
    print("""\n1. Altura Máxima
2. Pendiente
3. Aceleración Promedio
4. Desplazamiento
5. Rango
6. Velocidad Promedio
7. Velocidad Inicial
8. Velocidad Final
9. Aceleración
10. Tiempo
11. Movimiento Parabólico
12. Ángulos
13. Posición en x
14. Tiempo cuando chocan dos objetos
15. Sistema Masa Resorte
"""
    )

    while True:
        n = input(
            "\nIntroduce un número para elegir la calculadora a usar o presiona cualquier otra tecla para salir de esta sección: "
        )  # Entrada para elegir cual funcion el usuario deseaa utilizar

        match n:
            case "1":  # Salida para funcion de altura maxima
                x = alturamaxima()
                print(f"Altura máxima: {x:.4f}")

            case "2":  # Salida para funcion de pendiente
                x = pendiente()
                print(f"Pendiente: {x:.4f}")

            case "3":  # Salida para funcion de aceleracion promedio
                x = aceleracionpromedio()
                print(f"Aceleración promedio: {x:.4f}")

            case "4":  # Salida para funcion de desplazamiento
                print("\nCalculadora de Desplazamiento:")
                while True:
                    try:
                        v0 = float(input("Velocidad Inicial: "))  # Entrada para velocidad inicial
                        break
                    except ValueError:
                        print(
                            "Error: Ingrese un número válido para la velocidad inicial."
                        )

                while True:
                    try:
                        a = float(input("Aceleración: "))  # Entrada para aceleracion
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para la aceleración.")

                while True:
                    try:
                        t = float(input("Tiempo: "))  # Entrada para tiempo
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para el tiempo.")
                x = desplazamiento(v0, a, t)
                print(f"Desplazamiento: {x:.4f}")  # Despliega el desplazamiento

            case "5":  # Salida para funcion de rango
                print("\nCalculadora de Rango:")
                while True:
                    try:
                        velocidadinicial = float(input("Velocidad Inicial: "))  # Entrada de velocidad inicial
                        break
                    except ValueError:
                        print(
                            "Error: Ingrese un número válido para la velocidad inicial."
                        )

                while True:
                    try:
                        angulo = float(input("Ángulo: "))  # Entrada de angulo
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para el ángulo.")
                x = rango(angulo, velocidadinicial)
                print(f"Rango: {x:.4f}")  # Despliega el rango

            case "6":  # Salida para funcion de velocidad promedio
                x = velocidadpromedio()
                print(f"Velocidad Promedio: {x:.4f}")

            case "7":  # Salida para funcion de velocidad inicial
                x = velocidad_inicial()
                print(f"Velocidad Inicial: {x:.4f}")

            case "8":  # Salida para funcion de velocidad final
                print("\nCalculadora de Velocidad Final:")
                while True:
                    try:
                        v1 = float(input("Velocidad inicial: "))  # Entrada de velocidad inicial
                        break
                    except ValueError:
                        print(
                            "Error: Ingrese un número válido para la velocidad inicial."
                        )

                while True:
                    try:
                        a = float(input("Aceleración: "))  # Entrada de aceleracion
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para la aceleración.")

                while True:
                    try:
                        s = float(input("Desplazamiento: "))  # Entrada de desplazamiento
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para el desplazamiento.")
                x = velocidadfinal(v1, a, s)
                print(f"Velocidad Final: {x:.4f}")  # Despliega la velocidad final

            case "9":  # Salida para funcion de aceleracion
                x = aceleracion()
                print(f"Aceleración: {x:.4f}")

            case "10":  # Salida para funcion de tiempo
                print("\nCalculadora de Tiempo:")
                while True:
                    try:
                        vi = float(input("Velocidad Inicial: "))  # Entrada de velocidad inicial
                        break
                    except ValueError:
                        print(
                            "Error: Ingrese un número válido para la velocidad inicial."
                        )

                while True:
                    try:
                        vf = float(input("Velocidad Final: "))  # Entrada de velocidad final
                        break
                    except ValueError:
                        print(
                            "Error: Ingrese un número válido para la velocidad final."
                        )

                while True:
                    try:
                        s = float(input("Desplazamiento: "))  # Entrada de desplazamiento
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido para el desplazamiento.")
                x = tiempo(vi, vf, s)
                print(f"Tiempo: {x:.4f}")  # Despliega el tiempo

            case "11":  # Salida para funcion de proyectiles
                proyectiles()

            case "12":  # Salida para funcion de angulos
                x = angulos()
                print(f"Ángulos: {x:.4f}")

            case "13":  # Salida para funcion de posicion x
                x = posicion_x()
                print(f"Posición x: {x:.4f}")

            case "14":  # Salida para funcion de tiempo choque
                x = tiempo_choque()
                print(f"Tiempo: {x:.4f}")

            case "15":  # Salida para funcion de masa resorte
                masa_resorte()

            case _:  # Regresa al manu principal
                main()


# QUIZ
def quiz():  # Funcion para el quiz
    Dir = Path.cwd() / "Preguntas"
    nombre = input("Introduce tu nombre: ")
    respuestas = ""
    correctas = 0

    PathUsr = Path.cwd() / nombre  # Path

    if PathUsr.exists():  # Checar si el nombre no se repite
        print("El nombre que introdujo ya está en uso.\n")
        nombre = input("Introduce tu nombre: ")
        PathUsr = Path.cwd() / nombre

    Path(PathUsr).mkdir()

    respuestas = respuestas + "Respuestas de: " + nombre + "\n"

    for quizNum in range(15):
        Pregunta = f"Pregunta{quizNum + 1}.txt"
        Res = f"Ans{quizNum + 1}.txt"

        Pre = open(Pregunta)  # Despliega la pergunta
        PreC = Pre.read()

        Ans = open(Res)
        AnsC = Ans.read()

        print(PreC)
        UsRes = input().lower()  # Entrada de respuesta

        respuestas = respuestas + "\nPregunta: " + PreC + "\nTu respuesta: " + UsRes + "\n"

        if UsRes == AnsC:  # Checa si la respuesta es correcta o incorrecta
            respuestas += "correcto\n" 
            correctas += 1
        else:
            respuestas += "incorrecto\n"

    print("\nFinalizaste el quiz!")
    print(f"Tus respuestas las puedes encontrar en: {PathUsr}")
    promedio = (correctas*100) / 15  # Calculo para calificacion
    ResUsr = Path(PathUsr / "respuestas1.txt")
    ResUsr.write_text(
        f"{respuestas} \n\nSacaste {correctas}/15 \nCalificación: {round(promedio,1)} \n\nTus respuestas las puedes encontrar en: {PathUsr}"
    )  # Despliega la calificacion y donde encontrar las respuestas


# MAIN
def main():  # Funcion del menu principal
    print("""\nBIENVENIDO A LA CALCULADORA DE FÍSICA CINEMÁTICA. POR FAVOR ESCRIBE EL NÚMERO DE LA OPCIÓN QUE ELIJAS
1. Calculadoras
2. Quiz
3. Graficadora
4. Salir
"""
    )
    while True:
        num = input("Introduce el número de la función que desees correr: ")  # Entrada para indicar que elige el usuario del menu principal
        match num:
            case "1":
                calculadora_uf()

            case "2":
                quiz()

            case "3":
                graficadora()

            case "4":
                exit()

            case _:
                print("Número no válido")
                continue


main()  # Muestra el menu principal
