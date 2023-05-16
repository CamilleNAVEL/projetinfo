import pandas as pd

def appurement_correspondances(table):
    """Supprime les correspondances superflues. 
    
    A utiliser après avoir filtré la table. Supprime les correspondances qui sont hors du graphe
    ainsi que celles qui doublonnent des trajets TGV ou TER existant.
    
    Parameters
    ----------
    table : dataframe
        la table des trajets, issue de creation_tableTrajets
            
    Returns
    -------
    TableTrajets
        La table des trajets filtrée.
    """
    
    correspondances=table[table.type == 'correspondance']
    tgvter=table[table.type != 'correspondance']
    
    gares1=tgvter[['code_origine']]
    gares1=gares1.rename(columns = {"code_origine" : "gare"})
    gares2=tgvter[['code_destination']]
    gares2=gares2.rename(columns = {"code_destination" : "gare"})
    
    gares=pd.concat([gares1,gares2])
    gares.drop_duplicates(keep = 'first', inplace=True)
    
    # On vérifie que les origines et destinations sont dans les trajets hors correspondance
    gares_origine=gares.rename(columns={"gare" : "code_origine" })
    correspondances=correspondances.merge(gares_origine,on='code_origine',
                                          suffixes=(False, False))
    
    gares_destination=gares.rename(columns={"gare" : "code_destination" })
    correspondances=correspondances.merge(gares_destination,on='code_destination',
                                        suffixes=(False, False))
    
    # On s'assure que la correspondance n'existe pas dans les TGV (peu probable) ou TER
    # on va créer une clé code_origine + code_destination
        
    correspondances["cle"] = correspondances.code_origine + correspondances.code_destination
    correspondances = correspondances[~correspondances.cle.isin(
        tgvter.code_origine + tgvter.code_destination)]
    
    correspondances = correspondances.drop(columns='cle')
    
    return pd.concat([tgvter, correspondances])
