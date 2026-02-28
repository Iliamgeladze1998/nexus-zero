import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import pytz  # დროის ზონისთვის

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: Mobile & Desktop Optimized (Light Mode)
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
    }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .stSlider p, .stMultiSelect label, .stTextInput label {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    .stButton>button {
        width: 100% !important;
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 10px;
        height: 3.5em;
        font-weight: bold;
    }
    .stInfo {
        border-left: 5px solid #10B981 !important;
        background-color: #FFFFFF !important;
        color: #000000 !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- TIME LOGIC (Tbilisi Fix) ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
now_tbilisi = datetime.now(tbilisi_tz)
timestamp = now_tbilisi.strftime('%Y-%m-%d %H:%M')

# --- MAIN INTERFACE ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.write(f"STATUS: **ONLINE** | {timestamp}") # აქ გამოჩნდება სწორი დრო

st.write("---")

# პარამეტრები მთავარ გვერდზე მობილურისთვის
col1, col2 = st.columns([1, 1])
with col1:
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    asset_list = [
        "Tech/Dev", "Crypto/Web3", "Business/Sales", "Finance/Investment", 
        "Creative/Design", "Art/Culture", "Real Estate", "Marketing/PR", 
        "Capital", "Charisma", "Education/Academic"
    ]
    skills = st.multiselect("Available Assets:", asset_list)

st.write("")
mission = st.text_input("DEFINE MISSION:", placeholder="e.g. Find a business partner in Real Estate...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("ANALYZING VECTORS..."):
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            
            context = f"User is {social_type} with skills in {skills}."
            if is_georgian:
                prompt = f"კონტექსტი: {context}. მისია: {mission}. მოამზადე სოციალური სტრატეგია თბილისისთვის. იყავი კონკრეტული."
            else:
                prompt = f"Context: {context}. Mission: {mission}. Tactical social blueprint for Tbilisi. Be specific."

            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "system", "content": "You are a senior social strategist for Tbilisi. Match the user's language."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                
                st.markdown("### 🎯 STRATEGIC INTEL")
                st.info(result)
                
                # Maps Link Extraction (Simple)
                venue_name = "Tbilisi"
                if "Venue Name:" in result:
                    venue_name = result.split("Venue Name:")[1].split("\n")[0].strip()
                
                m1, m2 = st.columns(2)
                with m1:
                    st.link_button("📍 DEPLOY TO MAPS", f"https://www.google.com/maps/search/{urllib.parse.quote(venue_name)}")
                with m2:
                    st.download_button("💾 DOWNLOAD DOSSIER", result, file_name="nexus_intel.txt")
            except:
                st.error("Connection Interrupted.")
    else:
        st.warning("MISSION INPUT REQUIRED.")

# Footer Section
st.write("---")
with st.expander("⚖️ LEGAL & PRIVACY POLICY"):
    st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze. No data is stored permanently.")

f1, f2 = st.columns([2, 1])
with f1:
    st.markdown(f"**Architect:** Ilia Mgeladze | **Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
with f2:
    st.markdown(f"<div style='text-align: right; color: #64748B;'>V3.6 | SYSTEM OPERATIONAL</div>", unsafe_allow_html=True)
