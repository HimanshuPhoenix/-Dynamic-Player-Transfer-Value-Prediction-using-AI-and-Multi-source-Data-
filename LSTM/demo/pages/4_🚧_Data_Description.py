import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
st.markdown("""<h2>Data Description:</h2>
<ol><li>
The model uses Transfermrkt players as mater data list</li>
<li>
Over 1500 players were scraped from the Top-Competitions Page </li>
<li>
Players were matched using fuzzy-logic with the players list from StatsBomb database on the basis of names and nicknames (around 1300 matches were saved).
</li>
<li>Injury data has been scraped from respective player pages from Transfermarkt
</li>
<li>For sentiment analysis, reddit posts were scanned and TextBlob was used for sentiment score
            </li>
""",unsafe_allow_html=True)
st.markdown("""
<style>
.stImage {
  background-color: white;
  padding: 10px; # Optional: add some padding
}
</style>
""", unsafe_allow_html=True)
st.image("pages/data.png")