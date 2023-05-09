import pandas as pd
from creation_tableTGV import creation_tableTGV
from creation_tableTER import creation_tableTER
from creation_tableCorrespondances import creation_tableCorrespondances


def creation_tableTrajets():
    """Création de la table des trajets.
    

    Returns
    -------
    dataframe
        Avec les colonnes Gare Origine, Gare origine - code UIC, Destination,
        Gare destination - code UIC, Prix
    """
    # Il va falloir reflechir. Relier gare de Massy et autres d'idf
    tableTGV = creation_tableTGV()
    tableTER = creation_tableTER()
    tableCorrespondances = creation_tableCorrespondances()
    tableTrajets=pd.concat([tableTGV,tableTER,tableCorrespondances])
    
    return(tableTrajets)

