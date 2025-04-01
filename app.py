import openai
import streamlit as st

st.set_page_config(page_title="AI Kaarttekst Generator", page_icon="💌")

st.title("💌 AI Kaarttekst Generator")
st.write("Vul hieronder kort in voor wie en welke gelegenheid je een kaarttekst nodig hebt. De AI doet de rest.")

# API Key invullen
openai_api_key = st.text_input("Jouw OpenAI API-sleutel", type="password")

# Input van gebruiker
prompt = st.text_area("Wat is de gelegenheid of boodschap? ✍️", 
                      placeholder="Bijvoorbeeld: Mijn tante is jarig en ze houdt van tuinieren.")

if st.button("Genereer kaarttekst") and openai_api_key and prompt:
    with st.spinner("AI is aan het schrijven..."):
        try:
            openai.api_key = openai_api_key

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Je schrijft warme, persoonlijke, stijlvolle kaartteksten voor alle gelegenheden. Hou het menselijk en oprecht."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.8
            )

            kaarttekst = response.choices[0].message.content.strip()
            st.success("🎉 Hier is jouw kaarttekst:")
            st.write(kaarttekst)

        except Exception as e:
            st.error(f"Er ging iets mis: {e}")
