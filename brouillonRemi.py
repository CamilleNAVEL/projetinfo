import __init__

import tableTrajets

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