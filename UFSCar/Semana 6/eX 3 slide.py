# Escreva um programa que leia duas strings e gere uma terceira, na
# qual os caracteres da segunda foram retirados da primeira.

s1 = input()
s2 = input()
s3 = ''

for i in range(len(s2)):
    if s1.find(s2[i]) != -1:
        s1 = s1.replace(s2[i], '')

s3 = s1
print(s3)