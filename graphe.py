class Graphe :
    """Définir la classe graphe
    
    Parameters
    ----------
    vertex : dict
        dictionnaire des noeuds du graphe et de leur voisins
    edge : dict
        dictionnaire des arcs du graphe
    """
    def __init__(self):
        self.vertex={}
        self.edges={}
    
    def add_vertex(self,node):
        """Ajoute un noeud dans la liste des noeuds du graphe

        Parameters
        ----------
        node : int
            noeud à rajouter dans le graphe, ici l'id d'une gare
        """
        if node not in self.vertex:
            self.vertex[node]=set()       
            #le noeud est ajouté en temps que clée et la valeur associée sera un set des noeuds adjacents 
    
    def add_edge(self,n_start,n_end,prix=1):
        """Ajoute un arc au graphe, les noeuds peuvent déja exister

        Parameters
        ----------
        n_start : int
            noeud de départ de l'arc, id d'une gare
        n_end : int
            noeud d'arrivée de l'arc, id d'une gare
        prix : float
            le prix du billet

        """
        self.add_vertex(n_start)
        self.add_vertex(n_end)
        self.vertex[n_start].add(n_end)       #c'est pas grave si e n'est pas dans la liste des noeuds de s
        self.edges[(n_start,n_end)]=prix      

