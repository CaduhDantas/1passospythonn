nc = input(str('digite seu nome completo ')).strip()
print('analisando teu nome...')
print('seu nome em maiusculas é: {}'.format(nc.upper()))
print('seu nome em minusculas é: {}'.format(nc.lower()))
print('seu nome tem {} letras :)'.format(len(nc) - nc.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nc.find(' ')))
separados = nc.split()
#print(separados)
print('seu primeiro nome é {} e ele tem {} letras'.format(separados[0], len(separados[0])))

#strip elimina espaços no mei das palavras antes e dps da frase
#- 'nc.count(' ')' para contar apenas as letras do nome, não o espaço entre elas





















