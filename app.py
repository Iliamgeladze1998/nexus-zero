import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI UPGRADE: Slate Theme (No more pure black)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    /* მთავარი ფონი - Slate Gray */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'JetBrains Mono', monospace;
        background-color: #1E1E2E !important; 
        color: #CDD6F4;
    }

    /* Sidebar - ოდნავ მუქი */
    [data-testid="stSidebar"] {
        background-color: #181825 !important;
        border-right: 2px solid #313244;
    }

    /* სათაური */
    h1 { color: #89B4FA !important; }

    /* Input ველები - თეთრი ფონით უკეთესი კონტრასტისთვის */
    .stTextInput>div>div>input {
        background-color: #313244 !important;
        color: #F5E0DC !important;
        border: 2px solid #45475A !important;
        border-radius: 10px;
    }

    /* ღილაკი */
    .stButton>button {
        border: none !important;
        background-color: #F5C2E7 !important;
        color: #11111B !important;
        font-weight: bold;
        border-radius: 10px;
        height: 3.5em;
    }
    .stButton>button:hover {
        background-color: #CBA6F7 !important;
        box-shadow: 0 0 15px #CBA6F7;
    }

    /* პასუხის ბლოკი - ძალიან მკაფიო */
    .stInfo {
        border: 2px solid #A6E3A1 !important;
        background-color: #313244 !important;
        color: #FFFFFF !important;
        font-size: 1.1em;
        border-radius: 15px;
        padding: 25px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ⚙️ PARAMETERS")
    social_type = st.select_slider("Energy:", options=["Introvert", "Balanced", "Extrovert"])
    skills = st.multiselect("Assets:", ["Tech", "Business", "Art", "Finance", "Marketing"])
    st.write("---")
    with st.expander("⚖️ LEGAL"):
        st.caption("Developed by Ilia Mgeladze.")
    if st.button("RESET"):
        st.rerun()

# --- MAIN INTERFACE ---
st.title("⚡ NEXUS ZERO: TBILISI GRID")
st.write(f"SYSTEM STATUS: ONLINE | {datetime.now().strftime('%H:%M')}")

mission = st.text_input("DEFINE MISSION:", placeholder="მაგ: მინდა ვიპოვო პარტნიორი...")

if st.button("EXECUTE"):
    if mission:
        with st.spinner("PROCESSING..."):
            context = f"User: {social_type}, Skills: {skills}."
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            
            prompt = (f"Context: {context}. Mission: {mission}. Provide tactical advice for Tbilisi. "
                      f"Respond in {'Georgian' if is_georgian else 'English'}.")
            
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3
            }
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                st.info(result)
            except:
                st.error("Error.")
    else:
        st.warning("Input required.")

# --- FOOTER ---
st.write("---")
st.markdown(f"**Architect:** Ilia Mgeladze | **Contact:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
