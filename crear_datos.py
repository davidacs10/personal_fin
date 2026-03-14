import pandas as pd

datos = {
    "Fecha": [
        "2024-01-05",
        "2024-01-12",
        "2024-01-18",
        "2024-02-03",
        "2024-02-15",
        "2024-02-22",
    ],
    "Concepto": ["Supermercado", "Netflix", "Gasolina", "Restaurante", "Gym", "Uber"],
    "Monto": [1200, 250, 800, 450, 350, 180],
    "Categoria": ["Comida", "Ocio", "Transporte", "Comida", "Salud", "Transporte"],
}
pd.DataFrame(datos).to_excel("data/gastos_ejemplo.xlsx", index=False)
print("✅ Archivo creado en data/gastos_ejemplo.xlsx")
