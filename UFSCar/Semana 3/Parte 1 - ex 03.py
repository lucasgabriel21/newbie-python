# Construa um programa que solicite o consumo de telefone no mês em
# minutos e calcule a conta de telefone de acordo com o consumo do mês
# e as seguintes taxas praticadas pela empresa, dependendo da faixa de consumo:
# ▫ Abaixo de 200 minutos: R$ 0.20 por minuto
# ▫ De 200 a 400 minutos: R$ 0.18 por minuto
# ▫ Acima de 400 minutos: R$ 0.15 por minuto
# • Imprima o valor da conta telefônica
consumo_tel = int(input('Informe o consumo de telefone em minutos: '))
if consumo_tel < 200:
    taxa = 0.2*consumo_tel
elif consumo_tel <= 400:
    taxa = 0.18*consumo_tel
else:
    taxa = 0.15*consumo_tel
print('O valor de sua conta telefônica é R$ {:.2f}'.format(taxa))