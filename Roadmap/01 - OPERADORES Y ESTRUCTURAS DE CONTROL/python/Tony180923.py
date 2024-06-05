"""
Operadores
"""

# Operadores aritméticos
print(f"Suma: 10 + 3 = 10 {10 + 3}")
print(f"Resta: 10 - 3 = 10 {10 - 3}")
print(f"Multiplicación: 10 * 3 = 10 {10 * 3}")
print(f"División: 10 / 3 = 10 {10 / 3}")
print(f"Módulo: 10 % 3 = 10 {10 % 3}")
print(f"Exponente: 10 ** 3 = 10 {10 ** 3}")
print(f"División entera: 10 // 3 = 10 {10 // 3}")

# Operadores de comparación 
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 10 es {10 <= 3}")

# Operadores lógicos 
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1  == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de Asignación 
my_number = 11 # asignación 
print(my_number)
my_number += 1  #suma y asignación 
print(my_number)
my_number -= 1 #resta y asignación 
print(my_number)
my_number *= 1 # multiplicación y asignación
print(my_number)
my_number /= 1 # división y asignación 
print(my_number)
my_number %= 1 #módulo y asignación
print(my_number)
my_number **= 1 #exponente y asignación
print(my_number)
my_number //= 1 #división entera y asignación 
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia 
print(f"'u'  not in 'Juan' = {'u' not in 'Juan'}")
print(f"'f' not in 'Juan' = {'f' not in 'Juan'}")

# Operadores de bit
a = 10 #1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3 }") # 0010
print(f"OR: 10 | 3 = {10 | 3 }") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3 }") # 1001
print(f"NOT: 10 ~ 3 = {~10}") 
print(f"Desplazamiento a la derecha: 10 >> 2 = { 10 >> 2 }") # 0010
print(f"Desplazamiento a la izquierda 10 << 2 = {10 << 2 }") # 101000

"""
Estructuras de control
"""

# Condicionales 

my_string = "Antonio"

if my_string == "Juan":
    print("my_string es 'Juan'")
elif my_string == "Antonio":
    print("my_string es 'Antonio'")
else:
    print("my_string no es 'Juan' ni 'Antonio'")

    #interativas

for i in range(11):
        print(i)

        i = 0 

        while i <= 10:
            print(i)
            i += 1

            # manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
     print("ha finalizado el manejo de excepciones")

"""
Extra
"""


for number in range(10, 56):
     if number % 2 == 0 and number != 16 and number % 3  != 0: 
          print(number)

