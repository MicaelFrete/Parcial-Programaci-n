def nombrar_participantes(cantidad_elementos:int,valor_elementos:any) -> list:
    """Enlistar a los participantes del concurso

    Args:
        cantidad_elementos (int): cantidad de participantes
        valor_elementos (any): nombre de los participantes

    Returns:
        list: Array de nombres de participantes
    """
    array = [valor_elementos] * cantidad_elementos

    return array

def formar_matriz(cantidad_filas:list,cantidad_columnas:list, 
                  valor_elementos:any) -> list:
    """Formar matriz de puntajes del concurso

    Args:
        cantidad_filas (list): Notas de participantes
        cantidad_columnas (list): Notas de Jurados
        valor_elementos (any): Notas propiamente dichas

    Returns:
        list: Matriz de 5x3 
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_elementos] * cantidad_columnas
        matriz += [fila]

    return matriz

def mostrar_lista(array:list) -> None:
    """Mostrar matriz 

    Args:
        array (list): Matriz de notas que se mostrará
    """
    for i in range(len(array)):
        print(f"Participante {i + 1}: {array[i]}")

def mostrar_participante(array_participantes: list, 
                         matriz_puntaje: list) -> None:
    for i in range(len(array_participantes)):
        print(f"--- PARTICIPANTE {i + 1} ---")
        print(f"Nombre: {array_participantes[i]}")
        print(f"Nota Jurado 1: {matriz_puntaje[i][0]}")
        print(f"Nota Jurado 2: {matriz_puntaje[i][1]}")
        print(f"Nota Jurado 3: {matriz_puntaje[i][2]}")
        print("")

def sumar_puntaje(matriz_numerica:list,indice_fila:int) -> int | float:
    """Acumulador de notas de participantes

    Args:
        matriz_numerica (list): Matriz de notas
        indice_fila (int): Cada uno de los puntajes del participante

    Returns:
        int | float: Suma de las notas de participantes
    """
    suma_fila = 0
    
    for col in range(len(matriz_numerica[indice_fila])):
        if (type(matriz_numerica[indice_fila][col]) == int or 
    type(matriz_numerica[indice_fila][col]) == float):
            suma_fila += matriz_numerica[indice_fila][col]
    
    return suma_fila

def calcular_promedio(matriz_puntuacion:list, indice:int) -> float | None:
    """Calcula el promedio

    Args:
        matriz_puntuacion (list): Matriz de nota que utiliza
        indice (int): Índices con los que hará el cálculo 

    Returns:
        float | None: Si las notas son mayores a 0 retornará el promedio.
          De lo contrario nada
    """
    suma_fila = sumar_puntaje(matriz_puntuacion,indice)
    contador_fila = len(matriz_puntuacion[indice])

    if contador_fila != 0:
        promedio = suma_fila / contador_fila
        return promedio
    else:
        return None

def mostrar_puntajes(lista_participantes:list,matriz_puntaje:list,
                     indice:int) -> bool:
    """Muestra los nombres, los puntajes de los participantes y su promedio

    Args:
        lista_participantes (list): Lista de nombres de participantes
        matriz_puntaje (list): Matriz de notas del concurso
        indice (int): Índice de cada uno de los participantes 

    Returns:
        bool: True cuando haya matriz, nombres y promedios bien cargados
    """
    if (type(matriz_puntaje) == list and type(lista_participantes) == list and 
    len(matriz_puntaje) > 0 and len(lista_participantes) > 0 and 
    (indice < len(lista_participantes) and indice >= 0)):

        retorno = True
        print(f"NOMBRE DEL PARTICIPANTE: {lista_participantes[indice]}")
        print(f"PUNTAJE JURADO 1: {matriz_puntaje[indice][0]}")
        print(f"PUNTAJE JURADO 2: {matriz_puntaje[indice][1]}")
        print(f"PUNTAJE JURADO 3: {matriz_puntaje[indice][2]}")
        print(f"PUNTAJE PROMEDIO: {calcular_promedio(matriz_puntaje,indice)}")
        print("")
    else:
        retorno = False
        
    return retorno

def mostrar_alumnos_no_superan_la_nota_promedio(lista_participante:list,
                                                matriz_puntuacion:list,
                                                promedio:float) -> bool:
    """Muestra los alumnos que no superaron determinada nota que le pases

    Args:
        lista_participante (list): Nómina de participantes
        matriz_puntuacion (list): Matriz de puntuación
        promedio (float): Muestra el promedio que no supera det. nivel
    Returns:
        bool: True si se mostró algún alumno, False si ninguno cumple
    """
    encontrado = False

    for i in range(len(lista_participante)):
        nota_promedio = calcular_promedio(matriz_puntuacion,i)
        if nota_promedio < promedio:
            mostrar_puntajes(lista_participante,matriz_puntuacion,i)
            encontrado = True
    return encontrado

def mostrar_promedios_jurados(matriz_puntuacion: list) -> None:
    for i in range(len(matriz_puntuacion[0])):
        promedio = calcular_promedio_jurados(matriz_puntuacion, i)
        print(f"Promedio del jurado {i + 1}: {round(promedio, 2)}")


def sumar_columna(matriz_puntuacion:list,indice_col:int) -> int:
    """Acumula los puntajes de los jurados guardados en columna

    Args:
        matriz_puntuacion (list): Matriz de puntajes
        indice_col (int): Columnas desde donde se toman las notas a sumar

    Returns:
        int: Acumulación y suma de notas de las columnas
    """
    acumulador = 0
    for fil in range(len(matriz_puntuacion)):
        if type(matriz_puntuacion[fil][indice_col]) == int or type(matriz_puntuacion[fil][indice_col]) == float:
                acumulador += matriz_puntuacion[fil][indice_col]
        
    return acumulador

def calcular_promedio_jurados(matriz_puntuacion:list, indice_col:
                              int) -> float | None:
    """Calcula el promedio de las notas de cada jurado

    Args:
        matriz_puntuacion (list): Matriz de puntajes 
        indice_col (int): Índice de la columna del jurado que sepromediará.

    Returns:
        float | None: Promedio de puntajes del jurado si la matriz tiene filas
    """
   
    suma_columna = sumar_columna(matriz_puntuacion,indice_col)
    contador_columna = len(matriz_puntuacion)

    if contador_columna != 0:
        promedio = suma_columna / contador_columna
        return promedio
    else:
        return None

def jurado_mas_estricto(matriz_puntuacion: list) -> list:
    """Calcular cuál es el jurado más estricto

    Args:
        matriz_puntuacion (list): La matriz habrá que recorrer
        para saber qué jurado tiene el promedio más bajo 

    Returns:
        list: Índices de los jurados más exigentes
    """
    jurados_estrictos = [0] * 3
    contador = 1
    primer_promedio_estricto = calcular_promedio_jurados(matriz_puntuacion, 0)
    
    for i in range(1, len(matriz_puntuacion[0])):
        promedio_actual = calcular_promedio_jurados(matriz_puntuacion, i)

        if promedio_actual < primer_promedio_estricto:
            primer_promedio_estricto = promedio_actual
            jurados_estrictos[0] = i
            contador = 1
        elif promedio_actual == primer_promedio_estricto:
            jurados_estrictos[contador] = i
            contador += 1
    resultado = [0] * contador
    for j in range(contador):
        resultado[j] = jurados_estrictos[j]

    return resultado

def jurado_mas_generoso(matriz_puntuacion: list) -> list:
    """Calcula el jurado menos exigente y más generoso con su puntaje

    Args:
        matriz_puntuacion (list): Recorre la matriz para saber cuál es el 
        jurado más generoso con sus notas

    Returns:
        list: Índices de los jurados que es más generosoa
    """
    jurados_generosos = [0] * 3
    contador = 1
    primer_promedio_generoso = calcular_promedio_jurados(matriz_puntuacion, 0)

    for i in range(1, len(matriz_puntuacion[0])):
        promedio_actual = calcular_promedio_jurados(matriz_puntuacion, i)

        if promedio_actual > primer_promedio_generoso:
            primer_promedio_generoso = promedio_actual
            jurados_generosos[0] = i
            contador = 1
        elif promedio_actual == primer_promedio_generoso:
            jurados_generosos[contador] = i
            contador += 1
    resultado = [0] * contador
    for j in range(contador):
        resultado[j] = jurados_generosos[j]

    return resultado

def mostrar_puntuacion_igual(lista_participantes: list, 
                             matriz_puntuacion: list) -> bool:
    """Muestra la puntuación igual entre los participantes

    Args:
        lista_participantes (list): Lista de participantes que hay que recorrer
        matriz_puntuacion (list): La matriz de puntajes de los participantes

    Returns:
        bool: True si se halla una puntuación igual a otra
    """
    bandera_hay_puntuacion_igual = False

    for fil_i in range(len(lista_participantes)):
        suma_fil_i = sumar_puntaje(matriz_puntuacion,fil_i)

        for fil_j in range(fil_i + 1,len(lista_participantes)):
            suma_fil_j = sumar_puntaje(matriz_puntuacion,fil_j)
            if suma_fil_i == suma_fil_j:
                print(f"Los participantes '{lista_participantes[fil_i]}' y "
                      f" '{lista_participantes[fil_j]}' tienen la misma "
                      f" cantidad de puntos: {suma_fil_j}")
                bandera_hay_puntuacion_igual = True

    return bandera_hay_puntuacion_igual

def buscar_participante(nombre: str, lista_participantes: list, 
                        matriz_puntuacion: list) -> bool:
    """Busca participantes y los encuentra

    Args:
        nombre (str): _description_
        lista_participantes (list): Lista con los participantes
        matriz_puntuacion (list): Matriz de notas, filas participantes, 
        columnas, los jurados

    Returns:
        bool: True si se encuentra al participante buscado
    """
    encontrado = False

    for i in range(len(lista_participantes)):
        if lista_participantes[i] == nombre:
            mostrar_puntajes(lista_participantes, matriz_puntuacion, i)
            encontrado = True
            break

    return encontrado

def ordenar_participantes_alfabeticamente(lista_participantes: list, 
                                          matriz_puntuacion: list) -> bool:
    """Ordenar alfabéticamente a los participantes

    Args:
        lista_participantes (list): A partir de su lista de nombres
        matriz_puntuacion (list): Según su matriz de puntajes que se deberá 
        también ordenar

    Returns:
        bool: True si se ordenan los nombres y los puntajes
    """
    bandera_ordenados = False
    numero_participantes = len(lista_participantes)

    for i in range(numero_participantes - 1):
        for j in range(numero_participantes - 1 - i): 
            if lista_participantes[j] > lista_participantes[j + 1]:
                intercambiar_indices(lista_participantes, j, j + 1)
                intercambiar_indices(matriz_puntuacion, j, j + 1)
                bandera_ordenados = True

    return bandera_ordenados

def intercambiar_indices(array: list, i: int, j: int) -> None:
    """Intercambia índices necesarios del array para ordenar alfabéticamente 

     Args:
        array (list): Lista sobre la cual se realizará el intercambio.
        i (int): Índice del primer elemento.
        j (int): Índice del segundo elemento.
    """
    aux = array[i]
    array[i] = array[j]
    array[j] = aux




########
def mostrar_jurado_estricto(matriz: list) -> None:
    indice = jurado_mas_estricto(matriz)
    promedio = calcular_promedio_jurados(matriz, indice)
    print(f"El jurado más estricto fue el jurado {indice + 1} con un promedio de {round(promedio, 2)}")


# def mostrar_top_3(lista_participantes: list, matriz_puntuacion: list) -> None:
#     numero_participantes = len(lista_participantes)
#     promedios = [0] * numero_participantes
    
#     for i in range(numero_participantes):
#         promedios[i] = calcular_promedio(matriz_puntuacion, i)
    
    
#     for i in range(3):
#         for j in range(i + 1, numero_participantes):
#             if promedios[j] > promedios[i]:
#                 aux = promedios[i]
#                 promedios[i] = promedios[j]
#                 promedios[j] = aux
#                 aux_p = lista_participantes[i]
#                 lista_participantes[i] = lista_participantes[j]
#                 lista_participantes[j] = aux_p

#     print("🔝 Top 3 participantes con mayor promedio:\n")
#     for i in range(min(3, numero_participantes)):
#         mostrar_puntajes(lista_participantes, matriz_puntuacion, i)
#         print("-" * 30)

# from Inputs import *


# lista_participantes = nombrar_participantes(2,"")
# matriz_puntuacion = formar_matriz(2,3,0)

# cargar_puntaje(matriz_puntuacion)
# print(matriz_puntuacion)