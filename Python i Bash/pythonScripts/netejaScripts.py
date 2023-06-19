import sys
import io

def netejaScripts(entrada, sortida):
    with open(entrada, 'r') as f_entrada:
        contingut = f_entrada.read()

    final = contingut.replace('|', '').replace('#', '').replace("'", '').replace("||", '').replace(".", '').replace("  ", ' ')

    with io.open(sortida, 'w') as f_sortida:
        f_sortida.write(final.decode('utf-8'))

if __name__ == '__main__':
    entradaScript = sys.argv[1]
    sortidaScript = sys.argv[2]
    netejaScripts(entradaScript,  sortidaScript)