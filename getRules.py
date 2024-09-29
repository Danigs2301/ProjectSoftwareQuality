import requests
import csv

organization = "danigs2301"  # Reemplaza con el identificador de tu organización
url = "https://sonarcloud.io/api/rules/search"
params = {
    "organization": organization,
    "types": "CODE_SMELL",  # Tamaño de página
    "ps" : 500,
    "p": 1      # Número de página
}

all_rules = []
while True:
    response = requests.get(url, params=params)
    data = response.json()
    all_rules.extend(data.get("rules", []))
    
    if len(data.get("rules", [])) < params["ps"]:
        break  # No más reglas disponibles en la siguiente página
    params["p"] += 1


with open('rules.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir los encabezados del CSV
    writer.writerow(['rule', 'name', 'mdDesc', 'severity', 'remFnBaseEffort', 'cleanCodeAttribute', 'cleanCodeAttributeCategory', 'impacts', 'securityStandards'])

    # Escribir las filas con los detalles de cada all_rules
    for rule in all_rules:
        writer.writerow([
            rule['key'],  # ID del all_rules
            rule['name'],  # Nombre del all_rules o regla
            rule['mdDesc'],  # Descripción en Markdown
            rule['severity'],  # Severidad del all_rules
            rule.get('remFnBaseEffort', 'N/A'),  # Esfuerzo base de remediación
            rule['cleanCodeAttribute'],  # Atributo de código limpio
            rule['cleanCodeAttributeCategory'],  # Categoría del atributo de código limpio
            rule['impacts'],  # Impactos del all_rules
            rule['securityStandards']  # Estándares de seguridad relacionados
        ])

print(f"Total de reglas obtenidas: {len(all_rules)}")
print(all_rules[0].keys())
