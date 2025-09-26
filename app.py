import streamlit as st
from ui import sett_stil, vis_header
from logic import vis_pausekort
from data import vis_statistikk
from i18n import hent_tekst
from config import ikon_urls

# 🌙 Mørk modus og layout
sett_stil(mørk=True)
vis_header()

# 🌐 Språkvalg
språk = st.selectbox("Språk / Language", ["Norsk", "English"])
tekst = hent_tekst(språk)

# 🧘 Pausevalg
st.markdown(f"### {tekst['valg']}")
valg = st.radio("", ["Pust", "Skjermpause", "Fokus", "Bevegelse"], label_visibility="collapsed")

# ▶️ Start pause
if st.button(tekst["start"]):
    vis_pausekort(valg, ikon_urls.get(valg))

# 📊 Statistikk
st.markdown("---")
st.subheader(tekst["statistikk"])
col1, col2 = st.columns(2)
col1.metric(tekst["antall"], "3")
col2.metric(tekst["tid"], "6 minutter")

# 🔗 Footer
st.markdown("---")
st.caption("Utviklet av Torbjørn Kleiven – [infera.no](https://www.infera.no)")
