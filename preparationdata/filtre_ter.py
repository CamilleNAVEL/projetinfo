import pandas as pd

def filtre_ter(table, tarif_lib=[], tarif_type=[], departements=[],
                regions=[]):
    """Filtre les lignes TER de la table des trajets selon les critères choisis.
    
    Parameters
    ----------
    table : dataframe
        la table des trajets, issue de creation_tableTrajets
    tarif_lib : list[str]
        liste des tarifs appliqués retenus, si la liste est vide on ne filtre pas.
    tarif_type : list[str]
        liste des types de tarif retenues, si la liste est vide on ne filtre pas.
    departements : list[str]
        liste des départements retenus, si la liste est vide on ne filtre pas.
    regions : list[str]
        liste des régions retenues, si la liste est vide on ne filtre pas.
            
    Returns
    -------
    Dataframe
        La table des trajets filtrée.
    """
    df=table[table.type == 'TER']
    
    if tarif_lib != []:
        df = df[df.Transporteur.isin(tarif_lib)]
    if tarif_type != []:
        df = df[df.Classe.isin(tarif_type)] 
    if departements !=[]:
        # A faire
        pass
    if regions !=[]:
        # A faire
        pass
           
    res=pd.concat([df,table[table.type != 'TER']])
    
    return res
            