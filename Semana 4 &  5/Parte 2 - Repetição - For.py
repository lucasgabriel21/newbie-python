# for: repete o comando para certos valores de um conjunto finito especificado  (para cada elemento ... faça)
# Cria loops definidos, sempre sabemos o número de repetições que ocorrerão
# O loop for percorre todos os itens do conjunto definido, um a cada iteração
# A repetição acaba quando chega no fim da coleção

# exemplo 1
for i in [15,9,8]:
 print(i)
print("Fim")

# exemplo 2
for i in ["Alex","Bia","Julia"]:
    print("Oi",i)
print("Fim")

# Função range (gerador de listas)
# range(ini,limite,salto)
# ini: elemento inicial (pode ser oculto, o padrão é 0) - OPCIONAL
# limite: limite superior (não entra no intervalo, mas demarca o limite) - OBRIGATÓRIO
# salto: determina valor de incremento ou decremento a cada elemento, o valor padrão é 1 - OPCIONAL

# exemplos:
for e in range(5,100,1):
 print(e) #imprime números inteiros de 5 a 99

for e in range(0,10,2):
 print(e) # imprime números pares de 0 a 8 (10 é o limite, não entra no conjunto)