import matplotlib.pyplot as plt

def goals_distribution(data):
    """
    Calcula la distribución de goles marcados por los equipos
    locales y visitantes.

    Para cada número de goles, obtiene el número de partidos
    en los que ha producido dicho resultado.

    Args:
        data (DataFrame): Dataset de partidos de La Liga entre 1996 y 2026

    Returns:
        tuple: Tupla formada por:
            - distr_goals_home (DataFrame): Distribución de goles
              marcados por los equipos locales.
            - distr_goals_away (DataFrame): Distribución de goles
              marcados por los equipos visitantes.
    """

    distr_goals_home = (
        data["FTHG"]
        .value_counts()
        .sort_index()
        .to_frame(name="Matches")
    )

    distr_goals_away = (
        data["FTAG"]
        .value_counts()
        .sort_index()
        .to_frame(name="Matches")
    )

    return distr_goals_home, distr_goals_away


def plot_goals_distribution(distr_goals_home, distr_goals_away):
    """
        Genera una figura con dos gráficos de barras que muestran
        la distribución de goles de los equipos locales y visitantes.

        Args:
            distr_goals_home (DataFrame): Distribución de goles
                marcados por los equipos locales.
            distr_goals_away (DataFrame): Distribución de goles
                marcados por los equipos visitantes.

        Returns:
            None
        """
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # HOME
    ax[0].bar(
        distr_goals_home.index,
        distr_goals_home["Matches"]
    )

    ax[0].set_title("Goles equipo local")
    ax[0].set_xlabel("Número de goles")
    ax[0].set_ylabel("Número de partidos")

    # AWAY
    ax[1].bar(
        distr_goals_away.index,
        distr_goals_away["Matches"]
    )

    ax[1].set_title("Goles equipo visitante")
    ax[1].set_xlabel("Número de goles")
    ax[1].set_ylabel("Número de partidos")

    plt.tight_layout()