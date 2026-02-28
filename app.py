import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI UPGRADE: Better Contrast & Readability
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    /* Background & Main Container */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'JetBrains Mono', monospace;
        background-color: #0e1117; /* Deep Charcoal instead of Pure Black */
        color: #e0e0e0;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }

    /* Input Field Styling */
    .stTextInput>div>div>input {
        background-color: #1c2128 !important;
        color: #00ffcc !important;
        border: 1px solid #30363d !important;
        border-radius: 8px;
    }

    /* Execute Button */
    .stButton>button {
        border: 1px solid #ff00ff !important;
        background-color: rgba(255, 0, 255, 0.05) !important;
        color: #ff00ff !important;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        background-color: #ff00ff !important;
        color: white !important;
        box-shadow: 0 0 25px rgba(255, 0, 255, 0.5);
    }

    /* Strategic Intel Box (Glassmorphism) */
    .stInfo {
        border: 1px solid #00ffcc !important;
        background-color: rgba(0, 255, 204, 0.05) !important;
        color: #ffffff !important;
        font-size: 1.1em;
        line-height: 1.6;
        border-radius: 12px;
        padding: 25px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    /* Professional Footer */
    .footer-text {
        color: #8b949e;
        font-size: 0.9em;
    }
    a {
        color: #58a6ff !important;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ⚙️ STRATEGIC PARAMETERS")
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
    asset_list = ["Tech/Dev", "Crypto/Web3", "Business/Sales", "Finance/Investment", "Creative/Design", "Art/Culture", "Real Estate", "Marketing/PR", "Capital", "Charisma"]
    skills = st.multiselect("Available Assets:", asset_list)
    st.write("---")
    with st.expander("⚖️ LEGAL & PRIVACY"):
        st.caption("Nexus Zero Protocol. Encrypted session. Developed by Ilia Mgeladze.")
    if st.button("RESET SESSION"):
        st.rerun()

# --- MAIN INTERFACE ---
st.title("⚡ NEXUS ZERO: TBILISI GRID")
st.markdown(f"<p style='color:#8b949e;'>STATUS: <span style='color:#00ffcc;'>ONLINE</span> | {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>", unsafe_allow_html=True)

mission = st.text_input("DEFINE MISSION:", placeholder="მაგ: მინდა ვიპოვო პარტნიორი სტარტაპისთვის...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("ANALYZING SOCIAL VECTORS..."):
            context = f"User: {social_type}, Skills: {skills}."
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            
            if is_georgian:
                prompt = (
                    f"კონტექსტი: {context}. მისია: {mission}. "
                    "მოამზადე მკაცრი სოციალური ბლუპრინტი თბილისისთვის. "
                    "სტრუქტურა დაიცავი უზუსტესად: "
                    "1. ვენიუს სახელი: (კონკრეტული ადგილი). "
                    "2. ზუსტი წერტილი: (სად უნდა დადგე/დაჯდე). "
                    "3. სამიზნე პერსონა: (ვისთან დაამყარო კონტაქტი). "
                    "4. პროფესიონალური Icebreaker: (ზუსტი ფრაზა). "
                    "5. სტრატეგიული გეგმა: (ნაბიჯ-ნაბიჯ მოქმედება). "
                    "6. ალბათობის ლოგიკა: (რატომ არის ეს ადგილი იდეალური). "
                    "ტონი: ტაქტიკური, მოკლე, პროფესიონალური. დაიწყე პირდაპირ 'ვენიუს სახელი:'-ით."
                )
            else:
                prompt = (
                    f"User context: {context}. Mission: {mission}. "
                    "Provide an elite Social Blueprint for Tbilisi. "
                    "Structure: 1. Venue Name, 2. Exact Spot, 3. Persona Identification, "
                    "4. Professional Icebreaker, 5. Strategic Action Plan, 6. Logic of Probability. "
                    "Tone: Professional, tactical. Start with 'Venue Name:'."
                )
            
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "system", "content": "You are a senior social strategist. Respond strictly in the language used by the user."},
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
                st.error("Connection Interrupted.")
    else:
        st.warning("MISSION INPUT REQUIRED.")

# --- FOOTER ---
st.write("---")
f1, f2 = st.columns([2, 1])
with f1:
    st.markdown(f"<div class='footer-text'><b>Architect:</b> Ilia Mgeladze<br><b>Inquiries:</b> <a href='mailto:mgeladzeilia39@gmail.com'>mgeladzeilia39@gmail.com</a></div>", unsafe_allow_html=True)
with f2:
    st.markdown("<div style='text-align: right; color: #555;'>V2.7 | SYSTEM OPERATIONAL</div>", unsafe_allow_html=True)
