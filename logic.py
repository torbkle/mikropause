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

# 🎨 Animasjoner per pausetype
animasjoner = {
    "Pust": """
        <div style="text-align:center; margin-top:20px;">
            <div style="width:60px; height:60px; border-radius:50%; background:#4CAF50; animation:breath 3s ease-in-out infinite;"></div>
        </div>
        <style>
        @keyframes breath {
            0% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.4); opacity: 0.4; }
            100% { transform: scale(1); opacity: 0.8; }
        }
        </style>
    """,
    "Skjermpause": """
        <div style="display:flex; justify-content:center; gap:5px; margin-top:20px;">
            <div style="width:8px; height:30px; background:#2196F3; animation:wave 1s infinite;"></div>
            <div style="width:8px; height:30px; background:#2196F3; animation:wave 1s infinite 0.2s;"></div>
            <div style="width:8px; height:30px; background:#2196F3; animation:wave 1s infinite 0.4s;"></div>
        </div>
        <style>
        @keyframes wave {
            0%, 100% { transform: scaleY(1); }
            50% { transform: scaleY(2); }
        }
        </style>
    """,
    "Fokus": """
        <div style="text-align:center; margin-top:20px;">
            <div style="width:80px; height:6px; background:#FF9800; animation:pulseLine 2s infinite;"></div>
        </div>
        <style>
        @keyframes pulseLine {
            0% { opacity: 1; }
            50% { opacity: 0.3; }
            100% { opacity: 1; }
        }
        </style>
    """,
    "Bevegelse": """
        <div style="text-align:center; margin-top:20px;">
            <div style="width:40px; height:40px; border-radius:50%; background:#E91E63; animation:spin 2s linear infinite;"></div>
        </div>
        <style>
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        </style>
    """
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
    """Spiller av lyd automatisk med usynlig spiller."""
    st.markdown(
        f"""
        <audio autoplay style="display:none;">
            <source src="{lydfil_url}" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )

def vis_pausekort(pausetype, ikon_url):
    """Viser pausekort med ikon, instruksjon, lyd og tematisk animasjon."""
    st.image(ikon_url, width=100)
    instruksjon = hent_ai_variant(pausetype)
    st.markdown(f"### {instruksjon}")

    # 🔊 Spill lyd
    lyd_url = f"https://torbkle.github.io/mikropause-assets/audio/{pausetype.lower()}.mp3"
    spill_autolyd(lyd_url)

    # 🌈 Vis animasjon basert på pausetype
    animasjon = animasjoner.get(pausetype)
    if animasjon:
        st.markdown(animasjon, unsafe_allow_html=True)
