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

    chave = elements_text(nfe,'chNFe')
    chaves.append(chave)

    forn = elements_text(nfe,'xNome')
    fornecedores.append(forn)

    total = elements_number(nfe,'vNF')
    valor_total.append(total)

    num = elements_text(nfe,'nNF')
    num_nfe.append(num)

    data = elements_date(nfe,'dhEmi')
    datas.append(data)
    

df = pd.DataFrame()
df['Chave'] = chaves
df['Número NFE'] = num_nfe
df['Data Emissão'] = datas
df['Fornecedor'] = fornecedores
df['Valor NFE'] = valor_total

df = df.sort_values(['Data Emissão'])
df = df.reset_index(drop=True)
df.to_excel('/home/henrique/Documentos/Projetos/Processador XML/NFE_Março.xlsx')