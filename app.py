import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI UPGRADE: Light Mode for Maximum Readability
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    /* მთავარი ფონი - ღია და სუფთა */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #F0F2F6 !important; 
        color: #1A1C25 !important;
    }

    /* Sidebar - მკაფიო კონტრასტით */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #D1D5DB;
    }

    /* ტექსტები Sidebar-ში - მაქსიმალურად მუქი */
    [data-testid="stWidgetLabel"], .stSlider p {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 1.1em !important;
    }

    /* სათაური */
    h1 { color: #1E3A8A !important; font-weight: 800; }

    /* Input ველები */
    .stTextInput>div>div>input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #3B82F6 !important;
        border-radius: 8px;
    }

    /* ღილაკი - მყვირალა ლურჯი */
    .stButton>button {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        font-weight: bold;
        border: none !important;
        border-radius: 8px;
        height: 3.5em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #1D4ED8 !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }

    /* პასუხის ბლოკი - თეთრი ფონი, შავი ტექსტი */
    .stInfo {
        border-left: 5px solid #10B981 !important;
        background-color: #FFFFFF !important;
        color: #111827 !important;
        font-size: 1.15em;
        border-radius: 8px;
        padding: 25px !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ⚙️ PARAMETERS")
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
    asset_list = ["Tech", "Business", "Art", "Finance", "Marketing", "Real Estate", "Charisma"]
    skills = st.multiselect("Available Assets:", asset_list)
    st.write("---")
    with st.expander("⚖️ LEGAL & PRIVACY"):
        st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")
    if st.button("RESET SESSION"):
        st.rerun()

# --- MAIN INTERFACE ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.markdown(f"**STATUS:** <span style='color:green;'>ONLINE</span> | {datetime.now().strftime('%Y-%m-%d %H:%M')}", unsafe_allow_html=True)

mission = st.text_input("DEFINE MISSION:", placeholder="მაგ: მინდა ვიპოვო ბიზნეს პარტნიორი...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("ANALYZING..."):
            context = f"User: {social_type}, Skills: {skills}."
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            
            if is_georgian:
                prompt = f"კონტექსტი: {context}. მისია: {mission}. მოამზადე სტრატეგია თბილისისთვის ქართულად."
            else:
                prompt = f"Context: {context}. Mission: {mission}. Provide strategy for Tbilisi in English."
            
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "system", "content": "You are a social strategist."}, {"role": "user", "content": prompt}],
                "temperature": 0.3
            }
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                
                st.markdown("### 🎯 STRATEGIC INTEL")
                st.info(result)
                
                m1, m2 = st.columns(2)
                with m1:
                    st.link_button("📍 GOOGLE MAPS", f"https://www.google.com/maps/search/{urllib.parse.quote('Tbilisi')}")
                with m2:
                    st.download_button("💾 DOWNLOAD", result, file_name="nexus_mission.txt")
            except:
                st.error("Error connecting to system.")
    else:
        st.warning("Please enter mission.")

# --- FOOTER ---
st.write("---")
st.markdown(f"**Architect:** Ilia Mgeladze | **Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
