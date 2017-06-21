from models import *

try:
    arquivo = open('perfis.csv', 'r')
    valores = arquivo.readline().split(':')
    Perfil(*valores)
    arquivo.close()
except (FileNotFoundError, TypeError) as erro:
    print('Deu error %s' % erro)