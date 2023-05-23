import pandas as pd

def filtre_depreg(table, departements=[],
                regions=[]):
    """Filtre les gares d'origine et d'arrivée sur les départements et régions.
    
    Parameters
    ----------
    table : dataframe
        la table des trajets, issue de creation_tableTrajets
    departements : list[str]
        liste des départements retenus, si la liste est vide on ne filtre pas.
    regions : list[str]
        liste des régions retenues, si la liste est vide on ne filtre pas.

        
    Returns
    -------
    TableTrajets
        La table des trajets filtrée.
    """
    df=table
       
    if departements !=[]:
        df = df[df.dep_origine.isin(departements)]
        df = df[df.dep_destination.isin(departements)]        
    if regions !=[]:
        df = df[df.reg_origine.isin(regions)]
        df = df[df.reg_destination.isin(regions)]      
    
          
    return df
            