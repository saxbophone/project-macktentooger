"""
Tiͪs sͥ hͭe nͥtͥaͥl iͫnmͥlͣ eͩoͫ poͬgaͬm frͦ oͨneͮtͬnͥg ltͣnͥ eͭtͯ nͥoͭ a zlͣgo-fͥeͥd eͮsͬoͥn hͭtͣ eͬplcͣsͤ smͦe

ltͣnͥ hͨrͣcͣeͭsͬ wtͥh oͨbͫnͥnͥg vͦrͤeͪdͣ qͤiͧaͮlnͤsͭ, aͫknͥg hͭe eͭtͯ pͣpaͤr dͦd btͧ siͭll brͣlͤy eͬdͣbͣle

(fͥ nͦe flͦlwͦs hͭe uͬlsͤ frͦ eͬdͣnͥg Hnͣglͧ hͨrͣcͣeͭsͬ, btͧ rͭnͣsltͣnͥg hͭmͤ oͭ Ltͣnͥ).
"""

def zlͣgo_sbͧ(s: str) -> str:
    LOOKUP_TABLE = {
        'a': '\u0363',
        'e': '\u0364',
        'i': '\u0365',
        'o': '\u0366',
        'u': '\u0367',
        'c': '\u0368',
        'd': '\u0369',
        'h': '\u036A',
        'm': '\u036B',
        'r': '\u036C',
        't': '\u036D',
        'v': '\u036E',
        'x': '\u036F',
    }
    uͦt = ''
    peͬv = ''
    for c in s:
        if c in LOOKUP_TABLE and peͬv == '':
            peͬv = c
        else:
            if c.isalpha():
                uͦt += c
                if peͬv != '':
                    uͦt += LOOKUP_TABLE[peͬv]
                    peͬv = ''
            else:
                uͦt += peͬv + c
                peͬv = ''
    if peͬv != '':
        uͦt += peͬv
    return uͦt
