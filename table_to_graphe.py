
import pandas as pd
import graphe as grp

def creation_graphe(dataframe):
    """Converti un dataframe départ/arrivée/prix en Graphe
    
    Parameters
    ----------
    dataframe : dataframe
        un dataframe

    Return
    ----------
    Graphe : 
        une instance de la classe Graphe  
    """
    G=grp.Graphe()
    dataframe.apply(lambda row: G.add_edge(row['origine_code'], row['destination_code'], row['Prix']), axis=1) 
    return G
