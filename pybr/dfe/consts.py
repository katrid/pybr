from pybr.consts import UF, CODIGO_UF
from enum import Enum


class TipoEmissao(Enum):
    Normal = 0
    Contingencia = 1
    SCAN = 2
    DPEC = 3
    FSDA = 4
    SVCAN = 5
    SVCRS = 6
    SVCSP = 7
    OffLine = 8


class TagAssinatura(Enum):
    Sempre = 0
    Nunca = 1
    SomenteSeAssinada = 2
    SomenteParaNaoAssinada = 3


class TipoAmbiente:
    PRODUCAO = 1
    HOMOLOGACAO = 2


AMBIENTE = (
    ('1', 'Produção'),
    ('2', 'Homologação'),
)


XML_ENCODING = '<?xml version="1.0" encoding="utf-8"?>'
XML_ENCODING_STD = '<?xml version="1.0" encoding="utf-8" standalone="no"?>'
