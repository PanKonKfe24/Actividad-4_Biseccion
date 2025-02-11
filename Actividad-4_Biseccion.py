"""
           Autor:
   Juan Pablo Buitrago Rios
   juanybrisagames@gmail.com
   Version 2.0 : 10/02/2025 01:10am

"""


import numpy as np
import matplotlib.pyplot as plt

# Definir la función que va introducirse en
# el esquema del metodo de biseccion
def f(x):
    return x**3 - 4.0*x - 9.0

# Algoritmo numerico del
# Método de Bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
# Verificar si el método de bisección es aplicable
# Para que sea aplicable, f(a) y f(b) deben tener signos opuestos
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en el intervalo dado.")
        return None
    
    # Listas para almacenar los valores de iteraciones y errores
    iteraciones = []  # Almacena los valores de 'c' en cada iteración
    errores_abs = []  # Lista para almacenar el error absoluto
    errores_rel = []  # Lista para almacenar el error relativo
    errores_cua = []  # Lista para almacenar el error cuadrático
    c_old = a  # Inicialización de c_old para el cálculo de errores en la primera iteración

    # Imprimir encabezado de la tabla de iteraciones
    print("\nIteraciones del Método de Bisección:")
    print("Iter |       a       |       b       |       c       |      f(c)      |     Error_abs     |     Error_rel     |     Error_cua     ")
    print("-" * 85)


    #Iniciamos el ciclo
    for i in range(max_iter):
        c = (a + b) / 2  # Calculamos el punto medio
        iteraciones.append(c) #Agregamos C a la lista de iteraciones
        
        #Calculamos los errores
        error_abs = abs(c - c_old) #Error Absoluto
        error_rel = error_abs/c    #Error Relativo
        error_cua = (c - c_old)**2 #Error Cuadrátivo

        errores_abs.append(error_abs) # Agregar error absoluto a la lista
        errores_rel.append(error_rel) # Agregar error relativo a la lista
        errores_cua.append(error_cua) # Agregar error cuadrático a la lista


        #Mostrar los valores en cada iteracion en un formato designado
        print(f"{i+1:4d} | {a:.8f} | {b:.8f} | {c:.8f} | {f(c):.8f} | {error_abs:.8e} | {error_rel:.8e} | {error_cua:.8e}")

        if abs(f(c)) < tol or error_abs < tol:
            break

        #Actualizmos el intervalo según sea el caso
        if f(a) * f(c) < 0:
            b = c # El nuevo límite superior es 'c'
        else:
            a = c # El nuevo límite inferior es 'c'
        
        c_old = c # Guardar el valor anterior de c para el cálculo del error en la siguiente iteración

    return iteraciones, errores_abs, errores_rel, errores_cua 

# Parámetros iniciales
# se introduce el intervalo [a, b]
a, b = 2, 3
#a, b = 0, 1.5
#a, b = -2, -1
iteraciones, errores_abs, errores_rel, errores_cua = biseccion(a, b)

# Crear la figura
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica de la función y la convergencia de iteraciones
x = np.linspace(a - 1, b + 1, 400)
y = f(x)

ax[0].plot(x, y, label=r'$f(x) = x**3 - 4.0*x - 9.0$', color='b')
ax[0].axhline(0, color='k', linestyle='--', linewidth=1)  # Línea en y=0
ax[0].scatter(iteraciones, [f(c) for c in iteraciones], color='red', label='Iteraciones')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title("Convergencia del Método de Bisección")
ax[0].legend()
ax[0].grid()

# Gráfica de convergencia del error
ax[1].plot(range(1, len(errores_abs)+1), errores_abs, label = "Error Absoluto" , marker='o', linestyle='-', color='r')
ax[1].plot(range(1, len(errores_rel)+1), errores_rel, label = "Error Relativo" , marker='s', linestyle='-', color='b')
ax[1].plot(range(1, len(errores_cua)+1), errores_cua, label = "Error Cuadrático" , marker='^', linestyle='-', color='y')
ax[1].set_yscale("log")  # Escala logarítmica
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Errores")
ax[1].set_title("Errores de cada Iteración")
ax[1].legend()
ax[1].grid()

# Guardar la figura
plt.savefig("biseccion_convergencia.png", dpi=300)
plt.show()

