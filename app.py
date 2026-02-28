import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import pytz

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: Cyber Grid WITH HIGH VISIBILITY
st.markdown("""
<style>
    /* მუქი და მკაფიო Grid ფონი */
    [data-testid="stAppViewContainer"] {
        background-color: #F0F4F8 !important;
        background-image: 
            linear-gradient(rgba(37, 99, 235, 0.15) 2px, transparent 2px),
            linear-gradient(90deg, rgba(37, 99, 235, 0.15) 2px, transparent 2px) !important;
        background-size: 40px 40px !important;
        color: #0F172A !important;
    }

    /* ელემენტების სტილი */
    .stSlider p, .stMultiSelect label, .stTextInput label {
        color: #1E3A8A !important;
        font-weight: 900 !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }
    
    .stButton>button {
        background-color: #1D4ED8 !important;
        color: white !important;
        border: 2px solid #1E40AF !important;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# --- REST OF THE CODE REMAINS THE SAME ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
now_tbilisi = datetime.now(tbilisi_tz)
timestamp = now_tbilisi.strftime('%H:%M:%S')

st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.write(f"GRID STATUS: **ACTIVE** | {timestamp}")

col1, col2 = st.columns(2)
with col1:
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    skills = st.multiselect("Available Assets:", ["Tech/Dev", "Crypto/Web3", "Business/Sales", "Finance/Investment", "Creative/Design", "Art/Culture", "Real Estate", "Marketing/PR", "Capital", "Charisma"])

mission = st.text_input("DEFINE MISSION:", placeholder="e.g. Locate a partner in Tbilisi...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("SCANNING..."):
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            prompt = f"Mission: {mission}. Profile: {social_type}. Assets: {skills}. Tactical advice for Tbilisi."
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3}
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                st.info(response.json()["choices"][0]["message"]["content"])
            except:
                st.error("System error.")
    else:
        st.warning("Input required.")

st.write("---")
st.markdown(f"**Architect:** Ilia Mgeladze | V3.7.1")
