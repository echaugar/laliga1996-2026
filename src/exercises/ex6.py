import pandas as pd
import matplotlib.pyplot as plt


# =========================
# GOALS TOTAL
# =========================
def fun_total_goals(data):
    """
        Calcula el número total de goles marcados. Obtiene los goles marcados
        por los equipos locales, visitantes y su suma total.

        Args:
            data (DataFrame): Dataset de partidos de La Liga entre 1996 y 2026.

        Returns:
            tupla:
                - home_goals: Goles marcados por los locales.
                - away_goals: Goles marcados por los visitantes.
                - total_goals: Goles totales marcados.
        """

    home_goals = int(data["FTHG"].sum())
    away_goals = int(data["FTAG"].sum())
    total_goals = home_goals + away_goals

    return home_goals, away_goals, total_goals


# =========================
# GOALS BY TEAM
# =========================
def fun_total_goals_by_team(data):
    """
        Calcula los goles marcados por cada equipo local, visitante
        y el total acumulado sumando total y visitante.
        Args:
            data (DataFrame): Dataset de partidos de La Liga entre 1996 y 2026.

        Returns:
            tuplas de dataframes:
                - home_goals_by_team: Goles marcados
                  por cada equipo como local.
                - away_goals_by_team: Goles marcados
                  por cada equipo como visitante.
                - total_goals_by_team: Goles totales
                  marcados por cada equipo.
        """

    home_goals_by_team = (
        data.groupby("HomeTeam")["FTHG"]
        .sum()
        .to_frame("HomeGoals")
    )

    away_goals_by_team = (
        data.groupby("AwayTeam")["FTAG"]
        .sum()
        .to_frame("AwayGoals")
    )

    total_goals_by_team = (
        home_goals_by_team["HomeGoals"]
        .add(away_goals_by_team["AwayGoals"], fill_value=0)
        .sort_values(ascending=False)
        .to_frame("TotalGoals")
    )

    return home_goals_by_team, away_goals_by_team, total_goals_by_team


# =========================
# SUMMARY TABLE
# =========================
def fun_summary_1996_2025(
    total_points_by_team,
    home_goals_by_team,
    away_goals_by_team,
    total_goals_by_team
):
    """
       Genera una tabla con las estadísticas acumuladas
       de cada equipo durante el periodo 1996-2026.

       Combina los puntos totales, los goles marcados como local,
       los goles marcados como visitante y los goles totales.

       Args:
           total_points_by_team: Puntos acumulados por equipo.
           home_goals_by_team: Goles marcados como local.
           away_goals_by_team: Goles marcados como visitante.
           total_goals_by_team: Goles totales marcados.

       Returns:
           DataFrame: Tabla resumen ordenada por puntos totales.
       """

    summary_1996_2025 = pd.concat(
        [
            total_points_by_team.rename("TotalPoints"),
            home_goals_by_team,
            away_goals_by_team,
            total_goals_by_team
        ],
        axis=1
    )

    summary_1996_2025 = summary_1996_2025.sort_values(
        "TotalPoints",
        ascending=False
    )

    return summary_1996_2025


# =========================
# PODIUM PLOT
# =========================
def podium(summary_1996_2025):
    """
    Crea dos listas (teams y points), con el nombre de los tres equipos más ganadores
    y su puntuación conseguida.

    Crea un gráfico de barras con los puntos acummulados
    para esos tres equipos, mostrándose el podium histórico.

    Args:
        summary_1996_2025 (DataFrame): Tabla resumen ordenada por puntos totales.
    """

    top3 = summary_1996_2025.head(3)

    teams = top3.index.tolist()
    points = top3["TotalPoints"].tolist()

    plt.figure(figsize=(6, 4))

    # posiciones: izquierda-centro-derecha
    x_pos = [0, 1, 2]

    plt.bar(x_pos, points)

    # nombres encima de las barras
    for i, team in enumerate(teams):
        plt.text(i, points[i], team, ha="center", va="bottom")

    plt.xticks([])
    plt.yticks([])
    plt.title("Podium histórico")

    plt.tight_layout()
