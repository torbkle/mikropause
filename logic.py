import streamlit as st
import openai

# 🔐 Hent API-nøkkel fra Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def hent_ai_variant(pausetype):
    """Returnerer AI-generert instruksjon basert på valgt pausetype."""
    prompt = f"Gi en kort, vennlig instruksjon for en mikropause med fokus på {pausetype.lower()}."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].message.content.strip()

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
    """Viser pausekort med ikon, AI-instruksjon og lyd."""
    st.image(ikon_url, width=100)
    instruksjon = hent_ai_variant(pausetype)
    st.markdown(f"### {instruksjon}")
    lyd_url = f"https://torbkle.github.io/mikropause-assets/audio/{pausetype.lower()}.mp3"
    spill_autolyd(lyd_url)
