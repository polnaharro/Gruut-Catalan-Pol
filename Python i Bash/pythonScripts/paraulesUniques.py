import string
import sys

def paraulesUniques(entrada, sortida):
    
    with open(entrada, 'r') as f_entrada:
        linies = f_entrada.readlines()

    paraules = []
    for linia in linies:
        for paraula in linia.split():
            paraula = paraula.translate(string.maketrans("", ""), string.punctuation)
            if paraula not in paraules:
                paraules.append(paraula)
    paraules.sort()

    with open(sortida, 'w') as f_sortida:
        for paraula in paraules:
            f_sortida.write(paraula + '\n')

if __name__ == '__main__':
    entradaScript = sys.argv[1]
    sortidaScript = sys.argv[2]
    paraulesUniques(entradaScript, sortidaScript)