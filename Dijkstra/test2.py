from Dijkstra.dijkstra_source_vers_destination import dijkstra_source_vers_destination
import pandas as pd
import __init__
from preparationdata.appurement_correspondances import appurement_correspondances
from preparationdata.creation_tableTrajets import creation_tableTrajets
from preparationdata.filtre_type import filtre_type
from preparationdata.filtre_depreg import filtre_depreg
from preparationdata.filtre_tgv import filtre_tgv
from preparationdata.filtre_ter import filtre_ter

# On charge la table de tous les trajets
tableTrajets = creation_tableTrajets()

# TGV bretons
table11=filtre_type(tableTrajets, delete="TER")
table11=filtre_depreg(table11,regions=["53"])
table11[["reg_origine","dep_origine","type"]].value_counts()
table11[["reg_destination","dep_destination","type"]].value_counts()

table11
dijkstra_source_vers_destination(table11, "RENNES", "BREST")


# Ensemble des trajets possibles
table1=appurement_correspondances(tableTrajets)
table1[["type"]].value_counts()
dijkstra_source_vers_destination(table1, "RENNES", "STRASBOURG")
