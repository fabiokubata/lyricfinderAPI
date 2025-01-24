import requests
import streamlit as st

def search_lyrics(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra

st.image("https://i.imgur.com/yAR32l0.png")
st.title ("Letras de músicas")

banda = st.text_input("Nome da Banda: ", key = "band")
musica = st.text_input("Nome da música: ", key= "song")
search = st.button ("Pesquisar")

if search:
    letra = search_lyrics(banda, musica)
    if letra:
        st.success("Aqui está a letra da música")
        st.text(letra)
    else: 
        st.error("Não encontramos a letra")