# -*- coding: utf-8 -*-
import sys
import io
def eliminarRepetits(entrada, sortida):
    diccionari = {}
    
    with open(entrada, 'r') as f_entrada:
        linies = f_entrada.readlines()

    for linia in linies:
        elements = linia.strip().split('\t')
        paraula = elements[0]
        valor = elements[1]
        
        diccionari[paraula] = valor
    with io.open(sortida, 'w') as f_sortida:
        for paraula, valor in diccionari.items():
            
            f_sortida.write(paraula.decode('utf-8'))
            f_sortida.write(' '.decode('utf-8'))
            f_sortida.write(valor.decode('utf-8'))
            f_sortida.write('\n'.decode('utf-8'))


if __name__ == '__main__':
    entradaScript = sys.argv[1]
    sortidaScript = sys.argv[2]
    eliminarRepetits(entradaScript, sortidaScript)