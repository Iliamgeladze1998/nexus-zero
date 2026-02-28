import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import pytz

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: Grid Background + Fixed Elements
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        background-image: 
            linear-gradient(rgba(37, 99, 235, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(37, 99, 235, 0.1) 1px, transparent 1px) !important;
        background-size: 35px 35px !important;
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
        font-weight: bold;
        height: 3.5em;
    }
</style>
""", unsafe_allow_html=True)

# --- TIME LOGIC ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
now_tbilisi = datetime.now(tbilisi_tz)
timestamp = now_tbilisi.strftime('%Y-%m-%d %H:%M')

# --- MAIN INTERFACE (Logo & Title Back) ---
st.title("🎯 NEXUS ZERO: TBILISI GRID") # ლოგო დაბრუნდა
st.write(f"STATUS: **ONLINE** | {timestamp}")

st.write("---")

# პარამეტრები ეგრევე ეკრანზე
col1, col2 = st.columns(2)
with col1:
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    asset_list = ["Tech/Dev", "Crypto/Web3", "Business/Sales", "Finance/Investment", "Creative/Design", "Art/Culture", "Real Estate", "Marketing/PR", "Capital", "Charisma"]
    skills = st.multiselect("Available Assets:", asset_list)

mission = st.text_input("DEFINE MISSION:", placeholder="e.g. Find a business partner in Real Estate...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("ANALYZING..."):
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            prompt = f"Mission: {mission}. Profile: {social_type}. Assets: {skills}. Tactical Tbilisi guide."
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3}
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                st.info(response.json()["choices"][0]["message"]["content"])
            except:
                st.error("Error.")
    else:
        st.warning("Input required.")

# Privacy Policy & Legal (დაბრუნდა)
with st.expander("⚖️ LEGAL & PRIVACY POLICY"):
    st.caption("Nexus Zero Protocol. Encrypted session. Developed by Ilia Mgeladze.")

st.write("---")
st.markdown(f"**Architect:** Ilia Mgeladze | **Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
