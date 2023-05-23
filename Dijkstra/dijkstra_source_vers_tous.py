import heapq

def dijkstra_vers_tous(self, origine):
    """
    Dans cet algorithme, G représente le graphe sous forme d'un dictionnaire où chaque clé est un sommet et chaque valeur est un dictionnaire des sommets adjacents
     et des poids des arêtes correspondantes. sdeb est le sommet de départ. La fonction retourne un dictionnaire d des distances les plus courtes de sdeb à chaque sommet
    sdans G.
    """
    # Initialisation des distances à l'infini, sauf pour le sommet de départ
    d = {s: float('inf') for s in self}
    d[origine] = 0
    
    # Initialisation de la file de priorité avec le sommet de départ
    pq = [(0, origine)]
    
    while pq:
        # Extraction du sommet avec la plus petite distance estimée
        dist, u = heapq.heappop(pq)
        
        # Mise à jour des distances pour tous les sommets accessibles depuis u
        for v, w_uv in G[u].items():
            alt = dist + w_uv
            if alt < d[v]:
                d[v] = alt
                heapq.heappush(pq, (alt, v))
    
    return d
