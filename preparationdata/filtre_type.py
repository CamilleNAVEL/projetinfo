import pandas as pd

def filtre_type(table, delete):
    """Supprime les lignes d'un type ('TGV', 'TER' ou 'Correspondance' de la table 
    des trajets 
    
    Parameters
    ----------
    table : dataframe
        la table des trajets, issue de creation_tableTrajets
    delete : str
        type de trajets à supprimer, vaut 'TGV', 'TER' ou 'Correspondnace'. 
        
    Returns
    -------
    Dataframe
        La table des trajets filtrée.
    """
      
    return table[table.type != delete]
            