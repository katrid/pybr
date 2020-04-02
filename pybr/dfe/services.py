import os
import datetime
import requests
from lxml import etree
from pybr.utils.xml_utils import tag
from pybr.dfe.leiaute import Grupo, TipoGrupo


class Header:
    soapVersion: str = None
    element: str = None
    xmlns: str = None
    cUF: str = None
    versaoDados: str = None

    def __str__(self):
        v = str(self.soapVersion) + ':' if self.soapVersion else ''
        kwargs = {}
        if self.xmlns:
            kwargs['xmlns'] = self.xmlns
        return tag(
            v + 'Header',
            tag(
                self.element,
                tag('cUF', self.cUF),
                tag('versaoDados', self.versaoDados),
                **kwargs
            ),
        )


class Body:
    soapVersion: str = None
    xmlns: str = None
    element: str = None
    xml: str = None

    def __str__(self):
        v = str(self.soapVersion) + ':' if self.soapVersion else ''
        kwargs = {}
        if self.xmlns:
            kwargs['xmlns'] = self.xmlns
        return tag(
            v + 'Body',
            tag(
                self.element,
                self.xml,
                **kwargs
            ),
        )


class Service:
    header: Header
    body: Body
    webservice: str
    method: str
    contentType = 'application/soap+xml; charset=utf-8;'
    xml = None
    xmlattrs = 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"'
    _xmlresp: etree.Element
    response: requests.Response
    Retorno: TipoGrupo
    retorno: Grupo

    def __init__(self, dfe):
        self.dfe = dfe
        self.config = dfe.config
        if self.header:
            self.header = self.header()
            self.header.xmlns = self.xmlns
        if self.body:
            self.body = self.body()
            self.body.xmlns = self.xmlns
        self.clear()

    def clear(self):
        """Limpar o elemento para que um novo envio seja realizado."""
        self.criar_xml()

    def criar_xml(self):
        """Criar um novo elemento xml"""
        if self.__class__.xml:
            self.xml = self.__class__.xml()

    @property
    def url(self):
        assert self.dfe.cUF, 'Nenhuma UF informada'
        return self.dfe.settings.services[self.dfe.versao][self.dfe.uf][self.dfe.tpAmb][self.webservice]

    def envelope(self):
        self.preparar()
        s = ''
        if self.header:
            s += str(self.header)
        xml = self.xml._to_xml()
        xml.attrib['xmlns'] = self.dfe.namespace
        self.body.xml = etree.tostring(xml).decode('utf-8')
        s += str(self.body)
        t = self.body.soapVersion + ':Envelope'
        return f'<?xml version="1.0" encoding="UTF-8"?><{t} {self.xmlattrs}>{s}</{t}>'.encode('utf-8')

    def executar(self):
        envelope = self.envelope()
        self.enviar(envelope)
        self.finalizar()
        return self.response.status_code == 200

    def preparar(self):
        if self.header:
            self.header.cUF = self.dfe.cUF
        self.xml.prepare(self.dfe)

    def finalizar(self):
        if self.response.status_code == 200:
            self._xmlresp = etree.fromstring(self.response.content)
            ret = self.Retorno()
            xml = self.find(ret.campo)
            ret._read_xml(xml)
            self.retorno = ret

    def enviar(self, data):
        # salvar arquivo antes de prosseguir
        if self.dfe.config.diretorio:
            with open(os.path.join(self.dfe.config.diretorio, self.filename('env')), 'wb') as f:
                f.write(data)
        res = self._enviar(data)
        # salvar o arquivo de retorno
        if self.dfe.config.diretorio:
            with open(os.path.join(self.dfe.config.diretorio, self.filename('ret')), 'wb') as f:
                f.write(res.content)
        self.response = res

    def _enviar(self, data):
        return requests.post(
            self.url, data, verify=False,
            cert=(self.config.certificado.chave_publica, self.config.certificado.chave_privada),
            headers=self.headers,
        )

    @property
    def wsdl(self):
        return self.dfe.namespace + '/wsdl'

    @property
    def xmlns(self):
        return '%s/%s' % (self.wsdl, self.webservice)

    @property
    def soapwsdl(self):
        return '%s/%s/%s' % (self.wsdl, self.webservice, self.method)

    @property
    def headers(self):
        return {
            'SOAPAction': '"%s"' % self.soapwsdl,
            'Content-Type': self.contentType,
        }

    @property
    def versao(self):
        return self.dfe.versao

    def filename(self, suffix=None):
        if suffix:
            suffix += '-'
        else:
            suffix = ''
        return '%s-%s%s.xml' % (datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'), suffix, self.method.lower())

    def find(self, tag, xml=None):
        if xml is None:
            xml = self._xmlresp
        return xml.find('.//{%s}%s' % (self.dfe.namespace, tag))

