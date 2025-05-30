def es_alfabetico(cadena:str) -> bool:
    """Verifica si una cadena contiene únicamente letras y espacios.

    Args:
        cadena (str): Cadena de caracteres a validar.

    Returns:
        bool: True si la cadena es alfabética (letras y espacios)
    """
    if len(cadena) > 0:
        retorno = True
     
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])

            if (valor_ascii > 90 or valor_ascii < 65) and (valor_ascii > 
            122 or valor_ascii < 97) and valor_ascii != 32:
                retorno = False
                break
    else:
        retorno = False

    return retorno
  
def registrar_participantes(lista_participantes:list) -> bool:
    """Registra la lista de nombres de participantes

    Args:
        lista_participantes (list): La lista donde se guardan los datos

    Returns:
        bool: True si re cargaron correctamente los caracteres
    """
    if type(lista_participantes) == list and len(lista_participantes) > 0:
        retorno = True
        for i in range(len(lista_participantes)):
            nombre = input("Ingrese el nombre del participante: ")

            while not es_alfabetico(nombre):
                print("Error: El nombre es inválido. Ingrese solo letras " 
                "y espacios")
                nombre = input("Reingrese el nombre del participante: ")
            lista_participantes[i] = nombre

    else:
        retorno = False
    return retorno

def es_entero(cadena:str) -> bool:
    """ Verifica si una cadena contiene solamente números enteros

    Args:
        cadena (str): Cadena de caracteres a validar

    Returns:
        bool: True si la cadena es numérica
    """
    if len(cadena) > 0:
        retorno = True
     
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])

            if valor_ascii > 57 or valor_ascii < 48:
                retorno = False
                break
    else:
        retorno = False

    return retorno

def cargar_puntaje(matriz_puntaje:list) -> bool:
    """Carga el puntaje de los jurado del concurso

    Args:
        matriz_puntaje (list): Matriz de puntuaciones, filas participantes,
        columnas las notas de cada jurado

    Returns:
        bool: True si el usuario pudo cargar exitosamente los datos
    """
    if type(matriz_puntaje) == list and len(matriz_puntaje) > 0:
        retorno = True
        
        for fil in range(len(matriz_puntaje)):
            for col in range(len(matriz_puntaje[fil])):        
                puntuacion_valida = False

                while not puntuacion_valida:
                    puntuacion = input(f"Ingrese el puntaje obtenido del"
                                       f" jurado {col + 1} para el"
                                       f" participante {fil + 1}: ")

                    if es_entero(puntuacion):
                        numero = int(puntuacion)
                        if 1 <= numero <= 10:
                            matriz_puntaje[fil][col] = numero
                            puntuacion_valida = True  
                        else:
                            print("Error: el puntaje debe estar entre 1 y 10.")
                    else:
                        print("Error: el valor ingresado no es válido. " \
                        "Debe ser un número entre 1 y 10.")
    else:
        retorno = False
    return retorno

def buscar_coincidencias(lista_participantes: list) -> bool:
    """Buscar coincidencias entre caenas de caracteres

    Args:
        lista_participantes (list): En la lista de los participantes

    Returns:
        bool: True si el sistema halló el nombre del participante buscado
    """
    if type(lista_participantes) == list and len(lista_participantes) > 0:
        nombre_buscado = input("Ingrese el nombre del participante que desea" \
        " buscar: ")

        while not es_alfabetico(nombre_buscado):
            print("Error: El nombre es inválido. Ingrese solo letras " \
                "y espacios")
            nombre_buscado = input("Reingrese el nombre del participante: ")

        encontrado = False

        for i in range(len(lista_participantes)):
            if lista_participantes[i] == nombre_buscado:
                print(f"Se encontró al participante '{nombre_buscado}' en"
                      f" la posición {i + 1}")
                encontrado = True
                # break


        return encontrado

def pedir_entero(mensaje: str) -> int:
    """Validación del menú de opciones

    Args:
        mensaje (str): Mensaje que observará el usuario

    Returns:
        int: Retorna sí o sí un valor de número entero
    """
    entrada = input(mensaje)
    while not es_entero(entrada):
        print("ERROR. Ingrese un número entero válido.")
        entrada = input(mensaje)
    return int(entrada)









    #     for fil in range(len(matriz_puntaje)):
    #         for col in range(len(matriz_puntaje[fil])):
    #             puntuacion = input(f"Ingrese el puntaje obtenido del jurado {fil + 1} para el participante {col + 1}: ")
                
    #             while not es_entero(puntuacion):
    #                 print("ERROR, NO ES UN PUNTAJE VÁLIDO (1-10)")
    #                 puntuacion = int(input(f"Reingrese el puntaje obtenido del jurado {fil + 1} para el participante {col + 1}: "))

    #             matriz_puntaje[fil][col] = int(puntuacion)
    # else:



































# from Funciones import *

# lista_participantes = nombrar_participantes(2,"")
# matriz_puntuacion = formar_matriz(2,3,0)

# cargar_puntaje(matriz_puntuacion)
# print(matriz_puntuacion)