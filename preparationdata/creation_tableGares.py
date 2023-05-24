import pandas as pd
import os

def creation_tableGares():
    """Création de la table des gares à partir
    du csv referentiel-gares-voyageurs
    
    Returns
    -------
    dataframe
        Avec les colonnes code_UIC, dep et reg
    """
       
    tableVoyageurs = pd.read_csv(os.path.join("preparationdata/data","referentiel-gares-voyageurs.csv"),sep=";",
                             dtype={'Code UIC': str,'Code Commune': str,'Code département': str})
    tableVoyageurs.columns = [c.replace(' ','_') for c in tableVoyageurs.columns]
    

    tableVoyageurs=tableVoyageurs.assign(Code_UIC = lambda df: df['Code_UIC'].str[2:])
    tableVoyageurs=tableVoyageurs.rename(columns = {"Code_UIC" : "code_UIC",
                                  "Code_département" : "dep"})
    
            
    return(tableVoyageurs)