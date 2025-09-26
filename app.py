import streamlit as st
from ui import sett_stil, vis_header
from logic import hent_ai_anbefaling, vis_pausekort
from data import vis_statistikk
from i18n import hent_tekst

sett_stil(mørk=True)
vis_header()

språk = st.selectbox("Språk / Language", ["Norsk", "English"])
tekst = hent_tekst(språk)

st.info(hent_ai_anbefaling())
st.markdown(f"### {tekst['valg']}")
valg = st.radio("", ["Pust", "Skjermpause", "Fokus", "Bevegelse"], label_visibility="collapsed")

ikon_urls = {
    "Pust": ".../wind.svg",
    "Skjermpause": ".../eye-off.svg",
    "Fokus": ".../target.svg",
    "Bevegelse": ".../stretch-horizontal.svg"
}

if st.button(tekst["start"]):
    vis_pausekort(valg, ikon_urls[valg])

vis_statistikk()
st.caption("Utviklet av Torbjørn Kleiven – [infera.no](https://www.infera.no)")
