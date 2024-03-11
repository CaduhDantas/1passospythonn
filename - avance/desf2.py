num = int(input('informe um numero: '))
#n = str(num)

#print('analisando seu numero, um momento..')
#print('unidade: {}'.format(n[3]))
#print('dezena: {}'.format(n[2]))
#print('centena: {}'.format(n[1]))
#print('milhar: {}'.format(n[0]))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('analisando seu numero, um momento..')
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))