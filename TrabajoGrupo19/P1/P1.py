# Usamos import csv para leer el dataset.
import csv

diccionario1 = dict()
encabezado = ()


def data_extractor():
    global encabezado # Usar la variable global

    with open("/workspaces/FSI/TrabajoGrupo19/P1/EPD12_5_datascience_salaries.csv","r",encoding="utf-8",) as archivo:
        contenido = csv.reader(archivo, delimiter=",")
        # Asignamos la primera línea a la tupla "encabezado"
        encabezado = next(contenido)

        # Empezamos a leer el contenido desde la segunda línea
        # Bucle para construir el diccionario tomando como clave el primer campo de cada línea.
        for linea in contenido:
            valor = tuple(linea)
            clave = valor[0]
            diccionario1[clave] = valor


def nuevo_registro():
    # Nuevo registro generado a partir de los campos de la tupla encabezado.
    # Tupla que hace referencia a los índices del encabezado del dataset.
    print("Introduzca nuevo registro:")

    # "nuevo_registro" contendrá el mismo número de elementos que "encabezado"
    nuevo_registro = []
    i = 0
    #   Bucle añade los campos necesarios para el nuevo registro.
    while len(nuevo_registro) < len(encabezado):
        nuevo_elemento = str(input("Introduzca " + encabezado[i] + ": "))
        nuevo_registro.append(nuevo_elemento)
        i = i + 1

    # La nueva_tupla será el valor del nuevo item del diccionario.
    nueva_tupla = tuple(nuevo_registro)

    # Evaluar si el nuevo no registro existe, caso contrario no se agregara el nuevo registro al diccionario.
    if nueva_tupla[0] not in diccionario1:
        diccionario1[(nueva_tupla[0])] = nueva_tupla
        print("\nEl registro :" + str(diccionario1.get(nueva_tupla[0])) + "\n Ha sido agregado correctamente!\n")
    else:
        print("El registro con ID [" + nueva_tupla[0] + "] ya existe. Intente con otro valor de registro.")


def tabla_diccionario():
    # Mostrar un formato de tabla con los tamaños de los campos fijos de la cabecera
    print("{:<6} {:<10} {:<18} {:<16} {:<26} {:<12} {:<16} {:<14} {:<20} {:<14} {:<18} {:<14}".format(*encabezado))
    # Mostrar un formato de tabla con los tamaños de los campos fijos del resto de filas
    for v in diccionario1.values():
        print("{:<6} {:<10} {:<18} {:<16} {:<26} {:<12} {:<16} {:<14} {:<20} {:<14} {:<18} {:<14}".format(*v))


def borrar_registro():
    # Mostramos los 10 primeros
    for i in range(1, 10):
        print(diccionario1.get(str(i)))

    # Verificar que el registro existe y pedir confirmación antes de eliminarlo
    reg = str(input("Introduce el ID del registro: "))
    while reg not in diccionario1.keys():
        print("ID no existe!")
        reg = str(input("Introduce el ID del registro: "))
    print("¿Desea eliminar el registro: " + reg + " ?")
    confirmar = str.upper(input("[S] para confirmar: "))

    # Si el registro existe en el diccionario y se confirma la acción
    if reg in diccionario1.keys() and confirmar == "S":
        diccionario1.pop(reg)
        print("Registro" + "[" + reg + "]" + "eliminado correctamente!\n")
    else:
        print("¡Operación cancelada!")
        print(("Registro" + "[" + reg + "]" + "no eliminado!\n"))

    # Mostramos los 10 primeros y verificamos que se ha eliminado
    for i in range(1, 10):
        print(diccionario1.get(str(i)))


def busca_clave_mostrar_valor():

    # Verificar que el registro existe, caso contrario pedir nuevamente el ID

    reg = str(input("Introduce el ID del registro: "))
    while reg not in diccionario1.keys():
        print("ID no existe!")
        reg = str(input("Introduce el ID del registro: "))
    # Mostrar datos de la tupla correspondiente al registro
    if reg in diccionario1.keys():
        d = diccionario1.get(reg) # Tomamos el valor del registro para mostrarlo en el mismo formato que el encabazado
        print("{:<6} {:<10} {:<18} {:<16} {:<26} {:<12} {:<16} {:<14} {:<20} {:<14} {:<18} {:<14}".format(*encabezado))
        print("{:<6} {:<10} {:<18} {:<16} {:<26} {:<12} {:<16} {:<14} {:<20} {:<14} {:<18} {:<14}".format(*d))
    return reg  # Retornamos 'reg' para usarlo en como entrada en otra funcion


def buscar_editar_mostrar():
    global diccionario1  # Usar el diccionario global
    reg = (busca_clave_mostrar_valor())  # Llamada a la función que busca y muestra un registro si este existe.
    print("Desea editar el registro?")
    editar = str.upper(input("[S] para confirmar: "))
    if editar != "S":  # Si no se confirma la operación se cancela y el registro no se edita.
        print("¡Operación cancelada!")
        return

    # Añadimos el nuevo registro:
    nuevo_registro = [reg]  # Tomamos 'reg' porque es el id del nuevo registro y lo almacenamos en la lista.
    i = 1
    #   Bucle añade los campos necesarios para el nuevo registro.
    while len(nuevo_registro) < len(encabezado):
        nuevo_elemento = str(input("Introduzca " + encabezado[i] + ": "))
        nuevo_registro.append(nuevo_elemento)
        i = i + 1

    # Nueva_tupla será el valor que remplazara al valor actual del registro.
    nueva_tupla = tuple(nuevo_registro)
    diccionario1[reg] = nueva_tupla
    d = diccionario1.get(reg) # Tomamos el valor del nuevo registro para mostrarlo en el mismo formato que el encabezado
    print("\nEl registro " + str(nuevo_registro[0] + " ha sido modificado:\n"))
    print("{:<6} {:<10} {:<18} {:<16} {:<26} {:<12} {:<16} {:<14} {:<20} {:<14} {:<18} {:<14}".format(*encabezado))
    print("{:<6} {:<10} {:<18} {:<16} {:<26} {:<12} {:<16} {:<14} {:<20} {:<14} {:<18} {:<14}".format(*d))


def mostrar_opciones():
    print(" **** Menu del programa **** ", end="\n\n")
    print("1. Agregar un nuevo registro")
    print("2. Buscar un registro por su clave y mostrar sus valores")
    print("3. Buscar un registro por su clave, editarlo y mostrar sus valores")
    print("4. Borrar un registro a partir de su clave")
    print("5. Listar todos los registros en formato de tabla")
    print("6. Salir")


def menu_principal():
    # Menu que muestra las opciones y evalúa la opción seleccionada
    s = True
    while s:
        mostrar_opciones()
        opt = input("Seleccione una opción (1-6): ")
        print("\n")

        match opt:
            case "1":
                print("Agregar un nuevo registro", end="\n\n")
                nuevo_registro()
            case "2":
                print("Buscar un registro por su clave y mostrar sus valores", end="\n\n")
                busca_clave_mostrar_valor()
            case "3":
                print("Buscar un registro por su clave, mostrar sus valores y editarlos", end="\n\n")
                buscar_editar_mostrar()
            case "4":
                print("Borrar un registro a partir de su clave", end="\n\n")
                borrar_registro()
            case "5":
                print("Listar todos los registros en formato de tabla", end="\n\n")
                tabla_diccionario()
            case "6":
                s = False
                print("Adios")
            case _:
                print("Opción no valida!", end="\n\n")
        if s is True:
            input("Presione [Enter] para volver al menu principal  ")
