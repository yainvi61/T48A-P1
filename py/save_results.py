import pandas as pd

branch_name = os.getenv('BRANCH_NAME')

# Supongamos que tienes los resultados de las pruebas en una lista de diccionarios
test_results = [
    {'rama': branch_name}
]

# Convierte la lista de diccionarios en un DataFrame de pandas
df = pd.DataFrame(test_results)

# Guarda el DataFrame en un archivo CSV
df.to_csv('results.csv', index=False)

print("Resultados guardados en results.csv")
