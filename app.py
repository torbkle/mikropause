import streamlit as st
import datetime
import requests

st.set_page_config(page_title="Mikropause", page_icon="🧘", layout="centered")

# Stil
st.markdown("""
    <style>
    .pausekort {
        background-color: #F1F8F9;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .ikon {
        width: 40px;
        vertical-align: middle;
        margin-right: 10px;
    }
    .pausevalg {
        font-size: 18px;
        font-weight: 500;
        color: #005F73;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🧘 Mikropause")
st.subheader("Pustepauser for et klarere hode")

# AI-anbefaling
hour = datetime.datetime.now().hour
if hour < 11:
    anbefaling = "🌅 Start dagen med en rolig pustepause"
elif hour < 15:
    anbefaling = "🧠 Ta en skjermpause for å bevare fokus"
else:
    anbefaling = "🌇 Avslutt dagen med en mikrobevegelse"
st.info(anbefaling)

# Pausevalg
st.markdown("### Velg type mikropause:")
pausevalg = st.radio("", ["🫁 Pust", "👀 Skjermpause", "🔕 Fokus", "🧍‍♂️ Bevegelse"], label_visibility="collapsed")

# Ikoner og lydfiler via GitHub CDN
ikon_urls = {
    "Pust": "https://raw.githubusercontent.com/torbkle/mikropause/main/assets/icons/wind.svg",
    "Skjermpause": "https://raw.githubusercontent.com/torbkle/mikropause/main/assets/icons/eye-off.svg",
    "Fokus": "https://raw.githubusercontent.com/torbkle/mikropause/main/assets/icons/target.svg",
    "Bevegelse": "https://raw.githubusercontent.com/torbkle/mikropause/main/assets/icons/stretch-horizontal.svg"
}

lyd_urls = {
    "Pust": "https://raw.githubusercontent.com/torbkle/mikropause/main/assets/audio/pust.mp3",
    "Skjermpause": "https://raw.githubusercontent.com/torbkle/mikropause/main/assets/audio/skjermpause.mp3",
    "Fokus": "https://raw.githubusercontent.com/torbkle/mikropause/main/assets/audio/fokus.mp3",
    "Bevegelse": "https://raw.githubusercontent.com/torbkle/mikropause/main/assets/audio/bevegelse.mp3"
}

# Automatisk lydavspilling med fallback
def spill_autolyd(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            html = f"""
            <audio autoplay>
                <source src="{url}" type="audio/mp3">
                Din nettleser støtter ikke lydavspilling.
            </audio>
            """
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.warning("🔇 Lydfilen kunne ikke lastes. Prøv igjen senere.")
    except Exception:
        st.warning("🔇 Lydstøtte er ikke tilgjengelig akkurat nå.")

# Pausekort med autoplay
if st.button("Start pause"):
    st.markdown("---")
    st.markdown('<div class="pausekort">', unsafe_allow_html=True)

    if "Pust" in pausevalg:
        st.markdown(f'<img src="{ikon_urls["Pust"]}" class="ikon"> <span class="pausevalg">Pustepause</span>', unsafe_allow_html=True)
        st.markdown("🫁 Pust inn i 4 sekunder, hold i 4, pust ut i 6. Gjenta i 1 minutt.")
        spill_autolyd(lyd_urls["Pust"])
    elif "Skjermpause" in pausevalg:
        st.markdown(f'<img src="{ikon_urls["Skjermpause"]}" class="ikon"> <span class="pausevalg">Skjermpause</span>', unsafe_allow_html=True)
        st.markdown("👀 Se ut av vinduet i 60 sekunder. La øynene hvile.")
        spill_autolyd(lyd_urls["Skjermpause"])
    elif "Fokus" in pausevalg:
        st.markdown(f'<img src="{ikon_urls["Fokus"]}" class="ikon"> <span class="pausevalg">Fokuspause</span>', unsafe_allow_html=True)
        st.markdown("🔕 Lukk alle faner. Sett en intensjon for neste oppgave.")
        spill_autolyd(lyd_urls["Fokus"])
    elif "Bevegelse" in pausevalg:
        st.markdown(f'<img src="{ikon_urls["Bevegelse"]}" class="ikon"> <span class="pausevalg">Bevegelsespause</span>', unsafe_allow_html=True)
        st.markdown("🧍‍♂️ Strekk armene over hodet og rull skuldrene. 3 ganger.")
        spill_autolyd(lyd_urls["Bevegelse"])

    st.markdown('</div>', unsafe_allow_html=True)

# Statistikk
st.markdown("---")
st.subheader("📊 Dagens pauser")
col1, col2 = st.columns(2)
col1.metric("Antall pauser", "3")
col2.metric("Total pausetid", "6 minutter")

# Footer
st.markdown("---")
st.caption("Utviklet av Torbjørn Kleiven – [infera.no](https://www.infera.no)")
