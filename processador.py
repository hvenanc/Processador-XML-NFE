from os import chdir, listdir
from os.path import isfile
from xml.dom import minidom
import xml.etree.ElementTree as ET
import pandas as pd


class ProcessadorNFE:

    def __init__(self, caminho):
        self._caminho = caminho

    @staticmethod
    def valida_nfe(nfe):
        tree = ET.parse(nfe)
        root = tree.getroot()
        # Namespace
        namespace = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
        tag = 'nfe:ide/nfe:nNF'
        for dado in root.findall('.//nfe:infNFe', namespace):
            item = dado.find(tag, namespace)
            if item.text is not None:
                return True

    @staticmethod
    def valida_xml(arquivo):
        try:
            ET.parse(arquivo)
            return True
        except ET.ParseError:
            return False

    @staticmethod
    def elements_text(nfe, tag):
        element = nfe.getElementsByTagName(tag)
        element = element[0].firstChild.data

        return element

    @staticmethod
    def elements_number(nfe, tag):
        element = nfe.getElementsByTagName(tag)
        element = element[0].firstChild.data

        return float(element)

    @staticmethod
    def elements_date(nfe, tag):
        element = nfe.getElementsByTagName(tag)
        element = element[0].firstChild.data

        return element[8:10] + '/' + element[5:7] + '/' + element[0:4]

    def buscar_arquivos(self, caminho):
        arquivos = []
        chdir(caminho)
        for arquivo in listdir():
            if isfile(arquivo) and self.valida_xml(arquivo):
                arquivos.append(arquivo)

        return arquivos

    def buscar_nfes(self, caminho):
        arquivos = self.buscar_arquivos(caminho)
        nfes = []
        x = 0
        while x < len(arquivos):
            doc = str(arquivos[x])
            if self.valida_nfe(doc) is not None:
                nfes.append(doc)
            x += 1
        return nfes

    def buscar_dados(self, caminho):

        chaves = []
        fornecedores = []
        valor_total = []
        num_nfe = []
        datas = []

        for x in self.buscar_nfes(caminho):
            xml = open(x)
            nfe = minidom.parse(xml)

            chave = self.elements_text(nfe, 'chNFe')
            chaves.append(chave)

            forn = self.elements_text(nfe, 'xNome')
            fornecedores.append(forn)

            total = self.elements_number(nfe, 'vNF')
            valor_total.append(total)

            num = self.elements_text(nfe, 'nNF')
            num_nfe.append(num)

            data = self.elements_date(nfe, 'dhEmi')
            datas.append(data)

        return chaves, fornecedores, valor_total, num_nfe, datas

    def relatorio(self, caminho, nome):
        df = pd.DataFrame()
        df['Chave'] = self.buscar_dados(caminho)[0]
        df['Número NFE'] = self.buscar_dados(caminho)[3]
        df['Data Emissão'] = self.buscar_dados(caminho)[4]
        df['Fornecedor'] = self.buscar_dados(caminho)[1]
        df['Valor NFE'] = self.buscar_dados(caminho)[2]

        df = df.sort_values(['Data Emissão'])
        df = df.reset_index(drop=True)
        df.to_excel(f'{caminho}{nome}.xlsx')
        return 'Relatório Gerado com Sucesso'
