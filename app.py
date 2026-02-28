import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import pytz

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: Cyber Grid Optimization
st.markdown("""
<style>
    /* Grid Background Effect */
    [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        background-image: 
            linear-gradient(rgba(37, 99, 235, 0.05) 1px, transparent 1px),
            linear-gradient(90sdeg, rgba(37, 99, 235, 0.05) 1px, transparent 1px);
        background-size: 30px 30px; /* ბადის ზომა */
        color: #0F172A !important;
    }

    /* მობილურზე ბადის ზომის შემცირება */
    @media (max-width: 768px) {
        [data-testid="stAppViewContainer"] {
            background-size: 20px 20px;
        }
    }

    .stSlider p, .stMultiSelect label, .stTextInput label {
        color: #000000 !important;
        font-weight: 800 !important;
    }
    
    .stButton>button {
        width: 100% !important;
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 12px;
        height: 3.8em;
        font-weight: bold;
        border: none !important;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
    }
    
    .stInfo {
        border-left: 8px solid #2563EB !important;
        background-color: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(5px);
        color: #000000 !important;
        border-radius: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- TIME LOGIC ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
now_tbilisi = datetime.now(tbilisi_tz)
timestamp = now_tbilisi.strftime('%Y-%m-%d %H:%M:%S')

# --- INTERFACE ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.write(f"SYSTEM STATUS: **ONLINE** | {timestamp} (GET)")

st.write("---")

# Grid Layout for Parameters
col1, col2 = st.columns([1, 1])
with col1:
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    asset_list = ["Tech/Dev", "Crypto/Web3", "Business/Sales", "Finance/Investment", "Creative/Design", "Art/Culture", "Real Estate", "Marketing/PR", "Capital", "Charisma"]
    skills = st.multiselect("Available Assets:", asset_list)

st.write("")
mission = st.text_input("DEFINE MISSION:", placeholder="e.g. Find a strategic partner for a Web3 project...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("SCANNING GRID..."):
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            prompt = f"Mission: {mission}. User: {social_type}, Skills: {skills}. Tactical Tbilisi guide."
            
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "system", "content": "Senior strategist. Respond in " + ("Georgian" if is_georgian else "English")}, {"role": "user", "content": prompt}],
                "temperature": 0.3
            }
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                st.markdown("### 🎯 INTEL RECEIVED")
                st.info(result)
            except:
                st.error("Grid connection timeout.")
    else:
        st.warning("Input required.")

# Footer
st.write("---")
f1, f2 = st.columns([2, 1])
with f1:
    st.markdown(f"**Architect:** Ilia Mgeladze | **Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
with f2:
    st.markdown(f"<div style='text-align: right; color: #64748B;'>V3.7 | {timestamp}</div>", unsafe_allow_html=True)
