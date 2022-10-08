#Tipos de dados básicos: Inteiros (int) ex: 10, 1200 ; Reais/Ponto flutuante (float) ex: 3.5, 1.00 ;
# Texto literal (string) ex: 'Brasil' ; Lógico/booleano (bool) ex: True ou False

#Atribuição de variáveis feitas através do comando '=' (recebe)

#exemplo 1
curso = "Engenharia de Produção"
# variável curso recebe a string "Engenharia de Produção"
nota = 100
# variável nota recebe o valor inteiro 100
media = 6.5
# variável media recebe o valor real 6.5

#exemplo 2
cursoA = "Engenharia de Civil"
cursoB = cursoA # cursoB recebe o valor de cursoA
print("cursoA:",cursoA)
print("cursoB:", cursoB)
cursoA = "Estatística"
print("cursoA:",cursoA)
print("cursoB:", cursoB)
#Nesse caso o cursoB mantém o seu valor, quando ele recebeu cursoA,
# mesmo após mudança dessa última variável.

#Conversão de dados de um tipo para o outro
#As funções int(), float() e str() convertem os argumentos para o seu tipo,
#assim como a função f em f(x)=x^2 converte o argumento x em seu valor ao quadrado

#exemplo 3
int("3") #converte a string "3" para 3
float("3.4") #converte aquela string para 3.4
str(3.4) #converte o número real para a string "3.4"
int(3.4) #converte o número de ponto flutuante para 3 (inteiro)
int("3.4") # erro! Não podemos converter a string contendo float para int
int("banana") # erro! Não se converte uma string contendo palavras para números int ou float