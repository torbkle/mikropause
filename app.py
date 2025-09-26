import streamlit as st
import datetime

# Konfigurasjon
st.set_page_config(page_title="Mikropause", page_icon="🧘", layout="centered")

# Header
st.title("🧘 Mikropause")
st.subheader("Pustepauser for et klarere hode")

# AI-anbefaling (simulert)
now = datetime.datetime.now()
hour = now.hour

if hour < 11:
    anbefaling = "🌅 Start dagen med en rolig pustepause"
elif hour < 15:
    anbefaling = "🧠 Ta en skjermpause for å bevare fokus"
else:
    anbefaling = "🌇 Avslutt dagen med en mikrobevegelse"

st.info(anbefaling)

# Pausevalg
st.markdown("### Velg type mikropause:")
pausevalg = st.radio("", ["🫁 Pust", "👀 Skjermpause", "🔕 Fokus", "🧍‍♂️ Bevegelse"])

# Start pause
if st.button("Start pause"):
    st.markdown("---")
    if "Pust" in pausevalg:
        st.markdown("🫁 **Pust inn i 4 sekunder, hold i 4, pust ut i 6.** Gjenta i 1 minutt.")
    elif "Skjermpause" in pausevalg:
        st.markdown("👀 **Se ut av vinduet i 60 sekunder.** La øynene hvile.")
    elif "Fokus" in pausevalg:
        st.markdown("🔕 **Lukk alle faner. Sett en intensjon for neste oppgave.**")
    elif "Bevegelse" in pausevalg:
        st.markdown("🧍‍♂️ **Strekk armene over hodet og rull skuldrene.** 3 ganger.")

# Statistikk (simulert)
st.markdown("---")
st.subheader("📊 Dagens pauser")
st.metric("Antall pauser", "3")
st.metric("Total pausetid", "6 minutter")

# Footer
st.markdown("---")
st.caption("Utviklet av Torbjørn Kleiven – [infera.no](https://www.infera.no)")
