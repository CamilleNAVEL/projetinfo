from tabletrajet import tabletrajet
from dijkstra_source_vers_destination import dijkstra_source_vers_destination
def dijkstra_source_vers_destination(self, origine):
    """
    Applique l’algo de Dijkstra de l’origine aux sommets du graphe.
    Arguments
    graphe : graphe
    le graphe des trajets.
    origine : str
    Code UIC de la gare d’origine.
    Renvoie
    Un dictionnaire qui à chaque sommet (str UIC) associe Parcours le moins cher.
    A modifier (algo v dest cc)
    """
    parcours = []
    # Contiendra le nom des sommets visités
    for destination in self:
        parcours += dijkstra_source_vers_destination(self, origine , destination)
    return parcours
