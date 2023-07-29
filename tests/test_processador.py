import pytest

from processador import ProcessadorXML


class TestClass:

    def test_busca_das_nfe_a_lista_deve_possuir_78_arquivos(self):
        """
        Teste que valida que apenas arquivos .xml que representam
        uma NFE serão abertos.
        O diretório possuia 268 Aqruivos, no qual 78 eram do formato
        .xml e representava um Nota Fiscal Eletrônica (NFE).
        """
        cam = '/home/henrique/Documentos/NFE/'
        notas = ProcessadorXML(cam)
        arquivos = notas.buscar_nfes(cam)

        esperado = 78
        resultado = len(arquivos)

        assert esperado == resultado

    def test_ignora_arquivos_com_formato_diferente_de_xml(self):
        """
        Teste que valida que arquivos com formato diferente .xml
        serão ignorados.
        O diretório possuia 268 Aqruivos, no qual 3 eram do formato
        .xlsx os demais eram do tipo .xml.
        """

        cam = '/home/henrique/Documentos/NFE/'
        notas = ProcessadorXML(cam)
        arquivos = notas.buscar_arquivos(cam)

        esperado = 265
        resultado = len(arquivos)

        assert esperado == resultado

    def test_valida_arquivo_tipo_xml(self):
        with pytest.raises(Exception):
            cam = '/home/henrique/Documentos/NFE/Teste4.xlsx'
            notas = ProcessadorXML(cam)
            resultado = notas.valida_xml(cam)

            assert resultado

    def test_relatorio_gerado_com_sucesso(self):
        cam = '/home/henrique/Documentos/NFE/'
        notas = ProcessadorXML(cam)
        relatorio = notas.relatorio('/home/henrique/Documentos/NFE/', 'Notas Março')

        esperado = 'Relatório Gerado com Sucesso'
        resultado = relatorio

        assert esperado == resultado
