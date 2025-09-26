def hent_tekst(språk="Norsk"):
    return {
        "Norsk": {
            "start": "Start pause",
            "valg": "Velg type mikropause",
            "statistikk": "📊 Dagens pauser",
            "antall": "Antall pauser",
            "tid": "Total pausetid"
        },
        "English": {
            "start": "Start break",
            "valg": "Choose your microbreak",
            "statistikk": "📊 Today's breaks",
            "antall": "Breaks taken",
            "tid": "Total break time"
        }
    }[språk]
