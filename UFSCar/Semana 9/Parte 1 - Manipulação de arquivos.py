# Permite ler e escrever em arquivos do computador

# Função open: cria ou abre um objeto file
arquivo = open(nome_arquivo,modo)
# O modo 'r' (read) permite leitura e o modo 'w' (write) é escrita. 'a' é escrita concatenando.

# Métodos

# write('w' ou 'a')
# ex no modo 'w':
arq = open('telefones.txt','w') # sobrescreve
arq.write('Ana 999811011')
arq.close()
#  ex no modo 'a':
arq = open('meuarquivo.txt','a') #escreve no final do arquivo
arq.write('\nÚltima linha')
arq.close() #grava e efetivamente e fecha o arquivo

# writelines()
# Escreve todos os itens de uma lista
arq = open("meuarquivo.txt","w")
lista=["1\n","11\n","111\n","1111\n"]
arq.writelines(lista)
arq.close()

# close()
# O arquivo deve ser fechado após o uso para gravar as mudanças
arq = open('meuarquivo.txt','w')
arq.write('teste 1 2 3.\nTestando\ntestando 1 2 3\n')
arq.close()

# read()
# Retorna string com o conteúdo de todo o arquivo
arq = open('meuarquivo.txt','r')
texto = arq.read()
print(texto)
arq.close()

# readlines()
# Cada linha do arquivo é armazenada como elemento de uma lista
arq = open('meuarquivo.txt','r')
texto = arq.readlines()
for linha in texto:
    print(linha)
arq.close()

# readline()
# Retorna uma linha do arquivo e passa para a próxima, ou "" depois de ler a última linha
arq = open('meuarquivo.txt','r')
texto = arq.readline()
while texto != "":
    print(texto)
    texto = arq.readline()
arq.close()