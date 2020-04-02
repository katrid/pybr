import os
from unittest import TestCase
from lxml import etree
from pybr.cte import leiaute
from pybr.cte.dfe import CTe
from pybr.dfe.consts import TipoAmbiente


class CTeTestCase(TestCase):
    def test_ler_cte(self):
        cte = leiaute.CTe()
        arq = os.environ['TEST_CTE_FILE']
        assert os.path.isfile(arq)
        with open(arq, 'rb') as f:
            xml = etree.fromstring(f.read())
        # cte._read_xml(xml.find('{http://www.portalfiscal.inf.br/cte}CTe'))
        cte._read_xml(xml)
        obj = dict(cte)
        self.assertIn('infCte', obj)
        self.assertIn('ide', obj['infCte'])
        xml = cte._to_xml()
        with open('files/out-cte.xml', 'wb') as f:
            f.write(etree.tostring(xml, encoding='utf-8', xml_declaration=True))
        print(etree.tostring(xml, encoding='utf-8', xml_declaration=True))

    def test_status(self):
        cte = CTe()
        cte.tpAmb = TipoAmbiente.HOMOLOGACAO
        cte.uf = 'BA'
        cte.config.certificado.pfx = os.environ['TEST_CERTIFICADO']
        cte.config.certificado.senha = os.environ['TEST_CERTIFICADO_SENHA']
        cte.status.executar()
        self.assertEqual(cte.status.retorno.cStat, 107)
        self.assertEqual(cte.status.retorno.tpAmb, TipoAmbiente.HOMOLOGACAO)

