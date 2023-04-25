class Graphe :
    """Définir la classe graphe
    
    Parameters
    ----------
    parameter1 : type
        description
    """
    def __init__(self):
        self.vertex={}
        self.edges={}
    
    def add_vertex(self,s):
        if s not in self.vertex:
            self.vertex[s]=set()       #le noeud est ajouté en temps que clée et la valeur associée sera un set des noeuds adjacents 
    
    def add_edge(self,s,e,poid=1):
    # def add_edge(self,s,e,nom_tarif,poid=1):      si on met un dictionnaire pour séparer les tarifs
        self.add_vertex(s)
        self.add_vertex(e)
        self.vertex[s].add(e)       #c'est pas grave si s n'est pas dans la liste des noeuds de e
        self.edges[(s,e)]=poid      #au lieu de poids on pourrait 
        # if (s,e) in list(self.edges.keys()):
        #     self.edges[(s,e)][nom_tarif]=poid
        # else :
        #     self.edges[(s,e)]={}
        #     self.edges[(s,e)][nom_tarif]=poid


