import networkx as nx
import matplotlib.pyplot as plt

def graf(data, selected_teams):
    """
    Crea un gráfico no dirigido de los quipos más ganadores de los últimos
    30 años.
    Los nodos muestran los 5 equipos con mayor puntuación histrórica
    acumulada.
    Las aristas muestran el número de enfrentamientos

    Args:
        data (DataFrame): Dataset de partidos de La Liga entre 1996 y 2026.
        selected_teams: lista con los 5 equipos con mas puntos.
    """

    # Filtrar partidos entre equipos seleccionados
    filtered = data[
        (data["HomeTeam"].isin(selected_teams)) &
        (data["AwayTeam"].isin(selected_teams))
    ]

    # Grafo no dirigido
    G = nx.Graph()

    # Añadir nodos
    for team in selected_teams:
        G.add_node(team)

    # Contar enfrentamientos
    matches = {}

    for _, row in filtered.iterrows():

        team1 = row["HomeTeam"]
        team2 = row["AwayTeam"]

        edge = tuple(sorted([team1, team2]))

        matches[edge] = matches.get(edge, 0) + 1

    # Añadir aristas con peso
    for edge, weight in matches.items():
        G.add_edge(edge[0], edge[1], weight=weight)

    # Posiciones
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 8))

    # Nodos
    colors = [
      "blue",
      "white",
      "red",
      "orange",
      "green"
    ]

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=2500,
        node_color=colors
    )
    # Aristas
    nx.draw_networkx_edges(
        G,
        pos,
        width=2
    )

    # Etiquetas nodos
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=7
    )

    # Etiquetas aristas
    edge_labels = nx.get_edge_attributes(
        G,
        "weight"
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels
    )

    plt.title("Conexiones entre los 5 mejores equipos")
    plt.axis("off")