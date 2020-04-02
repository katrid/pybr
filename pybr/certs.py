import os
from datetime import datetime
from OpenSSL import crypto


class Certificado(object):
    _loaded = False
    _pkcs12 = None
    _cert = None
    _key = None

    def __init__(self, pfx: str, senha: str):
        self.pfx = pfx
        self.senha = senha

    def load(self):
        self._arquivo_certificado, self._arquivo_chave = self.get_certificado(self.pfx, self.senha)
        certificate = crypto.load_certificate(crypto.FILETYPE_PEM, self.certificado)
        # Obter informações do certificado
        self._emissor = dict(certificate.get_issuer().get_components())
        self._proprietario = dict(certificate.get_subject().get_components())
        self._emissao = datetime.strptime(certificate.get_notBefore().decode('utf-8'), '%Y%m%d%H%M%SZ')
        self._validade = datetime.strptime(certificate.get_notAfter().decode('utf-8'), '%Y%m%d%H%M%SZ')

    @property
    def arquivo_certificado(self):
        self.load()
        return self._arquivo_certificado

    @property
    def arquivo_chave(self):
        self.load()
        return self._arquivo_chave

    @property
    def emissor(self):
        self.load()
        return self._emissor

    @property
    def proprietario(self):
        self.load()
        return self._proprietario

    @property
    def emissao(self):
        self.load()
        return self._emissao

    @property
    def validade(self):
        self.load()
        return self._validade

    @property
    def pkcs12(self):
        with open(self.pfx, 'rb') as f:
            self._pkcs12 = crypto.load_pkcs12(f.read(), self.senha.encode('utf-8'))
        return self._pkcs12

    @property
    def cert(self):
        if self._cert is None:
            self._cert, self._key = self._get_cert()
        return self._cert

    @property
    def key(self):
        if self._key is None:
            self._cert, self._key = self._get_cert()
        return self._key

    def _get_cert(self):
        p = self.pkcs12
        self.privatekey = p.get_privatekey()
        pkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, self.privatekey)
        cert = crypto.dump_certificate(crypto.FILETYPE_PEM, p.get_certificate())
        return cert, pkey

    def split_cert(self, pfx, pwd, cert_file, key_file):
        cert, pkey = self._get_cert()
        with open(key_file, 'wb') as pem_key:
            pem_key.write(pkey)
        with open(cert_file, 'wb') as crt_file:
            crt_file.write(cert)
        return cert, pkey

    def get_certificado(self, cert, pwd):
        cert_file = cert + '.cert'
        key_file = cert + '.key'
        self.certificado, self.chave = self.split_cert(cert, pwd, cert_file, key_file)
        return cert_file, key_file
