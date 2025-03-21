import pandas as pd
from functools import reduce

# Cargar el dataset
df = pd.read_csv('/workspaces/FSI/TrabajoGrupo19/P4/EPD12_5_datascience_salaries.csv')

# Crear el diccionario directamente
diccionario = {
    0: (0, 2020, "MI", "FT", "Data Scientist", 70000, "EUR", 79833, "DE", 0, "DE", "L"),
    1: (1, 2020, "SE", "FT", "Machine Learning Scientist", 260000, "USD", 260000, "JP", 0, "JP", "S"),
    2: (2, 2020, "SE", "FT", "Big Data Engineer", 85000, "GBP", 109024, "GB", 50, "GB", "M"),
    3: (3, 2020, "MI", "FT", "Product Data Analyst", 20000, "USD", 20000, "HN", 0, "HN", "S"),
    4: (4, 2020, "SE", "FT", "Machine Learning Engineer", 150000, "USD", 150000, "US", 50, "US", "L"),
    5: (5, 2020, "EN", "FT", "Data Analyst", 72000, "USD", 72000, "US", 100, "US", "L"),
    6: (6, 2020, "SE", "FT", "Lead Data Scientist", 190000, "USD", 190000, "US", 100, "US", "S"),
    7: (7, 2020, "MI", "FT", "Data Scientist", 11000000, "HUF", 35735, "HU", 50, "HU", "L"),
    8: (8, 2020, "MI", "FT", "Business Data Analyst", 135000, "USD", 135000, "US", 100, "US", "L"),
    9: (9, 2020, "SE", "FT", "Lead Data Engineer", 125000, "USD", 125000, "NZ", 50, "NZ", "S"),
    10: (10, 2020, "EN", "FT", "Data Scientist", 45000, "EUR", 51321, "FR", 0, "FR", "S"),
    11: (11, 2020, "MI", "FT", "Data Scientist", 3000000, "INR", 40481, "IN", 0, "IN", "L"),
    12: (12, 2020, "EN", "FT", "Data Scientist", 35000, "EUR", 39916, "FR", 0, "FR", "M"),
    13: (13, 2020, "MI", "FT", "Lead Data Analyst", 87000, "USD", 87000, "US", 100, "US", "L"),
    14: (14, 2020, "MI", "FT", "Data Analyst", 85000, "USD", 85000, "US", 100, "US", "L"),
    15: (15, 2020, "MI", "FT", "Data Analyst", 8000, "USD", 8000, "PK", 50, "PK", "L"),
    16: (16, 2020, "EN", "FT", "Data Engineer", 4450000, "JPY", 41689, "JP", 100, "JP", "S"),
    17: (17, 2020, "SE", "FT", "Big Data Engineer", 100000, "EUR", 114047, "PL", 100, "GB", "S"),
    18: (18, 2020, "EN", "FT", "Data Science Consultant", 423000, "INR", 5707, "IN", 50, "IN", "M"),
    19: (19, 2020, "MI", "FT", "Lead Data Engineer", 56000, "USD", 56000, "PT", 100, "US", "M"),
    20: (20, 2020, "MI", "FT", "Machine Learning Engineer", 299000, "CNY", 43331, "CN", 0, "CN", "M")
}

def generar_salary_by_job(diccionario):
    def reducer(acc, item): # acc es el acumulador
        job_title = item[1][4] # item[1] es el valor del diccionario (una tupla) y item[1][4] es el título del trabajo
        salary_in_usd = item[1][7] # item[1][7] es el salario en USD
        if job_title in acc: # Si el trabajo ya está en el diccionario, se actualiza el contador y el salario total
            count, total_salary = acc[job_title] # count es el número de trabajos y total_salary es el salario total
            acc[job_title] = (count + 1, total_salary + salary_in_usd) # Se actualiza el diccionario
        else:
            acc[job_title] = (1, salary_in_usd) # Si el trabajo no está en el diccionario, se añade
        return acc

    return reduce(reducer, diccionario.items(), {}) # Se aplica la función reduce() al diccionario y se devuelve el resultado

# Generar el diccionario salary_by_job
salary_by_job = generar_salary_by_job(diccionario)

# Calcular el salario promedio por trabajo y almacenarlo en un nuevo diccionario (diccionario por comprensión)
avg_salary_by_job = {job: (job, total_salary / count) for job, (count, total_salary) in salary_by_job.items()}

# Aplicar la función lambda a la colección avg_salary_by_job y mostrar los resultados
# Como resultado, tenemos un objeto iterable, porque map() devuelve un iterable.
print("Resultado de aplicar función map():")
list(map(lambda item: print(f"{item[0]}: {item[1][1]:.2f} USD"), avg_salary_by_job.items()))


# Calcular el promedio de salario global
def promedio_salario(avg_salary_by_job):
    total_salarios = reduce(lambda a, b: a + b[1][1], avg_salary_by_job.items(), 0) # Se suman los salarios de todos los trabajos
    promedio = total_salarios / len(avg_salary_by_job) # Se calcula el promedio
    print("\nResultado de aplicar función reduce():")
    print(f"Promedio de salario global: {promedio:.2f} USD")
    return promedio


promedio = promedio_salario(avg_salary_by_job)

# Usamos la función filter() para obtener los trabajos con un salario superior al promedio
trabajos_superiores_al_promedio = dict(filter(lambda item: item[1][1] > promedio, avg_salary_by_job.items()))

# Imprime los trabajos con un salario superior al promedio
print("\nResultado de aplicar función filter():")
print("Trabajos con salario superior al promedio global\n")
print("Cargo                         Salario Promedio (USD)")
for trabajo in trabajos_superiores_al_promedio.values():
    print(f"{trabajo[0]:<30} {trabajo[1]:.2f}")