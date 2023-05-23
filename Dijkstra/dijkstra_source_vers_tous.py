import pandas as pd
import numpy as np
from dijkstra_source_vers_destination import dijkstra_source_vers_destination


def dijkstra_source_vers_tous(self, origine):

    for destinations in np.unique(self.destination):

        print("\nChemin optimal vers" ,destinations)
        dijkstra_source_vers_destination(self,origine,destination= destinations)
