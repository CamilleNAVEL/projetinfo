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
    departements : list[str]
        liste des départements retenus, si la liste est vide on ne filtre pas.
    regions : list[str]
        liste des régions retenues, si la liste est vide on ne filtre pas.
    prix : str
        vaut "minimum" ou "maximum".
        
    Returns
    -------
    TableTrajets
        La table des trajets filtrée. La colonne du prix (min ou max) est renommée prix.
    """
    df=table[table.type == 'TGV']
    
    if transporteur != []:
        df = df[df.Transporteur.isin(transporteur)]
    if classe != []:
        df = df[df.Classe.isin(classe)] # Pb : numérique au lieu de str
    if profil_tarifaire !=[]:
        df = df[df.Profil_tarifaire.isin(profil_tarifaire)]
    if departements !=[]:
        df = df[df.dep_origine.isin(departements)]
        df = df[df.dep_destination.isin(departements)]        
    if regions !=[]:
        df = df[df.reg_origine.isin(regions)]
        df = df[df.reg_destination.isin(regions)]      
    
    if prix == 'minimum':
        df['prix']=df.Prix_minimum
    if prix == 'maximum':
        df['prix']=df.Prix_maximum
    
    res=pd.concat([df,table[table.type != 'TGV']])
    
    return res
            