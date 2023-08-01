from processador import ProcessadorNFE

cam = '/home/henrique/Documentos/NFE/'
notas = ProcessadorNFE(cam)
relatorio = notas.relatorio('/home/henrique/Documentos/NFE/', 'Notas Março')
print(relatorio)

