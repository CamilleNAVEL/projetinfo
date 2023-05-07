
import pandas as pd
import graphe as grp

def creation_graphe(dataframe):
    """Converti un dataframe départ/arrivée/prix en Graphe
    
    Parameters
    ----------
    dataframe : dataframe
        un dataframe

    Returns
    ----------
    Graphe : 
        une instance de la classe Graphe  
    """
    G=grp.Graphe()
    dataframe.apply(lambda row: G.add_edge(row['origine_code'], row['destination_code'], row['Prix']), axis=1) 
    return G

def creation_graphe2(dataframe):
    """Converti un dataframe départ/arrivée/prix en Graphe,
    Les types de tarif sont pris en compte
    
    Parameters
    ----------
    dataframe : dataframe
        un dataframe

    Returns
    ----------
    Graphe : 
        une instance de la classe Graphe  
    """
    G=Graphe()
    dataframe.apply(lambda row: G.add_edge2(row['origine_code'], row['destination_code'],row['Type_tarif'], row['Prix']), axis=1) 
    return G

# dict2 = {'origine_code':[87751321,87751321,87751321],
#          'destination_code':[87751750,87751438,87751750],
#          'Type_tarif':['Tarif normal','Tarif normal','Tarif spécial'],
#          'Prix':[21.8,15.2,50.4]}

# df2=pd.DataFrame(dict2)
# G=creation_graphe(df2)
# G.edges
# G.vertex
# G=creation_graphe2(df2)