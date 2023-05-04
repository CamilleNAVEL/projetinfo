
def rec_explorer(Graphe,node,visited=None):        
    """Fourni la liste des noeuds accessibles depuis un noeud
    
    Parameters
    ----------
    Graphe : Graphe
        une instance de la classe Graphe
    node : int
        code d'identification de la destination (noeud)
    visited : list
        liste de code d'identification (liste(noeuds))

    Return
    ----------
    list : 
        la liste des noeuds accessibles 
    """
    if visited is None:
        visited=[]
    if node not in visited:
        visited.append(node)
    
    unvisited=[n for n in Graphe.vertex[node] if n not in visited]  #on a accès aux noeuds voisins de node
    
    for node in unvisited:
        rec_explorer(Graphe,node,visited)    #on rentre dans le set des noeuds en récursif
    return visited

def verif_connexe(G):
    """Vérifie si un graphe est connexe
    Parameters
    ----------
    G : Graphe
        une instance de la classe Graphe
    
    Return
    ----------
    bool :
        True si G est connexe, False sinon
    """                   
    L=list(G.vertex.keys())             #liste des noeuds du graphe
    l=L[0]                              #le premier noeud
    return rec_explorer(G,l) == L       #il faut que les noeuds accessibles depuis un point du graphe soit égal à la liste de tous les noeuds du graphe
