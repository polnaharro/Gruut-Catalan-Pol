#!/bin/bash

archivo="frases-alicia-original.txt"
contador=1

mkdir -p gruutSortida
mkdir -p sortidaPython

while IFS= read -r linea; do
    frase="$linea"
    gruutNom="gruut-${contador}.txt"
    pythonNom="python-${contador}.txt"
    gruut --language ca "$frase" > "gruutSortida/$gruutNom"
    
    # Llamar al archivo Python y pasarle los argumentos
    python pythonScripts/gruutSortida.py "gruutSortida/$gruutNom" "sortidaPython/$pythonNom"
    
    contador=$((contador + 1))
    nomPython="sortidaPython/python-contador.txt"
done < "$archivo"

python pythonScripts/unioScripts.py $nomPython $contador "sortidaPython/gruutUnido.txt"
python pythonScripts/netejaScripts.py "sortidaPython/gruutUnido.txt" "gruut.txt"
