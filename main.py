from processador import ProcessadorNFE

cam = '/home/henrique/Área de Trabalho/Amostra'
notas = ProcessadorNFE(cam)
relatorio = notas.relatorio_nfce(cam + '/', 'Teste')
print(relatorio)

