import os
import pandas as pd
from creation_tableCorrespondances import creation_tableCorrespondances
# On charge les tables SNCF, on remplace les ' ' par des '_' dans les noms de colonnes

# A faire : convertir Classe en str. S'assurer du bon type des variables. Les id en str
tableTGV = pd.read_csv(os.path.join("data","tarifs-tgv-inoui-ouigo.csv"),sep=";")
tableTGV.columns = [c.replace(' ','_') for c in tableTGV.columns]

tableTER = pd.read_csv(os.path.join("data","tarifs-ter-par-od.csv"),sep=";")
tableTER.columns = [c.replace(' ','_') for c in tableTER.columns]

tableVoyageurs = pd.read_csv(os.path.join("data","referentiel-gares-voyageurs.csv"),sep=";")
tableVoyageurs.columns = [c.replace(' ','_') for c in tableVoyageurs.columns]

tableCorrespondances = creation_tableCorrespondances()
tableCorrespondances.columns = [c.replace(' ','_') for c in tableCorrespondances.columns]


