from dijkstra_source_vers_destination import dijkstra_source_vers_destination
import pandas as pd

graphe = pd.DataFrame({
    'origine': ["PARIS", "PARIS", "LYON"],
    'code_origine': ['1', '1', '2'],
    'destination': ["LYON", "MARSEILLE", "MARSEILLE"],
    'code_destination': ['2', '3', '3'],
    'prix': [50, 100, 30]
})

dijkstra_source_vers_destination(graphe, "PARIS", "MARSEILLE")
