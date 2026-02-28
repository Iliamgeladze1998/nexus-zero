import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import pytz

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: Adaptive Grid + No "Press Enter" + Visibility Fix
st.markdown("""
<style>
    /* Grid Background */
    [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        background-image: 
            linear-gradient(rgba(37, 99, 235, 0.08) 1px, transparent 1px),
            linear-gradient(90deg, rgba(37, 99, 235, 0.08) 1px, transparent 1px) !important;
        background-size: 30px 30px !important;
    }

    /* აქრობს "Press Enter to apply" ტექსტს */
    div[data-testid="stTextInput"] div[data-testid="stMarkdownContainer"] p {
        display: none !important;
    }
    .st-emotion-cache-1pxm8yv { display: none !important; }

    /* სათაურის და ტექსტის სტილი */
    h1 { color: #1E3A8A !important; font-weight: 800 !important; }
    p, label { color: #000000 !important; font-weight: 700 !important; }

    /* მობილურის ოპტიმიზაცია */
    @media (max-width: 768px) {
        .main .block-container { padding: 1rem !important; }
        h1 { font-size: 1.6rem !important; }
    }

    /* ღილაკის სტილი */
    .stButton>button {
        width: 100% !important;
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
        height: 3.5em;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# --- TIME ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
timestamp = datetime.now(tbilisi_tz).strftime('%H:%M')

# --- HEADER ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.caption(f"STATUS: ONLINE | TIME: {timestamp}")
st.write("---")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    social_type = st.select_slider("Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    skills = st.multiselect("Assets:", ["Tech", "Crypto", "Business", "Finance", "Art", "Marketing", "Real Estate", "Charisma"])

# Placeholder-ის ფიქსი შენი მოთხოვნით
mission = st.text_input("MISSION:", placeholder="e.g. I want to find a business partner...")

if st.button("EXECUTE ALIGNMENT"):
    if mission:
        with st.spinner("SCANNING..."):
            prompt = f"Mission: {mission}. Profile: {social_type}. Assets: {skills}. Tbilisi strategy."
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3}
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                st.info(response.json()["choices"][0]["message"]["content"])
            except:
                st.error("Grid Error.")

# --- FOOTER ---
st.write("---")
with st.expander("⚖️ LEGAL & PRIVACY"):
    st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")

st.markdown(f"**Architect:** Ilia Mgeladze")
st.markdown(f"**Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
