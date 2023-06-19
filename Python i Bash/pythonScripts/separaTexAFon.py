import sys
import io

def separaTexAFon(entrada, sortida):
    with open(entrada, 'r') as f_entrada:
        contingut = f_entrada.read()

    final = contingut.replace('|| || || ', '\n').replace('|| || ', '\n')

    with io.open(sortida, 'w') as f_sortida:
        f_sortida.write(final.decode('utf-8'))

if __name__ == '__main__':
    entradaScript = sys.argv[1]
    sortidaScript = sys.argv[2]
    separaTexAFon(entradaScript,  sortidaScript)