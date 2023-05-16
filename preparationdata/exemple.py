import __init__
from preparationdata.appurement_correspondances import appurement_correspondances
from preparationdata.creation_tableTrajets import creation_tableTrajets
from preparationdata.filtre_type import filtre_type

# On charge la table de tous les trajets
tableTrajets = creation_tableTrajets()
# init stocke la table des trajets deans tableTrajets

table=tableTrajets

table1=appurement_correspondances(tableTrajets)


table2=filtre_type(tableTrajets, delete="TGV")
table2=appurement_correspondances(table2)

table3=filtre_type(tableTrajets, delete="TER")
table3=appurement_correspondances(table3)