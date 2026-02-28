import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import pytz

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: Adaptive Grid + Mobile Fix
st.markdown("""
<style>
    /* საერთო ფონი და ბადე */
    [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        background-image: 
            linear-gradient(rgba(37, 99, 235, 0.08) 1px, transparent 1px),
            linear-gradient(90deg, rgba(37, 99, 235, 0.08) 1px, transparent 1px) !important;
        background-size: 40px 40px !important;
    }

    /* მობილურის სპეციალური ოპტიმიზაცია */
    @media (max-width: 768px) {
        [data-testid="stAppViewContainer"] {
            background-size: 20px 20px !important; /* უფრო ნაზი ბადე მობილურზე */
            padding: 10px !important;
        }
        h1 {
            font-size: 1.5rem !important; /* სათაური რომ არ დაიკარგოს */
            text-align: center;
        }
        .stSlider, .stMultiSelect {
            margin-bottom: 20px !important;
        }
    }

    /* ტექსტების და ღილაკების სტილი */
    .stSlider p, .stMultiSelect label, .stTextInput label {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    
    .stButton>button {
        width: 100% !important;
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 12px;
        height: 3.5em;
        font-weight: bold;
        border: none !important;
    }
    
    /* პასუხის ბლოკი */
    .stInfo {
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 15px !important;
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- TIME LOGIC (Tbilisi) ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
now_tbilisi = datetime.now(tbilisi_tz)
timestamp = now_tbilisi.strftime('%Y-%m-%d %H:%M')

# --- MAIN INTERFACE ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.write(f"STATUS: **ONLINE** | {timestamp}")

st.write("---")

# პარამეტრების განლაგება
col1, col2 = st.columns(2)
with col1:
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    asset_list = ["Tech/Dev", "Crypto/Web3", "Business/Sales", "Finance/Investment", "Creative/Design", "Art/Culture", "Real Estate", "Marketing/PR", "Capital", "Charisma"]
    skills = st.multiselect("Available Assets:", asset_list)

st.write("")
mission = st.text_input("DEFINE MISSION:", placeholder="e.g. Find a business partner in Real Estate...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("SCANNING GRID..."):
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            prompt = f"Mission: {mission}. Profile: {social_type}. Assets: {skills}. Tactical Tbilisi guide."
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3}
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                st.info(response.json()["choices"][0]["message"]["content"])
            except:
                st.error("Connection error.")
    else:
        st.warning("Input required.")

# Privacy & Footer
st.write("")
with st.expander("⚖️ LEGAL & PRIVACY POLICY"):
    st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")

st.write("---")
st.markdown(f"**Architect:** Ilia Mgeladze | **Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
