# -*- coding: utf-8 -*-
import sys

def adaptarDades(entrada, codiSortida, frasesSortida):

    frase=[]
    final=[]
    llistat=[]

    with open(entrada, 'r') as f_entrada:
        linies = f_entrada.readlines()
        for linia in linies:
            paraules= linia.split('\n')
            frase.append(paraules)

    for paraula in frase:
        posicio=0
        while posicio<len(paraula):
            if paraula[posicio]=='':
                paraula.pop(posicio)
            else:
                posicio=posicio+1


    for paraules in frase:
        for paraula in paraules:
            paraula= paraula.replace('( ', '').replace('")', '')
            llistat= paraula.split(' "')

            final.append(llistat)

    with open(frasesSortida, 'w') as f_frases:
        for frase in final:
            f_frases.write(str(frase[1]) + '\n')

    with open(codiSortida, 'w') as f_codi:
        
        for codi in final:
            f_codi.write(str(codi[0]) + '\n')

if __name__ == '__main__':
    entradaScript = sys.argv[1]
    sortidaFraseScript = sys.argv[2]
    sortidaCodiScript = sys.argv[3]
    adaptarDades(entradaScript, sortidaFraseScript, sortidaCodiScript)