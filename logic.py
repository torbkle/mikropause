import streamlit as st
import openai
from config import lyd_urls

openai.api_key = st.secrets["OPENAI_API_KEY"]
hent_ai_anbefaling = hent_ai_variant

def hent_ai_variant(pausetype):
    """Genererer en ny pauseinstruksjon basert på valgt type."""
    prompt = f"""
    Gi en kort og konkret instruksjon for en mikropause av typen '{pausetype}'.
    Den skal være litt annerledes enn standardversjonen, men fortsatt enkel og rolig.
    Maks 2 setninger. Skriv på norsk.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "🧘 Ta en kort pause. (AI-feil)"

def spill_autolyd(url):
    if url:
        html = f"""
        <audio autoplay>
            <source src="{url}" type="audio/mp3">
        </audio>
        <script>
            window.scrollTo({{ top: document.body.scrollHeight, behavior: 'smooth' }});
        </script>
        """
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("🔇 Lydfil mangler eller URL er tom.")

def vis_pausekort(valg, ikon_url):
    st.markdown("---")
    st.markdown('<div class="pausekort">', unsafe_allow_html=True)
    st.markdown(f'<img src="{ikon_url}" class="ikon"> <span class="pausevalg">{valg}</span>', unsafe_allow_html=True)

    instruksjon = hent_ai_variant(valg)
    st.markdown(instruksjon)
    spill_autolyd(lyd_urls.get(valg))

    st.markdown('</div>', unsafe_allow_html=True)
