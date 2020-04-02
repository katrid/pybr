import os
from datetime import datetime
from lxml import etree

from pybr.dfe.leiaute import Grupo
from pybr.dfe import consts
from pybr.dfe.config import Config
from pybr.dfe.services import Service


class DFe:
    Config = Config
    namespace = ''
    versao = 4.00
    cUF: str
    tpAmb = consts.TipoAmbiente.HOMOLOGACAO
    # CLASSES
    documentos = None
    Documento = None
    Status: Service
    recepcao: Service
    infTag: str = None

    def __init__(self, *args, **kwargs):
        self.config = self.Config(self)
        self._status = None
        self._uf = None
        if self.Documento:
            self.documentos = Documentos(self.Documento)

        if 'uf' in kwargs:
            self.uf = kwargs['uf']
        if 'certificado' in kwargs:
            self.config.certificado.pfx = kwargs['certificado']
            self.config.certificado.senha = kwargs['senha']

        for arg in args:
            self.documentos.add(arg)

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, value):
        self._uf = value
        self.cUF = consts.CODIGO_UF.get(value, '')

    def gerar_id(self, cUF, dhEmi, CNPJ, mod, serie, numero, tpEmis, codigo):
        def dv(ch):
            r = 0
            m = 2
            for c in ch[::-1]:
                r += int(c) * m
                if m == 9:
                    m = 1
                m += 1
            r = r % 11
            return 11 - r

        chave = '%s%s%s%s%s%s%s%s' % (
            cUF, dhEmi.strftime('%y%m'), CNPJ, mod, str(serie).zfill(3), str(numero).zfill(8), tpEmis,
            str(codigo).zfill(9),
        )
        chave += str(dv(chave))[-1]
        assert len(chave) == 44
        return chave

    def gerar_chave(self, cUF, dhEmi, CNPJ, mod, serie, numero, tpEmis, codigo):
        return self.__class__.__name__ + self.gerar_id(cUF, dhEmi, CNPJ, mod, serie, numero, tpEmis, codigo)

    def assinar(self, root, elemento, doc):
        doc = doc.find(elemento.campo)
        signed = self.config.certificado.assinar(doc, elemento.Id)
        doc.getparent().append(etree.fromstring(signed))
        root.signature = signed

    def assinado(self, grupo: Grupo) -> bool:
        return grupo.Signature is not None

    def ler_arquivo(self, arquivo_xml):
        assert os.path.isfile(arquivo_xml), 'Arquivo não encontrado "%s"' % arquivo_xml
        with open(arquivo_xml, 'rb') as f:
            self.documentos.add()._read_xml(etree.fromstring(f.read()))

    def enviar(self, lote: int=None):
        """Enviar todos os documentos para processamento."""
        self.recepcao.clear()
        envi = self.recepcao.xml
        res = []
        if self.documentos:
            tag = getattr(envi, self.documentos[0].campo, None)
            # validar a tag de recepção
            assert tag is not None, 'Nenhuma informada para o tipo de serviço recepção'

            for doc in self.documentos:

                # gerar chave antes de prosseguir
                doc._preparar(self)

                xml = doc._to_xml()
                self.assinar(doc, doc, xml)
                tag.append(doc)
                print(etree.tostring(xml))
                res.append(xml)
            envi.idLote = lote
        self.recepcao.executar()
        return res


class Documentos(list):
    def __init__(self, documento):
        super().__init__()
        self.documento = documento

    def add(self, obj: dict=None):
        doc = self.documento()
        if obj:
            doc._load(obj)
        self.append(doc)
        return doc
