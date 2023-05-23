import pandas as pd
import os
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

    
    # On enlève les gares étrangères
    tableVoyageurs = pd.read_csv(os.path.join("preparationdata/data","referentiel-gares-voyageurs.csv"),
                                 sep=";",
                                 dtype={'Code UIC': str,'Code Commune': str,'Code département': str})
    tableVoyageurs.columns = [c.replace(' ','_') for c in tableVoyageurs.columns]
    
    
    gares=tableVoyageurs[["Code_UIC"]]
    
    gares=gares.assign(Code_UIC = lambda df: df['Code_UIC'].str[2:])
    
    gares_origine=gares.rename(columns={"Code_UIC" : "code_origine" })
    tableTrajets=tableTrajets.merge(gares_origine,on='code_origine',
                                          suffixes=(False, False))
    
    gares_destination=gares.rename(columns={"Code_UIC" : "code_destination" })
    tableTrajets=tableTrajets.merge(gares_destination,on='code_destination',
                                          suffixes=(False, False))
        
    return(tableTrajets)

