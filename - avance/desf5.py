fs = str(input('Escreva uma frase: ')).strip().upper()
#strip para n contar os espaçõs(acho q vou tirar pela posição)
#upper para q as letras informadas fiquem maiusculas

print('A letra A aparece {} vezes na frase.'.format(fs.count('A')))
#count, como o nome ja diz, conta qts vzs apareceu a letra
print('A primeira letra A aparece na posição {}'.format(fs.find('A')+1))
#mostra  a primeira aparição da letra, mas acho q podem haver outros usos
print('A ultima letra A aparece na posição {}'.format(fs.rfind('A')+1))
#aparece a primeira letrea escolhida a partir do lado direiro

#print('A primeira letra A aparece na posição {}'.format(frase.find('A')))
#lembrar de mudar o format(frase.find('A'))), colocar : fs = s











