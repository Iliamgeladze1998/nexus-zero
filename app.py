import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI UPGRADE: High Contrast & Pure Readability
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'JetBrains Mono', monospace;
        background-color: #000000;
        color: #ffffff;
    }

    /* Sidebar - მკაფიო გამყოფი ხაზით */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a !important;
        border-right: 2px solid #333;
    }

    /* ტექსტის შეყვანის ველი - თეთრი ტექსტით */
    .stTextInput>div>div>input {
        background-color: #111 !important;
        color: #ffffff !important;
        border: 2px solid #00ffcc !important;
        border-radius: 5px;
        font-size: 1.1em;
    }

    /* ღილაკი - მკვეთრი ნეონი */
    .stButton>button {
        border: 2px solid #ff00ff !important;
        background-color: transparent !important;
        color: #ff00ff !important;
        font-weight: bold;
        height: 3.5em;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        background-color: #ff00ff !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #ff00ff;
    }

    /* პასუხის ბლოკი - მაქსიმალური კითხვადობა */
    .stInfo {
        border: 2px solid #00ffcc !important;
        background-color: #050505 !important;
        color: #ffffff !important;
        font-size: 1.15em;
        padding: 20px !important;
        border-radius: 10px;
    }

    /* ფუტერი - ნაცრისფერი ტექსტი */
    .footer-container {
        margin-top: 50px;
        border-top: 1px solid #333;
        padding-top: 20px;
        color: #aaaaaa;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ⚙️ PARAMETERS")
    social_type = st.select_slider("Energy Profile:", options=["Introvert", "Balanced", "Extrovert"])
    asset_list = ["Tech/Dev", "Crypto/Web3", "Business/Sales", "Finance/Investment", "Creative/Design", "Art/Culture", "Real Estate", "Marketing/PR", "Capital", "Charisma"]
    skills = st.multiselect("Available Assets:", asset_list)
    st.write("---")
    with st.expander("⚖️ LEGAL & PRIVACY"):
        st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")
    if st.button("RESET"):
        st.rerun()

# --- MAIN INTERFACE ---
st.title("⚡ NEXUS ZERO: TBILISI GRID")
st.write(f"STATUS: ONLINE | {datetime.now().strftime('%Y-%m-%d %H:%M')}")

mission = st.text_input("DEFINE MISSION:", placeholder="მაგ: მინდა ვიპოვო პარტნიორი სტარტაპისთვის...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("PROCESSING..."):
            context = f"User: {social_type}, Skills: {skills}."
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            
            if is_georgian:
                prompt = (
                    f"კონტექსტი: {context}. მისია: {mission}. "
                    "მოამზადე მკაცრი სოციალური ბლუპრინტი თბილისისთვის. "
                    "სტრუქტურა დაიცავი: 1. ვენიუს სახელი, 2. ზუსტი წერტილი, 3. სამიზნე პერსონა, "
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
                    {"role": "system", "content": "You are a senior social strategist. Be specific, provide actionable intelligence for Tbilisi."},
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
                
                st.markdown("### 🎯 STRATEGIC INTEL")
                st.info(result)
                
                m1, m2 = st.columns(2)
                with m1:
                    st.link_button("📍 GOOGLE MAPS", f"https://www.google.com/maps/search/{urllib.parse.quote(venue_name + ' Tbilisi')}")
                with m2:
                    st.download_button("💾 DOWNLOAD", result, file_name="nexus_mission.txt")
                    
            except Exception:
                st.error("Connection Interrupted.")
    else:
        st.warning("MISSION INPUT REQUIRED.")

# --- FOOTER ---
st.markdown("<div class='footer-container'></div>", unsafe_allow_html=True)
f1, f2 = st.columns([2, 1])
with f1:
    st.markdown("**Architect:** Ilia Mgeladze")
    st.markdown("**Inquiries:** [Mgeladzeilia39@gmail.com](mailto:Mgeladzeilia39@gmail.com)")
with f2:
    st.markdown(f"<div style='text-align: right;'>V2.8 | SYSTEM OPERATIONAL</div>", unsafe_allow_html=True)
