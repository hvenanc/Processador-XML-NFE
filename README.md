# Processador-XML

Script que filtra arquivos .XML que definem uma NFE/NFCE e extrai algumas informações gerando um
arquivo do tipo .xlsx (Excel).

### Informações extraidas

#### NFE

- Chave de Acesso da NFE
- Número da NFE
- Data da Emissão
- Nome do Fornecedor
- Valor Total da NFE

#### NFCE

- Código EAN dos Produtos
- Descrição do Produto
- Valor total de cada item
- Unidade Tributada
- Código fiscal de operação de cada item (CFOP)

### Relatório Gerado

![RELATORIO](Exemplo.png)

### Instalação

- Linux/Mac:

```python3 -m venv venv```

```source venv/bin/activate```

```pip install Processador-XML-NFE```

- Windows:

```virtaulenv venv```

```venv/Scripts/Activate```

```pip install Processador-XML-NFE```

### Exemplo de uso

```python
from processador import ProcessadorNFE

cam = '/home/henrique/Área de Trabalho/Amostra' #Diretório com os arquivos
notas = ProcessadorNFE(cam)
nfce = notas.relatorio_nfce(cam + '/', 'Dia 08-08')
nfe = notas.relatorio_nfe(cam + '/', 'NFCES Dia 08-08')
print(nfce)
print(nfe)

```