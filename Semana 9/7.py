# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Programa que retorna dados do contato salvo em um arquivo

# Registro de novos contatos (opcional)
arquivo = open('contatos.txt','a')
entradas = 0

pergunta = input('Deseja inserir novos contatos? (S ou N): ')
if pergunta == 'S':
    while entradas < 5:
        arquivo.write('{}\n'.format(input('Insira o contato no formato CSV(nome;telefone;email): ')))
        entradas = entradas + 1

arquivo.close()

# Leitura dos contatos para pesquisa de nome
arquivo_entrada = open('contatos.txt','r')
nome = input('Nome pesquisado: ')
contatos = arquivo_entrada.readlines()
# A lista de dados armazena apenas os dados do contato desejado
dados = [contatos[i] for i in range(len(contatos)) if nome in contatos[i]]
arquivo_entrada.close()

if dados != []: # Caso o contato seja encontrado
    arquivo_saida = open('saida.txt','w')
    # Dados são transcritos para o arquivo de saída
    arquivo_saida.writelines(dados)
    arquivo_saida.close()

    arquivo_saida = open('saida.txt','r') # Leitura de dados na saída
    saidas = arquivo_saida.read().replace('\n','').split(';')
    nome = saidas[0]
    fone = saidas[1]
    email = saidas[2]
    print('{}\nFone: {}\nEmail: {}'.format(nome,fone,email))

else:
    print('Nome não encontrado')