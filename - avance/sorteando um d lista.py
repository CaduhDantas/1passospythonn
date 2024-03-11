import random
n1 = str(input('digite o primeiro nome: '))
n2 = str(input('digite outro: '))
n3 = str(input('digite o ultimo: '))
lista = [n1, n2 ,n3]
escolha = random.choice(lista)
print('o aluno escolhido foi: {}'.format(escolha))