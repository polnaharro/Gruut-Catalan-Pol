import sys
import io


def unioScripts(entrada, cont, sortida):
    with io.open(sortida, 'w') as f_sortida:
        for i in range(1, int(cont)):
            nomEntrada = entrada.replace("contador",str(i))
            with io.open(nomEntrada, 'r') as f_entrada:
                frase = f_entrada.read()

            f_sortida.write(frase)
            f_sortida.write('\n'.decode('utf-8'))

if __name__ == '__main__':
    entradaNom = sys.argv[1]
    cont = sys.argv[2]
    sortidaScript = sys.argv[3]
    unioScripts(entradaNom, cont,  sortidaScript)