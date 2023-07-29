from processador import ProcessadorXML

cam = '/home/henrique/Documentos/NFE/'
notas = ProcessadorXML(cam)
relatorio = notas.relatorio('/home/henrique/Documentos/NFE/', 'Notas Março')
print(relatorio)

