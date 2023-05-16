import pandas as pd
from preparationdata.creation_tableTGV import creation_tableTGV
from preparationdata.creation_tableTER import creation_tableTER
from preparationdata.creation_tableCorrespondances import creation_tableCorrespondances
from preparationdata.creation_tableDep import creation_tableDep

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
    
    # rajout des départements et régions
    gares=creation_tableDep()
    gares_origine=gares.rename(columns = {"code_UIC" : "code_origine",
                                          "dep" : "dep_origine",
                                          "reg" : "reg_origine"})
    gares_destination=gares.rename(columns = {"code_UIC" : "code_destination",
                                          "dep" : "dep_destination",
                                          "reg" : "reg_destination"})
    
    tableTrajets = tableTrajets.merge(gares_origine,on="code_origine",
                                      suffixes=(True,False))
    
    tableTrajets = tableTrajets.merge(gares_destination,on="code_destination",
                                      suffixes=(True,False))

        
    return(tableTrajets)

