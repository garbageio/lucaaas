import numpy as  np


vezs = [
    'vez',
    'vezz',
    'vecchio',
    'zi',
    'ziiii',
    'vecchioOo',
]

intros = [
    'allora',
    'fondamentalmente',
    'praticamente',
    'beh',
    'zi',
    'no ma',
    'posso dirti,',
]

mains = [
    'i sugoli li puoi mangiare in 2 modi',
    'questo è un desiderata',
    'non so se salgo questa settimana vez',
    'mi è guarita l unghia del piede',
    'mi è diventata nera un altra unghia',
    'per provare il sesso anale devi prima lubrificare la zona',
    'è constatato che la stimolazione del perineo fa eccitare tantissimo sia le femmine che i maschi',
]

intro_domandas = [
    'sai',
    'ma sai',
]

domandas = [
    'cosa mangiavano gli etruschi ?',
    'qual è il segno zodiacale che manca sulla torre dell orologio ?',
    'qual è il segno zodiacale che manca sulla torre dell orologio ?',
    'che a bitonto c è la circonvalla a forma di cerchio perfetto ?',
    'cosa sono le giuggiole ?',
    'cosa possiamo fare adesso ?',
    'che la cuperosi è la dilatazione delle piccole vene del viso, che possono presentare ramificazioni a livello cutaneo',
]

esclamaziones = [
    'strabello',
    'strafico',
    'strabuono',
    'minchia',
    'spacca',
]

b4_vezs = [
    'manda foto',
    'foto o fake',
    'per forza',
    'ci sta',
    'una quota parte',
]

pseudobestemmias = [
    'zio can',
    'zio porco',
]

frase_interas = [
    'posso dire',
    'allora, al netto di questo',
    'sai cosa ??',
    'però poi bombiamo',
    'si zii ci spacchiamo di negroni, caldarroste e pistacchi tostati',
    'ma comeEe',
    'prontoOo',
    'allora ..',
    'mmmmm vabbè',
    'vediamo se ci sono eventi stasera ..',
    'si o no !?',
    'quanto vuoi scommetterci ?',
    'i panini me li ha fatti la Luisa',
    'SEPARATE DALLA NASCITA',
    'quanto sei vecchio che vai a casa adesso ?',
    'cuperosi',
    '🤣',
    '❤️',
]


def generate_tormentone():
    intro = np.random.choice(intros)
    main = np.random.choice(mains)
    return f'{intro} {main}'


def generate_little_tormentone():
    b4_vez = np.random.choice(b4_vezs)
    vez = np.random.choice(vezs)
    return f'{b4_vez} {vez}'


def generate_frase_intera():
    frase_intera = np.random.choice(frase_interas)
    return f'{frase_intera}'


def generate_esclamazione():
    esclamazione = np.random.choice(esclamaziones)
    return f'{esclamazione}!'


def generate_esclamazione_vez():
    esclamazione = np.random.choice(esclamaziones)
    vez = np.random.choice(vezs)
    return f'{esclamazione} {vez}'


def generate_pseudobestemmia():
    pseudobestemmia = np.random.choice(pseudobestemmias)
    return f'{pseudobestemmia}'


def generate_domanda():
    intro_domanda = np.random.choice(intro_domandas)
    domanda = np.random.choice(domandas)
    return f'{intro_domanda} {domanda}'


def generate_sentence():
    gen = np.random.choice(
        [
            generate_tormentone,
            generate_little_tormentone,
            generate_frase_intera,
            generate_esclamazione,
            generate_esclamazione_vez,
            generate_domanda,
            # generate_pseudobestemmia
        ],
        p=[0.3, 0.2, 0.3, 0.05, 0.05, 0.1]
    )
    return f'{gen()}'


if __name__ == '__main__':
    print('\n\n=======', generate_sentence(), '\n')



