resposta = 1
grenais = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0

while resposta == 1:

    [gols_inter, gols_gremio] = input().split()
    [gols_inter, gols_gremio] = [int(gols_inter), int(gols_gremio)]

    if gols_inter > gols_gremio:
        vitorias_inter = vitorias_inter + 1

    elif gols_inter < gols_gremio:
        vitorias_gremio = vitorias_gremio + 1

    else:
        empates = empates + 1

    grenais = grenais + 1

    print('Novo grenal (1-sim 2-nao)')
    resposta = int(input())

print('{} grenais'.format(grenais))
print('Inter:{}'.format(vitorias_inter))
print('Gremio:{}'.format(vitorias_gremio))
print('Empates:{}'.format(empates))

if vitorias_inter > vitorias_gremio:
    print('Inter venceu mais')

elif vitorias_gremio > vitorias_inter:
    print('Gremio venceu mais')

else:
    print('Nao houve vencedor')