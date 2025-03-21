import sqlite3
import csv

# Crear conexión
conn = sqlite3.connect("BBDD.sqlite")

# Obtener cursor
cursor = conn.cursor()
header = []

# Ejecutar sentencia para creación de tabla
cursor.execute("CREATE TABLE SALARIOS_DS(id INTEGER, work_year INTEGER, experience_level VARCHAR(5), employment_type VARCHAR(5), job_title VARCHAR(50), salary INTEGER, salary_currency VARCHAR(5), salary_in_usd INTEGER, employee_residence VARCHAR(5), remote_ratio INTEGER, company_location VARCHAR(5), company_size VARCHAR(5))")

with open("/workspaces/FSI/TrabajoGrupo19/P3/EPD12_5_datascience_salaries.csv", "r") as archivo:
    contenido = csv.reader(archivo, delimiter=",")
    header = next(contenido)
    # Insertar registro
    for row in contenido:
        cursor.execute("INSERT INTO SALARIOS_DS VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                      (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
conn.commit()


# Sentencia "SELECT 1" para obtener profesionales con salario entre 100,000 y 150,000 USD
cursor.execute("SELECT id, job_title, experience_level, salary_in_usd, company_size FROM SALARIOS_DS WHERE salary_in_usd >= 100000 AND salary_in_usd <= 150000")
rows = cursor.fetchall()
print("Profesionales con salario entre 100,000 y 150,000 USD:")
head = ["ID", "JOB TITLE", "EXP LEVEL", "SALARY (USD)", "COMPANY SIZE"]
print("{:<6} {:<30} {:<10} {:<13} {:<10}\n".format(*head))
for row in rows:
    print("{:<6} {:<30} {:<10} {:<13} {:<10}".format(*row))
    

# Sentencia "SELECT 2" para obtener información sobre Data Scientists
cursor.execute("SELECT id, job_title, salary_in_usd, company_location, remote_ratio FROM SALARIOS_DS WHERE job_title = 'Data Scientist'")
rows = cursor.fetchall()
print("\nInformación sobre Data Scientists:\n")
head = ["ID", "JOB TITLE", "SALARY (USD)", "LOCATION", "REMOTE %"]
print("{:<6} {:<20} {:<13} {:<10} {:<10}\n".format(*head))
for row in rows:
    print("{:<6} {:<20} {:<13} {:<10} {:<10}".format(*row))


# Sentencia "UPDATE" para cambiar la modalidad remota de Data Scientists
cursor.execute("UPDATE SALARIOS_DS SET remote_ratio = 100 WHERE job_title = 'Data Scientist' AND remote_ratio = 0")
conn.commit()


# Sentencia "SELECT 3" para verificar la actualización
cursor.execute("SELECT id, job_title, salary_in_usd, company_location, remote_ratio FROM SALARIOS_DS WHERE job_title = 'Data Scientist'")
rows = cursor.fetchall()
print("\nActualización de la modalidad remota para Data Scientists:\n")
head = ["ID", "JOB TITLE", "SALARY (USD)", "LOCATION", "REMOTE %"]
print("{:<6} {:<20} {:<13} {:<10} {:<10}\n".format(*head))
for row in rows:
    print("{:<6} {:<20} {:<13} {:<10} {:<10}".format(*row))
    

# Sentencia "SELECT" compleja 1 para obtener salarios promedio agrupados por nivel de experiencia y año. Ordenados por año y nivel de experiencia.
cursor.execute("SELECT experience_level, work_year, AVG(salary_in_usd) AS SALARY_AVG FROM SALARIOS_DS GROUP BY experience_level, work_year ORDER BY work_year, experience_level") # 
rows = cursor.fetchall()
print("\nSalarios promedio agrupados por nivel de experiencia y año:\n")
print("EXP LEVEL | AÑO     | SALARIO PROMEDIO USD\n")
for row in rows:
    print("{:<10}| {:<8}| {:<20.2f}".format(*row))


# Sentencia "DELETE" para limpiar la tabla de salarios con valores menores a 20,000 USD
cursor.execute("DELETE FROM SALARIOS_DS WHERE salary_in_usd < 20000")
conn.commit()


# Sentencia "SELECT" compleja 2 para obtener salarios promedio por ubicación de empresa (con letra 'U') y tamaño de empresa
cursor.execute("SELECT company_location, company_size, AVG(salary_in_usd) AS SALARY_AVG FROM SALARIOS_DS WHERE company_location LIKE '%U%' GROUP BY company_location, company_size ORDER BY SALARY_AVG DESC")
rows = cursor.fetchall()
print("\nSalarios promedio por ubicación de empresa (con letra 'U') y tamaño de empresa:\n")
print("¡Datos actualizados!")
print("UBICACIÓN | TAMAÑO EMPRESA | SALARIO PROMEDIO USD\n")
for row in rows:
    print("{:<10}| {:<15}| {:<20.2f}".format(*row))

# Cerrar conexión
conn.close()
