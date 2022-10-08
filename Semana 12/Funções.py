# Sequência de instruções que realiza determinada tarefa
# Simplifica os programas, escondendo passagens repetitivas dentro de uma função
# Sintaxe:
def nomeFuncao(parametros):
    bloco_de_comandos

# Funções frutíferas são as que retornam um valor, ex:
def f(x):
    y = x**2
    return y #retorna y = f(x) = x^2
# Funções NÃO frutíferas não retornam valores, apenas executam os passos definidos

# Funções podem chamar outra função, ex:
def par(x):
    return (x%2 == 0) #True ou False
def par_ou_impar(x):
    if par(x): #relaciona com a função definida anteriormente
        return 'par'
    else:
        return 'ímpar'
print(par_ou_impar(3))
print(par_ou_impar(54))

# Variáveis locais a uma função são valores conhecidos apenas dentro da função
# inicializados a cada chamada da função

# Variáveis globais são conhecidas no programa inteiro, mas são sobrepostas por
# variáveis locais de mesmo nome no escopo local
# Recomendação 1: Não utilizar variáveis globais e locais com o mesmo nome. Isso torna o código confuso!
# Recomendação2: não utilizar variáveis globais dentro de funções. Isso também torna o código confuso!
# Recomendação3: não usar variáveis globais! Usar apenas variáveis locais e passagem parâmetros entre funções.
def muda_e_imprime(a):
    a += 1 #VARIÁVEL LOCAL NÃO ALTERA A GLOBAL
    print ("a dentro da função: %d" % a) #6
a = 5 #VARIÁVEL GLOBAL
print ("a antes de chamar a função: %d" % a) #5
muda_e_imprime(a)
print ("a depois de chamar a função: %d" % a)#Continua 5