import streamlit as st

st.set_page_config(page_title="Agent IA Orientation", layout="wide")

# -------------------------
# css
# -------------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}

.card {
    background: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    transition: transform 0.2s ease-in-out;
}
.card:hover {
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


st.sidebar.title("Préférences")

debouche = st.sidebar.selectbox(
    "Débouché",
    ["Développeur Web", "Cybersécurité", "IA"]
)

modules_aimes = st.sidebar.multiselect(
    "Modules que tu aimes",
    ["IA", "Python", "Réseaux", "Maths", "Web"]
)

modules_detestes = st.sidebar.multiselect(
    "Modules que tu détestes",
    ["IA", "Python", "Réseaux", "Maths", "Web"]
)

rythme = st.sidebar.radio(
    "Rythme",
    ["Alternance", "Initial"]
)

localisation = st.sidebar.selectbox(
    "Localisation",
    ["Ile-de-France", "Lyon", "Lille", "Toulouse"]
)
st.markdown('<div class="titre">Ton Master</div>', unsafe_allow_html=True)
st.markdown('<div class="sous-titre">Trouve le master parfait pour toi</div>', unsafe_allow_html=True)

st.write("")

if st.button("Analyser"):

    # Code à mettre pour trouver les masters

    # Exemple de résulat
    st.divider()
    st.subheader("Masters trouvés")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="card">
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
        <div class="card">
            <h3>Master IA</h3>
            <p>Université Paris 8</p>
            <p>Ile-de-France</p>
            <p class="pourcent moyen">Score : 50%</p>
            <p>Bon pour IA</p>
            <p>Contient des maths</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("📊 Compatibilité globale")
    st.progress(0.70)