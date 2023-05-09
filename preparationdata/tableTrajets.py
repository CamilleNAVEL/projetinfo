import pandas as pd
from creation_tableTrajets import creation_tableTrajets

class TableTrajets:
    """Définit une table de trajets.*
    
    Parameters
    ----------
    
    type : str
        Vaut "TGV" ou "TER". Peut être génant par la suite...
        ...remplacer par ["TGV"],["TER"],ou["TGV","TER"]
    """
    
    def __init__(self,type='TGV'):
        if not (isinstance(type, str) or isinstance(type,list)):
            raise TypeError("'type' doit être une instance de str ou de liste.")
        if isinstance(type, str) and not type in ['TGV','TER']:
            raise ValueError("Le 'type' doit valoir 'TGV' ou 'TER' ou ['TGV','TER'].")
        if isinstance(type,list):
            for elt in type:
                if not type in ['TGV','TER']:
                    raise ValueError("Le 'type' doit valoir 'TGV' ou 'TER' ou ['TGV','TER'].")
        
        table = creation_tableTrajets()
        if type == 'TGV':
            self.table = table[table.type != 'TER']
        elif type == 'TER':
            self.table = table[table.type != 'TGV']

        
    def filtre_tgv(self, transporteur=[], classe=[], profil_tarifaire=[], departements=[],
                    regions=[], prix="minimum"):
        """Filtre la table TGV selon les critères choisis. La variable prix permet de choisir
        entre la colonne prix minimal et prix maximal.
        
        Parameters
        ----------
        transporteur : list[str]
            liste des transporteurs retenus, si la liste est vide on ne filtre pas.
        classe : list[str]
            liste des classes retenues, si la liste est vide on ne filtre pas.
        profil_tarifaire : list[str]
            liste des profils tarifaires retenus, si liste vide on ne filtre pas.
        departements : list[str]
            liste des départements retenus, si la liste est vide on ne filtre pas.
        regions : list[str]
            liste des régions retenues, si la liste est vide on ne filtre pas.
        prix : str
            vaut "minimum" ou "maximum".
            
        Returns
        -------
        TableTrajets
            La TableTrajets filtrée. La colonne du prix (min ou max) est renommée prix.
        """
        if self.type != 'TGV':
            raise ValueError("Le 'type' doit valoir 'TGV'.")
        
        res=self
        df=res.table
        
        if transporteur != []:
            df = df[df.Transporteur.isin(transporteur)]
        if classe != []:
            df = df[df.Classe.isin(classe)] # Pb : numérique au lieu de str
        if profil_tarifaire !=[]:
            df = df[df.Profil_tarifaire.isin(profil_tarifaire)]
        if departements !=[]:
            # A faire
            pass
        if regions !=[]:
            # A faire
            pass
        
        if prix == 'minimum':
            df['prix']=df.Prix_minimum
        if prix == 'maximum':
            df['prix']=df.Prix_maximum
        
        df = df.rename(columns = {"Gare_origine" : "origine",
                                  "Gare_origine_-_code_UIC" : "code_origine",
                                  "Destination" : "destination",
                                  "Gare_destination_-_code_UIC" : "code_destination"})
        
        df = df [["origine","code_origine","destination","code_destination","prix"]]
        res.table = df
        res.type = 'TGV'
        
        return res
                        
    def ajout_correspondances(self):
        """Ajoute les correspondances possibles à la table.
                            
        Returns
        -------
        TableTrajets
            La TableTrajets avec les correspondnaces.
        """
        
        
        res = self
        correspondances = tableCorrespondances
        
        # Filtre les correspodances pertinentes. Ne semble pas marcher...
        correspondances = correspondances.code_origine.isin(
            set(res.table.code_origine).union(set(res.table.code_destination)))
        correspondances = correspondances.code_destination.isin(
            set(res.table.code_origine).union(set(res.table.code_destination)))
        
        res.table = pd.concat([res.table,correspondances])
        
        return res