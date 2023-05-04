import pandas as pd
import os

def creation_tableTER():
    """Création de la table des trajets TER.
    A faire en deux étapes ?

    Returns
    -------
    dataframe
        Avec les colonnes Gare Origine, Gare origine - code UIC, Destination,
        Gare destination - code UIC, Prix
    """
    # Il va falloir reflechir. Relier gare de Massy et autres d'idf
    tableTER = pd.read_csv(os.path.join("data","tarifs-ter-par-od.csv"),sep=";",
                             dtype={'Origine - code UIC': str,'Destination - code UIC': str})
    tableTER.columns = [c.replace(' ','_') for c in tableTER.columns]

    tableTER=tableTER.rename(columns = {"Région" : "region",
                                        "Origine" : "origine",
                                        "Origine_-_code_UIC" : "code_origine",
                                        "Destination" : "destination",
                                        "Destination_-_code_UIC" : "code_destination",
                                        "Libellé_tarif" : "tarif_lib",
                                        "Type_tarif" : "tarif_type",
                                        "Prix" : "prix"})
        
        # df = df [["origine","code_origine","destination","code_destination","prix"]]
        
    tableTER['type'] = 'TER'

    
    return(tableTER)