"""
Módulo principal de ejecución del proyecto LaLiga 1996-2026.

Autor: Eric Chaume García
Fecha: Junio de 2026
"""

from datetime import datetime
import matplotlib.pyplot as plt

from exercises.ex1 import load_and_eda, plot_home_away_goals

from exercises.ex2 import total_matches, plot_matches_team_total

from exercises.ex3 import goals_distribution, plot_goals_distribution
from exercises.ex4 import FTR, plot_FTR
from exercises.ex5 import add_points, fun_total_points, alltime_winner

from exercises.ex6 import (
    fun_total_goals,
    fun_total_goals_by_team,
    fun_summary_1996_2025,
    podium
)

from exercises.ex7 import graf

#Configuración global: funciones globales

nom_alumne = "Eric Chaume García"
date_time = datetime.now().strftime("%Y%m%d_%H%M%S")


def save_fig(ex_number):
    """
    Guardar la gráfica generada en función del ejercicio, alumno y momento creación
    """
    plt.savefig(
        f"img/grafica_ex{ex_number}_{nom_alumne}_{date_time}.png"
    )


#-----------------
# EJERCICIO 1:
#-----------------

def run_ex1():
    """
    Agrupar código del ejercicio 1 para posterior ejecución en la función main().
    """

    data = load_and_eda("data/LaLiga_Matches.csv")

    print(data.head())

    # Gráfico ejercicio 1
    plot_home_away_goals(data)

    save_fig(1)
    plt.close()

    print("Ex1 ejecutado correctamente")

    return data

#-----------------
#EJERCICIO 2:
#-----------------

def run_ex2(df):
    """
    Agrupar código del ejercicio 2 para posterior ejecución en la función def main():
    """

    matches_team_total = total_matches(df)

    print("Top 10 equipos:")
    print(matches_team_total.head(10))

    max_matches = matches_team_total["Matches"].max()

    siempre_presente = matches_team_total[
        matches_team_total["Matches"] == max_matches
    ]

    print("\nEquipos siempre en Primera:")
    print(siempre_presente["Team"].tolist())

    plot_matches_team_total(matches_team_total)

    save_fig(2)
    plt.close()

    print("Ex2 ejecutado correctamente")


#-----------------
#EJERCICIO 3:
#-----------------

def run_ex3(df):
    """
    Agrupar código del ejercicio 3 para posterior ejecución en la función def main():
    """

    d_home, d_away = goals_distribution(df)

    print("Distribución goles locales:")
    print(d_home)

    print("\nDistribución goles visitantes:")
    print(d_away)

    plot_goals_distribution(d_home, d_away)

    save_fig(3)
    plt.close()

    print("Ex3 ejecutado correctamente")

#-----------------
#EJERCICIO 4:
#-----------------

def run_ex4(df):
    """
    Agrupar código del ejercicio 4 para posterior ejecución en la función def main():
    """

    ftr = FTR(df)

    print("Distribución FTR:")
    print(ftr)

    # porcentaje de victorias locales
    home_wins = ftr.loc["H", "Matches"]
    total = ftr["Matches"].sum()

    porcentaje_casa = home_wins / total * 100

    print(f"\nPorcentaje de victorias locales: {porcentaje_casa:.2f}%")

    # gráfico
    plot_FTR(ftr)

    save_fig(4)
    plt.close()

    print("Ex4 ejecutado correctamente")

#-----------------
# EJERCICIO 5:
#-----------------

def run_ex5(df):
    """
    Agrupar código del ejercicio 5 para posterior ejecución en la función def main():
    """

    # 1. Añadir puntos
    df = add_points(df)

    print(df[["HomeTeam", "AwayTeam", "FTR", "HTP", "ATP"]].head(10))

    # 2. Puntos totales
    series_points, df_total_points = fun_total_points(df)

    print("\nTop 10 equipos por puntos:")
    print(df_total_points.head(10))

    # 3. Ganador histórico (1996-2026)
    winner = alltime_winner(df_total_points)
    points = df_total_points.loc[winner, "TotalPoints"]

    print(f"\nGanador histórico: {winner} con {points} puntos")

    print("Ex5 ejecutado correctamente")

    return df, df_total_points

#-----------------
# EJERCICIO 6:
#-----------------

def run_ex6(df, df_total_points):
    """
    Agrupar código del ejercicio 6 para posterior ejecución en la función def main():
    """

    # Goles totales
    home_g, away_g, total_g = fun_total_goals(df)

    print("Goles locales:", home_g)
    print("Goles visitantes:", away_g)
    print("Goles totales:", total_g)

    # Goles por equipo
    home_goals, away_goals, total_goals = fun_total_goals_by_team(df)

    print("\nTop 10 equipos en goles:")
    print(total_goals.head(10))

    # Resumen
    summary = fun_summary_1996_2025(
        df_total_points["TotalPoints"],
        home_goals,
        away_goals,
        total_goals
    )

    print("\nSummary:")
    print(summary.head())

    # Podium
    podium(summary)

    save_fig(6)
    plt.close()

    print("Ex6 ejecutado correctamente")

    return summary

#-----------------
# EJERCICIO 7:
#-----------------

def run_ex7(data, summary_1996_2025):
    """
    Agrupar código del ejercicio 7 para posterior ejecución en la función def main():
    """

    selected_teams = (
        summary_1996_2025
        .head(5)
        .index
        .tolist()
    )

    print("Top 5 equipos históricos:")
    print(selected_teams)

    graf(data, selected_teams)

    save_fig(7)
    plt.close()

    print("Ex7 ejecutado correctamente")


# =========================
# MAIN (ejecución secuencial)
# =========================
def main():
    """Ejecuta todos los ejercicios de forma secuencial."""

    df = run_ex1()

    run_ex2(df)

    run_ex3(df)

    run_ex4(df)

    df, df_total_points = run_ex5(df)

    summary_1996_2025 = run_ex6(
        df,
        df_total_points
    )

    run_ex7(
        df,
        summary_1996_2025
    )

if __name__ == "__main__":
    main()
