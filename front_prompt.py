import streamlit as st

st.set_page_config(page_title="Agent IA Orientation", layout="wide")

# style css
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

.boite {
    background: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    transition: transform 0.2s ease-in-out;
}
.boite:hover {
    transform: scale(1.02);
}

.pourcent {
    padding: 5px 10px;
    border-radius: 10px;
    font-size: 12px;
}

.bien {background-color: #1f7a1f;}
.moyen {background-color: #b58900;}
.mauvais {background-color: #a83232;}

.titre {
    font-size: 40px;
    font-weight: bold;
}

.sous-titre {
    font-size: 18px;
    color: #aaa;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center;">
    <h1>Ton Master</h1>
</div>
""", unsafe_allow_html=True)

st.chat_message("assistant").write("Trouve le master parfait pour toi")
    
user_input = st.text_area(
    "Décris ce que tu veux",
    placeholder="Ex: Je veux devenir développeur web, j’aime Python mais pas les maths...",
    height=150
)

if st.button("Analyser"):

    # Code pour trouver les masters

    st.divider()
    if user_input.strip() == "":
        st.warning("Veuillez entrer une description")
    else:

        # exemple Backend
        st.subheader("Masters trouvés")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            <div class="boite">
                <h3>Master IA</h3>
                <p>Université Paul Sabatier</p>
                <p>Toulouse</p>
                <p class="pourcent bien">Score : 90%</p>
                <p>Correspond à Data Scientist</p>
                <p>Modules IA et Python</p>
                <p>Compatible alternance</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="boite">
                <h3>Master IA</h3>
                <p>Université Paris 8</p>
                <p>Ile-de-France</p>
                <p class="pourcent moyen">Score : 50%</p>
                <p>Bon pour IA</p>
                <p>Contient des maths</p>
            </div>
            """, unsafe_allow_html=True)

        st.subheader("Compatibilité globale")
        st.progress(0.70)