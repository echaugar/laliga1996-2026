from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

nom_alumne = "TuNombre"
date_time = datetime.now().strftime("%Y%m%d_%H%M%S")


def load_and_eda(file):
    """
    Leer csv y eliminar columnas de mitad de partido (HT...)

    Args:
        file: archivo csv

    Returns: dataframe sin columnas referentes a mitad partido "HTHG", "HTAG", "HTR"
    """
    data = pd.read_csv(file)
    cols_to_drop = ["HTHG", "HTAG", "HTR"]
    data = data.drop(columns=cols_to_drop)
    return data

def plot_home_away_goals(data):
    """
    Genera un diagrama de cajas y bigotes con el número de goles en casa y fuera

    Args:
        data (DataFrame): Dataset de partidos de La Liga entre 1996 y 2026
    """
    plt.figure(figsize=(8,5))
    plt.boxplot([data["FTHG"], data["FTAG"]], labels=["Home Goals", "Away Goals"])
    plt.title("Distribución de goles")
    plt.ylabel("Número de goles")
