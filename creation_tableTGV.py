import pandas as pd

def creation_tableTGV():
    """Création de la table des trajets TGV.
    A faire en deux étapes ?

    Returns
    -------
    dataframe
        Avec les colonnes Gare Origine, Gare origine - code UIC, Destination,
        Gare destination - code UIC, Prix
    """
    # Il va falloir reflechir. Relier gare de Massy et autres d'idf
    tableTGV = pd.read_csv(os.path.join("data","tarifs-tgv-inoui-ouigo.csv"),sep=";")
    tableTGV.columns = [c.replace(' ','_') for c in tableTGV.columns]
    
    tableTGV = tableTGV.rename(columns = {"Transporteur" : "transporteur",
                                          "Gare_origine" : "origine",
                                          "Gare_origine_-_code_UIC" : "code_origine",
                                          "Destination" : "destination",
                                          "Gare_destination_-_code_UIC" : "code_destination",
                                          "Classe" : "classe",
                                          "Profil_tarifaire" : "tarif_profil",
                                          })
        
        # df = df [["origine","code_origine","destination","code_destination","prix"]]
        
    tableTGV['type'] = 'TGV'

    
    return(tableTGV)