import pandas as pd
import numpy as np

def dijkstra_source_vers_destination(graphe, origine, destination):
    # Initialisation
    noeuds = np.unique(list(np.concatenate([graphe['origine'], graphe['destination']]).flat))
    distances = {noeud: np.inf for noeud in noeuds}
    distances[origine] = 0
    predecesseurs = {noeud: origine for noeud in noeuds}
    visite = set()

    # Algorithme de Dijkstra
    while visite != set(noeuds):
        # Sélectionner le nœud avec la distance minimale non visitée
        noeud_courant = min(
            set(distances.keys()) - visite, key=lambda x: distances[x]
        )
        visite.add(noeud_courant)

        # Mettre à jour les distances des nœuds voisins
        voisins = graphe[
            (graphe['origine'] == noeud_courant) | (graphe['destination'] == noeud_courant)
        ]
        for _, voisin in voisins.iterrows():
            if voisin['origine'] == noeud_courant:
                noeud_voisin = voisin['destination']
            else:
                noeud_voisin = voisin['origine']

            if noeud_voisin not in visite:
                nouveau_prix = distances[noeud_courant] + voisin['prix']
                if nouveau_prix < distances[noeud_voisin]:
                    predecesseurs[noeud_voisin] = noeud_courant  # Mettre à jour le prédécesseur
                    distances[noeud_voisin] = nouveau_prix  # Mettre à jour la distance

    # Récupérer le chemin optimal de destination vers l'origine
    chemin_optimal = []
    noeud_actuel = destination
    while noeud_actuel != origine:
        chemin_optimal.insert(0, noeud_actuel)
        noeud_actuel = predecesseurs[noeud_actuel]
    chemin_optimal.insert(0, origine)

    # Résultats
    print("Prix minimal")
    print(distances[destination],'\u20AC' )
    
    print("\nChemin optimal :")
    print(" -> ".join(chemin_optimal))
    print("\n\n")

