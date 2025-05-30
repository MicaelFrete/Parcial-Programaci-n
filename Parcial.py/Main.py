#Se requiere un sistema que permita:
#Registrar los nombres de los participantes (5 en total)
#Registrar las puntuaciones que cada jurado otorga a cada participante
#Procesar y mostrar diferentes informaciones relevantes a partir de los datos
#  cargados
import os
from Funciones import *
from Inputs import *

lista_participantes = nombrar_participantes(5,"")
matriz_puntuacion = formar_matriz(5,3,0)
bandera_carga_participantes = False
bandera_carga_puntaje = False


while True:
    print(
        "1. Cargar participantes\n"
        "2. Cargar puntuaciones de jurados\n"
        "3. Mostrar puntuaciones y promedio general\n"
        "4. Mostrar participantes con promedio menor a 4\n"
        "5. Mostrar participantes con promedio menor a 8\n"
        "6. Mostrar promedio de cada jurado\n"
        "7. Jurado más estricto (menor promedio)\n"
        "8. Jurado más generoso (mayor promedio)\n"
        "9. Participantes con puntuaciones iguales\n"
        "10. Buscar participante por nombre\n"
        "0. Salir"
    )
    opcion = pedir_entero("Elija su opción: ")

    while opcion >12 or opcion < 0: 
        opcion = int(input("Reingrese su opción(0-12): "))
    
    if opcion == 1:
        if registrar_participantes(lista_participantes) == True:
            print("Los participantes han sido cargados correctamente")
            mostrar_lista(lista_participantes)
            bandera_carga_participantes = True
        else:
            print("Has tenido un error al cargar los participantes")
        pass
    elif opcion == 2: 
        if cargar_puntaje(matriz_puntuacion) == True:
            print("Puntajes guardados correctamente")
            bandera_carga_puntaje = True
            mostrar_participante(lista_participantes, matriz_puntuacion) 
        else:
            print("Puntajes mal cargados.")
        pass

    elif opcion == 3:
        if (bandera_carga_participantes == True and 
            bandera_carga_puntaje == True):

            for i in range(len(lista_participantes)):
                mostrar_puntajes(lista_participantes, matriz_puntuacion, i)       
        else:
            print("Primero deben cargarse los participantes y sus puntajes " \
            "antes de mostrar los mismos")    
        pass

    elif opcion == 4:
        if (bandera_carga_participantes == True and 
            bandera_carga_puntaje == True):
            if not (mostrar_alumnos_no_superan_la_nota_promedio
             (lista_participantes,matriz_puntuacion,4)):
                print("No hay ningún promedio por debajo de 4")
            
        else:
            print("Primero deben cargarse los participantes y sus puntajes")
        pass
    
    elif opcion == 5:
        if (bandera_carga_participantes == True and 
            bandera_carga_puntaje == True):
            if not mostrar_alumnos_no_superan_la_nota_promedio(
                lista_participantes,matriz_puntuacion,8):
                print("No hay ningún promedio menor a 8")
        else:
            print("Primero deben cargarse los participantes y sus puntajes")
        pass
    
    elif opcion == 6:
        if (bandera_carga_participantes == True and 
            bandera_carga_puntaje == True):
            mostrar_promedios_jurados(matriz_puntuacion)
        else:
            print("Primero deben cargarse los participantes y sus puntajes")
        pass
    
    elif opcion == 7: 
        if (bandera_carga_participantes == True and 
            bandera_carga_puntaje == True):
            indice = jurado_mas_estricto(matriz_puntuacion)
            for i in range(len(indice)):
                promedio = calcular_promedio_jurados(matriz_puntuacion, indice[i])
                print(f"El jurado más estricto fue el jurado {indice[i] + 1}"
                      f" con un promedio de {round(promedio, 2)}")
        else:
            print("Primero deben cargarse los participantes y sus puntajes")
        pass

    elif opcion == 8:
        if (bandera_carga_participantes == True and 
            bandera_carga_puntaje == True):
            indice = jurado_mas_generoso(matriz_puntuacion)
            for i in range(len(indice)):
                promedio = calcular_promedio_jurados(matriz_puntuacion, 
                                                     indice[i])
                print(f"El jurado más estricto fue el jurado {indice[i] + 1} "
              f"con un promedio de {round(promedio, 2)}")
        else:
            print("Primero deben cargarse los participantes y sus puntajes")
        pass

    elif opcion == 9:
        if (bandera_carga_participantes == True and 
            bandera_carga_puntaje == True):
            if not mostrar_puntuacion_igual(lista_participantes, 
                                        matriz_puntuacion):
                print("No hay participantes con la misma cantidad total " \
                "de puntos.")        
        else:
            print("Primero deben cargarse los participantes y sus puntajes")
        pass

    elif opcion == 10:
        if (bandera_carga_participantes == True and 
            bandera_carga_puntaje == True):
            if not buscar_coincidencias(lista_participantes):
                print("No se encontró ningún participante con ese nombre.")
        else:
            print("Primero deben cargarse los participantes y sus puntajes")
        pass

    elif opcion == 11:
        pass

    elif opcion == 12:
        if (bandera_carga_participantes == True and 
            bandera_carga_puntaje == True):
            if ordenar_participantes_alfabeticamente(lista_participantes, 
                                                 matriz_puntuacion):
                print("Participantes ordenados correctamente.")
            else:
                print("Los participantes ya estaban ordenados.")
        
            for i in range(len(lista_participantes)):
                mostrar_puntajes(lista_participantes, matriz_puntuacion, i) 
        else:
            print("Primero deben cargarse los participantes y sus puntajes")
        
        pass

    elif opcion == 0:
        print("Saliendo...")

    input("Toque cualquier botón para continuar...")
    os.system("clear")


#resolver punto 11
#Revisar en chat gpt lo que tenemos
#Resolver las validaciones
#Resolver que si no hay datos cargados, no se pueden solucionar los demás opciones
#Resolver las 79 líneas