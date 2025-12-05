# PORTADA

# Nombre: Luis Roberto Garcia Guillen
# Matrícula: 2530041
# Grupo: 1-3


# RESUMEN EJECUTIVO
"""
    Una función en Python es un bloque de código reutilizable que ejecuta 
    una acción específica. Los parámetros son variables que se definen en 
    la función, y los argumentos son los valores reales que se envían al 
    llamarla. Separar la lógica en funciones permite crear programas más 
    ordenados y fáciles de mantener. Las funciones pueden regresar valores 
    usando return, lo cual es mejor que solo imprimir resultados, porque 
    permite reutilizar los datos en otras partes del programa. Este trabajo 
    contiene 6 programas que aplican funciones, validaciones y pruebas.
"""


# PRINCIPIOS Y BUENAS PRÁCTICAS
"""
    - Cada función debe realizar una sola tarea.
    - Evitar repetir código, usar funciones reutilizables.
    - Las funciones puras son más confiables y fáciles de probar.
    - Usar nombres descriptivos en funciones y variables.
    - Documentar el propósito de cada función.
"""


# PROBLEMA 1

# Cálculo de área y perímetro de un rectángulo

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

width = 5
height = 3

if width > 0 and height > 0:
    print("Area:", calculate_area(width, height))
    print("Perimeter:", calculate_perimeter(width, height))
else:
    print("Error: invalid input")


#  PROBLEMA 2

# Clasificador de calificaciones

def classify_grade(score):
    if score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    else:
        return "A"

score = 88
if 0 <= score <= 100:
    print("Score:", score)
    print("Category:", classify_grade(score))
else:
    print("Error: invalid input")


# PROBLEMA 3

# Estadísticas de una lista de números

def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }

numbers_text = "10,20,30,40"
if numbers_text.strip() != "":
    try:
        numbers_list = [float(x) for x in numbers_text.split(",")]
        if len(numbers_list) > 0:
            stats = summarize_numbers(numbers_list)
            print("Min:", stats["min"])
            print("Max:", stats["max"])
            print("Average:", stats["average"])
        else:
            print("Error: invalid input")
    except:
        print("Error: invalid input")
else:
    print("Error: invalid input")


# PROBLEMA 4

# Aplicar descuento a una lista de precios

def apply_discount(prices_list, discount_rate):
    return [price * (1 - discount_rate) for price in prices_list]

prices_text = "100,250,300"
discount_rate = 0.10

try:
    prices_list = [float(x) for x in prices_text.split(",")]
    if len(prices_list) > 0 and all(p > 0 for p in prices_list) and 0 <= discount_rate <= 1:
        new_prices = apply_discount(prices_list, discount_rate)
        print("Original prices:", prices_list)
        print("Discounted prices:", new_prices)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")


# PROBLEMA 5

# Saludo con parámetro por defecto

def greet(name, title=""):
    name = name.strip()
    title = title.strip()
    if title != "":
        full_name = f"{title} {name}"
    else:
        full_name = name
    return f"Hello, {full_name}!"

name = "Alice"
print("Greeting:", greet(name))
print("Greeting:", greet(name="Bob", title="Eng."))


# PROBLEMA 6

# Factorial (versión iterativa)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5
if isinstance(n, int) and 0 <= n <= 20:
    print("n:", n)
    print("Factorial:", factorial(n))
else:
    print("Error: invalid input")


# CONCLUSIONES
"""
    Las funciones permiten dividir el trabajo en partes pequeñas y fáciles 
    de entender. Es mejor usar return porque los resultados pueden 
    reutilizarse en diferentes cálculos. Los parámetros y valores por 
    defecto ofrecen flexibilidad al llamar funciones. La lógica principal 
    del programa queda más limpia al delegar cálculos repetidos a funciones. 
    Aprendí la importancia de validar entradas antes de procesarlas. 
    También comprendí la diferencia entre funciones de apoyo y el flujo 
    principal del programa.
"""


# REFERENCIAS
"""
    1) Python Official Docs - Functions
    2) W3Schools - Python Functions Tutorial
    3) Apuntes de clase sobre programación estructurada
    4) Real Python - Best practices for function design
    5) Tutoriales de ciclos y listas en Python
"""