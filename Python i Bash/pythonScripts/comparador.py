# -*- coding: utf-8 -*-
import sys

def calcular_similitud(arxiu1, arxiu2):
    with open(arxiu1, 'r') as f1, open(arxiu2, 'r') as f2:
        cont1 = f1.readlines()
        cont2 = f2.readlines()

    if len(cont1) > 20:
        similitudes = []
        i = 0
        while i < len(cont1):
            contingut1 = ''.join(cont1[i:i+20])
            contingut2 = ''.join(cont2[i:i+20])
            longitud_igual = comparativa(contingut1, contingut2)
            similitud = (2.0 * longitud_igual) / (len(contingut1) + len(contingut2)) * 100
            similitudes.append(similitud)
            i += 20

        similitud_media = sum(similitudes) / len(similitudes)
        return similitud_media

    else:
        contingut1 = ''.join(cont1)
        contingut2 = ''.join(cont2)
        longitud_igual = comparativa(contingut1, contingut2)
        similitud = (2.0 * longitud_igual) / (len(contingut1) + len(contingut2)) * 100
        return similitud




def calcular_similitud_version_linea(arxiu1, arxiu2):
    with open(arxiu1, 'r') as f1, open(arxiu2, 'r') as f2:
        similitud=[]
        cont1 = f1.readlines()
        cont2 = f2.readlines()

        if len(cont1) > 20:
            return similitud

        contingut1 = guardar_en_lista(cont1)
        contingut2 = guardar_en_lista(cont2)
        for i in range(len(contingut1)):
            longitud_igual = comparativa(contingut1[i][0], contingut2[i][0])
            similitud.append((2.0 * longitud_igual) / (len(contingut1[i][0]) + len(contingut2[i][0])) * 100) 
    
    return similitud

def guardar_en_lista(entrada):
    contingut=[]
    for linea in entrada:
            paraules= linea.split('\n')
            contingut.append(paraules)

    for paraula in contingut:
        posicio=0
        while posicio<len(paraula):
            if paraula[posicio]=='':
                paraula.pop(posicio)
            else:
                posicio=posicio+1           
    return contingut

def comparativa(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else: 
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

if __name__ == '__main__':
    opcio = sys.argv[1]
    arxiu1 = sys.argv[2]
    arxiu2 = sys.argv[3]

    if opcio == "LINIA":
        similitud = calcular_similitud_version_linea(arxiu1, arxiu2)
        cont=0

        if not similitud:
            print('El tamany del fitxer és massa gran per aquesta opció')
        else:
            for simi in similitud:
                cont+=1
                print("El percentatge de similitud entre els fitxers en la línea {} és: {:.2f}%".format(cont, simi))
    else:
        similitud = calcular_similitud(arxiu1, arxiu2)
        print("El percentatge de similitud entre els fitxers {} i {} és: {:.2f}%".format(arxiu1, arxiu2, similitud))