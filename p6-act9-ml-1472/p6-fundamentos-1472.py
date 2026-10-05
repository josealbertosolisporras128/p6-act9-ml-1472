# practica 6 fundamentos
# jose solis nc 1472

# CASO 1, 3 EJEMPLOS
print("-------------")
print("ejemplo 1 Almacenar un número entero y un flotante")
edad = 25
estatura = 1.75

print(edad)
print(estatura)

print("-------------")
print("ejemplo 2 De número entero a texto")
puntuacion = 100        # puntuacion es de tipo int
puntuacion = "Excelente" # puntuacion ahora es de tipo str

print(puntuacion)

print("-------------")
print("ejemplo 3 Convertir un texto con número a entero, flotante y texto explícito")
numero_texto = "10"

a = int(numero_texto)    # a será el número entero 10
b = float(numero_texto)  # b será el número flotante 10.0
c = str(numero_texto)    # c será la cadena '10'

print(a)
print(b)
print(c)
 # CASO 2, 3 EJEMPLOS
print("-------------")
print("ejemplo 1")
nombre, ciudad, profesion = "Ana", "Madrid", "Ingeniera"

print(nombre)
print(ciudad)
print(profesion)

print("-------------")
print("ejemplo 2")
a = b = c = 100

print(a)
print(b)
print(c)

print("-------------")
print("ejemplo 3")
colores = ["Rojo", "Verde", "Azul"]
c1, c2, c3 = colores

print(c1)
print(c2)
print(c3)

# CASO 3, 3 EJEMPLOS
print("-------------")
print("ejemplo 1")
x = 10
y = 3.14
z = "Hola Python"

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>

print("-------------")
print("ejemplo 2")
x = True
y = False
z = None

print(type(x))  # <class 'bool'>
print(type(y))  # <class 'bool'>
print(type(z))  # <class 'NoneType'>

print("-------------")
print("ejemplo 3")
x = [1, 2, 3]
y = (1, 2, 3)
z = {"nombre": "Ana", "edad": 30}

print(type(x))  # <class 'list'>
print(type(y))  # <class 'tuple'>
print(type(z))  # <class 'dict'>

# CASO 4, 3 EJEMPLOS
print("-------------")
print("ejemplo 1")
x = 20
y = 6

print(x + y)   # 26 (Suma)
print(x - y)   # 14 (Resta)
print(x * y)   # 120 (Multiplicación)
print(x / y)   # 3.3333333333333335 (División flotante)
print(x % y)   # 2 (Módulo / Residuo de 20 ÷ 6)
print(x ** y)  # 64000000 (Potencia: 20 elevado a la 6)
print(x // y)  # 3 (División entera: resultado redondeado hacia abajo)

print("-------------")
print("ejemplo 2")
x = 12.5
y = 2.5

print(x + y)   # 15.0
print(x - y)   # 10.0
print(x * y)   # 31.25
print(x / y)   # 5.0
print(x % y)   # 0.0
print(x ** y)  # 559.0169943749475 (12.5 elevado a la 2.5)
print(x // y)  # 5.0

print("-------------")
print("ejemplo 3")
x = -17
y = 5

print(x + y)   # -12
print(x - y)   # -22
print(x * y)   # -85
print(x / y)   # -3.4
print(x % y)   # 3 (Residuo en Python ajustado al signo del divisor)
print(x ** y)  # -1419857 (-17 elevado a la 5)
print(x // y)  # -4 (Redondea hacia abajo hacia el infinito negativo)

# CASO 5, 3 EJEMPLOS
print("-------------")
print("ejemplo 1")
nota = 8.5

# Ambas expresiones evalúan si la nota está estrictamente entre 0 y 10
print(0 < nota < 10)             # True
print(0 < nota and nota < 10)     # True
print("-------------")
print("ejemplo 2")
edad = 150

# Evalúa si la edad está dentro de un rango realista (1 a 120)
print(1 <= edad <= 120)            # False
print(1 <= edad and edad <= 120)   # False
print("-------------")
print("ejemplo 3")
temperatura = 22

# Evalúa si la temperatura está entre el punto de congelación (0) y ebullición (100)
print(0 <= temperatura <= 100)               # True
print(0 <= temperatura and temperatura <= 100) # True

print("jose solis nc 1472")