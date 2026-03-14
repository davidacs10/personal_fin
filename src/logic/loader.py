import pandas as pd

COLUMNAS_REQUERIDAS = {"Fecha", "Concepto", "Monto", "Categoria"}


def cargar_excel(archivo) -> tuple[pd.DataFrame | None, str | None]:
    """
    Lee un archivo .xlsx y valida su estructura.
    Retorna (DataFrame, None) si es válido, o (None, mensaje_error) si no.
    """
    try:
        df = pd.read_excel(archivo, parse_dates=["Fecha"])
    except Exception as e:
        return None, f"No se pudo leer el archivo: {e}"

    columnas_faltantes = COLUMNAS_REQUERIDAS - set(df.columns)
    if columnas_faltantes:
        return None, f"Columnas faltantes: {', '.join(columnas_faltantes)}"

    # Limpieza básica
    df["Monto"] = pd.to_numeric(df["Monto"], errors="coerce")
    df = df.dropna(subset=["Monto"])
    df["Categoria"] = df["Categoria"].str.strip().str.title()

    return df, None
