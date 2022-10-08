X = int(input())

if X % 2 == 0:
    for i in range(1, 12, 2):
        print(X + i)

elif X % 2 != 0:
    print(X)
    for j in range (1, 10, 2):
        print(X + j + 1)