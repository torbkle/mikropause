import streamlit as st
import datetime
from config import lyd_urls

def hent_ai_anbefaling():
    """Gir en enkel anbefaling basert på tidspunkt på dagen."""
    hour = datetime.datetime.now().hour
    if hour < 11:
        return "🌅 Start dagen med en rolig pustepause"
    elif hour < 15:
        return "🧠 Ta en skjermpause for å bevare fokus"
    else:
        return "🌇 Avslutt dagen med en mikrobevegelse"

def spill_autolyd(url):
    """Spiller av lyd automatisk via HTML. Ingen HEAD-sjekk – mer stabilt."""
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
    """Viser pausekort med instruksjon og automatisk lyd."""
    st.markdown("---")
    st.markdown('<div class="pausekort">', unsafe_allow_html=True)

    instruksjoner = {
        "Pust": "🫁 Pust inn i 4 sekunder, hold i 4, pust ut i 6.",
        "Skjermpause": "👀 Se ut av vinduet i 60 sekunder.",
        "Fokus": "🔕 Lukk alle faner. Sett en intensjon.",
        "Bevegelse": "🧍‍♂️ Strekk armene og rull skuldrene."
    }

    st.markdown(f'<img src="{ikon_url}" class="ikon"> <span class="pausevalg">{valg}</span>', unsafe_allow_html=True)
    st.markdown(instruksjoner.get(valg, "🧘 Ta en kort pause."))
    spill_autolyd(lyd_urls.get(valg))
    st.markdown('</div>', unsafe_allow_html=True)
