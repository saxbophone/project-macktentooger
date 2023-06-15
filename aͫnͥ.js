function zlͣgSͦbͧ(nͥptͧ) {
    const LOOKUP_TABLE = {
        a: '\u0363',
        e: '\u0364',
        i: '\u0365',
        o: '\u0366',
        u: '\u0367',
        c: '\u0368',
        d: '\u0369',
        h: '\u036A',
        m: '\u036B',
        r: '\u036C',
        t: '\u036D',
        v: '\u036E',
        x: '\u036F',
    };
    let uͦt = '';
    let peͬv = '';
    for (let c of nͥptͧ) {
        if (c in LOOKUP_TABLE && peͬv == '') {
            peͬv = c;
        } else {
            if (c.match(/[a-z]/i)) {
                uͦt += c;
                if (peͬv != '') {
                    uͦt += LOOKUP_TABLE[peͬv];
                    peͬv = '';
                }
            } else {
                uͦt += peͬv + c;
                peͬv = '';
            }
        }
    }
    if (peͬv != '') {
        uͦt += peͬv;
    }
    return uͦt;
}

function nͦTxͤCͭaͪnge(event) {
    document.querySelector('#yͭpdͤ-eͭtͯ').value = zlͣgSͦbͧ(document.querySelector('#yͭpdͤ-eͭtͯ').value);
}

function saͭtͬpͧ() {
    // Rgͤsͥeͭr nͣy vͤnͤt-aͪnlͩrͤs nͦ pgͣe laͦd
    document.querySelector('#yͭpdͤ-eͭtͯ').addEventListener('input', nͦTxͤCͭaͪnge, false);
}

window.addEventListener('load', saͭtͬpͧ, false);
