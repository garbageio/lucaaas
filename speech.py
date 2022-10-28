import numpy as  np


vezs = [
    'vez',
]

esclamaziones = [
    'esagerato',
]

pseudobestemmias = [
    'zio can',
]

frase_interas = [
    'mmmmm vabbè',
    'quota parte',
    '🤣',
    'ETRUSCHI',
    '❤️'
]



def generate_tormentone():
    vez = np.random.choice(vezs)
    esclamazione = np.random.choice(esclamaziones)
    pseudobestemmia = np.random.choice(pseudobestemmias)
    return f'{vez} {esclamazione} {pseudobestemmia}'


def generate_only_exclamation():
    esclamazione = np.random.choice(esclamaziones)
    return f'{esclamazione}!'


def generate_frase_intera():
    frase_intera = np.random.choice(frase_interas)
    return f'{frase_intera}'


def generate_sentence():
    gen = np.random.choice([
        generate_tormentone,
        generate_only_exclamation,
        generate_frase_intera], 
        p = [0.4, 0.1, 0.5])
    return f'{gen()}'


if __name__ == '__main__':
    print('\n\n=======', generate_sentence(), '\n')



