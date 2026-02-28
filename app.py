import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide", initial_sidebar_state="expanded")

# UI: მობილურზე მორგებული სტილი
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
    }
    /* სლაიდერის და მულტისელექტის ფერები */
    .stSlider p, .stMultiSelect label {
        color: #000000 !important;
        font-weight: bold !important;
    }
    .stButton>button {
        width: 100% !important;
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- MAIN INTERFACE (Sidebar-ის გარეშე, პირდაპირ ეკრანზე) ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.write(f"STATUS: ONLINE | {datetime.now().strftime('%H:%M')}")

st.write("---")
# პარამეტრები გადმოვიტანეთ აქ, რომ მობილურზე ეგრევე ჩანდეს
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
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "system", "content": "Senior strategist. Respond in " + ("Georgian" if is_georgian else "English")},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                st.info(result)
            except:
                st.error("Connection error.")
    else:
        st.warning("Input required.")

# Privacy & Info ბოლოში
with st.expander("⚖️ LEGAL & PRIVACY POLICY"):
    st.caption("Nexus Zero Protocol. Encrypted session. Developed by Ilia Mgeladze.")

st.write("---")
st.markdown(f"**Architect:** Ilia Mgeladze | **Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
