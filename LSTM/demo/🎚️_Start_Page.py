import streamlit as st

col1, col2, col3 = st.columns(3)
with col1:
    st.empty()
with col2:
    st.image("https://www.infosys.com/content/dam/infosys-web/en/global-resource/18/springboard-logo.png")
with col3:
    st.empty()

st.title("Multipage demo for TransferIQ")