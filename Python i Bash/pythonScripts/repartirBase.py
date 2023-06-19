# -*- coding: utf-8 -*-
import sys
import io

def repartirBase(entrada, sortida80, sortida20):
    with open(entrada, 'r') as f_entrada:
        linies = f_entrada.readlines()

    total_linies = len(linies)
    lineasNum = int(total_linies * 0.8)

    linies_80 = linies[:lineasNum]
    linies_20 = linies[lineasNum:]
    
    with io.open(sortida80, 'w') as f_sorida80:
        for linia80 in linies_80:
            f_sorida80.writelines(linia80.decode('utf-8'))

    with io.open(sortida20, 'w') as f_sorida20:
        for linia20 in linies_20:
            f_sorida20.writelines(linia20.decode('utf-8'))

if __name__ == '__main__':
    entradaScript = sys.argv[1]
    sortidaScript80 = sys.argv[2]
    sortidaScript20 = sys.argv[3]
    repartirBase(entradaScript, sortidaScript80, sortidaScript20)