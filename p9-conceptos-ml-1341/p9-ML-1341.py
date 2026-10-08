# valeria yaretzi NC =
import pandas as pd

# ==========================================
# ACT 12 - CONCEPTOS FUNDAMENTALES DE DATOS
# Número de lista: 36
# Dataset correspondiente: datos6
# ==========================================

datos6 = {
    'distancia_km': [3.7, 2.4, 6.8, 1.3, 4.0],
    'trafico_nivel': [1, 3, 3, 1, 2],
    'edad_repartidor': [27, 39, 44, 20, 32],
    'tiempo_entrega_min': [25, 22, 65, 10, 32]
}

# Crear DataFrame
df = pd.DataFrame(datos6)

# Mostrar todos los datos
print("======================================")
print("ACT 12 - DATOS 6")
print("Número de lista: 36")
print("======================================")

print("\n--- DATASET COMPLETO ---")
print(df)

# Separar variables de entrada (X)
X = df[
    [
        'distancia_km',
        'trafico_nivel',
        'edad_repartidor'
    ]
]

# Variable objetivo (y)
y = df['tiempo_entrega_min']

# Mostrar variables de entrada
print("\n--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X)

# Mostrar variable objetivo
print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y)

# Mostrar los primeros datos
print("\n--- PRIMEROS 2 REGISTROS ---")
print(X.head(2))

print("\n--- PRIMEROS 2 VALORES DEL TARGET ---")
print(y.head(2))
print("valeria yaretzi NC = 1341")