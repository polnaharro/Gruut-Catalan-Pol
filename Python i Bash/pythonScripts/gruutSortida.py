import json
import sys
import io

def gruutSortida(entrada, sortida):
    with open(entrada, 'r') as f_entrada:
        dades = json.load(f_entrada)
        words = dades['words']
        
        phonemes = []
        for word in words:
            if word['is_spoken']:
                if phonemes:
                    phonemes.append('#')
                phoneme = ' '.join(word['phonemes'])
                phonemes.append(phoneme)
        final = ' '.join(phonemes)
        
    with io.open(sortida, 'w', encoding='utf-8') as f_sortida:
            f_sortida.write(final)



if __name__ == '__main__':
    entradaScript = sys.argv[1]
    sortidaScript = sys.argv[2]
    gruutSortida(entradaScript, sortidaScript)