import sys
import io

def processarLinea(linia):
    parts = linia.split('\t')
    if len(parts) >= 2:
        paraula = parts[0].strip()
        transcripcio = ' '.join(parts[1].strip().split())
        return paraula+'\t'+transcripcio
    else:
        return ""

def espeakAdaptador(entrada, sortida):

    with io.open(entrada, 'r') as f_entrada:
        linies = f_entrada.readlines()

    processades = [processarLinea(linia) for linia in linies]
    processades = [valor for valor in processades if valor != '']
    processades = [valor.replace('\t', ' ') for valor in processades]
    with io.open(sortida, 'w') as f_sortida:
        f_sortida.write('\n'.decode('utf-8').join(processades))


if __name__ == '__main__':
    entradaScript = sys.argv[1]
    sortidaScript = sys.argv[2]
    espeakAdaptador(entradaScript, sortidaScript)