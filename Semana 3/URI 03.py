# Autor: Lucas Gabriel
# Data de Criação: 10/03/2021

valores = input().split()
A, B, C = valores
A = float(A)
B = float(B)
C = float(C)
if A<B+C and B<A+C and C<A+B:
    print('Perimetro = {:.1f}'.format(A+B+C))
else:
    print('Area = {}'.format(((A+B)/2)*C))