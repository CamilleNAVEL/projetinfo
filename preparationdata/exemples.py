import __init__
from preparationdata.appurement_correspondances import appurement_correspondances
from preparationdata.creation_tableTrajets import creation_tableTrajets
from preparationdata.filtre_type import filtre_type
from preparationdata.filtre_depreg import filtre_depreg
from preparationdata.filtre_tgv import filtre_tgv
from preparationdata.filtre_ter import filtre_ter

# On charge la table de tous les trajets
tableTrajets = creation_tableTrajets()
# init stocke la table des trajets deans tableTrajets

# Ensemble des trajets possibles
table1=appurement_correspondances(tableTrajets)
table1[["type"]].value_counts()

# Trajets TER
table2=filtre_type(tableTrajets, delete="TGV")
table2=appurement_correspondances(table2)
table2[["type"]].value_counts()

# Trajets TGV
table3=filtre_type(tableTrajets, delete="TER")
table3=appurement_correspondances(table3)
table3[["type"]].value_counts()

# TER en Bretagne
table4=filtre_depreg(table2,regions=["53"])
table4=appurement_correspondances(table4)
table4[["reg_origine","type"]].value_counts()
table4[["reg_destination","type"]].value_counts()

# TGV 1ere classe
table5=filtre_type(tableTrajets, delete="TER")
table5=filtre_tgv(table5,classe=["1"])
table5=appurement_correspondances(table5)
table5[["classe","type"]].value_counts()

# TGV profil tarifaire réglementé
table6=filtre_type(tableTrajets, delete="TER")
table6=filtre_tgv(table6,profil_tarifaire=["Tarif Réglementé"])
table6=appurement_correspondances(table6)
table6[["tarif_profil","type"]].value_counts()

# Trajets TER Libellé tarif valant :
# "Tarif Normal","Billet Tarif Normal Régional" ou "Billet Tarif Normal
table7=filtre_type(tableTrajets, delete="TGV")
table7=filtre_ter(table7,tarif_lib=["Tarif Normal","Billet Tarif Normal Régional","Billet Tarif Normal"])
table7=appurement_correspondances(table7)
table7[["type","tarif_lib"]].value_counts()

# Trajets TER type de tarif valant "Abonnement jeune"
table8=filtre_type(tableTrajets, delete="TGV")
table8=filtre_ter(table8,tarif_type=["Abonnement jeune"])
table8=appurement_correspondances(table8)
table8[["type","tarif_type"]].value_counts()

# TGV colonne prix maximum
table9=filtre_type(tableTrajets, delete="TER")
table9=filtre_tgv(table9,prix="maximum")
table9=appurement_correspondances(table9)
table9[["prix","Prix_minimum","Prix_maximum"]]

# TGV transporteur valant "TGV INOUI"
table10=filtre_type(tableTrajets, delete="TER")
table10=filtre_tgv(table10,transporteur=["TGV INOUI"])
table10[["transporteur","type"]].value_counts()

# TGV bretons
table11=filtre_type(tableTrajets, delete="TER")
table11=filtre_depreg(table11,regions=["53"])
table11[["reg_origine","dep_origine","type"]].value_counts()
table11[["reg_destination","dep_destination","type"]].value_counts()

