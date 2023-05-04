import os
import pandas as pd

from creation_tableTrajets import creation_tableTrajets
# On charge les tables SNCF, on remplace les ' ' par des '_' dans les noms de colonnes

# A faire : convertir Classe en str. S'assurer du bon type des variables. Les id en str
# tableTGV = pd.read_csv(os.path.join("data","tarifs-tgv-inoui-ouigo.csv"),sep=";")
# tableTGV.columns = [c.replace(' ','_') for c in tableTGV.columns]
tableTrajets = creation_tableTrajets()

tableVoyageurs = pd.read_csv(os.path.join("data","referentiel-gares-voyageurs.csv"),sep=";")
tableVoyageurs.columns = [c.replace(' ','_') for c in tableVoyageurs.columns]
