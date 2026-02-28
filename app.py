import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import pytz

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: Adaptive Design with Bottom Visibility Fix
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        background-image: 
            linear-gradient(rgba(37, 99, 235, 0.08) 1px, transparent 1px),
            linear-gradient(90deg, rgba(37, 99, 235, 0.08) 1px, transparent 1px) !important;
        background-size: 30px 30px !important;
    }

    /* მობილურის ფიქსი */
    @media (max-width: 768px) {
        .main .block-container {
            padding-top: 2rem !important;
            padding-bottom: 5rem !important;
        }
        h1 { font-size: 1.4rem !important; }
        .stSlider p, .stMultiSelect label, .stTextInput label {
            font-size: 0.8rem !important;
        }
        footer {visibility: hidden;}
    }

    .stSlider p, .stMultiSelect label, .stTextInput label {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    
    .stButton>button {
        width: 100% !important;
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- TIME ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
now_tbilisi = datetime.now(tbilisi_tz)
timestamp = now_tbilisi.strftime('%H:%M')

# --- HEADER ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.write(f"STATUS: **ONLINE** | {timestamp}")
st.write("---")

# --- CONTROLS ---
col1, col2 = st.columns(2)
with col1:
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    skills = st.multiselect("Available Assets:", ["Tech", "Crypto", "Business", "Finance", "Art", "Marketing", "Real Estate", "Charisma"])

mission = st.text_input("DEFINE MISSION:", placeholder="e.g. Find a partner...")

if st.button("EXECUTE"):
    if mission:
        with st.spinner("ANALYZING..."):
            prompt = f"Mission: {mission}. Profile: {social_type}. Assets: {skills}. Tbilisi social strategy."
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3}
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                st.info(response.json()["choices"][0]["message"]["content"])
            except:
                st.error("System error.")

# --- FOOTER (ესენი აღარ გაქრება) ---
st.write("")
with st.expander("⚖️ LEGAL & PRIVACY POLICY"):
    st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")

st.write("---")
st.markdown(f"**Architect:** Ilia Mgeladze | **Contact:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
