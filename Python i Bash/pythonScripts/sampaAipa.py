# -*- coding: utf-8 -*-
import sys
from io import open
import unicodedata

def cambiaForma(entrada, frasesSortida, fonemesSortida):
    with open(entrada, 'r', encoding='utf-8') as f_entrada:
        texts=[]
        fonemes=[]
        linies = f_entrada.readlines()
        for linia in linies:
            paraules = linia.split('\t')
            for posicio in range(0, len(paraules)):
                paraules[posicio] = paraules[posicio].replace('\n', '')
            texts.append(paraules[0])
            fonemes.append(paraules[1])

    with open(frasesSortida, 'w', encoding='utf-8') as f_frases:
        for text in texts:
            f_frases.write(text + '\n')

    with open(fonemesSortida, 'w', encoding='utf-8') as f_fonemas:
        for fonema in fonemes:
            f_fonemas.write(fonema + '\n')

def eliminarEspais(entrada):
    for paraula in entrada:
        posicio=0
        while posicio<len(paraula):
            if paraula[posicio]=='':
                paraula.pop(posicio)
            else:
                posicio=posicio+1    
    return entrada

def deSampaIpa(opcio, taula, entrada, sortida):
    with open(taula, 'r') as f_taula:
        llistat = []
        contingutTaula = f_taula.readlines()
        for line in contingutTaula:
            conversio = line.split('\n')
            llistat.append(conversio)
            
    llistat = eliminarEspais(llistat)

    lista = []
    for paraules in llistat:
        for paraula in paraules:
            paraula = paraula.split('\t')
            lista.append(paraula)
      
    IPA = []
    SAMPA = []

    for fonema in lista:
        IPA.append(fonema[0])
        SAMPA.append(fonema[1])
        
    with open(entrada, 'r') as f_entrada:
        frase = []
        contingutEntrada = f_entrada.readlines()
        for line in contingutEntrada:
            paraules = line.split('\n')
            frase.append(paraules)

    frase = eliminarEspais(frase)

    final = []
    for paraules in frase:
        for paraula in paraules:
            for posicio in range(len(IPA)):
                if opcio == 'IPA':
                    paraula = paraula.replace(IPA[posicio], SAMPA[posicio])
                elif opcio == 'SAMPA':
                    if SAMPA[posicio] != 'rr':
                        paraula = paraula.replace(SAMPA[posicio], IPA[posicio])
            paraula = paraula.replace('ɾɾ'.decode('utf-8'), 'r')
            final.append(paraula)
            
    with open(sortida, 'w') as f_sortida:
        for paraula in final:
            f_sortida.write(paraula)
            f_sortida.write('\n'.decode('utf-8'))

def unio(fraseEntrada, entradaFonema, sortida):
    with open(fraseEntrada, 'r') as f_frases:
        paraules=[]
        contingutFrase = f_frases.readlines()
        for line in contingutFrase:
            paraula= line.split('\n')
            paraules.append(paraula)

    paraules = eliminarEspais(paraules)
             
    with open(entradaFonema, 'r') as f_fonemes:
        fonemas=[]
        contingutfonemas = f_fonemes.readlines()
        for liniaFon in contingutfonemas:
            fonema= liniaFon.split('\n')
            fonemas.append(fonema)
            
    fonemas = eliminarEspais(fonemas)
            
    with open(sortida, 'w') as f_sortida:
        for i in range(len(paraules)):
            Paraula=paraules[i][0].replace("['",'').replace("']",'')
            Fonema=fonemas[i][0].replace('["','').replace('"]','').replace("['",'').replace("']",'')

            f_sortida.write(Paraula)
            f_sortida.write('\t'.decode('utf-8'))
            f_sortida.write(Fonema)
            f_sortida.write('\n'.decode('utf-8'))

if __name__ == '__main__':
    opcio = sys.argv[1]
    entradaScript = sys.argv[2]
    sortidaScript = sys.argv[3]
    cambiaForma(entradaScript, 'sortidaPython/frasesSortida.fr', 'sortidaPython/fonemesSortida.fo')
    deSampaIpa(opcio, 'pythonScripts/taulaConversio.txt', 'sortidaPython/fonemesSortida.fo', 'sortidaPython/fonemesIPA.fo')
    unio('sortidaPython/frasesSortida.fr', 'sortidaPython/fonemesIPA.fo', sortidaScript)