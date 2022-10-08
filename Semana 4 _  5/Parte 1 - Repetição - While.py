# Estruturas de repetição executam o comando várias vezes, dependendo de alguma condição imposta
# while: repete o comando enquanto a condição resultar True (bool)  (enquanto.. faça)
# Funcionamento: 1) avalia-se a condição do booleano antes de entrar no bloco da repetição
# 2) a repetição ocorre enquanto a condição for True, para quando der False
# 3) ao fim de uma repetição ocorre uma nova avaliação do booleano
# 4) repetição pode ocorrer de 0 a infinitas vezes

# exemplo:
n = 5
while n > 0 :
    print(n)
    n= n - 1
print('FIM')

# obs: deve haver algum comando que atualize a informação e eventualmente retorne o booleano False
# o comando while permite criar loops indefinidos, quando não sabemos o momento em que ele termina

# Podemos fazer repetições aninhadas, uma iteração dentro da outra

# exemplo:
for tabuada in range (1,11):
    print ("\nTabuada de %d \n" % tabuada)
    for n in range (1,11):
        print ("%d x %d = %d" % (n,tabuada,n*tabuada))