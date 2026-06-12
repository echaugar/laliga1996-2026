import numpy as np

def add_points(data):
    """
    Copia del dataframe original seleccionándose de las columnas FTR H, A Y D
    y adjudicándose 3,1,0 en función del ganador del partido.

    Args:
        data (DataFrame): Dataset de partidos de La Liga entre 1996 y 2026:

    Returns:
        DataFrame: Tabla con nuevas columnas HTP,ATP en las que aparecen los puntos en la mitad parte
    """

    data = data.copy()

    data["HTP"] = np.select(
        [data["FTR"] == "H", data["FTR"] == "D", data["FTR"] == "A"],
        [3, 1, 0]
    )

    data["ATP"] = np.select(
        [data["FTR"] == "H", data["FTR"] == "D", data["FTR"] == "A"],
        [0, 1, 3]
    )

    return data


def fun_total_points(data):
    """
       Calcula los puntos totales acumulados para cada equipo.

       Suma los puntos obtenidos como local (HTP) y como visitante
       (ATP), generando una clasificación histórica ordenada de
       mayor a menor puntuación(ascending=False).

       Args:
           data (DataFrame): Dataset de partidos de La Liga entre 1996 y 2026:

       Returns:
           tuple:
               - total_points (Series): Puntos totales por equipo.
               - df_total_points (DataFrame): Tabla con los puntos
                 totales por equipo.
       """
    home_points = data.groupby("HomeTeam")["HTP"].sum()
    away_points = data.groupby("AwayTeam")["ATP"].sum()

    total_points = home_points.add(away_points, fill_value=0)\
                              .sort_values(ascending=False)

    df_total_points = total_points.to_frame(name="TotalPoints")

    return total_points, df_total_points


def alltime_winner(df_total_points):
    """
    Calcula el equipo que mas puntos ha ganado

    Args:
         df_total_points (DataFrame): Dataset con la columna TotalPoints para cada equipo.

    Returns:
        Nombre del equipo tipo texto (str) que ocupa la primera posición
    """
    return df_total_points["TotalPoints"].idxmax()