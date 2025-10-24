#primer ejercicio
def cuadrados():
    # Pedimos un número al usuario
    numero = int(input("Escribe un número entero positivo: "))

    # Creamos un diccionario vacío
    diccionario = {}

    # Recorremos los números desde 1 hasta el número que escribió el usuario
    for i in range(1, numero + 1):
        # Guardamos en el diccionario el número y su cuadrado
        diccionario[i] = i * i

    # Mostramos el resultado final
    print("Los cuadrados son:", diccionario)

# Llamamos la función para que se ejecute
cuadrados()
#segundo ejercicio
def contar_caracteres():
    # Pedimos una palabra o frase
    texto = input("Escribe una palabra o frase: ")

    # Creamos un diccionario vacío
    conteo = {}

    # Recorremos cada letra del texto
    for letra in texto:
        # Si la letra ya está en el diccionario, aumentamos su cantidad
        if letra in conteo:
            conteo[letra] = conteo[letra] + 1
        # Si la letra no está, la agregamos con valor 1
        else:
            conteo[letra] = 1

    # Mostramos cuántas veces aparece cada letra
    print("Las letras aparecen así:", conteo)

# Llamamos la función
contar_caracteres()
#ejercicio 3
def frutas():
    # Creamos un diccionario con el nombre de la fruta y su precio por kilo
    precios = {
        "manzana": 1500,
        "pera": 2000,
        "naranja": 1800,
        "fresa": 2500
    }

    # Usamos un ciclo para repetir el proceso hasta que el usuario diga que no
    while True:
        # Pedimos el nombre de la fruta
        fruta = input("Escribe el nombre de la fruta: ")

        # Revisamos si la fruta está en el diccionario
        if fruta in precios:
            # Pedimos cuántos kilos se vendieron
            kilos = float(input("Cuántos kilos vendiste: "))
            # Calculamos el total multiplicando precio * kilos
            total = precios[fruta] * kilos
            # Mostramos el total
            print("El total a pagar es:", total)
        else:
            # Si la fruta no existe, mostramos un mensaje de error
            print("Esa fruta no está en la lista.")

        # Preguntamos si quiere hacer otra consulta
        seguir = input("¿Quieres hacer otra consulta? (s/n): ")

        # Si el usuario escribe algo diferente de 's', el ciclo termina
        if seguir != "s":
            break

# Llamamos la función
frutas()
