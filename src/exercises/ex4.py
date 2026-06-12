
import matplotlib.pyplot as plt


def FTR(data):
    """
    Calcula el número de partidos ganados por el equipo local,
    visitante y empatados.

    La información se obtiene a partir de la columna FTR
    (Full Time Result) del dataset.

    Args:
        data (DataFrame): Dataset de partidos de La Liga entre 1996 y 2026.

    Returns:
        DataFrame: Tabla con el número de partidos para cada
        resultado posible: H, A, D.
    """

    ftr = (
        data["FTR"]
        .value_counts()
        .reindex(["H", "A", "D"])
        .to_frame(name="Matches")
    )

    return ftr


def plot_FTR(ftr):
    """
    Genera un gráfico de barras con la distribución de resultados
    finalizados los partidos.

    El eje X representa los posibles resultados:
    H (victoria local), A (victoria visitante) y D (empate).
    El eje Y muestra el número de partidos de cada categoría.

    Args:
        ftr (DataFrame): DataFrame con el número de partidos
        para cada resultado final.
    """

    plt.figure(figsize=(6, 4))

    plt.bar(
        ftr.index,
        ftr["Matches"]
    )

    plt.title("Resultados finales de los partidos")
    plt.xlabel("Resultado (H, A, D)")
    plt.ylabel("Número de partidos")

    plt.grid(axis="y", alpha=0.3)