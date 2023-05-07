import pytest
import re
from verifie_connexe import verif_connexe


@pytest.mark.parametrize(
    'params, erreur, message_erreur',
    [
        ({'destination': ['Paris']},
         TypeError, "'destination' doit être une instance de str."),
        ({'source': {'Laval'}},
         TypeError, "'source' doit être une instance de str."),
        ({'poids': 1+3j, 'mode': 'normal'},
         TypeError, "'poids' doit être une instance de int ou float."),
        ({'poids': -42},
         ValueError, "'poids' doit être strictement positif."),
        ({'mode': 'apide'},
         ValueError, "'mode' doit être 'normal' ou 'rapide'."),
        ({'format_lettre': 'A5'},
         ValueError, "'format_lettre' doit être 'A3' ou 'A4'."),
    ]
)
def test_init_lettre(params, erreur, message_erreur):
    dico = {'destination': 'Paris', 'source': 'Laval', 'poids': 42,
            'mode': 'normal', 'format_lettre': 'A4'}
    dico.update(**params)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Lettre(**dico)
