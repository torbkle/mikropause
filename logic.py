import streamlit as st
import datetime
import requests

lyd_urls = {
    "Pust": ".../pust.mp3",
    "Skjermpause": ".../skjermpause.mp3",
    "Fokus": ".../fokus.mp3",
    "Bevegelse": ".../bevegelse.mp3"
}

def hent_ai_anbefaling():
    hour = datetime.datetime.now().hour
    if hour < 11:
        return "🌅 Start dagen med en rolig pustepause"
    elif hour < 15:
        return "🧠 Ta en skjermpause for å bevare fokus"
    else:
        return "🌇 Avslutt dagen med en mikrobevegelse"

def spill_autolyd(url):
    try:
        if requests.head(url).status_code == 200:
            st.markdown(f"""
                <audio autoplay>
                    <source src="{url}" type="audio/mp3">
                </audio>
                <script>window.scrollTo({{ top: document.body.scrollHeight, behavior: 'smooth' }});</script>
            """, unsafe_allow_html=True)
        else:
            st.warning("🔇 Lydfilen kunne ikke lastes.")
    except:
        st.warning("🔇 Lydstøtte er ikke tilgjengelig.")

def vis_pausekort(valg, ikon_url):
    st.markdown("---")
    st.markdown('<div class="pausekort">', unsafe_allow_html=True)
    st.markdown(f'<img src="{ikon_url}" class="ikon"> <span class="pausevalg">{valg}</span>', unsafe_allow_html=True)
    instruksjoner = {
        "Pust": "🫁 Pust inn i 4 sekunder, hold i 4, pust ut i 6.",
        "Skjermpause": "👀 Se ut av vinduet i 60 sekunder.",
        "Fokus": "🔕 Lukk alle faner. Sett en intensjon.",
        "Bevegelse": "🧍‍♂️ Strekk armene og rull skuldrene."
    }
    st.markdown(instruksjoner[valg])
    spill_autolyd(lyd_urls[valg])
    st.markdown('</div>', unsafe_allow_html=True)
