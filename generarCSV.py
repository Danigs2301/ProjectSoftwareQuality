import requests
import csv

# Paso 1: URL del API con la clave de tu proyecto
project_key = "Danigs2301_zephyr"  # Cambia por tu clave de proyecto
url = f"https://sonarcloud.io/api/issues/search?componentKeys={project_key}&types=CODE_SMELL&ps=500&additionalFields=ruleDescriptionContextKey"

# Paso 2: Realizar la solicitud a la API
response = requests.get(url)
data = response.json()
#print(data)

# Paso 3: Extraer los issues
issues = data.get('issues', [])

# Paso 4: Crear el archivo CSV
with open('sonarcloud_code_smells.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir los encabezados del CSV
    writer.writerow(['Key', 'rule', 'Message'])

    # Escribir las filas con los detalles de cada issue
    for issue in issues:
        writer.writerow([
            issue['key'],  # ID del issue
            issue['rule'],
            issue['message']  # Descripción del problema
        ])

print("Informe exportado correctamente a 'sonarcloud_code_smells.csv'")
