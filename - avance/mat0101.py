from math import sqrt, floor
#iniciando o estudo de import's
mat = int(input('digite um numberrrr'))
raiz = sqrt(mat)
print('a raiz de {} é igual a {:.3f}. ou se preferir uma raiz exata, fica: {}'.format(mat, raiz, floor(raiz)))