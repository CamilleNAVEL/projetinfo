import pandas as pd
import os

def creation_tableDep():
    """Création de la table des Départements et régions pour les gares
    du referentiel des gares.
    
    Returns
    -------
    dataframe
        Avec les colonnes code_UIC, dep et reg
    """
   
    tableDep = pd.read_csv(os.path.join("preparationdata/data","v_departement_2023.csv"),sep=",",
                             dtype={'DEP': str,'REG': str})   
    
    tableDep = tableDep.rename(columns = {"DEP" : "dep",
                                          "REG" : "reg"})
    
    tableDep=tableDep[["reg","dep"]]
    
    tableVoyageurs = pd.read_csv(os.path.join("preparationdata/data","referentiel-gares-voyageurs.csv"),sep=";",
                             dtype={'Code UIC': str,'Code Commune': str,'Code département': str})
    tableVoyageurs.columns = [c.replace(' ','_') for c in tableVoyageurs.columns]
    
    gares=tableVoyageurs[["Code_UIC","Code_département"]]
    # gares['Code_UIC']=gares['Code_UIC'].str[2:]
    gares=gares.assign(Code_UIC = lambda df: df['Code_UIC'].str[2:])
    gares=gares.rename(columns = {"Code_UIC" : "code_UIC",
                                  "Code_département" : "dep"})
    
    gares=gares.merge(tableDep,on="dep",suffixes=(True,False))
            
    return(gares)