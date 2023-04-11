import pandas as pd

def creation_tableCorrespondances():
    """Création de la table des correspondnaces.
    A faire en deux étapes ?

    Returns
    -------
    dataframe
        Avec les colonnes Gare Origine, Gare origine - code UIC, Destination,
        Gare destination - code UIC, Prix
    """
    # Il va falloir reflechir. Relier gare de Massy et autres d'idf
    
    df=pd.DataFrame({'origine' : ["PARIS GARE DE LYON","PARIS GARE DE LYON","PARIS GARE DE LYON"],
                     'code_origine' : ['87686006'],
                     'destination' : ['PARIS EST'],
                     'code_destination' : ['87113001'],
                     'prix' : [1.5]}
                    )
    
    return(df)