# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Incorporação dos dados

tabela = open('tabela.txt','r')
dados_incorporados = [] # Lista dos dados com acréscimo do IMC

# Cálculo do IMC
for linha in tabela:
    info = linha.split() # Listagem dos dados de uma linha
    peso = float(info[2])
    altura = float(info[3])
    IMC = peso/(altura**2)
    info.insert(3,'{:.1f}'.format(IMC)) # Insere IMC após o peso
    dados_incorporados.append(info) # Acumula os dados das linhas

tabela.close()

# Inserção dos dados de IMC na tabela
novo_arquivo = open('tabela.txt','w')

for i in range(len(dados_incorporados)):
    linha = dados_incorporados[i] # Cada elemento da lista representa uma linha
    novo_arquivo.write('{}\n'.format(' '.join(linha)))

novo_arquivo.close()
print('Suas informações foram salvas com sucesso!')