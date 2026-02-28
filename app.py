import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# აიძულებს თემას იყოს Light მობილურზეც
st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

st.markdown("""
<style>
    /* მობილურის ოპტიმიზაცია და ფერების ჩაკეტვა */
    [data-testid="stAppViewContainer"], html, body {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
    }
    
    /* Sidebar-ის ფერი მობილურზეც */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }

    /* ტექსტის ზომა მობილურისთვის */
    h1 {
        font-size: 1.8rem !important;
        color: #1E3A8A !important;
    }

    /* ღილაკი მობილურზე */
    .stButton>button {
        width: 100% !important;
        background-color: #2563EB !important;
        color: white !important;
        border: none !important;
        padding: 10px !important;
        font-weight: bold !important;
    }

    /* Placeholder-ის ფერი */
    ::placeholder {
        color: #94A3B8 !important;
        opacity: 1;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ⚙️ PARAMETERS")
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
    asset_list = ["Tech/Dev", "Crypto/Web3", "Business/Sales", "Finance/Investment", "Creative/Design", "Art/Culture", "Real Estate", "Marketing/PR", "Capital", "Charisma", "Education/Academic"]
    skills = st.multiselect("Available Assets:", asset_list)
    st.write("---")
    with st.expander("⚖️ LEGAL & PRIVACY"):
        st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")
    if st.button("RESET SESSION"):
        st.rerun()

# --- MAIN ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.write(f"STATUS: ONLINE | {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# ინგლისური Placeholder, როგორც გინდოდა
mission = st.text_input("DEFINE MISSION:", placeholder="e.g. Find a business partner in Real Estate...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("ANALYZING..."):
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            prompt = f"Mission: {mission}. User: {social_type}, Skills: {skills}. Tactical blueprint for Tbilisi."
            
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "system", "content": "You are a social strategist. Be specific. Respond in " + ("Georgian" if is_georgian else "English")}, {"role": "user", "content": prompt}],
                "temperature": 0.3
            }
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                st.info(result)
                
                m1, m2 = st.columns(2)
                with m1:
                    st.link_button("📍 GOOGLE MAPS", f"https://www.google.com/maps/search/{urllib.parse.quote('Tbilisi')}")
                with m2:
                    st.download_button("💾 DOWNLOAD", result, file_name="nexus_mission.txt")
            except:
                st.error("System connection error.")
    else:
        st.warning("Input required.")

# --- FOOTER ---
st.write("---")
st.markdown(f"**Architect:** Ilia Mgeladze | **Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
st.markdown(f"<div style='text-align: right; color: #64748B;'>V3.4 | SYSTEM OPERATIONAL</div>", unsafe_allow_html=True)
