n = str(input('qual seu nome? ')).strip()
#sn = print(n.upper() == 'SILVA')
print('seu nome tem silva? {}'.format('silva' in n.lower().split()))
#print('Seu nome possui "SILVA"? {}'.format('SILVA' in nome.upper().split()))



# 1) Recebo o nome tratado para evitar espaços extras
nome = str(input('Informe seu nome completo: ')).strip() ok

# 2) Converto o nome para letras maiúsculas, depois ok
# o divido e guardo a lista em uma nova variável:
divisao = nome.upper().split()

# 3) Agora executo o teste para verificar se existe SILVA em
# alguns dos itens da lista criada.
print('SILVA' in divisao)










