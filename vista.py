import streamlit as st
import pandas as pd

st.set_page_config(page_title="Valorizzazione Minacce RIDA", layout="wide")
st.title("Valorizzazione Minacce su dimensioni RIDA")

# Esempio di minacce
minacce = [
    {"ID": "M001", "Nome": "SQL Injection"},
    {"ID": "M002", "Nome": "Phishing"},
    {"ID": "M003", "Nome": "Accesso non autorizzato"},
]

dimensioni_rida = ["Riservatezza", "Integrità", "Disponibilità", "Autenticità"]

# Griglia: Righe = minacce, Colonne = RIDA
st.write("## Matrice di Valorizzazione")

dati_rida = {}

# Mostra intestazione colonne RIDA
cols = st.columns([2] + [1]*len(dimensioni_rida))
cols[0].markdown("**Minaccia**")
for i, dim in enumerate(dimensioni_rida):
    cols[i+1].markdown(f"**{dim}**")

# Costruzione della tabella
for minaccia in minacce:
    cols = st.columns([2] + [1]*len(dimensioni_rida))
    cols[0].markdown(f"{minaccia['ID']} - {minaccia['Nome']}")
    valori_rida = {}
    for i, dim in enumerate(dimensioni_rida):
        key = f"{minaccia['ID']}_{dim}"
        valori_rida[dim] = cols[i+1].checkbox("", key=key)
    dati_rida[minaccia["ID"]] = valori_rida

# Mostra il risultato finale alla fine
if st.button("Salva Valutazioni"):
    st.success("Valutazioni salvate!")
    df = pd.DataFrame.from_dict(dati_rida, orient="index").astype(int)
    st.dataframe(df)
    # Puoi anche esportare: df.to_excel("valutazioni_minacce.xlsx")
