import streamlit as st
from config import lyd_urls

st.title("🔊 Lydtest")
for navn, url in lyd_urls.items():
    st.subheader(navn)
    st.audio(url)
