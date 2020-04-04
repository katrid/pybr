from datetime import datetime
from pybr.dfe.leiaute import G, A, E, CG, CE, Grupo, Signature, CampoCNPJ, CampoCPF, Xml


# EXPRESSÕES REGULARES
ER1 = r"""(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))- (29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))"""
ER2 = r"""[0-9]{2}"""
ER3 = r"""[0-9]{7}"""
ER4 = r"""[0-9]{44}"""
ER5 = r"""[0-9]{14}"""
ER6 = r"""[0-9]{6,14}"""
ER7 = r"""[0-9]{3,14}"""
ER8 = r"""[0-9]{0}|[0-9]{14}"""
ER9 = r"""[0-9]{11}"""
ER10 = r"""[0-9]{3,11}"""
ER11 = r"""(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))"""
ER12 = r"""0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?"""
ER13 = r"""0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,2}(\.[0-9]{3})?"""
ER14 = r"""[0-9]{1,3}(\.[0-9]{2,3})?"""
ER15 = r"""0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?"""
ER16 = r"""0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{3})?"""
ER17 = r"""0\.[1-9]{1}[0-9]{2}|0\.[0-9]{2}[1-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,7}(\.[0-9]{3})?"""
ER18 = r"""0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?"""
ER19 = r"""0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?"""
ER20 = r"""0\.[1-9]{1}[0-9]{5}|0\.[0-9]{1}[1-9]{1}[0-9]{4}|0\.[0-9]{2}[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}[0-9]{2}|0\.[0-9]{4}[1-9]{1}[0-9]{1}|0\.[0-9]{5}[1-9]{1}|[1-9]{1}[0- 9]{0,8}(\.[0-9]{6})?"""
ER21 = r"""0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?"""
ER22 = r"""0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?"""
ER23 = r"""0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?"""
ER24 = r"""0\.[1-9]{1}[0-9]{2}|0\.[0-9]{2}[1-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?"""
ER25 = r"""0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?"""
ER26 = r"""0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?"""
ER27 = r"""0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?"""
ER28 = r"""0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?"""
ER29 = r"""[0-9]{2,14}"""
ER30 = r"""[0-9]{0,14}|ISENTO"""
ER31 = r"""[0-9]{1,4}"""
ER32 = r"""[1-9]{1}[0-9]{0,8}"""
ER33 = r"""[0-9]{15}"""
ER34 = r"""0|[1-9]{1}[0-9]{0,2}"""
ER35 = r"""[0-9]{3}"""
ER36 = r"""[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}"""
ER37 = r"""[0-9]\.[0-9]{6}|[1-8][0-9]\.[0-9]{6}|90\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-8][0-9]\.[0-9]{6}|-90\.[0-9]{6}"""
ER38 = r"""[0-9]\.[0-9]{6}|[1-9][0-9]\.[0-9]{6}|1[0-7][0-9]\.[0-9]{6}|180\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-9][0-9]\.[0-9]{6}|-1[0-7][0-9]\.[0-9]{6}|-180\.[0-9]{6}"""
ER39 = r"""(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"""
ER40 = r"""[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}|[A-Z0-9]{7}"""
ER41 = r"""[0-9]{8}"""
ER42 = r"""[0-9]{1}"""
ER43 = r"""[0-9]{8,9}"""
ER44 = r"""[1-9]{1}[0-9]{1,8}"""
ER45 = r"""3\.(0[0-9]|[1-9][0-9])"""
ER46 = r"""[A-Z0-9]+"""
ER47 = r"""[0-9]{1,6}"""
ER48 = r"""CTe[0-9]{44}"""
ER49 = r"""((HTTPS?|https?)://.*\?chCTe=[0-9]{44}&tpAmb=[1-2](&sign=[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})?)"""
ER50 = r"""[0-9]{7,12}"""
ER51 = r"""[123567][0-9]([0-9][1-9]|[1-9][0-9])"""
ER52 = r"""[^@]+@[^\.]+\..+"""
ER53 = r"""[0-9]{1,15}"""
ER54 = r"""[0-9]{8}|ISENTO"""
ER55 = r"""[0-9]{12}"""
ER56 = r"""(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])"""
ER57 = r"""3\.00"""
ER58 = r"""[1-9]{1}[0-9]{0,5}"""
ER59 = r"""[0-9]{9}"""
ER60 = r"""M"""
ER61 = r"""[0-9]{4}|ND"""
ER62 = r"""[1-9]{1}[0-9]{0,9}"""
ER63 = r"""[0-9]{25}"""
ER64 = r"""((HTTPS?|https?)://.*\?chCTe=[0-9]{44}&tpAmb=[1-2](&sign=[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})?)"""

# DOMINIOS
D1 = ('1', '2')
D2 = ('11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53')
D3 = ('11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '90', '91')
D4 = '67'
D5 = ('57', '67')
D6 = '57'
D7 = ('1', '04')
D8 = ('1', '2', '3', '4', '5', '6', '7')
D9 = ('1', '2', '3', '4')
D10 = ('AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'EX')
D11 = ('AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO')
D12 = ('1', '4', '5', '7', '8')
D13 = '1'
D14 = ('0', '1', '2', '3', '4')
D15 = ('0', '1')
D16 = ('1', '2', '9')
D17 = ('0', '1', '2', '3')
D18 = '4'
D19 = '0'
D20 = ('1', '2', '3')
D21 = ('00', '01', '02', '03', '04', '05')
D22 = ('00', '10', '59', '65', '99')
D23 = ('1', '5', '7', '8')
D24 = ('6', '7', '8')
D25 = ('4', '5')
D26 = '0'
D27 = '20'
D28 = ('40', '41', '51')
D29 = '60'
D30 = '90'
D31 = ('101', '102', '103', '104', '105', '106', '107', '108', '201', '302', '303', '304', '305', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '501', '502', '503', '504', '505', '506', '507', '508', '509', '601', '602', '603', '604', '605', '701', '702', '703', '704', '705', '706', '707', '708', '709', '710', '711', '712', '713', '716', '717', '718', '719', '720', '721', '722', '801', '802', '901', '902', '903', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '100 8', '1009', '1010', '1101', '1102', '1103', '1104', '1201', '1202', '1203', '1204', '1205', '1206', '1207', '1208', '1209', '1210', '1211', '1212', '1213', '1214', '1215', '1216', '1217', '1302', '1303', '1304', '1305', '1401', '1402', '1403', '1404', '1405', '1406', '1407', '1408', '1409', '1410', '1411', '1412', '1413', '1501', '1502', '1503', '1504', '1505', '1506', '1 507', '1508', '1509', '1510', '1511', '1512', '1513', '1514', '1515', '1516', '1517', '1518', '1601', '1701', '1702', '1703', '1704', '1705', '1706', '1708', '1709', '1710', '1711', '171 2', '1713', '1714', '1715', '1716', '1717', '1718', '1719', '1720', '1721', '1722', '1723', '1724', '1801', '1901', '2001', '2002', '2003', '2101', '2201', '2301', '2401', '2501', '2502', '2503', '2504', '2601', '2701', '2801', '2901', '3001', '3101', '3201', '3301', '3401', '3501', '3601', '3701', '3801', '3901', '4001')
D32 = ('07', '08', '09', '10', '11', '12', '13')
D33 = ('01', '1B', '02', '2D', '2E', '04', '06', '07', '08', '8B', '09', '10', '11', '13', '14', '15', '16', '17', '18', '20', '21', '22', '23', '24', '25', '26', '27', '28', '55')
D34 = ('01', '02', '03', '04')
D35 = ('01', '02', '03', '04', '05', '06')
D36 = ('0', '3')
D37 = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '99')
D38 = ('1', '2', '3', '4', '5')
D39 = ('N', 'S', 'L', 'O')
D40 = ('0', '1', '2')




## Dados do modal

class rodo(G(ref=1, nivel=0, descricao='Informações do modal Rodoviário', ocorrencias=(1, 1))):
    RNTRC: str = E(
        ref=2, nivel=1, descricao='Registro Nacional de Transportadores Rodoviários de Carga', tipo='C',
        ocorrencias=(1, 1), tam=8, regex=ER54,
        obs='Registro obrigatório do emitente do CT-e junto à ANTT para exercer a atividade de transportador rodoviário de cargas por conta de terceiros e mediante remuneração.'
    )

    class occ(G(ref=3, nivel=1, descricao='Ordens de Coleta associados', ocorrencias=(0, 10))):
        serie: str = E(ref=4, nivel=2, descricao='Série da OCC', tipo='C', ocorrencias=(0, 1), tam=(1, 3), regex=ER36)
        nOcc: str = E(ref=5, nivel=2, descricao='Número da Ordem de coleta', tipo='N', ocorrencias=(1, 1), tam=(1, 6), regex=ER58)
        dEmi: str = E(
            ref=6, nivel=2, descricao='Data de emissão da ordem de coleta', tipo='D', ocorrencias=(1, 1),
            tam=10, regex=ER11, obs='Formato AAAA-MM-DD',
        )

        class emiOcc(G(ref=7, nivel=2, descricao='', ocorrencias=(1, 1))):
            CNPJ: str = CampoCNPJ(
                ref=8, nivel=3, descricao='Número do CNPJ', tipo='C', ocorrencias=(1, 1), tam=14, regex=ER5,
                obs='Informar os zeros não significativos.',
            )
            cInt: str = E(
                ref=9, nivel=3, descricao='Código interno de uso da transportadora', tipo='C',
                ocorrencias=(0, 1), tam=(1, 10), regex=ER36,
                obs='Uso interno das transportadoras.'
            )
            IE: str = E(ref=10, nivel=3, descricao='Inscrição Estadual', tipo='C', ocorrencias=(1, 1), tam=14, regex=ER29, prep_regex=r'\d+')
            UF: str = E(
                ref=11, nivel=3, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10,
                obs='Informar EX para operações com o exterior.'
            )
            fone: str = E(ref=12, nivel=3, descricao='Telefone', tipo='C', ocorrencias=(0, 1), tam=(6, 14), regex=ER6, prep_regex=r'\d+')



class ferrov(G(ref=1, nivel=0, descricao='Informações do modal Ferroviário', ocorrencias=(1, 1))):
    tpTraf: str = E(
        ref=2, nivel=1, descricao='Tipo de Tráfego', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D17,
        obs='Preencher com: 0-Próprio; Mútuo; Rodoferroviário; 3-Rodoviário.'
    )

    class trafMut(
        G(ref=3, nivel=1, descricao='Detalhamento de informações para o tráfego mútuo', ocorrencias=(0, 1))):
        respFat: str = E(
            ref=4, nivel=2, descricao='Responsável pelo Faturamento', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D1,
            obs='Preencher com: 1-Ferrovia de origem; 2-Ferrovia de destino'
        )
        ferrEmi: str = E(
            ref=5, nivel=2, descricao='Ferrovia Emitente do CTe', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D1,
            obs='Preencher com: 1-Ferrovia de origem; 2-Ferrovia de destino'
        )
        vFrete: str = E(
            ref=6, nivel=2, descricao='Valor do Frete do Tráfego Mútuo', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27,
            obs='15 posições, sendo 13 inteiras e 2 decimais.'
        )
        chCTeFerroOrigem: str = E(
            ref=7, nivel=2, descricao='Chave de acesso do CT-e emitido pelo ferrovia de origem', tipo='N',
            ocorrencias=(0, 1), tam=44, regex=ER4
        )

        class ferroEnv(
            G(ref=8, nivel=2, descricao='Informações das Ferrovias Envolvidas', ocorrencias=(0, -1))):
            CNPJ: str = CampoCNPJ(
                ref=9, nivel=3, descricao='Número do CNPJ', tipo='C', ocorrencias=(1, 1), tam=14, regex=ER5,
                obs='Informar o CNPJ da Ferrovia Envolvida. Caso a Ferrovia envolvida não seja inscrita no CNPJ o campo deverá preenchido com zeros. Informar os zeros não significativos.',
            )
            cInt: str = E(
                ref=10, nivel=3, descricao='Código interno da Ferrovia envolvida', tipo='C', ocorrencias=(0, 1), tam=(1, 10), regex=ER36,
                obs='Uso da transportadora'
            )
            IE: str = E(ref=11, nivel=3, descricao='Inscrição Estadual', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER29, prep_regex=r'\d+')
            xNome: str = E(ref=12, nivel=3, descricao='Razão Social ou Nome', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)

            class enderFerro(
                G(ref=13, nivel=3, descricao='Dados do endereço da ferrovia envolvida', ocorrencias=(1, 1))):
                xLgr: str = E(ref=14, nivel=4, descricao='Logradouro', tipo='C', ocorrencias=(1, 1), tam=(2, 255), regex=ER36)
                nro: str = E(ref=15, nivel=4, descricao='Número', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                xCpl: str = E(ref=16, nivel=4, descricao='Complemento', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                xBairro: str = E(ref=17, nivel=4, descricao='Bairro', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)
                cMun: str = E(
                    ref=18, nivel=4, descricao='Código do município', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3,
                    obs='Utilizar a tabela do IBGE Informar 9999999 para operações com o exterior.'
                )
                xMun: str = E(
                    ref=19, nivel=4, descricao='Nome do município', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36,
                    obs='Informar EXTERIOR para operações com o exterior.'
                )
                CEP: str = E(ref=20, nivel=4, descricao='CEP', tipo='N', ocorrencias=(1, 1), tam=8, regex=ER41, prep_regex=r'\d+')
                UF: str = E(
                    ref=21, nivel=4, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10,
                    obs='Informar EX para operações com o exterior.'
                )

    fluxo: str = E(
        ref=22, nivel=1, descricao='Fluxo Ferroviário', tipo='C', ocorrencias=(1, 1), tam=(1, 10), regex=ER36,
        obs='Trata-se de um número identificador do contrato firmado com o cliente'
    )



class aquav(G(ref=1, nivel=0, descricao='Informações do modal Aquaviário', ocorrencias=(1, 1))):
    vPrest: str = E(
        ref=2, nivel=1, descricao='Valor da Prestação Base de Cálculo do AFRMM', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27,
        obs='15 posições, sendo 13 inteiras e 2 decimais.'
    )
    vAFRMM: str = E(
        ref=3, nivel=1, descricao='AFRMM (Adicional de Frete para Renovação da Marinha Mercante)', tipo='N', ocorrencias=(1, 1),
        tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.'
    )
    xNavio: str = E(ref=4, nivel=1, descricao='Identificação do Navio', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)

    class balsa(G(ref=5, nivel=1, descricao='Grupo de informações das balsas', ocorrencias=(0, 3))):
        xBalsa: str = E(ref=6, nivel=2, descricao='Identificador da Balsa', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)

    nViag: str = E(ref=7, nivel=1, descricao='Número da Viagem', tipo='N', ocorrencias=(0, 1), tam=(1, 10), regex=ER62)
    direc: str = E(
        ref=8, nivel=1, descricao='Direção', tipo='C', ocorrencias=(1, 1), tam=1, dominio=D39,
        obs='Preencher com: N-Norte, L-Leste, S-Sul, O-Oeste'
    )
    irin: str = E(ref=9, nivel=1, descricao='Irin do navio sempre deverá ser informado', tipo='C', ocorrencias=(1, 1), tam=(1, 10))

    class detCont(
        G(ref=10, nivel=1,
          descricao='Grupo de informações de detalhamento dos contêineres (Somente para Redespacho Intermediário e serviço vinculado a multimodal)',
          ocorrencias=(0, -1))
    ):
        nCont: str = E(ref=11, nivel=2, descricao='Identificação do Container', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER46)

        class lacre(
            G(ref=12, nivel=2, descricao='Grupo de informações dos lacres dos cointainers da qtde da carga',
              ocorrencias=(0, 3))):
            nLacre: str = E(ref=13, nivel=3, descricao='Lacre', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)

        class infDoc(
            G(ref=14, nivel=2, descricao='Informações dos documentos dos conteiners', ocorrencias=(0, 1))):
            class infNF(CG(ref=15, nivel=3, descricao='Informações das NF', ocorrencias=(1, -1))):
                serie: str = E(ref=16, nivel=4, descricao='Série', tipo='C', ocorrencias=(1, 1), tam=(1, 3), regex=ER36)
                nDoc: str = E(ref=17, nivel=4, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
                unidRat: str = E(
                    ref=18, nivel=4, descricao='Unidade de medida rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2),
                    regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.'
                )

            class infNFe(CG(ref=19, nivel=3, descricao='Informações das NFe', ocorrencias=(1, -1))):
                chave: str = E(ref=20, nivel=4, descricao='Chave de acesso da NF-e', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)
                unidRat: str = E(
                    ref=21, nivel=4, descricao='Unidade de medida rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2),
                    regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.'
                )

    tpNav: str = E(
        ref=22, nivel=1, descricao='Tipo de Navegação', tipo='N', ocorrencias=(0, 1), tam=1, dominio=D15,
        obs='Preencher com: 0 - Interior; 1 - Cabotagem'
    )

    class duto(G(ref=1, nivel=0, descricao='Informações do modal Dutoviário', ocorrencias=(1, 1))):
        vTar: str = E(
            ref=2, nivel=1, descricao='Valor da tarifa', tipo='N', ocorrencias=(0, 1), tam=(9, 6), regex=ER20,
            obs='15 posições, sendo 9 inteiras e 6 decimais.'
        )
        dIni: str = E(
            ref=3, nivel=1, descricao='Data de Início da prestação do serviço', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11
        )
        dFim: str = E(ref=4, nivel=1, descricao='Data de Fim da prestação do serviço', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11)


class multimodal(G(ref=1, nivel=0, descricao='Informações do Multimodal', ocorrencias=(1, 1))):
    COTM: str = E(
        ref=2, nivel=1, descricao='Número do Certificado do Operador de Transporte Multimodal', tipo='C', ocorrencias=(1, 1), tam=(1, 20),
        regex=ER36
    )
    indNegociavel: str = E(
        ref=3, nivel=1, descricao='Indicador Negociável Preencher com: 0 - Não Negociável; 1 - Negociável',
        tipo='N', ocorrencias=(1, 1), tam=1, dominio=D15
    )

    class seg(G(ref=4, nivel=1, descricao='Informações de Seguro do Multimodal', ocorrencias=(0, 1))):
        class infSeg(G(ref=5, nivel=2, descricao='Informações da seguradora', ocorrencias=(1, 1))):
            xSeg: str = E(ref=6, nivel=3, descricao='Nome da Seguradora', tipo='C', ocorrencias=(1, 1), tam=(1, 30), regex=ER36)
            CNPJ: str = CampoCNPJ(
                ref=7, nivel=3, descricao='Número do CNPJ da seguradora', tipo='N', ocorrencias=(1, 1), tam=14, regex=ER8,
                obs='Obrigatório apenas se responsável pelo seguro for (2) responsável pela contratação do transporte - pessoa jurídica'
            )

        nApol: str = E(
            ref=8, nivel=2, descricao='Número da Apólice', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36,
            obs='Obrigatório pela lei 11.442/07 (RCTRC)'
        )
        nAver: str = E(
            ref=9, nivel=2, descricao='Número da Averbação', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36,
            obs='Não é obrigatório, pois muitas averbações ocorrem após a emissão do CT, mensalmente, por exemplo.'
        )



class aereo(G(ref=1, nivel=0, descricao='Informações do modal Aéreo', ocorrencias=(1, 1))):
    nMinu: str = E(
        ref=2, nivel=1, descricao='Número da Minuta', tipo='N', ocorrencias=(0, 1), tam=9, regex=ER59,
        obs='Documento que precede o CT-e, assinado pelo expedidor, espécie de pedido de serviço'
    )
    nOCA: str = E(
        ref=3, nivel=1, descricao='Número Operacional do Conhecimento Aéreo', tipo='N', ocorrencias=(0, 1), tam=11, regex=ER9,
        obs='Representa o número de controle comumente utilizado pelo conhecimento aéreo composto por uma sequência numérica de onze dígitos. Os três primeiros dígitos representam um código que os operadores de transporte aéreo associados à IATA possuem. Em seguida um número de série de sete dígitos determinados pelo operador  de transporte aéreo. Para finalizar, um dígito verificador, que é um sistema de módulo sete imponderado o qual divide o número de  série do conhecimento aéreo por sete e usa o resto como dígito de verificação.'
    )
    dPrevAereo: str = E(ref=4, nivel=1, descricao='Data prevista da entrega', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11, obs='Formato AAAA-MM-DD')

    class natCarga(G(ref=5, nivel=1, descricao='Natureza da carga', ocorrencias=(1, 1))):
        xDime: str = E(
            ref=6, nivel=2, descricao='Dimensão', tipo='C', ocorrencias=(0, 1), tam=(5, 14), regex=ER36,
            obs='Formato:1234X1234X1234 (cm). Esse campo deve sempre que possível ser preenchido. Entretanto, quando for impossível o preenchimento das dimensões, fica obrigatório o preenchimento da cubagem em metro cúbico do leiaute do CT-e da estrutura genérica (infQ).'
        )
        cInfManu: str = E(
            ref=7, nivel=2, descricao='Informações de manuseio', tipo='N', ocorrencias=(0, -1), tam=2, dominio=D37,
            obs='- certificado do expedidor para embarque de animal vivo; - artigo perigoso conforme Declaração do Expedidor anexa; 03 - somente em aeronave cargueira; 04 - artigo perigoso - declaração do expedidor não requerida; - artigo perigoso em quantidade isenta; - gelo seco para refrigeração (especificar no campo observações a quantidade); - não restrito (especificar a Disposição Especial no campo observações); - artigo perigoso em carga consolidada (especificar a quantidade no campo observações); - autorização da autoridade governamental anexa (especificar no campo observações); – baterias de íons de lítio em conformidade com a Seção II da PI965 – CAO; - baterias de íons de lítio em conformidade com a Seção II da PI966; 12 - baterias de íons de lítio em conformidade com a Seção II da PI967; 13 – baterias de metal lítio em conformidade com a Seção II da PI968 — CAO; 14 - baterias de metal lítio em conformidade com a Seção II da PI969; 15 - baterias de metal lítio em conformidade com a Seção II da PI970; 99 - outro (especificar no campo observações)'
        )

    class tarifa(G(ref=8, nivel=1, descricao='Informações de tarifa', ocorrencias=(1, 1))):
        CL: str = E(
            ref=9, nivel=2, descricao='Classe', tipo='C', ocorrencias=(1, 1), tam=1, regex=ER60,
            obs='Preencher com: M - Tarifa Mínima; G - Tarifa Geral; E - Tarifa Específica'
        )
        cTar: str = E(
            ref=10, nivel=2, descricao='Código da Tarifa', tipo='C', ocorrencias=(0, 1), tam=(1, 4), regex=ER36,
            obs='Deverão ser incluídos os códigos de três dígitos, correspondentes à tarifa.'
        )
        vTar: str = E(
            ref=11, nivel=2, descricao='Valor da Tarifa', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27,
            obs='15 posições, sendo 13 inteiras e 2 decimais. Valor da tarifa por kg quando for o caso.'
        )

    class peri(G(ref=12, nivel=1,
                 descricao='Preenchido quando for transporte de produtos classificados pela ONU como perigosos.',
                 ocorrencias=(0, -1))):
        nONU: str = E(
            ref=13, nivel=2, descricao='Número ONU/UN', tipo='C', ocorrencias=(1, 1), tam=4, regex=ER61,
            obs='Ver a legislação de transporte de produtos perigosos aplicadas ao modal'
        )
        qTotEmb: str = E(
            ref=14, nivel=2, descricao='Quantidade total de volumes contendo artigos perigosos', tipo='C', ocorrencias=(1, 1),
            tam=(1, 20), regex=ER36,
            obs='Preencher com o número de volumes (unidades) de artigos perigosos, ou seja, cada embalagem devidamente  marcada e etiquetada (por ex.: número de caixas, de tambores, de bambonas, dentre outros). Não deve ser preenchido com o número de ULD, pallets ou containers.'
        )

        class infTotAP(
            G(ref=15, nivel=2, descricao='Grupo de informações das quantidades totais de artigos perigosos',
              ocorrencias=(1, 1))):
            qTotProd: str = E(
                ref=16, nivel=3, descricao='Quantidade total de artigos perigosos', tipo='N', ocorrencias=(1, 1), tam=(11, 4),
                regex=ER21,
                obs='15 posições, sendo 11 inteiras e 4 decimais. 15 posições, sendo 11 inteiras e 4 decimais. Deve indicar a quantidade total do artigo perigoso, tendo como base a unidade referenciada na Tabela 3-1 do Doc 9284, por exemplo: litros; quilogramas; quilograma bruto etc. O preenchimento não deve, entretanto, incluir a unidade de medida. No caso de transporte de  material radioativo, deve-se indicar o somatório dos Índices de Transporte (TI). Não indicar a quantidade do artigo perigoso por embalagem.'
            )
            uniAP: str = E(
                ref=17, nivel=3, descricao='Unidade de medida', tipo='N', ocorrencias=(1, 1), tam=(1, 1), dominio=D38, regex=ER36,
                obs='– KG; – KG G (quilograma bruto); 3 – LITROS;'
            )





class CTe(Grupo):
    xmlns = A(default='http://www.portalfiscal.inf.br/cte')

    def _preparar(self, dfe):
        if not self.infCte.ide.cUF:
            self.infCte.ide.cUF = dfe.cUF
        if not self.infCte.ide.cCT:
            self.infCte.ide.cCT = datetime.now().strftime('%f').zfill(8)
        if not self.infCte.Id:
            self.infCte.Id = dfe.gerar_chave(
                self.infCte.ide.cUF, self.infCte.ide.dhEmi, self.infCte.emit.CNPJ, self.infCte.ide.mod,
                self.infCte.ide.serie, self.infCte.ide.nCT, self.infCte.ide.tpEmis, self.infCte.ide.cCT,
            )
        if not self.infCte.ide.cDV:
            self.infCte.ide.cDV = self.infCte.Id[-1]
        if not self.infCte.ide.tpAmb:
            self.infCte.ide.tpAmb = dfe.tpAmb

        if not self.infCTeSupl.qrCodCTe:
            self.infCTeSupl.qrCodCTe = 'https://dfe-portal.svrs.rs.gov.br/cte/qrCode?chCTe=%s&tpAmb=%s' % (
                self.infCte.Id[3:], self.infCte.ide.tpAmb
            )

    class infCte(G(ref=1, nivel=0, descricao='Informações do CT-e', ocorrencias=1)):
        versao: str = A(ref=2, nivel=1, descricao='Versão do leiaute', tipo='N', ocorrencias=(1, 1), tam='1-2v2', regex=ER57, obs='Ex: "3.00"', default=3)
        Id: str = A(ref=3, nivel=1, descricao='Identificador da tag a ser assinada', tipo='C', ocorrencias=(1, 1), tam=47, regex=ER48, obs='Informar a chave de acesso do CT-e e precedida do literal "CTe"')

        class ide(G(ref=4, nivel=1, descricao='Identificação do CT-e', ocorrencias=(1, 1))):
            cUF: str = E(ref=5, nivel=2, descricao='Código da UF do emitente do CT-e.', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D2, obs='Utilizar a Tabela do IBGE.')
            cCT: str = E(ref=6, nivel=2, descricao='Código numérico que compõe a Chave de Acesso.', tipo='C', ocorrencias=(1, 1), tam=8, regex=ER41, obs='Número aleatório gerado pelo emitente para cada  CT-e, com o objetivo de evitar acessos indevidos ao documento.')
            CFOP: str = E(ref=7, nivel=2, descricao='Código Fiscal de Operações e Prestações', tipo='N', ocorrencias=(1, 1), tam=4, regex=ER51)
            natOp: str = E(ref=8, nivel=2, descricao='Natureza da Operação', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)
            mod: str = E(ref=9, nivel=2, descricao='Modelo do documento fiscal', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D6, obs='Utilizar o código 57 para identificação do CT-e')
            serie: str = E(ref=10, nivel=2, descricao='Série do CT-e', tipo='N', ocorrencias=(1, 1), tam=(1, 3), regex=ER34, obs='Preencher com "0" no caso de série única')
            nCT: str = E(ref=11, nivel=2, descricao='Número do CT-e', tipo='N', ocorrencias=(1, 1), tam=(1, 9), regex=ER32)
            dhEmi: str = E(ref=12, nivel=2, descricao='Data e hora de emissão do CT-e', tipo='D', ocorrencias=(1, 1), tam=21, regex=ER1, obs='Formato AAAA-MM-DDTHH:MM:DD TZD', formato='%Y-%m-%dT%H:%M:%S-02:00')
            tpImp: str = E(ref=13, nivel=2, descricao='Formato de impressão do DACTE', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D1, obs='Preencher com: 1 - Retrato; 2 - Paisagem.')
            tpEmis: str = E(ref=14, nivel=2, descricao='Forma de emissão do CT-e', tipo='C', ocorrencias=(1, 1), tam=1, dominio=D12, obs='Preencher com: 1 - Normal; - EPEC pela SVC; - Contingência FSDA; 7 - Autorização pela SVC-RS; 8 - Autorização pela SVC-SP;')
            cDV: str = E(ref=15, nivel=2, descricao='Digito Verificador da chave de acesso do CT-e', tipo='C', ocorrencias=(1, 1), tam=1, regex=ER42, obs='Informar o dígito de controle da chave de acesso do CT-e, que deve ser calculado com a aplicação do algoritmo módulo 11 (base 2,9) da chave de acesso.')
            tpAmb: str = E(ref=16, nivel=2, descricao='Tipo do Ambiente', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D1, obs='Preencher com: 1 - Produção; 2 - Homologação')
            tpCTe: str = E(ref=17, nivel=2, descricao='Tipo do CT-e', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D17, obs='Preencher com: 0 - CT-e Normal; - CT-e de Complemento de Valores; - CT-e de Anulação; - CT-e de Substituição')
            procEmi: str = E(ref=18, nivel=2, descricao='Identificador do processo de emissão do CT-e', tipo='N', ocorrencias=1, tam=1, dominio=D36, obs='Preencher com: 0 - emissão de CT-e com aplicativo do contribuinte; 3- emissão CT-e pelo contribuinte com aplicativo fornecido pelo SEBRAE.')
            verProc: str = E(ref=19, nivel=2, descricao='Versão do processo de emissão', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36, obs='Informar a versão do aplicativo emissor de CT-e.')
            indGlobalizado: str = E(ref=20, nivel=2, descricao='Indicador de CT-e Globalizado', tipo='N', ocorrencias=(0, 1), tam=1, dominio=D13, obs='Informar valor 1 quando for Globalizado e não informar a tag quando não tratar de CT- e Globalizado')
            cMunEnv: str = E(ref=21, nivel=2, descricao='Código do Município de envio do CT-e (de onde o documento foi transmitido)', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3, obs='Utilizar a tabela do IBGE. Informar 9999999 para as operações com o exterior.')
            xMunEnv: str = E(ref=22, nivel=2, descricao='Nome do Município de envio do CT-e (de onde o documento foi transmitido)', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar PAIS/Município para as operações com o exterior.')
            UFEnv: str = E(ref=23, nivel=2, descricao='Sigla da UF de envio do CT-e (de onde o documento foi transmitido)', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar "EX" para operações com o exterior.')
            modal: str = E(ref=24, nivel=2, descricao='Modal', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D35, obs='Preencher com: 01-Rodoviário; 02-Aéreo; 03-Aquaviário; 04-Ferroviário; 05-Dutoviário; 06-Multimodal;', formato='%02d')
            tpServ: str = E(ref=25, nivel=2, descricao='Tipo do Serviço', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D14, obs='Preencher com: 0 - Normal; - Subcontratação; - Redespacho; - Redespacho Intermediário; - Serviço Vinculado a Multimodal')
            cMunIni: str = E(ref=26, nivel=2, descricao='Código do Município de início da prestação', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3, obs='Utilizar a tabela do IBGE. Informar 9999999 para operações com o exterior.')
            xMunIni: str = E(ref=27, nivel=2, descricao='Nome do Município do início da prestação', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar "EXTERIOR" para operações com o exterior.')
            UFIni: str = E(ref=28, nivel=2, descricao='UF do início da prestação', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar "EX" para operações com o exterior.')
            cMunFim: str = E(ref=29, nivel=2, descricao='Código do Município de término da prestação', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3, obs='Utilizar a tabela do IBGE. Informar 9999999 para operações com o exterior.')
            xMunFim: str = E(ref=30, nivel=2, descricao='Nome do Município do término da prestação', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar "EXTERIOR" para operações com o exterior.')
            UFFim: str = E(ref=31, nivel=2, descricao='UF do término da prestação', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar "EX" para operações com o exterior.')
            retira: str = E(ref=32, nivel=2, descricao='Indicador se o Recebedor retira no Aeroporto, Filial, Porto ou Estação de Destino?', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D15, obs='Preencher com: 0 - sim; 1 - não')
            xDetRetira: str = E(ref=33, nivel=2, descricao='Detalhes do retira', tipo='C', ocorrencias=(0, 1), tam=(1, 160), regex=ER36)
            indIEToma: str = E(ref=34, nivel=2, descricao='Indicador do papel do tomador na prestação do serviço: – Contribuinte ICMS; – Contribuinte isento de inscrição; 9 – Não Contribuinte', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D16, obs='Aplica-se ao tomador que for indicado no toma3 ou toma4')

            class toma3(G(ref=35, nivel=2, descricao='Indicador do "papel" do tomador do serviço no CT-e', ocorrencias=(1, 1))):
                toma: str = E(ref=36, nivel=3, descricao='Tomador do Serviço', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D17, obs='Preencher com: 0-Remetente; 1-Expedidor; 2-Recebedor; 3-Destinatário Serão utilizadas as informações contidas no respectivo grupo, conforme indicado pelo conteúdo deste campo')

            class toma4(CG(ref=37, nivel=2, descricao='Indicador do "papel" do tomador do serviço no CT-e', ocorrencias=(1, 1))):
                toma: str = E(ref=38, nivel=3, descricao='Tomador do Sref=erviço', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D18, obs='Preencher com: 4 - Outros Obs: Informar os dados cadastrais do tomador do serviço')
                CNPJ: str = CampoCNPJ(
                    ref=39, nivel=3, descricao='Número do CNPJ', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER8,
                    obs='Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros. Informar os zeros não significativos.',
                )
                CPF: str = CampoCPF(
                    ref=40, nivel=3, descricao='Número do CPF', tipo='C', ocorrencias=(0, 1), tam=11, regex=ER9,
                    obs='Informar os zeros não significativos.',
                )
                IE: str = E(ref=41, nivel=3, descricao='Inscrição Estadual', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER30, obs='Informar a IE do tomador ou ISENTO se tomador é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o tomador não seja contribuinte do ICMS não informar o conteúdo.', prep_regex=r'\d+')
                xNome: str = E(ref=42, nivel=3, descricao='Razão Social ou Nome', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
                xFant: str = E(ref=43, nivel=3, descricao='Nome Fantasia', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)
                fone: str = E(ref=44, nivel=3, descricao='Telefone', tipo='C', ocorrencias=(0, 1), tam=(6, 14), regex=ER6, prep_regex=r'\d+')

                class enderToma(G(ref=45, nivel=3, descricao='Dados do endereço', ocorrencias=(1, 1))):
                    xLgr: str = E(ref=46, nivel=4, descricao='Lref=ogradouro', tipo='C', ocorrencias=(1, 1), tam=(2, 255), regex=ER36)
                    nro: str = E(ref=47, nivel=4, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)
                    xCpl: str = E(ref=48, nivel=4, descricao='Complemento', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                    xBairro: str = E(ref=49, nivel=4, descricao='Bairro', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
                    cMun: str = E(ref=50, nivel=4, descricao='Código do município (utilizar a tabela do IBGE)', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3, obs='Informar 9999999 para operações com o exterior.')
                    xMun: str = E(ref=51, nivel=4, descricao='Nome do município', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar EXTERIOR para operações com o exterior.')
                    CEP: str = E(
                        ref=52, nivel=4, descricao='CEP', tipo='C', ocorrencias=(0, 1), tam=8, regex=ER41,
                        obs='Informar os zeros não significativos',
                        prep_regex=r'\d+'
                    )
                    UF: str = E(ref=53, nivel=4, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar EX para operações com o exterior.')
                    cPais: str = E(ref=54, nivel=4, descricao='Código do país', tipo='N', ocorrencias=(0, 1), tam=(1, 4), regex=ER31, obs='Utilizar a tabela do BACEN')
                    xPais: str = E(ref=55, nivel=4, descricao='Nome do país', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)

                email: str = E(ref=56, nivel=3, descricao='Endereço de e-mail', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER52)

            dhCont: str = E(ref=57, nivel=2, descricao='Data e Hora da entrada em contingência', tipo='C', ocorrencias=(0, 1), tam=21, regex=ER1, obs='Informar a data e hora no formato AAAA-MM- DDTHH:MM:SS')
            xJust: str = E(ref=58, nivel=2, descricao='Justificativa da entrada em contingência', tipo='C', ocorrencias=(0, 1), tam=(15, 256), regex=ER36)

        class compl(G(ref=59, nivel=1, descricao='Dados complementares do CT-e para fins operacionais ou comerciais', ocorrencias=(0, 1))):
            xCaracAd: str = E(ref=60, nivel=2, descricao='Característica adicional do transporte', tipo='C', ocorrencias=(0, 1), tam=(1, 15), regex=ER36, obs='Texto livre: REENTREGA; DEVOLUÇÃO; REFATURAMENTO; etc')
            xCaracSer: str = E(ref=61, nivel=2, descricao='Característica adicional do serviço', tipo='C', ocorrencias=(0, 1), tam=(1, 30), regex=ER36, obs='Texto livre: ENTREGA EXPRESSA; LOGÍSTICA REVERSA; CONVENCIONAL; EMERGENCIAL; etc')
            xEmi: str = E(ref=62, nivel=2, descricao='Funcionário emissor do CTe', tipo='C', ocorrencias=(0, 1), tam=(1, 20), regex=ER36)

            class fluxo(G(ref=63, nivel=2, descricao='Previsão do fluxo da carga', ocorrencias=(0, 1))):
                xOrig: str = E(ref=64, nivel=3, descricao='Sigla ou código interno da Filial/Porto/Estação/ Aeroporto de Origem', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36, obs='Observações para o modal aéreo:  Preenchimento obrigatório para o modal aéreo.  O código de três letras IATA do aeroporto de partida deverá ser incluído como primeira anotação. Quando não for possível, utilizar a sigla OACI.')

                class Pass(G(ref=65, nivel=3, descricao='', ocorrencias=(0, -1), elemento='pass')):
                    xPass: str = E(ref=66, nivel=4, descricao='Sigla ou código interno da Filial/Porto/Estação/Aeroporto de Passagem', tipo='C', ocorrencias=(0, 1), tam=(1, 15), regex=ER36, obs='Observação para o modal aéreo: - O código de três letras IATA, referente ao aeroporto de transferência, deverá ser incluído, quando for o caso. Quando não for possível, utilizar a sigla OACI. Qualquer solicitação de itinerário deverá ser incluída.')
                xDest: str = E(ref=67, nivel=3, descricao='Sigla ou código interno da Filial/Porto/Estação/Aeroporto de Destino', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36, obs='Observações para o modal aéreo: Preenchimento obrigatório para o modal aéreo. Deverá ser incluído o código de três letras IATA do aeroporto de destino. Quando não for possível, utilizar a sigla OACI.')
                xRota: str = E(ref=68, nivel=3, descricao='Código da Rota de Entrega', tipo='C', ocorrencias=(0, 1), tam=(1, 10), regex=ER36)

            class Entrega(G(ref=69, nivel=2, descricao='Informações ref. a previsão de entrega', ocorrencias=(0, 1))):

                class semData(CG(ref=70, nivel=3, descricao='Entrega sem data definida', ocorrencias=(1, 1))):
                    tpPer: str = E(ref=71, nivel=4, descricao='Tipo de data/período programado para entrega', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D19, obs='0- Sem data definida')

                class comData(CG(ref=72, nivel=3, descricao='Entrega com data definida', ocorrencias=(1, 1))):
                    tpPer: str = E(ref=73, nivel=4, descricao='Tipo de data/período programado para entrega', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D20, obs='Preencher com: 1-Na data; 2-Até a data; 3-A partir da data')
                    dProg: str = E(ref=74, nivel=4, descricao='Data programada', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11, obs='Formato AAAA-MM-DD')

                class noPeriodo(CG(ref=75, nivel=3, descricao='Entrega no período definido', ocorrencias=(1, 1))):
                    tpPer: str = E(ref=76, nivel=4, descricao='Tipo período', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D18, obs='4-no período')
                    dIni: str = E(ref=77, nivel=4, descricao='Data inicial', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11, obs='Formato AAAA-MM-DD')
                    dFim: str = E(ref=78, nivel=4, descricao='Data final', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11, obs='Formato AAAA-MM-DD')

                class semHora(CG(ref=79, nivel=3, descricao='Entrega sem hora definida', ocorrencias=(1, 1))):
                    tpHor: str = E(ref=80, nivel=4, descricao='Tipo de hora', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D19, obs='0- Sem hora definida')

                class comHora(CG(ref=81, nivel=3, descricao='Entrega com hora definida', ocorrencias=(1, 1))):
                    tpHor: str = E(ref=82, nivel=4, descricao='Tipo de hora', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D20, obs='Preencher com: 1 - No horário; - Até o horário; - A partir do horário')
                    hProg: str = E(ref=83, nivel=4, descricao='Hora programada', tipo='T', ocorrencias=(1, 1), tam=8, regex=ER56, obs='Formato HH:MM:SS')

                class noInter(CG(ref=84, nivel=3, descricao='Entrega no intervalo de horário definido', ocorrencias=(1, 1))):
                    tpHor: str = E(ref=85, nivel=4, descricao='Tipo de hora', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D18, obs='4 - No intervalo de tempo')
                    hIni: str = E(ref=86, nivel=4, descricao='Hora inicial', tipo='T', ocorrencias=(1, 1), tam=8, regex=ER56, obs='Formato HH:MM:SS')
                    hFim: str = E(ref=87, nivel=4, descricao='Hora final', tipo='T', ocorrencias=(1, 1), tam=8, regex=ER56, obs='Formato HH:MM:SS')
            origCalc: str = E(ref=88, nivel=2, descricao='Município de origem para efeito de cálculo do frete', tipo='C', ocorrencias=(0, 1), tam=(2, 40), regex=ER36)
            destCalc: str = E(ref=89, nivel=2, descricao='Município de destino para efeito de cálculo do frete', tipo='C', ocorrencias=(0, 1), tam=(2, 40), regex=ER36)
            xObs: str = E(ref=90, nivel=2, descricao='Observações Gerais', tipo='C', ocorrencias=(0, 1), tam=(1, 2000), regex=ER36)

            class ObsCont(G(ref=91, nivel=2, descricao='Campo de uso livre do contribuinte', ocorrencias=(0, 10))):
                xCampo: str = A(ref=92, nivel=3, descricao='Identificação do campo', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
                xTexto: str = E(ref=93, nivel=3, descricao='Conteúdo do campo', tipo='C', ocorrencias=(1, 1), tam=(1, 160), regex=ER36)

            class ObsFisco(G(ref=94, nivel=2, descricao='Campo de uso livre do contribuinte', ocorrencias=(0, 10))):
                xCampo: str = A(ref=95, nivel=3, descricao='Identificação do campo', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
                xTexto: str = E(ref=96, nivel=3, descricao='Conteúdo do campo', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)

        class emit(G(ref=97, nivel=1, descricao='Identificação do Emitente do CT-e', ocorrencias=(1, 1))):
            CNPJ: str = CampoCNPJ(ref=98, nivel=2, descricao='CNPJ do emitente', tipo='N', ocorrencias=(1, 1), tam=14, regex=ER5, obs='Informar zeros não significativos')
            IE: str = E(ref=99, nivel=2, descricao='Inscrição Estadual do Emitente', tipo='C', ocorrencias=(1, 1), tam=14, regex=ER29, prep_regex=r'\d+')
            IEST: str = E(ref=100, nivel=2, descricao='Inscrição Estadual do Substituto Tributário', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER29, prep_regex=r'\d+')
            xNome: str = E(ref=101, nivel=2, descricao='Razão social ou Nome do emitente', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
            xFant: str = E(ref=102, nivel=2, descricao='Nome fantasia', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)

            class enderEmit(G(ref=103, nivel=2, descricao='Endereço do emitente', ocorrencias=(1, 1))):
                xLgr: str = E(ref=104, nivel=3, descricao='Logradouro', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
                nro: str = E(ref=105, nivel=3, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)
                xCpl: str = E(ref=106, nivel=3, descricao='Complemento', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                xBairro: str = E(ref=107, nivel=3, descricao='Bairro', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
                cMun: str = E(ref=108, nivel=3, descricao='Código do município (utilizar a tabela do IBGE)', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3)
                xMun: str = E(ref=109, nivel=3, descricao='Nome do município', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
                CEP: str = E(
                    ref=110, nivel=3, descricao='CEP', tipo='N', ocorrencias=(0, 1), tam=8, regex=ER41,
                    obs='Informar zeros não significativos',
                    prep_regex=r'\d+'
                )
                UF: str = E(ref=111, nivel=3, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D11)
                fone: str = E(ref=112, nivel=3, descricao='Telefone', tipo='C', ocorrencias=(0, 1), tam=(6, 14), regex=ER6, prep_regex=r'\d+')

        class rem(G(ref=113, nivel=1, descricao='Informações do Remetente das mercadorias transportadas pelo CT-e', ocorrencias=(0, 1))):
            CNPJ: str = CampoCNPJ(
                ref=114, nivel=2, descricao='Número do CNPJ', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER8,
                obs='Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros. Informar os zeros não significativos.',
            )
            CPF: str = CampoCPF(
                ref=115, nivel=2, descricao='Número do CPF', tipo='C', ocorrencias=(0, 1), tam=11, regex=ER9,
                obs='A(ref= zeros não significativos.',
            )
            IE: str = E(ref=116, nivel=2, descricao='Inscrição Estadual', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER30, obs='Informar a IE do remetente ou ISENTO se remetente é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o remetente não seja contribuinte do ICMS não informar a tag.', prep_regex=r'\d+')
            xNome: str = E(ref=117, nivel=2, descricao='Razão social ou nome do remetente', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
            xFant: str = E(ref=118, nivel=2, descricao='Nome fantasia', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)
            fone: str = E(ref=119, nivel=2, descricao='Telefone', tipo='C', ocorrencias=(0, 1), tam=(6, 14), regex=ER6, prep_regex=r'\d+')

            class enderReme(G(ref=120, nivel=2, descricao='Dados do endereço', ocorrencias=(1, 1))):
                xLgr: str = E(ref=121, nivel=3, descricao='Logradouro', tipo='C', ocorrencias=(1, 1), tam=(2, 255), regex=ER36)
                nro: str = E(ref=122, nivel=3, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)
                xCpl: str = E(ref=123, nivel=3, descricao='Complemento', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                xBairro: str = E(ref=124, nivel=3, descricao='Bairro', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
                cMun: str = E(ref=125, nivel=3, descricao='Código do município (utilizar a tabela do IBGE)', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3, obs='Informar 9999999 para operações com o exterior.')
                xMun: str = E(ref=126, nivel=3, descricao='Nome do município', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar EXTERIOR para operações com o exterior.')
                CEP: str = E(
                    ref=127, nivel=3, descricao='CEP', tipo='C', ocorrencias=(0, 1), tam=8, regex=ER41, obs='Informar os zeros não significativos',
                    formato='%08d',
                    prep_regex=r'\d+'
                )
                UF: str = E(ref=128, nivel=3, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar EX para operações com o exterior.')
                cPais: str = E(ref=129, nivel=3, descricao='Código do país', tipo='N', ocorrencias=(0, 1), tam=(1, 4), regex=ER31, obs='Utilizar a tabela do BACEN')
                xPais: str = E(ref=130, nivel=3, descricao='Nome do país', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)
            email: str = E(ref=131, nivel=2, descricao='Endereço de e-mail', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER52)

        class exped(G(ref=132, nivel=1, descricao='Informações do Expedidor da Carga', ocorrencias=(0, 1))):
            CNPJ: str = CampoCNPJ(ref=133, nivel=2, descricao='Número do CNPJ', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER8, obs='Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros. Informar os zeros não significativos.',)
            CPF: str = CampoCPF(ref=134, nivel=2, descricao='Número do CPF', tipo='C', ocorrencias=(0, 1), tam=11, regex=ER9, obs='Informar os zeros não significativos.')
            IE: str = E(ref=135, nivel=2, descricao='Inscrição Estadual', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER30, obs='Informar a IE do expedidor ou ISENTO se expedidor é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o expedidor não seja contribuinte do ICMS não informar a tag.', prep_regex=r'\d+')
            xNome: str = E(ref=136, nivel=2, descricao='Razão Social ou Nome', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
            fone: str = E(ref=137, nivel=2, descricao='Telefone', tipo='C', ocorrencias=(0, 1), tam=(6, 14), regex=ER6, prep_regex=r'\d+')

            class enderExped(G(ref=138, nivel=2, descricao='Dados do endereço', ocorrencias=(1, 1))):
                xLgr: str = E(ref=139, nivel=3, descricao='Logradouro', tipo='C', ocorrencias=(1, 1), tam=(2, 255), regex=ER36)
                nro: str = E(ref=140, nivel=3, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)
                xCpl: str = E(ref=141, nivel=3, descricao='Complemento', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                xBairro: str = E(ref=142, nivel=3, descricao='Bairro', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
                cMun: str = E(ref=143, nivel=3, descricao='Código do município (utilizar a tabela do IBGE)', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3, obs='Informar 9999999 para operações com o exterior.')
                xMun: str = E(ref=144, nivel=3, descricao='Nome do município', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar EXTERIOR para operações com o exterior.')
                CEP: str = E(
                    ref=145, nivel=3, descricao='CEP', tipo='C', ocorrencias=(0, 1), tam=8, regex=ER41,
                    obs='Informar os zeros não significativos',
                    prep_regex=r'\d+',
                )
                UF: str = E(ref=146, nivel=3, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar EX para operações com o exterior.')
                cPais: str = E(ref=147, nivel=3, descricao='Código do país', tipo='N', ocorrencias=(0, 1), tam=(1, 4), regex=ER31, obs='Utilizar a tabela do BACEN')
                xPais: str = E(ref=148, nivel=3, descricao='Nome do país', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)
            email: str = E(ref=149, nivel=2, descricao='Endereço de e-mail', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER52)

        class receb(G(ref=150, nivel=1, descricao='Informações do Recebedor da Carga', ocorrencias=(0, 1))):
            CNPJ: str = CampoCNPJ(ref=151, nivel=2, descricao='Número do CNPJ', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER8, obs='Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros. Informar os zeros não significativos.')
            CPF: str = CampoCPF(ref=152, nivel=2, descricao='Número do CPF', tipo='C', ocorrencias=(0, 1), tam=11, regex=ER9, obs='Informar os zeros não significativos.')
            IE: str = E(ref=153, nivel=2, descricao='Inscrição Estadual', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER30, obs='Informar a IE do recebedor ou ISENTO se recebedor é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o recebedor não seja contribuinte do ICMS não informar o conteúdo.', prep_regex=r'\d+')
            xNome: str = E(ref=154, nivel=2, descricao='Razão Social ou Nome', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
            fone: str = E(ref=155, nivel=2, descricao='Telefone', tipo='C', ocorrencias=(0, 1), tam=(6, 14), regex=ER6, prep_regex=r'\d+')

            class enderReceb(G(ref=156, nivel=2, descricao='Dados do endereço', ocorrencias=(1, 1))):
                xLgr: str = E(ref=157, nivel=3, descricao='Logradouro', tipo='C', ocorrencias=(1, 1), tam=(2, 255), regex=ER36)
                nro: str = E(ref=158, nivel=3, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)
                xCplr: str = E(ref=159, nivel=3, descricao='Complemento', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                xBairro: str = E(ref=160, nivel=3, descricao='Bairro', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
                cMun: str = E(ref=161, nivel=3, descricao='Código do município (utilizar a tabela do IBGE)', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3, obs='Informar 9999999 para operações com o exterior.')
                xMun: str = E(ref=162, nivel=3, descricao='Nome do município', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar EXTERIOR para operações com o exterior.')
                CEP: str = E(
                    ref=163, nivel=3, descricao='CEP', tipo='C', ocorrencias=(0, 1), tam=8, regex=ER41, obs='Informar os zeros não significativos',
                    prep_regex=r'\d+',
                )
                UF: str = E(ref=164, nivel=3, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar EX para operações com o exterior.')
                cPais: str = E(ref=165, nivel=3, descricao='Código do país', tipo='N', ocorrencias=(0, 1), tam=(1, 4), regex=ER31, obs='Utilizar a tabela do BACEN')
                xPais: str = E(ref=166, nivel=3, descricao='Nome do país', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)
            email: str = E(ref=167, nivel=2, descricao='Endereço de e-mail', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER52)

        class dest(G(ref=168, nivel=1, descricao='Informações do Destinatário do CT-e', ocorrencias=(0, 1))):
            CNPJ: str = CampoCNPJ(ref=169, nivel=2, descricao='Número do CNPJ', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER8, obs='Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros. Informar os zeros não significativos.')
            CPF: str = CampoCPF(ref=170, nivel=2, descricao='Número do CPF', tipo='C', ocorrencias=(0, 1), tam=11, regex=ER9, obs='Informar os zeros não significativos.')
            IE: str = E(ref=171, nivel=2, descricao='Inscrição Estadual', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER30, obs='Informar a IE do destinatário ou ISENTO se destinatário é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o destinatário não seja contribuinte do ICMS não informar o conteúdo.', prep_regex=r'\d+')
            xNome: str = E(ref=172, nivel=2, descricao='Razão Social ou Nome do destinatário', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
            fone: str = E(ref=173, nivel=2, descricao='Telefone', tipo='C', ocorrencias=(0, 1), tam=(6, 14), regex=ER6, prep_regex=r'\d+')
            ISUF: str = E(ref=174, nivel=2, descricao='Inscrição na SUFRAMA', tipo='N', ocorrencias=(0, 1), tam=(8, 9), regex=ER43, obs='(Obrigatório nas operações com as áreas com benefícios de incentivos fiscais sob controle da SUFRAMA)')

            class enderDest(G(ref=175, nivel=2, descricao='Dados do endereço', ocorrencias=(1, 1))):
                xLgr: str = E(ref=176, nivel=3, descricao='Logradouro', tipo='C', ocorrencias=(1, 1), tam=(2, 255), regex=ER36)
                nro: str = E(ref=177, nivel=3, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)
                xCpl: str = E(ref=178, nivel=3, descricao='Complemento', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                xBairro: str = E(ref=179, nivel=3, descricao='Bairro', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
                cMun: str = E(ref=180, nivel=3, descricao='Código do município (utilizar a tabela do IBGE)', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3, obs='Informar 9999999 para operações com o exterior.')
                xMun: str = E(ref=181, nivel=3, descricao='Nome do município', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar EXTERIOR para operações com o exterior.')
                CEP: str = E(
                    ref=182, nivel=3, descricao='CEP', tipo='C', ocorrencias=(0, 1), tam=8, regex=ER41, obs='Informar os zeros não significativos',
                    prep_regex=r'\d+'
                )
                UF: str = E(ref=183, nivel=3, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar EX para operações com o exterior.')
                cPais: str = E(ref=184, nivel=3, descricao='Código do país', tipo='N', ocorrencias=(0, 1), tam=(1, 4), regex=ER31, obs='Utilizar a tabela do BACEN')
                xPais: str = E(ref=185, nivel=3, descricao='Nome do país', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)
            email: str = E(ref=186, nivel=2, descricao='Endereço de email', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER52)

        class vPrest(G(ref=187, nivel=1, descricao='Valores da Prestação de Serviço', ocorrencias=(1, 1))):
            vTPrest: str = E(ref=188, nivel=2, descricao='Valor Total da Prestação do Serviço', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais. Pode conter zeros quando o CT-e for de complemento de ICMS')
            vRec: str = E(ref=189, nivel=2, descricao='Valor a Receber', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

            class Comp(G(ref=190, nivel=2, descricao='Componentes do Valor da Prestação', ocorrencias=(0, -1))):
                xNome: str = E(ref=191, nivel=3, descricao='Nome do componente', tipo='C', ocorrencias=(1, 1), tam=(1, 15), regex=ER36, obs='Exemplos: FRETE PESO, FRETE VALOR, SEC/CAT, ADEME, AGENDAMENTO, etc')
                vComp: str = E(ref=192, nivel=3, descricao='Valor do componente', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

        class imp(G(ref=193, nivel=1, descricao='Informações relativas aos Impostos', ocorrencias=(1, 1))):

            class ICMS(G(ref=194, nivel=2, descricao='Informações relativas ao ICMS', ocorrencias=(1, 1))):

                class ICMS00(CG(ref=195, nivel=3, descricao='Prestação sujeito à tributação normal do ICMS', ocorrencias=1)):
                    CST: int = E(ref=196, nivel=4, descricao='classificação Tributária do Serviço', tipo='N', ocorrencias=1, tam=2, dominio=D26, obs='00 - tributação normal ICMS', formato='%02d')
                    vBC: float = E(ref=197, nivel=4, descricao='Valor da BC do ICMS', tipo='N', ocorrencias=1, tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    pICMS: float = E(ref=198, nivel=4, descricao='Alíquota do ICMS', tipo='N', ocorrencias=1, tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                    vICMS: float = E(ref=199, nivel=4, descricao='Valor do ICMS', tipo='N', ocorrencias=1, tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

                class ICMS20(CG(ref=200, nivel=3, descricao='Prestação sujeito à tributação com redução de BC do ICMS', ocorrencias=(1, 1))):
                    CST: str = E(ref=201, nivel=4, descricao='Classificação Tributária do serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D27, obs='20 - tributação com BC reduzida do ICMS')
                    pRedBC: str = E(ref=202, nivel=4, descricao='Percentual de redução da BC', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER15, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                    vBC: str = E(ref=203, nivel=4, descricao='Valor da BC do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    pICMS: str = E(ref=204, nivel=4, descricao='Alíquota do ICMS', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                    vICMS: str = E(ref=205, nivel=4, descricao='Valor do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

                class ICMS45(CG(ref=206, nivel=3, descricao='ICMS Isento, não Tributado ou diferido', ocorrencias=(1, 1))):
                    CST: str = E(ref=207, nivel=4, descricao='Classificação Tributária do Serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D28, obs='Preencher com: -  ICMS isenção; - ICMS não tributada; 51 - ICMS diferido')

                class ICMS60(CG(ref=208, nivel=3, descricao='Tributação pelo ICMS60 - ICMS cobrado por substituição tributária Responsabilidade do recolhimento do ICMS atribuído ao tomador ou 3º por ST', ocorrencias=(1, 1))):
                    CST: str = E(ref=209, nivel=4, descricao='Classificação Tributária do Serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D29, obs='60 - ICMS cobrado por substituição tributária')
                    vBCSTRet: str = E(ref=210, nivel=4, descricao='Valor da BC do ICMS ST retido', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais. Valor do frete sobre o qual será calculado o ICMS a ser substituído na Prestação.')
                    vICMSSTRet: str = E(ref=211, nivel=4, descricao='Valor do ICMS ST retido', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições,  sendo  13 inteiras e 2 decimais. Resultado da multiplicação do “vBCSTRet” x “pICMSSTRet” – que será valor do ICMS a ser retido pelo Substituto. Podendo o valor do ICMS a ser retido efetivamente, sofrer ajustes conforme a opção tributaria do transportador substituído.')
                    pICMSSTRet: str = E(ref=212, nivel=4, descricao='Alíquota do ICMS', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais. Percentual de Alíquota incidente na prestação de serviço de transporte.')
                    vCred: str = E(ref=213, nivel=4, descricao='Valor do Crédito outorgado/Presumido', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo  13 inteiras e 2 decimais. Preencher somente quando o transportador substituído, for optante pelo crédito outorgado previsto no Convênio 106/96 e corresponde ao percentual de 20% do valor do ICMS ST retido.')

                class ICMS90(CG(ref=214, nivel=3, descricao='ICMS Outros', ocorrencias=(1, 1))):
                    CST: str = E(ref=215, nivel=4, descricao='Classificação Tributária do Serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D30, obs='90 - ICMS outros')
                    pRedBC: str = E(ref=216, nivel=4, descricao='Percentual de redução da BC', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER15, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                    vBC: str = E(ref=217, nivel=4, descricao='Valor da BC do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    pICMS: str = E(ref=218, nivel=4, descricao='Alíquota do ICMS', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                    vICMS: str = E(ref=219, nivel=4, descricao='Valor do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    vCred: str = E(ref=220, nivel=4, descricao='Valor do Crédito Outorgado/Presumido', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

                class ICMSOutraUF(CG(ref=221, nivel=3, descricao='ICMS devido à UF de origem da prestação, quando diferente da UF do emitente', ocorrencias=(1, 1))):
                    CST: str = E(ref=222, nivel=4, descricao='Classificação Tributária do Serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D30, obs='90 - ICMS Outra UF')
                    pRedBCOutraUF: str = E(ref=223, nivel=4, descricao='Percentual de redução da BC', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER15, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                    vBCOutraUF: str = E(ref=224, nivel=4, descricao='Valor da BC do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    pICMSOutraUF: str = E(ref=225, nivel=4, descricao='Alíquota do ICMS', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                    vICMSOutraUF: str = E(ref=226, nivel=4, descricao='Valor do ICMS devido outra UF', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

                class ICMSSN(CG(ref=227, nivel=3, descricao='Simples Nacional', ocorrencias=(1, 1))):
                    CST: str = E(ref=228, nivel=4, descricao='Classificação Tributária do Serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D30, obs='90 - ICMS Simples Nacional')
                    indSN: str = E(ref=229, nivel=4, descricao='Indica se o contribuinte é Simples Nacional 1=Sim', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D13)
            vTotTrib: str = E(ref=230, nivel=2, descricao='Valor Total dos Tributos', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
            infAdFisco: str = E(ref=231, nivel=2, descricao='Informações adicionais de interesse do Fisco', tipo='C', ocorrencias=(0, 1), tam=(1, 2000), regex=ER36, obs='Norma referenciada, informações complementares, etc')

            class ICMSUFFim(G(ref=232, nivel=2, descricao='Informações do ICMS de partilha com a UF de término do serviço de transporte na operação interestadual', ocorrencias=(0, 1))):
                vBCUFFim: str = E(ref=233, nivel=3, descricao='Valor da BC do ICMS na UF de término da prestação do serviço de transporte', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                pFCPUFFim: str = E(ref=234, nivel=3, descricao='Percentual do ICMS relativo ao Fundo de Combate à pobreza (FCP) na UF de término da prestação do serviço de transporte', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais. Alíquota adotada nas operações internas na UF do destinatário')
                pICMSUFFim: str = E(ref=235, nivel=3, descricao='Alíquota interna da UF de término da prestação do serviço de transporte', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais. Alíquota adotada nas operações internas na UF do destinatário')
                pICMSInter: str = E(ref=236, nivel=3, descricao='Alíquota interestadual das UF envolvidas', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais. Alíquota interestadual das UF envolvidas')
                vFCPUFFim: str = E(ref=237, nivel=3, descricao='Valor do ICMS relativo ao Fundo de Combate á Pobreza (FCP) da UF de término da prestação', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                vICMSUFFim: str = E(ref=238, nivel=3, descricao='Valor do ICMS de partilha para a UF de término da prestação do serviço de transporte', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                vICMSUFIni: str = E(ref=239, nivel=3, descricao='Valor do ICMS de partilha para a UF de início da prestação do serviço de transporte', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

        class infCTeNorm(CG(ref=240, nivel=1, descricao='Grupo de informações do CT-e Normal e Substituto', ocorrencias=(1, 1))):

            class infCarga(G(ref=241, nivel=2, descricao='Informações da Carga do CT- e', ocorrencias=(1, 1))):
                vCarga: str = E(ref=242, nivel=3, descricao='Valor total da carga', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais. Dever ser informado para todos os modais, com exceção para o Dutoviário.')
                proPred: str = E(ref=243, nivel=3, descricao='Produto predominante', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36, obs='Informar a descrição do produto predominante')
                xOutCat: str = E(ref=244, nivel=3, descricao='Outras características da carga', tipo='C', ocorrencias=(0, 1), tam=(1, 30), regex=ER36, obs='FRIA, "GRANEL", "REFRIGERADA", "Medidas: 12X12X12"')

                class infQ(G(ref=245, nivel=3, descricao='Informações de quantidades da Carga do CT-e', ocorrencias=(1, -1))):
                    cUnid: str = E(ref=246, nivel=4, descricao='Código da Unidade de Medida', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D21, obs='Preencher com: 00-M3; KG; TON; UNIDADE; LITROS; MMBTU', formato='%02d')
                    tpMed: str = E(ref=247, nivel=4, descricao='Tipo da Medida', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36, obs='Exemplos: PESO BRUTO, PESO DECLARADO, PESO CUBADO, PESO AFORADO, PESO AFERIDO, PESO BASE DE CÁLCULO, LITRAGEM, CAIXAS')
                    qCarga: str = E(ref=248, nivel=4, descricao='Quantidade', tipo='N', ocorrencias=(1, 1), tam=(11, 4), regex=ER21, obs='15 posições, sendo 11 inteiras e 4 decimais.')
                vCargaAverb: str = E(ref=249, nivel=3, descricao='Valor da Carga para efeito de averbação', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER28, obs='15 posições, sendo 13 inteiras e 2 decimais. Normalmente igual ao valor declarado da mercadoria, diferente por exemplo, quando a mercadoria transportada é isenta de tributos nacionais para exportação, onde é preciso averbar um valor maior, pois no caso de indenização, o valor a ser pago será maior')

            class infDoc(G(ref=250, nivel=2, descricao='Informações dos documentos transportados pelo CT-e Opcional para Redespacho Intermediario e Serviço vinculado a multimodal.', ocorrencias=(0, 1))):

                class infNF(CG(ref=251, nivel=3, descricao='Informações das NF', ocorrencias=(1, -1))):
                    nRoma: str = E(ref=252, nivel=4, descricao='Número do Romaneio da NF', tipo='C', ocorrencias=(0, 1), tam=(1, 20), regex=ER36)
                    nPed: str = E(ref=253, nivel=4, descricao='Número do Pedido da NF', tipo='C', ocorrencias=(0, 1), tam=(1, 20), regex=ER36)
                    mod: str = E(ref=254, nivel=4, descricao='Modelo da Nota Fiscal', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D7, obs='Preencher com: 01 - NF Modelo 01/1A e Avulsa; 04 - NF de Produtor')
                    serie: str = E(ref=255, nivel=4, descricao='Série', tipo='C', ocorrencias=(1, 1), tam=(1, 3), regex=ER36)
                    nDoc: str = E(ref=256, nivel=4, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
                    dEmi: str = E(ref=257, nivel=4, descricao='Data de Emissão', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11, obs='Formato AAAA-MM-DD')
                    vBC: str = E(ref=258, nivel=4, descricao='Valor da Base de Cálculo do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    vICMS: str = E(ref=259, nivel=4, descricao='Valor Total do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    vBCST: str = E(ref=260, nivel=4, descricao='Valor da Base de Cálculo do ICMS ST', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    vST: str = E(ref=261, nivel=4, descricao='Valor Total do ICMS ST', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    vProd: str = E(ref=262, nivel=4, descricao='Valor Total dos Produtos', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    vNF: str = E(ref=263, nivel=4, descricao='Valor Total da NF', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    nCFOP: str = E(ref=264, nivel=4, descricao='CFOP Predominante', tipo='N', ocorrencias=(1, 1), tam=4, regex=ER51, obs='CFOP da NF ou, na existência de mais de um, predominância pelo critério de valor econômico.')
                    nPeso: str = E(ref=265, nivel=4, descricao='Peso total em Kg', tipo='N', ocorrencias=(0, 1), tam=(12, 3), regex=ER24, obs='15 posições, sendo 12 inteiras e 3 decimais.')
                    PIN: str = E(ref=266, nivel=4, descricao='PIN SUFRAMA', tipo='N', ocorrencias=(0, 1), tam=(2, 9), regex=ER44, obs='PIN atribuído pela SUFRAMA para a operação.')
                    dPrev: str = E(ref=267, nivel=4, descricao='Data prevista de entrega', tipo='D', ocorrencias=(0, 1), tam=10, regex=ER11, obs='Formato AAAA-MM-DD')

                    class infUnidCarga(G(ref=268, nivel=4, descricao='Informações das Unidades de Carga (Containeres/ULD/Outros)', ocorrencias=(0, -1))):
                        tpUnidCarga: str = E(ref=269, nivel=5, descricao='Tipo da Unidade de Carga', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D9, obs='- Container - ULD - Pallet - Outros')
                        idUnidCarga: str = E(ref=270, nivel=5, descricao='Identificação da Unidade de Carga', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER46, obs='Informar a identificação da unidade de carga, por exemplo: número do container.')

                        class lacUnidCarga(G(ref=271, nivel=5, descricao='Lacres das Unidades de Carga', ocorrencias=(0, -1))):
                            nLacre: str = E(ref=272, nivel=6, descricao='Número do lacre', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
                        qtdRat: str = E(ref=273, nivel=5, descricao='Quantidade rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.')

                    class infUnidTransp(G(ref=274, nivel=4, descricao='Informações das Unidades de Transporte (Carreta/Reboque/Vagão)', ocorrencias=(0, -1))):
                        tpUnidTransp: str = E(ref=275, nivel=5, descricao='Tipo da Unidade de Transporte', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D8, obs='- Rodoviário Tração - Rodoviário Reboque 3 - Navio - Balsa - Aeronave - Vagão - Outros')
                        idUnidTransp: str = E(ref=276, nivel=5, descricao='Identificação da Unidade de Transporte', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER46, obs='Informar a identificação conforme o tipo de unidade de transporte. Por exemplo: para rodoviário tração ou reboque deverá preencher com a placa do veículo.')

                        class lacUnidTransp(G(ref=277, nivel=5, descricao='Lacres das Unidades de Transporte', ocorrencias=(0, -1))):
                            nLacre: str = E(ref=278, nivel=6, descricao='Número do lacre', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)

                        class infUnidCarga(G(ref=279, nivel=5, descricao='Informações das Unidades de Carga (Containeres/ULD/Outros)', ocorrencias=(0, -1))):
                            tpUnidCarga: str = E(ref=280, nivel=6, descricao='Tipo da Unidade de Carga', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D9, obs='- Container - ULD - Pallet - Outros')
                            idUnidCarga: str = E(ref=281, nivel=6, descricao='Identificação da Unidade de Carga', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER46, obs='Informar a identificação da unidade de carga, por exemplo: número do container.')

                            class lacUnidCarga(G(ref=282, nivel=6, descricao='Lacres das Unidades de Carga', ocorrencias=(0, -1))):
                                nLacre: str = E(ref=283, nivel=7, descricao='Número do lacre', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
                            qtdRat: str = E(ref=284, nivel=6, descricao='Quantidade rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                        qtdRat: str = E(ref=285, nivel=5, descricao='Quantidade rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.')

                class infNFe(CG(ref=286, nivel=3, descricao='Informações das NF-e', ocorrencias=(1, -1))):
                    chave: str = E(ref=287, nivel=4, descricao='Chave de acesso da NF-e', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)
                    PIN: str = E(ref=288, nivel=4, descricao='PIN SUFRAMA', tipo='N', ocorrencias=(0, 1), tam=(2, 9), regex=ER44, obs='PIN atribuído pela SUFRAMA para a operação.')
                    dPrev: str = E(ref=289, nivel=4, descricao='Data prevista de entrega', tipo='D', ocorrencias=(0, 1), tam=10, regex=ER11, obs='Formato AAAA-MM-DD')

                    class infUnidCarga(G(ref=290, nivel=4, descricao='Informações das Unidades de Carga (Containeres/ULD/Outros)', ocorrencias=(0, -1))):
                        tpUnidCarga: str = E(ref=291, nivel=5, descricao='Tipo da Unidade de Carga', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D9, obs='- Container - ULD - Pallet - Outros')
                        idUnidCarga: str = E(ref=292, nivel=5, descricao='Identificação da Unidade de Carga', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER46, obs='Informar a identificação da unidade de carga, por exemplo: número do container.')

                        class lacUnidCarga(G(ref=293, nivel=5, descricao='Lacres das Unidades de Carga', ocorrencias=(0, -1))):
                            nLacre: str = E(ref=294, nivel=6, descricao='Número do lacre', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
                        qtdRat: str = E(ref=295, nivel=5, descricao='Quantidade rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.')

                    class infUnidTransp(G(ref=296, nivel=4, descricao='Informações das Unidades de Transporte (Carreta/Reboque/Vagão)', ocorrencias=(0, -1))):
                        tpUnidTransp: str = E(ref=297, nivel=5, descricao='Tipo da Unidade de Transporte', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D8, obs='- Rodoviário Tração - Rodoviário Reboque 3 - Navio - Balsa - Aeronave - Vagão - Outros')
                        idUnidTransp: str = E(ref=298, nivel=5, descricao='Identificação da Unidade de Transporte', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER46, obs='Informar a identificação conforme o tipo de unidade de transporte. Por exemplo: para rodoviário tração ou reboque deverá preencher com a placa do veículo.')

                        class lacUnidTransp(G(ref=299, nivel=5, descricao='Lacres das Unidades de Transporte', ocorrencias=(0, -1))):
                            nLacre: str = E(ref=300, nivel=6, descricao='Número do lacre', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)

                        class infUnidCarga(G(ref=301, nivel=5, descricao='Informações das Unidades de Carga (Containeres/ULD/Outros)', ocorrencias=(0, -1))):
                            tpUnidCarga: str = E(ref=302, nivel=6, descricao='Tipo da Unidade de Carga', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D9, obs='- Container - ULD - Pallet - Outros')
                            idUnidCarga: str = E(ref=303, nivel=6, descricao='Identificação da Unidade de Carga', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER46, obs='Informar a identificação da unidade de carga, por exemplo: número do container.')

                            class lacUnidCarga(G(ref=304, nivel=6, descricao='Lacres das Unidades de Carga', ocorrencias=(0, -1))):
                                nLacre: str = E(ref=305, nivel=7, descricao='Número do lacre', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
                            qtdRat: str = E(ref=306, nivel=6, descricao='Quantidade rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                        qtdRat: str = E(ref=307, nivel=5, descricao='Quantidade rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.')

                class infOutros(CG(ref=308, nivel=3, descricao='Informações dos demais documentos', ocorrencias=(1, -1))):
                    tpDoc: str = E(ref=309, nivel=4, descricao='Tipo de documento originário', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D22, obs='Preencher com: 00 - Declaração; 10 - Dutoviário; 59 - CF-e SAT; 65 - NFC-e; 99 - Outros')
                    descOutros: str = E(ref=310, nivel=4, descricao='Descrição do documento', tipo='C', ocorrencias=(0, 1), tam=(1, 100), regex=ER36)
                    nDoc: str = E(ref=311, nivel=4, descricao='Número', tipo='C', ocorrencias=(0, 1), tam=(1, 20), regex=ER36)
                    dEmi: str = E(ref=312, nivel=4, descricao='Data de Emissão', tipo='D', ocorrencias=(0, 1), tam=10, regex=ER11, obs='Formato AAAA-MM-DD')
                    vDocFisc: str = E(ref=313, nivel=4, descricao='Valor do documento', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER28, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    dPrev: str = E(ref=314, nivel=4, descricao='Data prevista de entrega', tipo='D', ocorrencias=(0, 1), tam=10, regex=ER11, obs='Formato AAAA-MM-DD')

                    class infUnidCarga(G(ref=315, nivel=4, descricao='Informações das Unidades de Carga (Containeres/ULD/Outros)', ocorrencias=(0, -1))):
                        tpUnidCarga: str = E(ref=316, nivel=5, descricao='Tipo da Unidade de Carga', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D9, obs='- Container - ULD - Pallet - Outros')
                        idUnidCarga: str = E(ref=317, nivel=5, descricao='Identificação da Unidade de Carga', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER46, obs='Informar a identificação da unidade de carga, por exemplo: número do container.')

                        class lacUnidCarga(G(ref=318, nivel=5, descricao='Lacres das Unidades de Carga', ocorrencias=(0, -1))):
                            nLacre: str = E(ref=319, nivel=6, descricao='Número do lacre', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
                        qtdRat: str = E(ref=320, nivel=5, descricao='Quantidade rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.')

                    class infUnidTransp(G(ref=321, nivel=4, descricao='Informações das Unidades de Transporte (Carreta/Reboque/Vagão)', ocorrencias=(0, -1))):
                        tpUnidTransp: str = E(ref=322, nivel=5, descricao='Tipo da Unidade de Transporte', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D8, obs='- Rodoviário Tração - Rodoviário Reboque 3 - Navio - Balsa - Aeronave - Vagão - Outros')
                        idUnidTransp: str = E(ref=323, nivel=5, descricao='Identificação da Unidade de Transporte', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER46, obs='Informar a identificação conforme o tipo de unidade de transporte. Por exemplo: para rodoviário tração ou reboque deverá preencher com a placa do veículo.')

                        class lacUnidTransp(G(ref=324, nivel=5, descricao='Lacres das Unidades de Transporte', ocorrencias=(0, -1))):
                            nLacre: str = E(ref=325, nivel=6, descricao='Número do lacre', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)

                        class infUnidCarga(G(ref=326, nivel=5, descricao='Informações das Unidades de Carga (Containeres/ULD/Outros)', ocorrencias=(0, -1))):
                            tpUnidCarga: str = E(ref=327, nivel=6, descricao='Tipo da Unidade de Carga', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D9, obs='- Container - ULD - Pallet - Outros')
                            idUnidCarga: str = E(ref=328, nivel=6, descricao='Identificação da Unidade de Carga', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER46, obs='Informar a identificação da unidade de carga, por exemplo: número do container.')

                            class lacUnidCarga(G(ref=329, nivel=6, descricao='Lacres das Unidades de Carga', ocorrencias=(0, -1))):
                                nLacre: str = E(ref=330, nivel=7, descricao='Número do lacre', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
                            qtdRat: str = E(ref=331, nivel=6, descricao='Quantidade rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                        qtdRat: str = E(ref=332, nivel=5, descricao='Quantidade rateada (Peso,Volume)', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER14, obs='5 posições, sendo 3 inteiras e 2 decimais.')

            class docAnt(G(ref=333, nivel=2, descricao='Documentos de Transporte Anterior', ocorrencias=(0, 1))):

                class emiDocAnt(G(ref=334, nivel=3, descricao='Emissor do documento anterior', ocorrencias=(1, -1))):
                    CNPJ: str = CampoCNPJ(ref=335, nivel=4, descricao='Número do CNPJ', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER8, obs='Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros. Informar os zeros não significativos.')
                    CPF: str = CampoCPF(ref=336, nivel=4, descricao='Número do CPF', tipo='C', ocorrencias=(0, 1), tam=11, regex=ER9, obs='Informar os zeros não significativos.')
                    IE: str = E(ref=337, nivel=4, descricao='Inscrição Estadual', tipo='N', ocorrencias=(1, 1), tam=14, regex=ER29, prep_regex=r'\d+')
                    UF: str = E(ref=338, nivel=4, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar EX para operações com o exterior.')
                    xNome: str = E(ref=339, nivel=4, descricao='Razão Social ou Nome do expedidor', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)

                    class idDocAnt(G(ref=340, nivel=4, descricao='Informações de identificação dos documentos de Transporte Anterior', ocorrencias=(1, 2))):

                        class idDocAntPap(CG(ref=341, nivel=5, descricao='Documentos de transporte anterior em papel', ocorrencias=(1, -1))):
                            tpDoc: str = E(ref=342, nivel=6, descricao='Tipo do Documento de Transporte Anterior', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D32, obs='Preencher com: 07-ATRE; DTA (Despacho de Transito Aduaneiro); Conhecimento Aéreo Internacional; – Conhecimento - Carta de Porte Internacional; – Conhecimento Avulso; 12-TIF (Transporte Internacional Ferroviário); 13- BL (Bill of Lading)')
                            serie: str = E(ref=343, nivel=6, descricao='Série do Documento Fiscal', tipo='C', ocorrencias=(1, 1), tam=(1, 3), regex=ER36)
                            subser: str = E(ref=344, nivel=6, descricao='Série do Documento Fiscal', tipo='C', ocorrencias=(0, 1), tam=(1, 2), regex=ER36)
                            nDoc: str = E(ref=345, nivel=6, descricao='Número do Documento Fiscal', tipo='C', ocorrencias=(1, 1), tam=(1, 30), regex=ER36)
                            dEmi: str = E(ref=346, nivel=6, descricao='Data de emissão (AAAA-MM- DD)', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11)

                        class idDocAntEle(CG(ref=347, nivel=5, descricao='Documentos de transporte anterior eletrônicos', ocorrencias=(1, -1))):
                            chCTe: str = E(ref=348, nivel=6, descricao='Chave de acesso do CT-e', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)

            class infModal(G(ref=349, nivel=2, descricao='Informações do modal', ocorrencias=(1, 1))):
                versaoModal: str = A(ref=350, nivel=3, descricao='Versão do leiaute específico para o Modal', tipo='N', ocorrencias=(1, 1), tam='1-2v2', regex=ER45, default=3)

                rodo = rodo()
                aereo = aereo()
                aquav = aquav()
                ferrov = ferrov()

            class veicNovos(G(ref=352, nivel=2, descricao='informações dos veículos transportados', ocorrencias=(0, -1))):
                chassi: str = E(ref=353, nivel=3, descricao='Chassi do veículo', tipo='C', ocorrencias=(1, 1), tam=17, regex=ER46)
                cCor: str = E(ref=354, nivel=3, descricao='Cor do veículo', tipo='C', ocorrencias=(1, 1), tam=(1, 4), regex=ER36, obs='Código de cada montadora')
                xCor: str = E(ref=355, nivel=3, descricao='Descrição da cor', tipo='C', ocorrencias=(1, 1), tam=(1, 40), regex=ER36)
                cMod: str = E(ref=356, nivel=3, descricao='Código Marca Modelo', tipo='C', ocorrencias=(1, 1), tam=(1, 6), regex=ER36, obs='Utilizar tabela RENAVAM')
                vUnit: str = E(ref=357, nivel=3, descricao='Valor Unitário do Veículo', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                vFrete: str = E(ref=358, nivel=3, descricao='Frete Unitário', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

            class cobr(G(ref=359, nivel=2, descricao='Dados da cobrança do CT-e', ocorrencias=(0, 1))):

                class fat(G(ref=360, nivel=3, descricao='Dados da fatura', ocorrencias=(0, 1))):
                    nFat: str = E(ref=361, nivel=4, descricao='Número da fatura', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                    vOrig: str = E(ref=362, nivel=4, descricao='Valor original da fatura', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER28, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    vDesc: str = E(ref=363, nivel=4, descricao='Valor do desconto da fatura', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER28, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    vLiq: str = E(ref=364, nivel=4, descricao='Valor líquido da fatura', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER28, obs='15 posições, sendo 13 inteiras e 2 decimais.')

                class dup(G(ref=365, nivel=3, descricao='Dados das duplicatas', ocorrencias=(0, -1))):
                    nDup: str = E(ref=366, nivel=4, descricao='Número da duplicata', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                    dVenc: str = E(ref=367, nivel=4, descricao='Data de vencimento da duplicata (AAAA-MM-DD)', tipo='D', ocorrencias=(0, 1), tam=10, regex=ER11)
                    vDup: str = E(ref=368, nivel=4, descricao='Valor da duplicata', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER28, obs='15 posições, sendo 13 inteiras e 2 decimais.')

            class infCteSub(G(ref=369, nivel=2, descricao='Informações do CT-e de substituição', ocorrencias=(0, 1))):
                chCte: str = E(ref=370, nivel=3, descricao='Chave de acesso do CT-e a ser substituído (original)', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)
                refCteAnu: str = CE(ref=371, nivel=3, descricao='Chave de acesso do CT-e de Anulação', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)

                class tomaICMS(CG(ref=372, nivel=3, descricao='Tomador é contribuinte do ICMS, mas não é emitente de documento fiscal eletrônico', ocorrencias=(1, 1))):
                    refNFe: str = CE(ref=373, nivel=4, descricao='Chave de acesso da NF-e emitida pelo Tomador', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)

                    class refNF(CG(ref=374, nivel=4, descricao='Informação da NF ou CT emitido pelo Tomador', ocorrencias=(1, 1))):
                        CNPJ: str = CampoCNPJ(ref=375, nivel=5, descricao='CNPJ do Emitente', tipo='N', ocorrencias=(0, 1), tam=14, regex=ER5, obs='Informar o CNPJ do emitente do Documento Fiscal')
                        CPF: str = CampoCPF(ref=376, nivel=5, descricao='Número do CPF', tipo='N', ocorrencias=(0, 1), tam=11, regex=ER9, obs='Informar o CPF do emitente do documento fiscal')
                        mod: str = E(ref=377, nivel=5, descricao='Modelo do Documento Fiscal', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D33)
                        serie: str = E(ref=378, nivel=5, descricao='Serie do documento fiscal', tipo='N', ocorrencias=(1, 1), tam=(1, 3), regex=ER34)
                        subserie: str = E(ref=379, nivel=5, descricao='Subserie do documento fiscal', tipo='N', ocorrencias=(0, 1), tam=(1, 3), regex=ER34)
                        nro: str = E(ref=380, nivel=5, descricao='Número do documento fiscal', tipo='N', ocorrencias=(1, 1), tam=(1, 6), regex=ER47)
                        valor: str = E(ref=381, nivel=5, descricao='Valor do documento fiscal.', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                        dEmi: str = E(ref=382, nivel=5, descricao='Data de emissão do documento fiscal.', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11)
                    refCte: str = CE(ref=383, nivel=4, descricao='Chave de acesso do CT-e emitido pelo Tomador', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)
                indAlteraToma: str = E(ref=384, nivel=3, descricao='Indicador de CT-e Alteração de Tomador', tipo='N', ocorrencias=(0, 1), tam=1, dominio=D13)

            class infGlobalizado(G(ref=385, nivel=2, descricao='Informações do CT-e Globalizado', ocorrencias=(0, 1))):
                xObs: str = E(ref=386, nivel=3, descricao='Preencher com informações adicionais, legislação do regime especial, etc', tipo='C', ocorrencias=(1, 1), tam=(15, 256), regex=ER36)

            class infServVinc(G(ref=387, nivel=2, descricao='Informações do Serviço Vinculado a Multimodal', ocorrencias=(0, 1))):

                class infCTeMultimodal(G(ref=388, nivel=3, descricao='informações do CT-e multimodal vinculado', ocorrencias=(1, -1))):
                    chCTeMultimodal: str = E(ref=389, nivel=4, descricao='Chave de acesso do CT-e Multimodal', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)

        class infCteComp(CG(ref=390, nivel=1, descricao='Detalhamento do CT-e complementado', ocorrencias=(1, 1))):
            chCTe: str = E(ref=391, nivel=2, descricao='Chave do CT-e complementado', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)

        class infCteAnu(CG(ref=392, nivel=1, descricao='Detalhamento do CT-e do tipo Anulação', ocorrencias=(1, 1))):
            chCte: str = E(ref=393, nivel=2, descricao='Chave de acesso do CT-e original a ser anulado e substituído', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)
            dEmi: str = E(ref=394, nivel=2, descricao='Data de emissão da declaração do tomador não contribuinte do ICMS', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11)

        class autXML(G(ref=395, nivel=1, descricao='Autorizados para download do XML do DF-e', ocorrencias=(0, 10))):
            CNPJ: str = CampoCNPJ(ref=396, nivel=2, descricao='CNPJ do autorizado', tipo='N', ocorrencias=(0, 1), tam=14, regex=ER5, obs='Informar zeros não significativos')
            CPF: str = CampoCPF(ref=397, nivel=2, descricao='CPF do autorizado', tipo='N', ocorrencias=(0, 1), tam=11, regex=ER9, obs='Informar zeros não significativos')

        class infRespTec(G(ref=398, nivel=1, descricao='Informações do Responsável Técnico pela emissão do DF-e', ocorrencias=(0, 1))):
            CNPJ: str = CampoCNPJ(ref=399, nivel=2, descricao='CNPJ da pessoa jurídica responsável técnica pelo sistema utilizado na emissão do documento fiscal eletrônico', tipo='N', ocorrencias=(1, 1), tam=14, regex=ER5, obs='Informar o CNPJ da pessoa jurídica desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico.')
            xContato: str = E(ref=400, nivel=2, descricao='Nome da pessoa a ser contatada', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar o nome da pessoa a ser contatada na empresa desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico. No caso de pessoa física, informar o respectivo nome.')
            email: str = E(ref=401, nivel=2, descricao='E-mail da pessoa jurídica a ser contatada', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER52)
            fone: str = E(ref=402, nivel=2, descricao='Telefone da pessoa jurídica a ser contatada', tipo='C', ocorrencias=(1, 1), tam=(7, 12), regex=ER6, obs='Preencher com o Código DDD + número do telefone.', prep_regex=r'\d+')
            idCSRT: str = E(ref=403, nivel=2, descricao='Identificador do código de segurança do responsável técnico', tipo='N', ocorrencias=(1, 1), tam=3, regex=ER35, obs='Identificador do CSRT utilizado para geração do hash')
            hashCSRT: str = E(ref=404, nivel=2, descricao='Hash do token do código de segurança do responsável técnico', tipo='C', ocorrencias=(1, 1), tam=28, obs='O hashCSRT é o resultado das funções SHA-1 e base64 do token CSRT fornecido pelo fisco + chave de acesso do DF-e. (Implementação em futura NT)  Observação: 28 caracteres são representados no schema como 20 bytes do tipo base64Binary')

    class infCTeSupl(G(ref=405, nivel=0, descricao='Informações suplementares do CT-e', ocorrencias=(0, 1))):
        qrCodCTe: str = E(ref=406, nivel=1, descricao='Texto com o QR-Code impresso no DACTE', tipo='CDATA', ocorrencias=1, tam=(50, 1000), regex=ER64)

    signature = Signature()




#### CTe Outros Serviços

class infCteOs(G(ref=2, nivel=0, descricao='Informações do CT-e Outros Serviços', ocorrencias=(1, 1))):
    versao: str = A(ref=3, nivel=1, descricao='Versão do leiaute', tipo='N', ocorrencias=(1, 1), tam=None, regex=ER57, obs='Ex: "3.00"')
    Id: str = A(ref=4, nivel=1, descricao='Identificador da tag a ser assinada', tipo='C', ocorrencias=(1, 1), tam=47, regex=ER48, obs='Informar a chave de acesso do CT-e OS e precedida do literal "CTe"')

    class ide(G(ref=5, nivel=1, descricao='Identificação do CT-e Outros Serviços', ocorrencias=(1, 1))):
        cUF: str = E(ref=6, nivel=2, descricao='Código da UF do emitente do CT-e.', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D2, obs='Utilizar a Tabela do IBGE.')
        cCT: str = E(ref=7, nivel=2, descricao='Código numérico que compõe a Chave de Acesso.', tipo='N', ocorrencias=(1, 1), tam=8, regex=ER41, obs='Número aleatório gerado pelo emitente para cada CT-e, com o objetivo de evitar acessos indevidos ao documento.')
        CFOP: str = E(ref=8, nivel=2, descricao='Código Fiscal de Operações e Prestações', tipo='N', ocorrencias=(1, 1), tam=4, regex=ER51)
        natOp: str = E(ref=9, nivel=2, descricao='Natureza da Operação', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)
        mod: str = E(ref=10, nivel=2, descricao='Modelo do documento fiscal', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D4, obs='Utilizar o código 67 para identificação do CT-e Outros Serviços, emitido em substituição a Nota Fiscal Modelo 7 para transporte de pessoas, valores e excesso de bagagem.')
        serie: str = E(ref=11, nivel=2, descricao='Série do CT-e OS', tipo='N', ocorrencias=(1, 1), tam=(1, 3), regex=ER34, obs='Preencher com "0" no caso de série única')
        nCT: str = E(ref=12, nivel=2, descricao='Número do CT-e OS', tipo='N', ocorrencias=(1, 1), tam=(1, 9), regex=ER32)
        dhEmi: str = E(ref=13, nivel=2, descricao='Data e hora de emissão do CT-e OS', tipo='C', ocorrencias=(1, 1), tam=21, regex=ER1, obs='Formato AAAA-MM-DDTHH:MM:DD TZD')
        tpImp: str = E(ref=14, nivel=2, descricao='Formato de impressão do DACTE OS', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D1, obs='Preencher com: 1 - Retrato; 2 - Paisagem.')
        tpEmis: str = E(ref=15, nivel=2, descricao='Forma de emissão do CT-e', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D23, obs='Preencher com: 1 - Normal; 5 - Contingência FSDA; 7 - Autorização pela SVC-RS; 8 - Autorização pela SVC-SP')
        cDV: str = E(ref=16, nivel=2, descricao='Digito Verificador da chave de acesso do CT-e', tipo='N', ocorrencias=(1, 1), tam=1, regex=ER42, obs='Informar o dígito de controle da chave de acesso do CT-e, que deve ser calculado com a aplicação do algoritmo módulo 11 (base 2,9) da chave de acesso.')
        tpAmb: str = E(ref=17, nivel=2, descricao='Tipo do Ambiente', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D1, obs='Preencher com: 1 - Produção; 2 - Homologação')
        tpCTe: str = E(ref=18, nivel=2, descricao='Tipo do CT-e OS', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D17, obs='Preencher com: 0 - CT-e Normal; 1 - CT-e complementar; 2 – CT-e de Anulação; 3 – CT-e de Substituição')
        procEmi: str = E(ref=19, nivel=2, descricao='Identificador do processo de emissão do CT-e OS', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D36, obs='Preencher com: 0 - emissão de CT-e com aplicativo do contribuinte; 3- emissão CT-e pelo contribuinte com aplicativo fornecido pelo Fisco.')
        verProc: str = E(ref=20, nivel=2, descricao='Versão do processo de emissão', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36, obs='Informar a versão do aplicativo emissor de CT-e.')
        cMunEnv: str = E(ref=21, nivel=2, descricao='Código do Município de envio do CT-e (de onde o documento foi transmitido)', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3, obs='Utilizar a tabela do IBGE. Informar 9999999 para as operações com o exterior.')
        xMunEnv: str = E(ref=22, nivel=2, descricao='Nome do Município de envio do CT-e (de onde o documento foi transmitido)', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar PAIS/Município para as operações com o exterior.')
        UFEnv: str = E(ref=23, nivel=2, descricao='Sigla da UF de envio do CT-e (de onde o documento foi transmitido)', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar "EX" para operações com o exterior.')
        modal: str = E(ref=24, nivel=2, descricao='Modal do CT-e OS', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D34, obs='Preencher com: 01-Rodoviário; 02- Aéreo; – Aquaviário; - Ferroviário', formato='%02d')
        tpServ: str = E(ref=25, nivel=2, descricao='Tipo do Serviço', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D24, obs='Preencher com: 6 - Transporte de Pessoas; 7 - Transporte de Valores; 8 - Excesso de Bagagem')
        indIEToma: str = E(ref=26, nivel=2, descricao='Indicador da IE do tomador: 1 – Contribuinte ICMS; 2 – Contribuinte isento de inscrição; 9 – Não Contribuinte', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D16, obs='Aplica-se ao tomador que for indicado no toma3 ou toma4')
        cMunIni: str = E(ref=27, nivel=2, descricao='Código do Município de início da prestação', tipo='N', ocorrencias=(0, 1), tam=7, regex=ER3, obs='Utilizar a tabela do IBGE. Informar 9999999 para operações com o exterior.')
        xMunIni: str = E(ref=28, nivel=2, descricao='Nome do Município do início da prestação', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36, obs='Informar "EXTERIOR" para operações com o exterior.')
        UFIni: str = E(ref=29, nivel=2, descricao='UF do início da prestação', tipo='C', ocorrencias=(0, 1), tam=2, dominio=D10, obs='Informar "EX" para operações com o exterior.')
        cMunFim: str = E(ref=30, nivel=2, descricao='Código do Município de término da prestação', tipo='N', ocorrencias=(0, 1), tam=7, regex=ER3, obs='Utilizar a tabela do IBGE. Informar 9999999 para operações com o exterior.')
        xMunFim: str = E(ref=31, nivel=2, descricao='Nome do Município do término da prestação', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36, obs='Informar "EXTERIOR" para operações com o exterior.')
        UFFim: str = E(ref=32, nivel=2, descricao='UF do término da prestação', tipo='C', ocorrencias=(0, 1), tam=2, dominio=D10, obs='Informar "EX" para operações com o exterior.')

        class infPercurso(G(ref=33, nivel=2, descricao='Informações do Percurso do CT-e Outros Serviços', ocorrencias=(0, 25))):
            UFPer: str = E(ref=34, nivel=3, descricao='Sigla das Unidades da Federação do percurso do veículo.', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Não é necessário repetir as UF de Início e Fim')
        dhCont: str = E(ref=35, nivel=2, descricao='Data e Hora da entrada em contingência', tipo='C', ocorrencias=(1, 1), tam=21, regex=ER1, obs='Informar a data e hora no formato AAAA- MM-DDTHH:MM:SS')
        xJust: str = E(ref=36, nivel=2, descricao='Justificativa da entrada em contingência', tipo='C', ocorrencias=(1, 1), tam=(15, 256), regex=ER36)

    class compl(G(ref=37, nivel=1, descricao='Dados complementares do CT-e para fins operacionais ou comerciais', ocorrencias=(0, 1))):
        xCaracAd: str = E(ref=38, nivel=2, descricao='Característica adicional do transporte', tipo='C', ocorrencias=(0, 1), tam=(1, 15), regex=ER36, obs='Texto livre: REENTREGA; DEVOLUÇÃO; REFATURAMENTO; etc')
        xCaracSer: str = E(ref=39, nivel=2, descricao='Característica adicional do serviço', tipo='C', ocorrencias=(0, 1), tam=(1, 30), regex=ER36, obs='Texto livre: ENTREGA EXPRESSA; LOGÍSTICA REVERSA; CONVENCIONAL; EMERGENCIAL; etc')
        xEmi: str = E(ref=40, nivel=2, descricao='Funcionário emissor do CTe', tipo='C', ocorrencias=(0, 1), tam=(1, 20), regex=ER36)
        xObs: str = E(ref=41, nivel=2, descricao='Observações Gerais', tipo='C', ocorrencias=(0, 1), tam=(1, 2000), regex=ER36)

        class ObsCont(G(ref=42, nivel=2, descricao='Campo de uso livre do contribuinte', ocorrencias=(0, 10))):
            xCampo: str = A(ref=43, nivel=3, descricao='Identificação do campo', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
            xTexto: str = E(ref=44, nivel=3, descricao='Conteúdo do campo', tipo='C', ocorrencias=(1, 1), tam=(1, 160), regex=ER36)

        class ObsFisco(G(ref=45, nivel=2, descricao='Campo de uso livre do contribuinte', ocorrencias=(0, 10))):
            xCampo: str = A(ref=46, nivel=3, descricao='Identificação do campo', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
            xTexto: str = E(ref=47, nivel=3, descricao='Conteúdo do campo', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)

    class emit(G(ref=48, nivel=1, descricao='Identificação do Emitente do CT-e OS', ocorrencias=(1, 1))):
        CNPJ: str = CampoCNPJ(ref=49, nivel=2, descricao='CNPJ do emitente', tipo='N', ocorrencias=(1, 1), tam=14, regex=ER5, obs='Informar zeros não significativos')
        IE: str = E(ref=50, nivel=2, descricao='Inscrição Estadual do Emitente', tipo='N', ocorrencias=(1, 1), tam=14, regex=ER29, prep_regex=r'\d+')
        IEST: str = E(ref=51, nivel=2, descricao='Inscrição Estadual do Substituto Tributário', tipo='N', ocorrencias=(0, 1), tam=14, regex=ER29, prep_regex=r'\d+')
        xNome: str = E(ref=52, nivel=2, descricao='Razão social ou Nome do emitente', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
        xFant: str = E(ref=53, nivel=2, descricao='Nome fantasia', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)

        class enderEmit(G(ref=54, nivel=2, descricao='Endereço do emitente', ocorrencias=(1, 1))):
            xLgr: str = E(ref=55, nivel=3, descricao='Logradouro', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
            nro: str = E(ref=56, nivel=3, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)
            xCpl: str = E(ref=57, nivel=3, descricao='Complemento', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
            xBairro: str = E(ref=58, nivel=3, descricao='Bairro', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
            cMun: str = E(ref=59, nivel=3, descricao='Código do município (utilizar a tabela do IBGE)', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3)
            xMun: str = E(ref=60, nivel=3, descricao='Nome do município', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
            CEP: str = E(ref=61, nivel=3, descricao='CEP', tipo='N', ocorrencias=(0, 1), tam=8, regex=ER41, obs='Informar zeros não significativos', prep_regex=r'\d+')
            UF: str = E(ref=62, nivel=3, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D11)
            fone: str = E(ref=63, nivel=3, descricao='Telefone', tipo='C', ocorrencias=(0, 1), tam=(6, 14), regex=ER6, prep_regex=r'\d+')

    class toma(G(ref=64, nivel=1, descricao='Informações do Tomador/Usuário do Serviço', ocorrencias=(0, 1))):
        CNPJ: str = CampoCNPJ(ref=65, nivel=2, descricao='Número do CNPJ', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER8, obs='Em caso de empresa não estabelecida no Brasil, será informado o CNPJ com zeros. Informar os zeros não significativos.')
        CPF: str = CampoCPF(ref=66, nivel=2, descricao='Número do CPF', tipo='C', ocorrencias=(0, 1), tam=11, regex=ER9, obs='Informar os zeros não significativos.')
        IE: str = E(ref=67, nivel=2, descricao='Inscrição Estadual', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER30, obs='Informar a IE do tomador ou ISENTO se tomador é contribuinte do ICMS isento de inscrição no cadastro de contribuintes do ICMS. Caso o tomador não seja contribuinte do ICMS não informar o conteúdo.', prep_regex=r'\d+')
        xNome: str = E(ref=68, nivel=2, descricao='Razão social ou nome do tomador', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
        xFant: str = E(ref=69, nivel=2, descricao='Nome fantasia', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)
        fone: str = E(ref=70, nivel=2, descricao='Telefone', tipo='C', ocorrencias=(0, 1), tam=(6, 14), regex=ER6, prep_regex=r'\d+')

        class enderToma(G(ref=71, nivel=2, descricao='Dados do endereço', ocorrencias=(1, 1))):
            xLgr: str = E(ref=72, nivel=3, descricao='Logradouro', tipo='C', ocorrencias=(1, 1), tam=(2, 255), regex=ER36)
            nro: str = E(ref=73, nivel=3, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER36)
            xCpl: str = E(ref=74, nivel=3, descricao='Complemento', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
            xBairro: str = E(ref=75, nivel=3, descricao='Bairro', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
            cMun: str = E(ref=76, nivel=3, descricao='Código do município (utilizar a tabela do IBGE)', tipo='N', ocorrencias=(1, 1), tam=7, regex=ER3, obs='Informar 9999999 para operações com o exterior.')
            xMun: str = E(ref=77, nivel=3, descricao='Nome do município', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar EXTERIOR para operações com o exterior.')
            CEP: str = E(ref=78, nivel=3, descricao='CEP', tipo='C', ocorrencias=(0, 1), tam=8, regex=ER41, obs='Informar os zeros não significativos', prep_regex=r'\d+')
            UF: str = E(ref=79, nivel=3, descricao='Sigla da UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10, obs='Informar EX para operações com o exterior.')
            cPais: str = E(ref=80, nivel=3, descricao='Código do país', tipo='N', ocorrencias=(0, 1), tam=(1, 4), regex=ER31, obs='Utilizar a tabela do BACEN')
            xPais: str = E(ref=81, nivel=3, descricao='Nome do país', tipo='C', ocorrencias=(0, 1), tam=(2, 60), regex=ER36)
        email: str = E(ref=82, nivel=2, descricao='Endereço de email', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER52)

    class vPrest(G(ref=83, nivel=1, descricao='Valores da Prestação de Serviço', ocorrencias=(1, 1))):
        vTPrest: str = E(ref=84, nivel=2, descricao='Valor Total da Prestação do Serviço', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais. Pode conter zeros quando o CT-e for de complemento de ICMS')
        vRec: str = E(ref=85, nivel=2, descricao='Valor a Receber', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

        class Comp(G(ref=86, nivel=2, descricao='Componentes do Valor da Prestação', ocorrencias=(0, -1))):
            xNome: str = E(ref=87, nivel=3, descricao='Nome do componente', tipo='C', ocorrencias=(1, 1), tam=(1, 15), regex=ER36, obs='Exxemplos: FRETE PESO, FRETE VALOR, SEC/CAT, ADEME, AGENDAMENTO, etc')
            vComp: str = E(ref=88, nivel=3, descricao='Valor do componente', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

    class imp(G(ref=89, nivel=1, descricao='Informações relativas aos Impostos', ocorrencias=1)):

        class ICMS(G(ref=90, nivel=2, descricao='Informações relativas ao ICMS', ocorrencias=1)):

            class ICMS00(CG(ref=91, nivel=3, descricao='Prestação sujeito à tributação normal do ICMS', ocorrencias=1)):
                CST: float = E(ref=92, nivel=4, descricao='classificação Tributária do Serviço', tipo='N', ocorrencias=1, tam=2, dominio=D26, obs='00 - tributação normal ICMS', formato='%02d')
                vBC: float = E(ref=93, nivel=4, descricao='Valor da BC do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                pICMS: float = E(ref=94, nivel=4, descricao='Alíquota do ICMS', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                vICMS: float = E(ref=95, nivel=4, descricao='Valor do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

            class ICMS20(CG(ref=96, nivel=3, descricao='Prestação sujeito à tributação com redução de BC do ICMS', ocorrencias=(1, 1))):
                CST: float = E(ref=97, nivel=4, descricao='Classificação Tributária do serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D27, obs='20 - tributação com BC reduzida do ICMS')
                pRedBC: float = E(ref=98, nivel=4, descricao='Percentual de redução da BC', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER15, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                vBC: float = E(ref=99, nivel=4, descricao='Valor da BC do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                pICMS: float = E(ref=100, nivel=4, descricao='Alíquota do ICMS', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                vICMS: float = E(ref=101, nivel=4, descricao='Valor do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

            class ICMS45(CG(ref=102, nivel=3, descricao='ICMS Isento, não Tributado ou diferido', ocorrencias=(1, 1))):
                CST: str = E(ref=103, nivel=4, descricao='Classificação Tributária do Serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D28, obs='Preencher com: - ICMS isenção; - ICMS não tributada; 51 - ICMS diferido.')

            class ICMS90(CG(ref=104, nivel=3, descricao='ICMS Outros', ocorrencias=(1, 1))):
                CST: str = E(ref=105, nivel=4, descricao='Classificação Tributária do Serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D30, obs='90 - Outros')
                pRedBC: str = E(ref=106, nivel=4, descricao='Percentual de redução da BC', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER15, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                vBC: str = E(ref=107, nivel=4, descricao='Valor da BC do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                pICMS: str = E(ref=108, nivel=4, descricao='Alíquota do ICMS', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                vICMS: str = E(ref=109, nivel=4, descricao='Valor do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                vCred: str = E(ref=110, nivel=4, descricao='Valor do Crédito Outorgado/Presumido', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

            class ICMSOutraUF(CG(ref=111, nivel=3, descricao='ICMS devido à UF de origem da prestação, quando diferente da UF do emitente', ocorrencias=(1, 1))):
                CST: str = E(ref=112, nivel=4, descricao='Classificação Tributária do Serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D30, obs='90 - ICMS Outra UF')
                pRedBCOutraUF: str = E(ref=113, nivel=4, descricao='Percentual de redução da BC', tipo='N', ocorrencias=(0, 1), tam=(3, 2), regex=ER15, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                vBCOutraUF: str = E(ref=114, nivel=4, descricao='Valor da BC do ICMS', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                pICMSOutraUF: str = E(ref=115, nivel=4, descricao='Alíquota do ICMS', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais.')
                vICMSOutraUF: str = E(ref=116, nivel=4, descricao='Valor do ICMS devido outra UF', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

            class ICMSSN(CG(ref=117, nivel=3, descricao='Simples Nacional', ocorrencias=(1, 1))):
                CST: str = E(ref=118, nivel=4, descricao='Classificação Tributária do Serviço', tipo='N', ocorrencias=(1, 1), tam=2, dominio=D30, obs='90 - ICMS Simples Nacional')
                indSN: str = E(ref=119, nivel=4, descricao='Indica se o contribuinte é Simples Nacional 1=Sim', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D13)
        vTotTrib: str = E(ref=120, nivel=2, descricao='Valor Total dos Tributos', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
        infAdFisco: str = E(ref=121, nivel=2, descricao='Informações adicionais de interesse do Fisco', tipo='C', ocorrencias=(0, 1), tam=(1, 2000), regex=ER36, obs='Norma referenciada, informações complementares, etc')

        class ICMSUFFim(G(ref=122, nivel=2, descricao='Informações do ICMS de partilha com a UF de término do serviço de transporte na operação interestadual', ocorrencias=(0, 1))):
            vBCUFFim: str = E(ref=123, nivel=3, descricao='Valor da BC do ICMS na UF de término da prestação do serviço de transporte', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
            pFCPUFFim: str = E(ref=124, nivel=3, descricao='Percentual do ICMS relativo ao Fundo de Combate à pobreza (FCP) na UF de término da prestação do serviço de transporte', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais. Alíquota adotada nas operações internas na UF do destinatário')
            pICMSUFFim: str = E(ref=125, nivel=3, descricao='Alíquota interna da UF de término da prestação do serviço de transporte', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais. Alíquota adotada nas operações internas na UF do destinatário')
            pICMSInter: str = E(ref=126, nivel=3, descricao='Alíquota interestadual das UF envolvidas', tipo='N', ocorrencias=(1, 1), tam=(3, 2), regex=ER12, obs='5 posições, sendo 3 inteiras e 2 decimais. Alíquota interestadual das UF envolvidas')
            vFCPUFFim: str = E(ref=127, nivel=3, descricao='Valor do ICMS relativo ao Fundo de Combate á Pobreza (FCP) da UF de término da prestação', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
            vICMSUFFim: str = E(ref=128, nivel=3, descricao='Valor do ICMS de partilha para a UF de término da prestação do serviço de transporte', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
            vICMSUFIni: str = E(ref=129, nivel=3, descricao='Valor do ICMS de partilha para a UF de início da prestação do serviço de transporte', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

        class infTribFed(G(ref=130, nivel=2, descricao='Informações dos tributos federais', ocorrencias=(0, 1))):
            vPIS: str = E(ref=131, nivel=3, descricao='Valor do PIS', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
            vCOFINS: str = E(ref=132, nivel=3, descricao='Valor COFINS', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
            vIR: str = E(ref=133, nivel=3, descricao='Valor de Imposto de Renda', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
            vINSS: str = E(ref=134, nivel=3, descricao='Valor do INSS', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
            vCSLL: str = E(ref=135, nivel=3, descricao='Valor do CSLL', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

    class infCTeNorm(CG(ref=136, nivel=1, descricao='Grupo de informações do CT-e OS Normal', ocorrencias=(1, 1))):

        class infServico(G(ref=137, nivel=2, descricao='Informações da Prestação do Serviço', ocorrencias=(1, 1))):
            xDescServ: str = E(ref=138, nivel=3, descricao='Descrição do Serviço prestado', tipo='C', ocorrencias=(1, 1), tam=(1, 30), regex=ER36)

            class infQ(G(ref=139, nivel=3, descricao='Informações de quantidades da Carga do CT-e', ocorrencias=(0, 1))):
                qCarga: str = E(ref=140, nivel=4, descricao='Quantidade', tipo='N', ocorrencias=(1, 1), tam=(11, 4), regex=ER21, obs='15 posições, sendo 11 inteiras e 4 decimais.')

        class infDocRef(G(ref=141, nivel=2, descricao='Informações dos documentos referenciados', ocorrencias=(0, -1))):
            nDoc: str = E(ref=142, nivel=3, descricao='Número', tipo='C', ocorrencias=(1, 1), tam=(1, 20), regex=ER36)
            serie: str = E(ref=143, nivel=3, descricao='Série', tipo='C', ocorrencias=(0, 1), tam=(1, 3), regex=ER36)
            subserie: str = E(ref=144, nivel=3, descricao='Subsérie', tipo='C', ocorrencias=(0, 1), tam=(1, 3), regex=ER36)
            dEmi: str = E(
                ref=145, nivel=3, descricao='Data de Emissão', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11, obs='Formato AAAA-MM-DD'
            )
            vDoc: str = E(ref=146, nivel=3, descricao='Valor Transportado', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')

        class seg(G(ref=147, nivel=2, descricao='Informações de Seguro da Carga', ocorrencias=(0, -1))):
            respSeg: str = E(ref=148, nivel=3, descricao='Responsável pelo seguro', tipo='N', ocorrencias=(1, 1), tam=(1, 1), dominio=D25, obs='Preencher com: 4 - Emitente do CT-e OS; 5 - Tomador de Serviço.')
            xSeg: str = E(ref=149, nivel=3, descricao='Nome da Seguradora', tipo='C', ocorrencias=(0, 1), tam=(1, 30), regex=ER36)
            nApol: str = E(ref=150, nivel=3, descricao='Número da Apólice', tipo='C', ocorrencias=(0, 1), tam=(1, 20), regex=ER36, obs='Obrigatório pela lei 11.442/07 (RCTRC)')

        class infModal(G(ref=151, nivel=2, descricao='Informações do modal Obrigatório para Pessoas e Bagagem', ocorrencias=(0, 1))):
            versaoModal: str = A(ref=152, nivel=3, descricao='Versão do leiaute específico para o Modal', tipo='N', ocorrencias=(1, 1), tam='1-2v2', regex=ER45, default=3)

            class rodoOS(G(ref=1, nivel=3, descricao='Informações do modal Rodoviário', ocorrencias=(1, 1))):
                TAF: str = CE(
                    ref=2, nivel=1, descricao='Termo de Autorização de Fretamento – TAF', tipo='N', ocorrencias=(1, 1), tam=12, regex=ER55,
                    obs='Registro obrigatório do emitente do CT-e OS junto à ANTT, de acordo com a Resolução ANTT nº 4.777/2015'
                )
                NroRegEstadual: str = CE(
                    ref=3, nivel=1, descricao='Número do Registro Estadual', tipo='N', ocorrencias=(1, 1), tam=25, regex=ER63,
                    obs='Registro obrigatório do emitente do CT-e OS junto à Agência Reguladora Estadual'
                )

                class veic(G(ref=4, nivel=4, descricao='Dados do Veículo', ocorrencias=(0, 1))):
                    placa: str = E(ref=5, nivel=2, descricao='Placa do veículo', tipo='C', ocorrencias=(1, 1), tam=4, regex=ER40)
                    RENAVAM: str = E(ref=6, nivel=2, descricao='RENAVAM do veículo', tipo='C', ocorrencias=(0, 1), tam=(9, 11), regex=ER36)

                    class prop(G(ref=7, nivel=2,
                                 descricao='Proprietários do Veículo. Só preenchido quando o veículo não pertencer à empresa emitente do CT-e OS',
                                 ocorrencias=(0, 1))):
                        CPF: str = CampoCPF(
                            ref=8, nivel=3, descricao='Número do CPF', tipo='C', ocorrencias=(0, 1), tam=11, regex=ER9,
                            obs='Informar os zeros não significativos.'
                        )
                        CNPJ: str = CampoCNPJ(
                            ref=9, nivel=3, descricao='Número do CNPJ', tipo='C', ocorrencias=(0, 1), tam=14, regex=ER8,
                            obs='Informar os zeros não significativos.'
                        )
                        TAF: str = CE(
                            ref=10, nivel=3, descricao='Termo de Autorização de Fretamento – TAF', tipo='N', ocorrencias=(1, 1), tam=12, regex=ER55,
                            obs='De acordo com a Resolução ANTT nº 4.777/2015'
                        )
                        NroRegEstadual: str = CE(
                            ref=11, nivel=3, descricao='Número do Registro Estadual', tipo='N', ocorrencias=(1, 1), tam=25, regex=ER63,
                            obs='Registro obrigatório do emitente do CT-e OS junto à Agência Reguladora Estadual'
                        )
                        xNome: str = E(ref=12, nivel=3, descricao='Razão Social ou Nome do proprietário', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36)
                        IE: str = E(ref=13, nivel=3, descricao='Inscrição Estadual', tipo='C', ocorrencias=(1, 1), tam=14, regex=ER30, prep_regex=r'\d+')
                        UF: str = E(ref=14, nivel=3, descricao='UF', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10)
                        tpProp: str = E(
                            ref=15, nivel=3, descricao='Tipo Proprietário', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D40,
                            obs='Preencher com: TAC – Agregado; TAC Independente; ou 2 – Outros.'
                        )

                    UF: str = E(
                        ref=16, nivel=2, descricao='UF em que veículo está licenciado', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D10,
                        obs='Sigla da UF de licenciamento do veículo.'
                    )

                class infFretamento(G(ref=17, nivel=1, descricao='Dados do fretamento (apenas para Transporte de Pessoas)',
                                      ocorrencias=(0, 1))):
                    tpFretamento: str = E(
                        ref=18, nivel=2, descricao='Tipo Fretamento', tipo='N', ocorrencias=(1, 1), tam=1, dominio=D1,
                        obs='Preencher com: 1 - Eventual 2 - Continuo'
                    )
                    dhViagem: str = E(
                        ref=19, nivel=2, descricao='Data e hora da viagem (Apenas para fretamento eventual)', tipo='C', ocorrencias=(0, 1), tam=21,
                        regex=ER1, obs='Formato AAAA-MM-DDTHH:MM:DD TZD'
                    )

        class infCteSub(G(ref=154, nivel=2, descricao='Informações do CT-e de substituição', ocorrencias=(0, 1))):
            chCte: str = E(ref=155, nivel=3, descricao='Chave de acesso do CT-e a ser substituído (original)', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)
            refCteAnu: str = CE(ref=156, nivel=3, descricao='Chave de acesso do CT-e de Anulação', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)

            class tomaICMS(CG(ref=157, nivel=3, descricao='Tomador é contribuinte do ICMS, mas não é emitente de documento fiscal eletrônico', ocorrencias=(1, 1))):
                refNFe: str = CE(ref=158, nivel=4, descricao='Chave de acesso da NF-e emitida pelo Tomador', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)

                class refNF(CG(ref=159, nivel=4, descricao='Informação da NF ou CT emitido pelo Tomador', ocorrencias=(1, 1))):
                    CNPJ: str = CampoCNPJ(ref=160, nivel=5, descricao='CNPJ do Emitente', tipo='N', ocorrencias=(0, 1), tam=14, regex=ER5, obs='Informar o CNPJ do emitente do Documento Fiscal')
                    CPF: str = CampoCPF(ref=161, nivel=5, descricao='Número do CPF', tipo='N', ocorrencias=(0, 1), tam=11, regex=ER9, obs='Informar o CPF do emitente do documento fiscal')
                    mod: str = E(ref=162, nivel=5, descricao='Modelo do Documento Fiscal', tipo='C', ocorrencias=(1, 1), tam=2, dominio=D33)
                    serie: str = E(ref=163, nivel=5, descricao='Serie do documento fiscal', tipo='N', ocorrencias=(1, 1), tam=(1, 3), regex=ER34)
                    subserie: str = E(ref=164, nivel=5, descricao='Subserie do documento fiscal', tipo='N', ocorrencias=(0, 1), tam=(1, 3), regex=ER34)
                    nro: str = E(ref=165, nivel=5, descricao='Número do documento fiscal', tipo='N', ocorrencias=(1, 1), tam=(1, 6), regex=ER47)
                    valor: str = E(ref=166, nivel=5, descricao='Valor do documento fiscal.', tipo='N', ocorrencias=(1, 1), tam=(13, 2), regex=ER27, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                    dEmi: str = E(ref=167, nivel=5, descricao='Data de emissão do documento fiscal.', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11)
                refCte: str = CE(ref=168, nivel=4, descricao='Chave de acesso do CT-e emitido pelo Tomador', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)
        refCTeCanc: str = E(ref=169, nivel=2, descricao='Chave de acesso do CT-e Cancelado Somente para Transporte de Valores', tipo='N', ocorrencias=(0, 1), tam=44, regex=ER4)

        class cobr(G(ref=170, nivel=2, descricao='Dados da cobrança do CT-e', ocorrencias=(0, 1))):

            class fat(G(ref=171, nivel=3, descricao='Dados da fatura', ocorrencias=(0, 1))):
                nFat: str = E(ref=172, nivel=4, descricao='Número da fatura', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                vOrig: str = E(ref=173, nivel=4, descricao='Valor original da fatura', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER28, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                vDesc: str = E(ref=174, nivel=4, descricao='Valor do desconto da fatura', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER28, obs='15 posições, sendo 13 inteiras e 2 decimais.')
                vLiq: str = E(ref=175, nivel=4, descricao='Valor líquido da fatura', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER28, obs='15 posições, sendo 13 inteiras e 2 decimais.')

            class dup(G(ref=176, nivel=3, descricao='Dados das duplicatas', ocorrencias=(0, -1))):
                nDup: str = E(ref=177, nivel=4, descricao='Número da duplicata', tipo='C', ocorrencias=(0, 1), tam=(1, 60), regex=ER36)
                dVenc: str = E(ref=178, nivel=4, descricao='Data de vencimento da duplicata (AAAA- MM-DD)', tipo='D', ocorrencias=(0, 1), tam=10, regex=ER11)
                vDup: str = E(ref=179, nivel=4, descricao='Valor da duplicata', tipo='N', ocorrencias=(0, 1), tam=(13, 2), regex=ER28, obs='15 posições, sendo 13 inteiras e 2 decimais.')

    class infCteComp(CG(ref=180, nivel=1, descricao='Detalhamento do CT-e complementado', ocorrencias=(1, 1))):
        chCTe: str = E(ref=181, nivel=2, descricao='Chave do CT-e complementado', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)

    class infCteAnu(CG(ref=182, nivel=1, descricao='Detalhamento do CT-e do tipo Anulação', ocorrencias=(1, 1))):
        chCte: str = E(ref=183, nivel=2, descricao='Chave de acesso do CT-e original a ser anulado e substituído', tipo='N', ocorrencias=(1, 1), tam=44, regex=ER4)
        dEmi: str = E(ref=184, nivel=2, descricao='Data de emissão da declaração do tomador não contribuinte do ICMS', tipo='D', ocorrencias=(1, 1), tam=10, regex=ER11)

    class autXML(G(ref=185, nivel=1, descricao='Autorizados para download do XML do DF-e', ocorrencias=(0, 10))):
        CNPJ: str = CampoCNPJ(ref=186, nivel=2, descricao='CNPJ do autorizado', tipo='N', ocorrencias=(0, 1), tam=14, regex=ER5, obs='Informar zeros não significativos')
        CPF: str = CampoCPF(ref=187, nivel=2, descricao='CPF do autorizado', tipo='N', ocorrencias=(0, 1), tam=11, regex=ER9, obs='Informar zeros não significativos')

    class infRespTec(G(ref=188, nivel=1, descricao='Informações do Responsável Técnico pela emissão do DF-e', ocorrencias=(0, 1))):
        CNPJ: str = CampoCNPJ(ref=189, nivel=2, descricao='CNPJ da pessoa jurídica responsável técnica pelo sistema utilizado na emissão do documento fiscal eletrônico', tipo='N', ocorrencias=(1, 1), tam=14, regex=ER5, obs='Informar o CNPJ da pessoa jurídica desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico.')
        xContato: str = E(ref=190, nivel=2, descricao='Nome da pessoa a ser contatada', tipo='C', ocorrencias=(1, 1), tam=(2, 60), regex=ER36, obs='Informar o nome da pessoa a ser contatada na empresa desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico. No caso de pessoa física, informar o respectivo nome.')
        email: str = E(ref=191, nivel=2, descricao='E-mail da pessoa jurídica a ser contatada', tipo='C', ocorrencias=(1, 1), tam=(1, 60), regex=ER52)
        fone: str = E(ref=192, nivel=2, descricao='Telefone da pessoa jurídica a ser contatada', tipo='C', ocorrencias=(1, 1), tam=(7, 12), regex=ER50, obs='Preencher com o Código DDD + número do telefone.', prep_regex=r'\d+')
        idCSRT: str = E(ref=193, nivel=2, descricao='Identificador do código de segurança do responsável técnico', tipo='N', ocorrencias=(1, 1), tam=3, regex=ER35, obs='Identificador do CSRT utilizado para geração do hash')
        hashCSRT: str = E(ref=194, nivel=2, descricao='Hash do token do código de segurança do responsável técnico', tipo='C', ocorrencias=(1, 1), tam=28, obs='O hashCSRT é o resultado das funções SHA-1 e base64 do token CSRT fornecido pelo fisco + chave de acesso do DF-e. (Implementação em futura NT)')


class infCTeSupl(G(ref=195, nivel=0, descricao='Informações  suplementares do CT-e', ocorrencias=(0, 1))):
    qrCodCTe: str = E(ref=196, nivel=1, descricao='Texto com o QR-Code impresso no DACTE', tipo='C', ocorrencias=(1, 1), tam=(50, 1000), regex=ER64)




### Web Services


class consStatServCte(G(ref='FP01', descricao='TAG raiz', xmlns="http://www.portalfiscal.inf.br/mdfe")):
    versao: str = A('FP02', tipo='N', ocorrencias=(1, 1), tam="2v2", obs='Versão do leiaute')
    tpAmb: str = E('FP03', tipo='N', ocorrencias=(1, 1), tam=1, obs='Identificação do Ambiente: 1 – Produção / 2 - Homologação')
    xServ: str = E('FP04', tipo='C', ocorrencias=(1, 1), tam=6, obs='Serviço solicitado: ‘STATUS’')


class retConsStatServCte(G(ref='FR01', descricao='TAG raiz da Resposta')):
    versao: str = A('FR02', tipo='N', ocorrencias=(1, 1), tam="2v2", obs='Versão do leiaute')
    tpAmb: str = E('FR03', tipo='N', ocorrencias=(1, 1), tam=1, obs='Identificação do Ambiente: 1 – Produção / 2 - Homologação')
    verAplic: str = E('FP04', tipo='C', ocorrencias=(1, 1), tam=6, obs='Versão do aplicativo que processou a consulta')
    cStat: int = E('FR05', tipo='N', ocorrencias=(1, 1), tam=3, obs='Código do status da resposta')
    xMotivo: str = E('FP06', tipo='C', ocorrencias=(1, 1), tam=(1, 255), obs='Serviço solicitado: ‘STATUS’')
    cUF: int = E('FR07', tipo='N', ocorrencias=(1, 1), tam=2, obs='Código da UF que atendeu à solicitação')
    dhRecbto: str = E('FR08', tipo='D', ocorrencias=(1, 1), tam=None, obs='Data e hora do recebimento do pedido')
    tMed: int = E('FR09', tipo='N', ocorrencias=(1, 1), tam=(1, 4), obs='Tempo médio de resposta do serviço')
    dhRetorno: str = E('FR10', tipo='D', ocorrencias=(1, 1), tam=None, obs='Data e hora previstas para o retorno do Web Service')
    xObs: str = E('FR11', tipo='C', ocorrencias=(1, 1), tam=(1, 255), obs='Informações adicionais ao contribuinte')


class enviCTe(G(ref='AP01', descricao='Tag raiz')):
    versao: float = A('AP02', tipo='N', ocorrencias=1, tam="2v2", obs='Versão do leiaute')
    idLote: int = E('AP03', tipo='N', ocorrencias=1, tam=(1, 15))
    CTe: CTe = CTe(ocorrencias=(1, 50))


class retEnviCte(G(ref='AR01', descricao='Tag raiz Resposta')):
    versao: float = A('AR02', tipo='N', ocorrencias=1, tam="2v2", obs='Versão do leiaute')
    tpAmb: int = E('AR03', tipo='N', ocorrencias=1, tam=1, obs='Identificação do Ambiente')
    cUF: str = E('AR03a', tipo='N', ocorrencias=1, tam=2, obs='Código da UF que atendeu a solicitação')
    verAplic: str = E('AR04', tipo='C', ocorrencias=1, tam=6, obs='Versão do aplicativo que processou a consulta')
    cStat: int = E('AR05', tipo='N', ocorrencias=1, tam=3, obs='Código do status da resposta')
    xMotivo: str = E('AR06', tipo='C', ocorrencias=1, tam=(1, 255), obs='Serviço solicitado: ‘STATUS’')

    class infRec(G(ref='AR07', obs='Dados do Recibo do Lote')):
        nRec: str = E(ref='AR08', tipo='N', ocorrencias=1, tam=15, obs='Número do Recibo gerado pelo Portal da SEFAZ')
        dhRecbto: datetime = E(ref='AR09', tipo='D', ocorrencias=1, obs='Data e Hora do Recebimento')
        tMed: int = E(ref='AR10', tipo='N', ocorrencias=1, tam=(1, 4), obs='Tempo médio de resposta')
