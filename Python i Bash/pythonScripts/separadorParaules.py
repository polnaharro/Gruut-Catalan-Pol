import sys
import io

def processarLinea(linia):
    parts = linia.split(' ')
    paraula = parts[0].strip()
    return paraula


def separadorParaules(entrada, sortida):

    with io.open(entrada, 'r') as f_entrada:
        linies = f_entrada.readlines()

    processades = [processarLinea(linia) for linia in linies]
    with io.open(sortida, 'w') as f_sortida:
        f_sortida.write('\n'.decode('utf-8').join(processades))


if __name__ == '__main__':
    entradaScript = sys.argv[1]
    sortidaScript = sys.argv[2]
    separadorParaules(entradaScript, sortidaScript)