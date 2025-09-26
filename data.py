import streamlit as st

def vis_statistikk():
    st.markdown("---")
    st.subheader("📊 Dagens pauser")
    col1, col2 = st.columns(2)
    col1.metric("Antall pauser", "3")
    col2.metric("Total pausetid", "6 minutter")
