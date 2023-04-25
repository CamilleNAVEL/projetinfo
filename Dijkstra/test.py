from dijkstra_source_vers_destination import dijkstra_source_vers_destination

graphe = [np.array([[0, 50, 100],[50, 0, 30]], [100,30,0]),{"Paris":"Paris" ,"Lyon" :"Lyon","Marseille":"Marseille"}]

dijkstra_source_vers_destination(graphe,"Paris","Marseille")
#ça marche pas