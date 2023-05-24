import pandas as pd
import os

from preparationdata.creation_tableTGV import creation_tableTGV

def creation_tableCorrespondances():
    """Création de la table des correspondnaces.
    A faire en deux étapes ?

    Returns
    -------
    dataframe
        Avec les colonnes Gare Origine, Gare origine - code UIC, Destination,
        Gare destination - code UIC, Prix
    """
    tableVoyageurs = pd.read_csv(os.path.join("preparationdata/data","referentiel-gares-voyageurs.csv"),sep=";",
                             dtype={'Code UIC': str,'Code Commune': str,'Code département': str})
    tableVoyageurs.columns = [c.replace(' ','_') for c in tableVoyageurs.columns]
    

    garesTGV=creation_tableTGV()[["origine","code_origine"]]
    garesTGV.drop_duplicates(keep = 'first', inplace=True)
    gares=tableVoyageurs[["Code_UIC","Code_département","Code_Commune"]]
    
    gares=gares.assign(Code_UIC = lambda df: df['Code_UIC'].str[2:])
   
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
        
    return(correspondances)