from processador import ProcessadorNFE

cam = '/home/henrique/Área de Trabalho/Amostra'
notas = ProcessadorNFE(cam)
nfce = notas.relatorio_nfce(cam + '/', 'Dia 08-08')
nfe = notas.relatorio_nfe(cam + '/', 'NFCES Dia 08-08')
print(nfce)
print(nfe)

