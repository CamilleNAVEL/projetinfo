import pandas as pd

def filtre_tgv(table, transporteur=[], classe=[], profil_tarifaire=[], departements=[],
                regions=[], prix="minimum"):
    """Filtre les lignes TGV de la table des trajets selon les critères choisis.
    La variable prix permet de choisir entre la colonne prix minimal et prix maximal.
    
    Parameters
    ----------
    table : dataframe
        la table des trajets, issue de creation_tableTrajets
    transporteur : list[str]
        liste des transporteurs retenus, si la liste est vide on ne filtre pas.
    classe : list[str]
        liste des classes retenues, si la liste est vide on ne filtre pas.
    profil_tarifaire : list[str]
        liste des profils tarifaires retenus, si liste vide on ne filtre pas.
    prix : str
        vaut "minimum" ou "maximum".
        
    Returns
    -------
    TableTrajets
        La table des trajets filtrée. La colonne du prix (min ou max) est renommée prix.
    """
    df=table[table.type == 'TGV']
    
    if transporteur != []:
        df = df[df.transporteur.isin(transporteur)]
    if classe != []:
        df = df[df.classe.isin(classe)] # Pb : numérique au lieu de str
    if profil_tarifaire !=[]:
        df = df[df.tarif_profil.isin(profil_tarifaire)]
    
    
    if prix == 'minimum':
        # df['prix']=df.Prix_minimum
        df=df.assign(prix = lambda df: df['Prix_minimum'])
    if prix == 'maximum':
        # df['prix']=df.Prix_maximum
        df=df.assign(prix = lambda df: df['Prix_maximum'])
      
    res=pd.concat([df,table[table.type != 'TGV']])
    
    return res
            