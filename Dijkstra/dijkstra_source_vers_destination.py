import heapq
def dijkstra_source_vers_destination(self, origine, destination):
    """Dans cette implémentation, la classe Graphe représente le graphe sous forme d'un dictionnaire adj, 
    où chaque clé est un sommet et chaque valeur est un dictionnaire des sommets adjacents et des poids des arêtes correspondantes. 
    La méthode ajouter_arete permet d'ajouter des arêtes au graphe.
    La méthode dijkstra_source_vers_destination utilise l'algorithme de Dijkstra pour calculer la distance la plus courte entre origine et destination. 
    Elle retourne la distance la plus courte entre ces deux sommets. Si destination n'est pas atteignable depuis origine, la fonction retourne float('inf').
    """
    # Initialisation des distances à l'infini, sauf pour le sommet de départ
    d = {s: float('inf') for s in self.adj}
    d[origine] = 0
        
    # Initialisation de la file de priorité avec le sommet de départ
    pq = [(0, origine)]
        
    while pq:
        # Extraction du sommet avec la plus petite distance estimée
        dist, u = heapq.heappop(pq)
            
        # Si on atteint la destination, on peut s'arrêter
        if u == destination:
         break
            
        # Mise à jour des distances pour tous les sommets accessibles depuis u
        for v, w_uv in self.adj[u].items():
            alt = dist + w_uv
            if alt < d[v]:
                d[v] = alt
                heapq.heappush(pq, (alt, v))
        
    return d[destination]

