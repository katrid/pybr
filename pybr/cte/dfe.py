from typing import List
from pybr.dfe.base import DFe, Documentos
from . import services
from . import leiaute
from . import settings as cte_settings


class CTe(DFe):
    versao = 3.00
    namespace = 'http://www.portalfiscal.inf.br/cte'
    settings = cte_settings
    Documento = leiaute.CTe
    documentos: List[leiaute.CTe]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status = services.Status(self)
        self.recepcao = services.Recepcao(self)
        # self.consulta = services.Consulta(self)
        # self.retorno = services.RetRecepcao(self)
        # self.consulta = services.Consulta(self)
        # self.consulta_nao_enc = services.ConsultaNaoEnc(self)
        # self.evento = services.Evento(self)
        # self.ret_recepcao = self.RetRecepecao(self)

    def assinar(self, root, elemento, doc):
        return super().assinar(root, elemento.infCte, doc)
