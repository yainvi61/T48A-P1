import pandas as pd

# Supongamos que tienes los resultados de las pruebas en una lista de diccionarios
test_results = [
    {'usuario': 'user1', 'prueba': 'test1', 'resultado': 'aprobado'},
    {'usuario': 'user2', 'prueba': 'test2', 'resultado': 'fallido'},
    {'usuario': 'user3', 'prueba': 'test3', 'resultado': 'aprobado'},
    # Agrega más resultados según sea necesario
]

# Convierte la lista de diccionarios en un DataFrame de pandas
df = pd.DataFrame(test_results)

# Guarda el DataFrame en un archivo CSV
df.to_csv('results.csv', index=False)

print("Resultados guardados en results.csv")
