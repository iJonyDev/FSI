import csv


# Clase que implementa las propiedades y métodos necesarios gestionar los objetos de datos de ciencia
class Registro:
    def __init__(self, id, work_year, experience_level, employment_type, job_title, salary, salary_currency, 
                 salary_in_usd, employee_residence, remote_ratio, company_location, company_size):
        self.id = id
        self.work_year = work_year
        self.experience_level = experience_level
        self.employment_type = employment_type
        self.job_title = job_title
        self.salary = salary
        self.salary_currency = salary_currency
        self.salary_in_usd = salary_in_usd
        self.employee_residence = employee_residence
        self.remote_ratio = remote_ratio
        self.company_location = company_location
        self.company_size = company_size

    def __str__(self):
        return f"{self.id},{self.work_year},{self.experience_level},{self.employment_type},{self.job_title},{self.salary},{self.salary_currency},{self.salary_in_usd},{self.employee_residence},{self.remote_ratio},{self.company_location},{self.company_size}"


# Funciones auxiliares para abstraer a las clases que las invocan de buena parte de la logica.
class Almacen:
    def __init__(self):
        self.registros = []
        self.encabezado = []
    
    def fromCSV(self, ruta_archivo):
        import csv
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = csv.reader(archivo, delimiter=",")
            self.encabezado = next(contenido)
            
            for i, linea in enumerate(contenido, 1):
                # Asumimos que los datos vienen en el mismo orden que la clase Registro
                registro = Registro(str(i), *linea[1:])
                self.registros.append(registro)
    
    def toCSV(self, ruta_archivo):
        import csv
        with open(ruta_archivo, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo, delimiter=",")
            escritor.writerow(self.encabezado)
            for registro in self.registros:
                escritor.writerow(str(registro).split(","))
    
    def alta_registro(self, id, registro):
        self.registros.append(registro)
        print(f"Registro con ID {id} añadido correctamente.")
    
    def baja_registro(self, id):
        for i, registro in enumerate(self.registros):
            if registro.id == str(id):
                del self.registros[i]
                print(f"Registro con ID {id} eliminado correctamente.")
                return
        print(f"No se encontró ningún registro con ID {id}.")
    
    def listado_registros(self):
        print(",".join(self.encabezado))
        for registro in self.registros:
            print(registro)
    
    def agrupar_por_campo(self):
        campo = input("Introduzca el campo por el que desea agrupar (ej. work_year, job_title, experience_level): ")
        if campo not in self.encabezado:
            print(f"El campo {campo} no existe.")
            return
        
        campo_agregado = input("Introduzca el campo que desea agregar (ej. salary_in_usd): ")
        if campo_agregado not in self.encabezado:
            print(f"El campo {campo_agregado} no existe.")
            return
        
        funcion_agregacion = input("Introduzca la función de agregación (sum, avg, max, min): ").lower()
        if funcion_agregacion not in ["sum", "avg", "max", "min"]:
            print(f"La función de agregación {funcion_agregacion} no es válida.")
            return
        
        indice_campo = self.encabezado.index(campo)
        indice_campo_agregado = self.encabezado.index(campo_agregado)
        valores = {}
        
        for registro in self.registros:
            valor = str(registro).split(",")[indice_campo]
            valor_agregado = float(str(registro).split(",")[indice_campo_agregado])
            if valor not in valores:
                valores[valor] = []
            valores[valor].append(valor_agregado)
        
        resultado = {}
        for valor, lista_valores in valores.items():
            if funcion_agregacion == "sum":
                resultado[valor] = sum(lista_valores)
            elif funcion_agregacion == "avg":
                resultado[valor] = sum(lista_valores) / len(lista_valores)
            elif funcion_agregacion == "max":
                resultado[valor] = max(lista_valores)
            elif funcion_agregacion == "min":
                resultado[valor] = min(lista_valores)
        
        print(f"\n--- Agrupación por {campo} y agregación de {campo_agregado} ({funcion_agregacion}) ---")
        for valor, resultado_agregado in resultado.items():
            print(f"{valor}: {resultado_agregado}")


class Funciones:
    def validar_datos_registro(self, id):
        work_year = input("Introduzca año de trabajo: ")
        experience_level = input("Introduzca nivel de experiencia: ")
        employment_type = input("Introduzca tipo de empleo: ")
        job_title = input("Introduzca título del trabajo: ")
        salary = input("Introduzca salario: ")
        salary_currency = input("Introduzca moneda del salario: ")
        salary_in_usd = input("Introduzca salario en USD: ")
        employee_residence = input("Introduzca residencia del empleado: ")
        remote_ratio = input("Introduzca ratio de trabajo remoto: ")
        company_location = input("Introduzca ubicación de la empresa: ")
        company_size = input("Introduzca tamaño de la empresa: ")
        
        registro = Registro(str(id), work_year, experience_level, employment_type, job_title, 
                         salary, salary_currency, salary_in_usd, employee_residence, 
                         remote_ratio, company_location, company_size)
        
        return id, registro
