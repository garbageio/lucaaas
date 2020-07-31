import numpy as  np


vezs = [
    'vez',
    'vecchio',
    'vecchius',
    'vekkyo',
    'brode',
    'zi',
    'brody',
]

esclamaziones = [
    'devastante',
    'pazzesko',
    'speciale',
    'top',
    'parkour',
    'spettacolo',
    'esagerato'
]

pseudobestemmias = [
    'porcodiaz',
    'zio can',
    'zio povero',
    'urco can',
    'zio bestia',
    'porcoddue'
]

frase_interas = [
    'NON CI CREDO MAI !',
    'ti dico',
    'MUOIO',
    'STO MALISSIMO',
    'zi',
    'non voglio snitch nel gang',
    'CIAVATTE',
    'piango vecchio',
    'no dai',
    'recommender system',
    'mi sbrego',
    'FACCIO UN CASINO',
    'MAIL A BELEN',
    'lo faccio',
    'si o no ?!',
    'VOLO DIRETTO VEKKYO DECOLLO',
    'GIUDICAMI',
    'cv in comunicazione',
    'coooos',
    'UGUALE',
    'top nic pastic',
    'PATENA',
    'sono in allianz',
    '🤣',
    'GANG',
    'TE DICO FERMETE',
    'se semo presi a bira',
    'sei un drago',
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



