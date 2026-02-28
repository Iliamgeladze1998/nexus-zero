import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import pytz

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: სათაურის ფერის და ქვედა ნაწილის ფიქსი
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        background-image: 
            linear-gradient(rgba(37, 99, 235, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(37, 99, 235, 0.1) 1px, transparent 1px) !important;
        background-size: 30px 30px !important;
    }

    /* სათაურის ფერი - აუცილებლად მუქი */
    h1 {
        color: #1E3A8A !important;
        font-weight: 800 !important;
        text-shadow: none !important;
    }

    /* მობილურზე ტექსტის და დაშორებების ოპტიმიზაცია */
    @media (max-width: 768px) {
        .main .block-container {
            padding-top: 1rem !important;
            padding-bottom: 2rem !important;
        }
        h1 { font-size: 1.6rem !important; }
        .stMarkdown p { font-size: 0.9rem !important; }
    }

    .stSlider p, .stMultiSelect label, .stTextInput label {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    .stButton>button {
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- TIME ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
timestamp = datetime.now(tbilisi_tz).strftime('%H:%M')

# --- HEADER (აქ ფერი ფიქსირებულია) ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.markdown(f"**STATUS:** ONLINE | **TIME:** {timestamp}")
st.write("---")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    skills = st.multiselect("Assets:", ["Tech", "Crypto", "Business", "Finance", "Art", "Marketing", "Real Estate", "Charisma"])

mission = st.text_input("MISSION:", placeholder="e.g. Find a partner...")

if st.button("EXECUTE"):
    if mission:
        with st.spinner("SCANNING..."):
            prompt = f"Mission: {mission}. Profile: {social_type}. Assets: {skills}. Tbilisi strategy."
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3}
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                st.info(response.json()["choices"][0]["message"]["content"])
            except:
                st.error("Error connecting to Grid.")

# --- FOOTER (გარანტირებული ხილვადობა) ---
st.write("---")
with st.expander("⚖️ LEGAL & PRIVACY"):
    st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")

st.markdown(f"**Architect:** Ilia Mgeladze | [**Contact**](mailto:mgeladzeilia39@gmail.com)")
