# By Matheus Eiji
import numpy as np

# Dado os arquivos em anexo:
# anos.txt ⇒ ano de nascimento das pessoas em ordem
# altura ⇒ alturas das pessoas em ordem
# Importe os 2 arquivos e descubra a média de altura de quem nasceu entre 1998 e 2005.
# DICA: ambos os arquivos têm o mesmo tamanho e estão relacionados pelo índice. Use o índice de um em outro.

altura = np.loadtxt('altura.txt')
idade = np.loadtxt('idade.txt')

arr = np.stack((altura, idade), axis=1)

found = 0
altura_total = 0
for row in arr:
    if row[1]>= 1998 and row[1]<=2005:
        print(row)
        found+=1
        altura_total+=row[0]

media = altura_total/found

print("Média de altura de quem nasceu entre 1998 e 2005: ", media)


# print(arr)