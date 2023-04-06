from os import chdir, listdir
from os.path import isfile
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd
from funcoes import *

cam = '/home/henrique/Área de Trabalho/NFE'

lista = []

chdir(cam)

for c in listdir():
    if isfile(c):
        #print(cam + '\\' + c)
        lista.append(c)

nfes = []
x = 0
while(x<len(lista)):
    doc = str(lista[x])
    if len(doc) == 48:
        nfes.append(doc)
    x+=1

chaves = []
fornecedores = []
valor_total = []
num_nfe = []
datas = []

for x in nfes:
    
    xml = open(x)
    nfe = minidom.parse(xml)

    chave = nfe.getElementsByTagName('chNFe')
    chave = chave[0].firstChild.data
    chaves.append(chave)

    forn = nfe.getElementsByTagName('xNome')
    forn = forn[0].firstChild.data
    fornecedores.append(forn)

    total = nfe.getElementsByTagName('vNF')
    total = total[0].firstChild.data
    valor_total.append(float(total))

    num = nfe.getElementsByTagName('nNF')
    num = num[0].firstChild.data
    num_nfe.append(num)

    data = nfe.getElementsByTagName('dhEmi')
    data = data[0].firstChild.data
    datas.append(formatar_data(data))
    

df = pd.DataFrame()

df['Chave'] = chaves
df['Número NFE'] = num_nfe
df['Data Emissão'] = datas
df['Fornecedor'] = fornecedores
df['Valor NFE'] = valor_total

df = df.sort_values(['Data Emissão'])
df = df.reset_index(drop=True)
df.to_excel('/home/henrique/Documentos/Projetos/Processador XML/NFE_Março.xlsx')

    