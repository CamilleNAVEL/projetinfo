import pandas as pd

def filtre_ter(table, tarif_lib=[], tarif_type=[]):
    """Filtre les lignes TER de la table des trajets selon les critères choisis.
    
    Parameters
    ----------
    table : dataframe
        la table des trajets, issue de creation_tableTrajets
    tarif_lib : list[str]
        liste des tarifs appliqués retenus, si la liste est vide on ne filtre pas.
    tarif_type : list[str]
        liste des types de tarif retenues, si la liste est vide on ne filtre pas.

            
    Returns
    -------
    Dataframe
        La table des trajets filtrée.
    """
    df=table[table.type == 'TER']
    
    if tarif_lib != []:
        df = df[df.tarif_lib.isin(tarif_lib)]
    if tarif_type != []:
        df = df[df.tarif_type.isin(tarif_type)] 

           
    res=pd.concat([df,table[table.type != 'TER']])
    
    return res
            