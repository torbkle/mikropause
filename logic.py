import streamlit as st
from openai import OpenAI

# 🔐 Initialiser OpenAI-klienten
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 🧘 Fallback-instruksjoner hvis AI ikke svarer
fallback_instruksjoner = {
    "Pust": "Lukk øynene og ta tre dype pust. Slipp spenninger i skuldrene.",
    "Skjermpause": "Se bort fra skjermen i 20 sekunder. Fokuser på et punkt langt unna.",
    "Fokus": "Lukk unødvendige faner. Sett en intensjon for de neste 5 minuttene.",
    "Bevegelse": "Strekk armene over hodet og rull skuldrene bakover. Gjenta tre ganger."
}

def hent_ai_variant(pausetype):
    """Returnerer AI-generert instruksjon, eller lokal fallback ved feil."""
    prompt = f"Gi en kort, vennlig instruksjon for en mikropause med fokus på {pausetype.lower()}."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return fallback_instruksjoner.get(pausetype, "Ta en kort pause og pust dypt.")

def spill_autolyd(lydfil_url):
    """Spiller av lyd automatisk via HTML."""
    st.markdown(
        f"""
        <audio autoplay>
            <source src="{lydfil_url}" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )

def vis_pausekort(pausetype, ikon_url):
    """Viser pausekort med ikon, AI-instruksjon (eller fallback) og spiller lyd uansett."""
    st.image(ikon_url, width=100)

    # 🎯 Prøv å hente AI-instruksjon, ellers bruk fallback
    try:
        instruksjon = hent_ai_variant(pausetype)
    except Exception:
        instruksjon = fallback_instruksjoner.get(pausetype, "Ta en kort pause og pust dypt.")

    st.markdown(f"### {instruksjon}")

    # 🔊 Spill lyd uansett
    lyd_url = f"https://torbkle.github.io/mikropause-assets/audio/{pausetype.lower()}.mp3"
    spill_autolyd(lyd_url)

