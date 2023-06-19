import sys
import io
import os

def selector(carpeta, entrada):

    frases = open(entrada, "w")
    for arxiu in os.listdir(carpeta):
        if arxiu.endswith(".txt") and arxiu.startswith("cv001_") and arxiu[6:9].isdigit():
            nom = os.path.splitext(arxiu)[0]
            if os.path.exists(os.path.join(carpeta, nom + ".err")):
                if os.path.getsize(os.path.join(carpeta, nom + ".err")) == 0:
                    with open(os.path.join(carpeta, arxiu), "r") as text:
                        with open(os.path.join(carpeta, nom + ".fon"), "r") as f_fonema:
                            fonema = f_fonema.read().strip().replace("\n", " ")
                            frase = text.read().strip()
                            frases.write(frase + "\t" + fonema + "\n")
    frases.close()


if __name__ == '__main__':
    entradaCarpeta = sys.argv[1]
    entradaScript = sys.argv[2]
    selector(entradaCarpeta, entradaScript)