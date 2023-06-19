# -*- coding: utf-8 -*-
import sys
import io

def eliminarColumna(entrada, sortida):
    final = []

    with open(entrada, 'r') as f_entrada:
        lineas = f_entrada.readlines()

    for linia in lineas:  
        paraules = linia.strip().split(' ')
        paraules.pop(0)
        espai =' '
        for longitud in range(0,len(paraules)):
            
            if(len(paraules)==(longitud+1)): espai =''

            final.append(paraules[longitud] + espai)
        
        final.append('\n')

    with io.open(sortida, 'w') as f_sorida:
        for linia in final:
            f_sorida.writelines(linia.decode('utf-8'))

if __name__ == '__main__':
    entradaScript = sys.argv[1]
    sortidaScript = sys.argv[2]
    eliminarColumna(entradaScript, sortidaScript)