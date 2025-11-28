import random
import pandas as pd

# hago la lista con 10 números random de 1 a 100
lista = [random.randint(1, 100) for _ in range(10)]

# creo la serie y le pongo el índice de 1 a 10
serie = pd.Series(lista, index=range(1, 11), name="numeros aleatorios")
serie.index.name = "idx"

# saco los cuadrados de los números
serie_cuadrados = serie**2
serie_cuadrados.name = "numeros_cuadrados"

# muestro los 4 últimos
print("Últimos 4:")
print(serie_cuadrados.tail(4))

# guardo los que son mayores a 500 (sin índice)
mayores_500 = serie_cuadrados[serie_cuadrados > 500].tolist()

print("\nNúmeros mayores a 500:")
print(mayores_500)