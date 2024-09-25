#1 a
lista_ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]

def promedio_20(lista_ingresos):
    n = 0
    for _ in lista_ingresos:
        n += 1

    cantidad = n // 5 
    suma = 0
    contador = 0

    for _ in range(cantidad):
        maximo = lista_ingresos[0]
        for ingreso in lista_ingresos:
            if ingreso > maximo:
                maximo = ingreso
        
        suma += maximo
        contador += 1
        
        nueva_lista = []
        encontrado = False
        for ingreso in lista_ingresos:
            if ingreso == maximo and not encontrado:
                encontrado = True
                continue
            nueva_lista = nueva_lista + [ingreso]
        lista_ingresos = nueva_lista

    if contador == 0:
        return 0
    return suma / contador

#b
def promedio_todos(lista_ingresos):
    suma = 0
    contador = 0
    for ingreso in lista_ingresos:
        suma += ingreso
        contador += 1
    return suma / contador if contador > 0 else 0

#c
def valor_mas_repetido(lista_ingresos):
    conteos = {}
    for ingreso in lista_ingresos:
        if ingreso in conteos:
            conteos[ingreso] += 1
        else:
            conteos[ingreso] = 1
    
    max_repeticiones = 0
    for clave in conteos:
        if conteos[clave] > max_repeticiones:
            max_repeticiones = conteos[clave]

    valores_mas_repetidos = []
    for clave in conteos:
        if conteos[clave] == max_repeticiones:
            valores_mas_repetidos = valores_mas_repetidos + [clave]
    
    return valores_mas_repetidos

#d
def media_geometrica(lista_ingresos):
    producto_total = 1
    contador = 0
    for ingreso in lista_ingresos:
        producto_total *= ingreso
        contador += 1

    if contador == 0:
        return 0
    raiz = producto_total ** (1 / contador)  
    return raiz

#e
def recorrer_lista_ambos_sentidos(lista_ingresos):
    recorrido = []
    for ingreso in lista_ingresos:
        recorrido = recorrido + [ingreso]  

    n = 0
    for _ in lista_ingresos:
        n += 1

    for i in range(n - 1, -1, -1):  
        recorrido = recorrido + [lista_ingresos[i]] 
    
    return recorrido

#2
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena",
"Mariela", "Ignacio"]

#a
edad_mayor = 0
nombre_mayor = 0

edad_menor = 0
nombre_menor = ""

contador = 0

for i in range(len(lista_edad)):

    if contador == 0:
        edad_mayor = lista_edad[i]
        nombre_mayor = lista_nombres[i]

        edad_menor = lista_edad[i]
        nombre_menor = lista_nombres[i]
        contador += 1

    if edad_mayor < lista_edad[i]:
        edad_mayor = lista_edad[i]
        nombre_mayor = lista_nombres[i]

    if edad_menor > lista_edad[i]:
        edad_menor = lista_edad[i]
        nombre_menor = lista_nombres[i]

#b
for edad in lista_edad:
    if edad > 65:
        print("Hay gente mayor de 65 años.")
        break

#c
suma_edades = 0
contador2 = 0

for edad in lista_edad:
    if edad <= 40:
        continue
    suma_edades += edad
    contador2 += 1

if contador2 > 0:
    media_etaria = suma_edades / contador2
    print(f"promedio {media_etaria:.2f}.")
else:
    print("No hay nadie mayor de 40.")

#3
nombres = []
sexos = []
horas_trabajadas = []
ingresos_semanales = []

def agregar_respondente():
    while True:
        nombre = input("Ingrese su nombre: ")
        nombres.append(nombre)
        sexo = input("Ingrese su sexo: ")
        sexos.append(sexo)
        horas = input("Ingrese sus horas trabajadas: ")
        horas_trabajadas.append(horas)
        ingreso = input("Ingrese su ingreso semanal: ")
        ingresos_semanales.append(ingreso)
        salida = input("Quiere seguir ingresando datos? s/n: ")
        if salida == "n":
            break

#5
def corregir_listas(lista, posicion, nuevo_valor):
    if 0 <= posicion < len(lista):
        lista[posicion] = nuevo_valor
    else:
        print("Posición inválida")

#6
def pedir_numeros(rango_minimo, rango_maximo):
    numeros = []
    print(f"Introduce 10 números entre {rango_minimo} y {rango_maximo}:")
    while len(numeros) < 10:
        numero = int(input(f"Numero {len(numeros) + 1}: "))
        if rango_minimo <= numero <= rango_maximo:
            numeros.append(numero)
        else:
            print(f"El numero debe estar entre {rango_minimo} y {rango_maximo}. Intentalo de nuevo.")
    return numeros

rango_minimo = 1
rango_maximo = 100

#7
nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

def encontrar_menores(nombres, edades):
    menor_edad = min(edades)   
    indices_menores = [i for i, edad in enumerate(edades) if edad == menor_edad]  
    menores = [(nombres[i], edades[i]) for i in indices_menores]
    return menores

#8
def verificar_tipos(lista):
    if not lista:
        return "La lista está vacía"    
    tipos = {type(elemento) for elemento in lista}

    if len(tipos) == 1:
        return tipos.pop()
    else:
        return tipos

#9
def agregar_valor(lista, valor):
    if not lista:
        print("La lista esta vacia. Agregando el primer valor.")
        lista.append(valor)
    elif isinstance(valor, type(lista[0])):
        lista.append(valor)
    else:
        print(f"Error: El valor '{valor}' no es del mismo tipo que los elementos de la lista.")

#11
def buscar_binario_recursivo(lista: list, buscado: any, inicio: int, final: int):    
    if inicio > final: #Si esta ordenada la lista significa que se revisaron todos
        return None
    medio = (inicio + final) // 2
    
    if lista[medio] == buscado:
        return medio
    elif lista[medio] < buscado:
        return buscar_binario_recursivo(lista, buscado, medio + 1, final) #coloco donde inicia
    else:
        return buscar_binario_recursivo(lista, buscado, inicio, medio - 1) #coloco donde termina

lista_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor_buscado = 8

inicio = 0
final = len(lista_ejemplo) - 1

resultado = buscar_binario_recursivo(lista_ejemplo, valor_buscado, inicio, final)

if resultado == None:
    print(f"Valor {valor_buscado} no encontrado")
else:
    print(f"Valor {valor_buscado} encontrado en el índice: {resultado}")