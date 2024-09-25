from ejercicio import *
#a
promedio_top = promedio_20(lista_ingresos)
print(f"Promedio del 20% que más gana: {promedio_top}")

#b
promedio_total = promedio_todos(lista_ingresos)
print(f"Promedio de todos los ingresos: {promedio_total}")

#c
valores_repetidos = valor_mas_repetido(lista_ingresos)
print(f"Valor(es) más repetido(s): {valores_repetidos}")

#d
media_geom = media_geometrica(lista_ingresos)
print(f"Media geométrica: {media_geom}")

#e
recorrido = recorrer_lista_ambos_sentidos(lista_ingresos)
print(f"Lista recorrida en ambos sentidos: {recorrido}")



#4
print("Nombres:", nombres)
print("Sexos:", sexos)
print("Horas trabajadas:", horas_trabajadas)
print("Ingresos semanales:", ingresos_semanales)

#6
numeros = pedir_numeros(rango_minimo, rango_maximo)
print("Los numeros ingresados son:", numeros)

#7
menores = encontrar_menores(nombres, edades)
for nombre, edad in menores:
    print(f"{nombre} tiene {edad} años")
    