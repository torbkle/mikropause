import streamlit as st

def sett_stil(mørk=False):
    bakgrunn = "#121212" if mørk else "#F1F8F9"
    tekst = "#E0E0E0" if mørk else "#005F73"
    st.markdown(f"""
        <style>
        html, body {{ background-color: {bakgrunn}; color: {tekst}; overflow-x: hidden; }}
        .pausekort {{ background-color: {bakgrunn}; padding: 24px; border-radius: 12px; margin-bottom: 24px; }}
        .ikon {{ width: 48px; vertical-align: middle; margin-right: 12px; }}
        .pausevalg {{ font-size: 20px; font-weight: 600; color: {tekst}; }}
        .stButton>button {{ font-size: 18px; padding: 12px 24px; width: 100%; border-radius: 8px; }}
        </style>
    """, unsafe_allow_html=True)

def vis_header():
    st.title("🧘 Mikropause")
    st.subheader("Pustepauser for et klarere hode")

