from typing import Optional
from lxml import etree
from pybr import certs


class Certificado:
    certificado: Optional[certs.Certificado] = None

    def __init__(self, config):
        self.config = config
        self._senha = None
        self._pfx = None

    def reset(self):
        if self._pfx and self._senha:
            self.certificado = certs.Certificado(self._pfx, self.senha)
        else:
            self.certificado = None

    @property
    def pfx(self):
        return self._pfx

    @pfx.setter
    def pfx(self, value):
        self._pfx = value
        self.reset()

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, value):
        self._senha = value
        self.reset()

    @property
    def chave_publica(self):
        return self.certificado.arquivo_certificado

    @property
    def chave_privada(self):
        return self.certificado.arquivo_chave

    def assinar(self, xml, ref):
        import signxml
        signer = signxml.XMLSigner(
            method=signxml.methods.enveloped,
            signature_algorithm='rsa-sha1',
            digest_algorithm='sha1',
            c14n_algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
        )
        signer.namespaces = {None: signer.namespaces['ds']}
        uri = '#' + ref
        signed = signer.sign(
            xml, key=self.certificado.key, cert=self.certificado.cert, reference_uri=uri
        ).find(".//{http://www.w3.org/2000/09/xmldsig#}Signature")
        return etree.tostring(signed, encoding=str).replace('\n', '')


class Config:
    def __init__(self, dfe):
        self.dfe = dfe
        self.certificado = Certificado(self)
        self.diretorio = 'files'
        self.schemas = None
