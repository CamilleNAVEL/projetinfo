import heapq
import verifie_connexe as vc


def my_dijkstra(self,start,end=None):
    inf=float('inf')                    #on set une valeur infinie
    n_connus = {start:[0,[start]]}      #[longueur,plus court chemint], les noeuds déja parcourus
    accessibles = vc.rec_explorer(self,start)       #noeuds accessibles depuis start
    n_inconnus = {k:[inf,''] for k in accessibles if k != start } #{key: [distance,précédent]}, dico des noeuds accessibles
    #on boucle sur les voisins de start 
    for suivant in self.vertex[start]:
        n_inconnus[suivant] = [self.edges[(start,suivant)],start]   #on met la bonne distance et maj du précédent
    #on while tant que tous les noeuds ne sont pas visités et qu'il y a des valeurs finies dans les dist   
    while n_inconnus and any(n_inconnus[k][0]< inf for k in n_inconnus):
        u = min(n_inconnus,key=n_inconnus.get)      #sommet distance minimale à start
        longueur_u,precedent_u=n_inconnus[u]        #longueur u est la valeur du plus court chemin start->u
        for v in self.vertex[u]:
             if v in n_inconnus:
                d = longueur_u + self.edges[(u,v)]
                if d<n_inconnus[v][0]:
                    n_inconnus[v]=[d,u]
        n_connus[u]=[longueur_u,n_connus[precedent_u][1]+[u]]     #n_connus[precedent_u][1]+[u] on prend le chemin précédent (clé dico + 2iem elmt liste) et on rajoute u
        del n_inconnus[u]
    if end == None :
        return n_connus     #dictionnaire {key: [d(start,key),[chemin start-key]]} , ici d renvoie le prix
    return n_connus[end]    # liste [d(start,key),[chemin start-key]]
        
#Si on ne précise rien pour end, on a la le trajet à chaque noeuds
