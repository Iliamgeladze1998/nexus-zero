import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: Light High-Contrast (ყველაფერი მკაფიოდ იკითხება)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #F8FAFC !important; 
        color: #0F172A !important;
    }
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 2px solid #E2E8F0;
    }
    [data-testid="stWidgetLabel"], .stSlider p {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    .stTextInput>div>div>input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #2563EB !important;
    }
    .stButton>button {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        font-weight: bold;
        border-radius: 8px;
        height: 3.5em;
    }
    .stInfo {
        border-left: 5px solid #10B981 !important;
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-size: 1.1em;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (აღდგენილი სრული სია) ---
with st.sidebar:
    st.markdown("### ⚙️ PARAMETERS")
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
    
    # სრული Assets სია, როგორც ადრე იყო
    asset_list = [
        "Tech/Dev", "Crypto/Web3", "Business/Sales", "Finance/Investment", 
        "Creative/Design", "Art/Culture", "Real Estate", "Marketing/PR", 
        "Capital", "Charisma", "Education/Academic"
    ]
    skills = st.multiselect("Available Assets:", asset_list)
    
    st.write("---")
    with st.expander("⚖️ LEGAL & PRIVACY"):
        st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")
    if st.button("RESET SESSION"):
        st.rerun()

# --- MAIN INTERFACE ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.write(f"STATUS: ONLINE | {datetime.now().strftime('%Y-%m-%d %H:%M')}")

mission = st.text_input("DEFINE MISSION:", placeholder="მაგ: მინდა ვიპოვო პარტნიორი სტარტაპისთვის...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("ANALYZING SOCIAL VECTORS..."):
            context = f"User: {social_type}, Skills: {skills}."
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            
            # სტრატეგიული პრომპტი (დაბრუნებული მკაცრი სტრუქტურა)
            if is_georgian:
                prompt = (
                    f"კონტექსტი: {context}. მისია: {mission}. "
                    "მოამზადე მკაცრი სოციალური ბლუპრინტი თბილისისთვის. "
                    "სტრუქტურა: 1. ვენიუს სახელი, 2. ზუსტი წერტილი, 3. სამიზნე პერსონა, "
                    "4. Icebreaker, 5. სტრატეგიული გეგმა, 6. ალბათობის ლოგიკა. "
                    "ტონი: ტაქტიკური, მოკლე. დაიწყე პირდაპირ 'ვენიუს სახელი:'-ით."
                )
            else:
                prompt = (
                    f"User context: {context}. Mission: {mission}. "
                    "Provide an elite Social Blueprint for Tbilisi. "
                    "Structure: 1. Venue Name, 2. Exact Spot, 3. Persona Identification, "
                    "4. Professional Icebreaker, 5. Strategic Action Plan, 6. Logic of Probability. "
                    "Tone: Tactical. Start with 'Venue Name:'."
                )
            
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "system", "content": "You are a senior social strategist. Be specific for Tbilisi locations."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                
                try:
                    venue_line = [l for l in result.split('\n') if ':' in l][0]
                    venue_name = venue_line.split(':')[1].strip()
                except:
                    venue_name = "Tbilisi"
                
                st.markdown("### 🎯 STRATEGIC INTEL ACQUIRED")
                st.info(result)
                
                m1, m2 = st.columns(2)
                with m1:
                    st.link_button("📍 DEPLOY TO GOOGLE MAPS", f"https://www.google.com/maps/search/{urllib.parse.quote(venue_name + ' Tbilisi')}")
                with m2:
                    st.download_button("💾 DOWNLOAD DOSSIER", result, file_name="nexus_mission.txt")
                    
            except Exception:
                st.error("System connection error.")
    else:
        st.warning("MISSION INPUT REQUIRED.")

# --- FOOTER (შენი სახელი და მეილი) ---
st.write("---")
f1, f2 = st.columns([2, 1])
with f1:
    st.markdown(f"**Architect:** Ilia Mgeladze<br>**Inquiries:** <a href='mailto:mgeladzeilia39@gmail.com'>mgeladzeilia39@gmail.com</a>", unsafe_allow_html=True)
with f2:
    st.markdown("<div style='text-align: right; color: #64748B;'>V3.2 | SYSTEM OPERATIONAL</div>", unsafe_allow_html=True)
