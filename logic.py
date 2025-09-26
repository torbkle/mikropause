import streamlit as st
from openai import OpenAI

# 🔐 Initialiser OpenAI-klienten
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 🧘 Fallback-instruksjoner
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
    except Exception:
        return fallback_instruksjoner.get(pausetype, "Ta en kort pause og pust dypt.")

def spill_autolyd(lydfil_url):
    """Spiller av lyd automatisk med synlig spiller og JS fallback."""
    st.markdown(
        f"""
        <audio id="mikropauseAudio" autoplay>
            <source src="{lydfil_url}" type="audio/mpeg">
            Nettleseren din støtter ikke lydavspilling.
        </audio>
        <script>
            var audio = document.getElementById("mikropauseAudio");
            if (audio) {{
                audio.play().catch(function(error) {{
                    console.log("Autoplay blokkert, viser spiller.");
                    audio.setAttribute("controls", "true");
                }});
            }}
        </script>
        """,
        unsafe_allow_html=True
    )

def vis_pausekort(pausetype, ikon_url):
    """Viser pausekort med ikon, instruksjon og lyd – lyd spilles alltid."""
    st.image(ikon_url, width=100)
    instruksjon = hent_ai_variant(pausetype)
    st.markdown(f"### {instruksjon}")
    lyd_url = f"https://torbkle.github.io/mikropause-assets/audio/{pausetype.lower()}.mp3"
    spill_autolyd(lyd_url)
