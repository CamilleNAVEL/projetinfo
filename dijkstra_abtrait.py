from abc import ABC, abstractmethod


class AbstractFunction(ABC):

    @abstractmethod
    def function_definition(self):
        """
        Renvoie un dataframe avec le trajet le moins cher (une ligne = 1 voyage) avec son prix
        """

