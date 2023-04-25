from math import inf
def dijkstra_source_vers_destination(self, origine, destination):
    """
    Applique l’algo de Dijkstra pour relier à moindre coût origine à destination.
    Arguments
    graphe : Graphe
    le graphe des trajets.
    origine : str
    Code UIC de la gare d’origine.
    Destination : str
    code UIC de la gare de destination.
    Renvoie
    Un parcours (cf classe parcours).
    """
    parcours = []  # Contiendra le nom des sommets visités
 
    # Distance minimale trouvée pour chaque valeur dès le départ
    distances = {sommet: (None, inf) for sommet in self}
    #     Sommet d'origine (None par défaut), distance
 
    distances[origine] = 0  # On initialise la distance du départ
 
    # Nombre de sommets du graphe, longueur du dictionnaire
    taille_graph = len(self)
 
    selection = origine
    coefficient = 0
 
    while len(parcours) < taille_graph:
        # On marque la 'selection'
        parcours.append(selection)
        # On parcours les voisins de 'selection'
        for voisin in self[selection]:
            # voisin est le couple (sommet, poids de l'arête)
            sommet = voisin[0]  # Le sommet qu'on, parcours
            poids = voisin[1]  # Le poids de selection au sommet
            # voir ici comment on accède aux données du graphe
            if sommet not in parcours:
                # Pour chaque voisin non marqué,
                # on compare coefficient + arête
                # avec la distance du dictionnaire
                d = distances[sommet][1]
                if coefficient + poids < d:
                    # Si c'est plus petit, on remplace
                    distances[sommet] = (selection, coefficient + poids)
        # On recherche le minimum parmi les non marqués
        selection = None
        minimum = inf
        for sommet in self:
            if sommet not in parcours and distances[sommet][1] < minimum[1]:
                selection = sommet
                minimum = distances[sommet][1]
 
        # puis il devient notre nouvelle 'selection' 
    sommet = destination
    parcours += [destination]
    longueur = distances[destination][1]
    # On parcours le graphe à l'envers pour obtenir le chemin
    while sommet != origine:
        sommet = distances[sommet][0]
        parcours.append(sommet)
    parcours.reverse()
    # On renvoie le chemin le plus court
    return parcours
