import pandas as pd


def resumen_por_categoria(df: pd.DataFrame) -> pd.DataFrame:
    """Total gastado por categoría, ordenado de mayor a menor."""
    return (
        df.groupby("Categoria")["Monto"]
        .sum()
        .reset_index()
        .rename(columns={"Monto": "Total"})
        .sort_values("Total", ascending=False)
    )


def resumen_por_mes(df: pd.DataFrame) -> pd.DataFrame:
    """Total gastado por mes, con columna legible 'Mes'."""
    df = df.copy()
    df["Mes"] = df["Fecha"].dt.to_period("M").astype(str)
    return (
        df.groupby("Mes")["Monto"]
        .sum()
        .reset_index()
        .rename(columns={"Monto": "Total"})
        .sort_values("Mes")
    )


def variacion_mensual(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega columna 'Variacion_%' que indica cuánto cambió
    el gasto respecto al mes anterior.
    """
    resumen = resumen_por_mes(df)
    resumen["Variacion_%"] = resumen["Total"].pct_change() * 100
    resumen["Variacion_%"] = resumen["Variacion_%"].round(1)
    return resumen
