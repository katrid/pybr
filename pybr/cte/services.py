from pybr import dfe
from .leiaute import consStatServCte, retConsStatServCte, enviCTe, retEnviCte


class Header(dfe.Header):
    soapVersion = 'soap12'
    versaoDados = '3.00'
    element = 'cteCabecMsg'


class Body(dfe.Body):
    soapVersion = 'soap12'
    element = 'cteDadosMsg'


class WebService(dfe.services.Service):
    header = Header
    body = Body

    def preparar(self):
        super().preparar()
        self.xml.versao = '%2.2f' % self.dfe.versao
        self.xml.tpAmb = self.dfe.tpAmb


class Status(WebService):
    webservice = 'CteStatusServico'
    method = 'cteStatusServicoCT'
    xml = consStatServCte
    Retorno = retConsStatServCte
    ret: retConsStatServCte

    def preparar(self):
        super().preparar()
        self.xml.xServ = 'STATUS'


class Recepcao(WebService):
    webservice = 'CteRecepcao'
    method = 'cteRecepcaoLote'
    xml = enviCTe
    Retorno = retEnviCte
    ret: retEnviCte
