import __init__
import pandas as pd
import numpy as np
import tableTrajets
from creation_tableTrajets import creation_tableTrajets
from creation_tableTGV import creation_tableTGV

trajets = TableTrajets('TGV')

trajets.table
trajets.type

t2=trajets.filtre_tgv(prix="minimum")

t2.table
t2.type

t3=t2.ajout_correspondances()
t3.table
"DIJON VILLE" in set(trajets.table.origine)
"DIJONh VILLE" in set(trajets.table.origine)

set(t2.table.code_origine).union(set(t2.table.code_destination))

creation_tableCorrespondances()

os.getcwd()

tableTGV.columns

pouet = pd.concat([tableTGV,tableTER,tableCorrespondances])
pouet.columns


pouet=creation_tableTGV()



garesParis=pouet[pouet['origine'].str.contains("PARIS")][["origine","code_origine"]]


garesParis.drop_duplicates(keep = 'first', inplace=True)
garesParis
garesParisDest = garesParis

garesParisDest=garesParisDest.rename(columns = {"origine" : "destination",
                                          "code_origine" : "code_destination"
                                          })
garesParisDest
# faire un produit cartesien puis virer les trajets nuls

garesParis=garesParis.merge(garesParisDest, how='cross')

garesParis

garesParis=garesParis[garesParis.code_origine != garesParis.code_destination]



# Trouvons les gares avec même commune

# dans init

import os

from creation_tableTGV import creation_tableTGV

tableVoyageurs = pd.read_csv(os.path.join("data","referentiel-gares-voyageurs.csv"),sep=";",
                             dtype={'Code UIC': str,'Code Commune': str,'Code département': str})
tableVoyageurs.columns = [c.replace(' ','_') for c in tableVoyageurs.columns]
# del gares

garesTGV=creation_tableTGV()[["origine","code_origine"]]
garesTGV.drop_duplicates(keep = 'first', inplace=True)
gares=tableVoyageurs[["Code_UIC","Code_département","Code_Commune"]]
gares['Code_UIC']=gares['Code_UIC'].str[2:]

gares=gares.merge(garesTGV,left_on="Code_UIC",right_on="code_origine",suffixes=(True,True))
 
gares['codecom']=gares['Code_département'] + gares['Code_Commune']

plusieursgares=gares.groupby(['codecom'])['codecom'].count().reset_index(name='counts')
plusieursgares=plusieursgares[plusieursgares.counts >1]
plusieursgares.drop_duplicates(keep = 'first', inplace=True)

gares2=gares.merge(plusieursgares, on='codecom', suffixes=(False, True))

gares2=gares2[["origine","Code_UIC","codecom"]]

garesorigine=gares2.rename(columns = {"Code_UIC" : "code_origine",
                                          "codecom" : "com_origine"
                                          })

garesdestination=gares2.rename(columns = {"origine" : "destination",
                                          "Code_UIC" : "code_destination",
                                          "codecom" : "com_destination"
                                          })

correspondances=garesorigine.merge(garesdestination,
                                   left_on="com_origine",right_on="com_destination",
                                   suffixes=(True,True))

correspondances=correspondances[correspondances.code_origine != correspondances.code_destination]

correspondances=correspondances[["origine","code_origine","destination","code_destination"]]

correspondances["prix"]=1.5
correspondances["type"]="correspondance"

creation_tableCorrespondances()

creation_tableTrajets()