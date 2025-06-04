import streamlit as st
import pandas as pd

st.title("Valorizzazione Minacce")

uploaded_file = st.file_uploader("Carica file Excel con minacce", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Anteprima dati:", df.head())
else:
    st.write("Oppure inserisci una nuova minaccia manualmente")

    with st.form("minaccia_form"):
        id_minaccia = st.text_input("ID")
        nome = st.text_input("Nome")
        descrizione = st.text_area("Descrizione")
        r = st.checkbox("Riservatezza")
        i = st.checkbox("Integrità")
        d = st.checkbox("Disponibilità")
        a = st.checkbox("Autenticità")
        submitted = st.form_submit_button("Salva")

        if submitted:
            nuova_minaccia = {
                "ID": id_minaccia,
                "Nome": nome,
                "Descrizione": descrizione,
                "R": int(r),
                "I": int(i),
                "D": int(d),
                "A": int(a)
            }
            st.success(f"Minaccia salvata: {nuova_minaccia}")

            # Salva su Excel
            try:
                df_salvate = pd.read_excel("minacce_salvate.xlsx")
            except FileNotFoundError:
                df_salvate = pd.DataFrame(columns=["ID", "Nome", "Descrizione", "R", "I", "D", "A"])
            df_salvate = pd.concat([df_salvate, pd.DataFrame([nuova_minaccia])], ignore_index=True)
            df_salvate.to_excel("minacce_salvate.xlsx", index=False)
            st.info("Minaccia aggiunta a minacce_salvate.xlsx")
