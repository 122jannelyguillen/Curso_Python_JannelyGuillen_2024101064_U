# Crear un programa que pida dos números y obtengan como resultado cuál de ellos es par, o si ambos lo son

# Pedir dos números al usuario 
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Verificar y mostrar cuáles son pares
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos números son pares.")
elif num1 % 2 == 0:
    print("El primer número es par.")
elif num2 % 2 == 0:
    print("El segundo número es par.")
else:
    print("Ninguno de los dos es par.")