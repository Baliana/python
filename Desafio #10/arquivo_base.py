import artwork

RECEITAS = {
    "espada": {
        "ingredientes": {
            "ferro": 3,
            "madeira": 1,
        },
        "custo": 10,
        "arte": artwork.espada
    },
    "escudo": {
        "ingredientes": {
            "ferro": 2,
            "madeira": 3,
        },
        "custo": 8,
        "arte": artwork.escudo
    },
    "arco": {
        "ingredientes": {
            "madeira": 4,
            "corda": 2,
        },
        "custo": 7,
        "arte": artwork.arco
    },
}

recursos = {
    "ferro": 10,
    "madeira": 10,
    "corda": 5,
}

ouro = 0

moedas = {
    "Moeda de Ouro": 1,
    "Moeda de Prata": 0.5,
    "Moeda de Cobre": 0.1,
}