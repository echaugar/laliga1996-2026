import matplotlib.pyplot as plt

def total_matches(data):
    """
    Calcula el número total de partidos jugados por cada equipo,
    sumando los encuentros disputados como local y como visitante.

    Args:
        data (DataFrame): Dataset de partidos de La Liga entre 1996 y 2026

    Returns:
        DataFrame: Tabla con los equipos y el número total de
        partidos jugados, ordenada de mayor a menor.
    """
    partidos_casa = data["HomeTeam"].value_counts()
    partidos_fuera = data["AwayTeam"].value_counts()

    matches_team_total = (
        partidos_casa.add(partidos_fuera, fill_value=0)
        .astype(int)
        .sort_values(ascending=False)
        .reset_index()
    )

    matches_team_total.columns = ["Team", "Matches"]

    return matches_team_total

def plot_matches_team_total(matches_team_total):
    """
       Genera un gráfico de barras con el número total de partidos
       disputados por cada equipo.

       Args:
           matches_team_total (DataFrame): DataFrame que contiene
           los equipos y el total de partidos jugados.

       Returns:
           None
       """

    plt.figure(figsize=(14,6))

    plt.bar(
        matches_team_total["Team"],
        matches_team_total["Matches"]
    )

    plt.title("Número total de partidos por equipo")
    plt.xlabel("Equipo")
    plt.ylabel("Partidos jugados")

    plt.xticks(rotation=90)
