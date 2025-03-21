from P2 import Almacen, Funciones

def main():
    almacen = Almacen()
    funcion = Funciones()
    almacen.fromCSV("/workspaces/FSI/TrabajoGrupo19/P1/EPD12_5_datascience_salaries.csv")
    # Menu que muestra las opciones y evalúa la opción seleccionada
    menu = True
    while menu:
        print(" **** Menu del programa **** ", end="\n\n")
        print("1. Alta registro de salario")
        print("2. Baja registro de salario")
        print("3. Lista de registros")
        print("4. Filtrado por campo")
        print("5. Guardar y salir")
        opt = input("Seleccione una opción (1-5): ")
        print("\n")

        match opt:
            case "1":
                print("*----- Alta Registro -----*", end="\n\n") 
                # Agregamos el nuevo registro al final de la lista, tomando el campo ID como campo autoincremental
                # El ID lo calculamos por el tamaño de la lista 'registros' + 1
                id, registro = funcion.validar_datos_registro(len(almacen.registros) + 1)
                almacen.alta_registro(id, registro)
            case "2":
                print("*----- Baja Registro -----*", end="\n\n")
                id = int(input("Introduzca el [id] del registro: "))
                almacen.baja_registro(id)
            case "3":
                print("*----- Lista de Registros -----*", end="\n\n")
                almacen.listado_registros()
            case "4":
                print("*----- Filtrado por Campo -----*", end="\n\n")
                almacen.agrupar_por_campo()
            case "5":
                print("*-----Guardar y salir-----*")
                almacen.toCSV("TrabajoGrupo19/P2/EPD12_5_datascience_salaries_updated.csv")
                menu = False
                print("Guardando datos ...\n" + "Adios!")
            case _:
                print("Opción no valida!", end="\n\n")
        if menu is True:
            input("Presione [Enter] para volver al menu principal  ")

if __name__ == "__main__":
    main()
