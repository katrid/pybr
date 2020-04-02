from pybr.dfe.consts import UF
from pybr.dfe.consts import TipoAmbiente


CTE_RS_3 = {
    TipoAmbiente.PRODUCAO: {
        "RecepcaoEvento": "https://cte.svrs.rs.gov.br/ws/cterecepcaoevento/CTeRecepcaoEvento.asmx",
        "CteRecepcao": "https://cte.svrs.rs.gov.br/ws/cterecepcao/CTeRecepcao.asmx",
        "CTeRetRecepcao": "https://cte.svrs.rs.gov.br/ws/cteretrecepcao/CTeRetRecepcao.asmx",
        "CTeInutilizacao": "https://cte.svrs.rs.gov.br/ws/cteinutilizacao/cteinutilizacao.asmx",
        "CTeConsultaProtocolo": "https://cte.svrs.rs.gov.br/ws/cteconsulta/CTeConsulta.asmx",
        "CteStatusServico": "https://cte.svrs.rs.gov.br/ws/ctestatusservico/CTeStatusServico.asmx",
        "CTeConsultaCadastro": "https://cad.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
        "CTeRecepcaoOS": "https://cte.svrs.rs.gov.br/ws/cterecepcaoos/cterecepcaoos.asmx",
        "CTeRecepcaoSinc": "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoSinc/CTeRecepcaosinc.asmx",
        "URL-QRCode": "https://dfe-portal.svrs.rs.gov.br/cte/qrCode",
        "URL-ConsultaCTe": "https://dfe-portal.svrs.rs.gov.br/CTE/Consulta",
    },
    TipoAmbiente.HOMOLOGACAO: {
        "RecepcaoEvento": "https://cte-homologacao.svrs.rs.gov.br/ws/cterecepcaoevento/CTeRecepcaoEvento.asmx",
        "CteRecepcao": "https://cte-homologacao.svrs.rs.gov.br/ws/cterecepcao/CTeRecepcao.asmx",
        "CTeRetRecepcao": "https://cte-homologacao.svrs.rs.gov.br/ws/cteretrecepcao/CTeRetRecepcao.asmx",
        "CTeInutilizacao": "https://cte-homologacao.svrs.rs.gov.br/ws/cteinutilizacao/cteinutilizacao.asmx",
        "CTeConsultaProtocolo": "https://cte-homologacao.svrs.rs.gov.br/ws/cteconsulta/CTeConsulta.asmx",
        "CteStatusServico": "https://cte-homologacao.svrs.rs.gov.br/ws/ctestatusservico/CTeStatusServico.asmx",
        "CTeConsultaCadastro": "https://cad-homologacao.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
        "CTeRecepcaoOS": "https://cte-homologacao.svrs.rs.gov.br/ws/cterecepcaoos/cterecepcaoos.asmx",
        "CTeRecepcaoSinc": "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoSinc/CTeRecepcaosinc.asmx",
        "URL-QRCode": "https://dfe-portal.svrs.rs.gov.br/cte/qrCode",
        "URL-ConsultaCTe": "https://dfe-portal.svrs.rs.gov.br/CTE/Consulta",
    },
}


services = {
    3.00: {
        uf: CTE_RS_3
        for uf in UF.values()
    }
}

services[3.00]['BA'][TipoAmbiente.PRODUCAO].update({
    "CTeConsultaCadastro": "https://nfe.sefaz.ba.gov.br/webservices/nfenw/CadConsultaCadastro2.asmx",
})

services[3.00]['BA'][TipoAmbiente.HOMOLOGACAO].update({
    "CTeConsultaCadastro": "https://hnfe.sefaz.ba.gov.br/webservices/nfenw/CadConsultaCadastro2.asmx",
})
