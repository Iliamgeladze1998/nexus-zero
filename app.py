import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import pytz

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: სრული ფიქსი სათაურის, დაშორებების და ფონტების
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        background-image: 
            linear-gradient(rgba(37, 99, 235, 0.08) 1px, transparent 1px),
            linear-gradient(90deg, rgba(37, 99, 235, 0.08) 1px, transparent 1px) !important;
        background-size: 25px 25px !important;
    }
    /* სათაურის ფერი და ზომა */
    h1 {
        color: #1E3A8A !important;
        font-size: 1.8rem !important;
        margin-bottom: 0 !important;
    }
    /* მობილურზე დაშორებების მინიმიზაცია */
    .main .block-container {
        padding: 1rem !important;
    }
    .stSlider, .stMultiSelect, .stTextInput {
        margin-bottom: -10px !important;
    }
    /* ტექსტების სიმკვეთრე */
    p, span, label {
        color: #000000 !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
timestamp = datetime.now(tbilisi_tz).strftime('%H:%M')

st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.caption(f"STATUS: ONLINE | TIME: {timestamp}")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    social_type = st.select_slider("Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    skills = st.multiselect("Assets:", ["Tech", "Crypto", "Business", "Finance", "Art", "Marketing", "Real Estate", "Charisma"])

# შენი მოთხოვნილი Placeholder
mission = st.text_input("MISSION:", placeholder="I want to find a business partner...")

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
                st.error("Error.")

# --- FOOTER (გარანტირებული ხილვადობა) ---
st.write("---")
with st.expander("⚖️ LEGAL & PRIVACY"):
    st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")

# აქ ჩავწერე შენი სახელი და მეილი პირდაპირ, რომ არასდროს გაქრეს
st.markdown(f"**Architect:** Ilia Mgeladze")
st.markdown(f"**Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
