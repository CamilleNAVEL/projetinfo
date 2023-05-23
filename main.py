import os
import pandas as pd
from preparationdata.creation_tableTrajets import creation_tableTrajets

from preparationdata.creation_tableTGV import creation_tableTGV
from preparationdata.creation_tableTER import creation_tableTER
from preparationdata.creation_tableCorrespondances import creation_tableCorrespondances
from preparationdata.creation_tableDep import creation_tableDep

from preparationdata.appurement_correspondances import appurement_correspondances
from preparationdata.filtre_type import filtre_type
from preparationdata.filtre_depreg import filtre_depreg
from preparationdata.filtre_tgv import filtre_tgv
from preparationdata.filtre_ter import filtre_ter

# On charge la table de tous les trajets
tableTrajets = creation_tableTrajets()

