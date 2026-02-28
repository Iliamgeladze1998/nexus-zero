import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI UPGRADE: Soft Dark & High Contrast
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    /* ფონი - აღარ არის "კუპრივით" შავი */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'JetBrains Mono', monospace;
        background-color: #0A0A0B; 
        color: #E0E0E0;
    }

    /* Sidebar - ოდნავ უფრო ღია ნაცრისფერი */
    [data-testid="stSidebar"] {
        background-color: #111112 !important;
        border-right: 1px solid #2D2D2E;
    }

    /* Input ველები - მკაფიო კონტურებით */
    .stTextInput>div>div>input {
        background-color: #1A1A1B !important;
        color: #00FFCC !important;
        border: 1px solid #3D3D3E !important;
        border-radius: 8px;
        font-size: 1.05em;
    }
    
    /* ტექსტის ფერი Sidebar-ში */
    [data-testid="stWidgetLabel"] {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }

    /* ღილაკი - მკვეთრი და ეფექტური */
    .stButton>button {
        border: 1px solid #FF00FF !important;
        background-color: rgba(255, 0, 255, 0.05) !important;
        color: #FF00FF !important;
        font-weight: bold;
        border-radius: 8px;
        height: 3.5em;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF00FF !important;
        color: #000000 !important;
        box-shadow: 0 0 20px rgba(255, 0, 255, 0.4);
    }

    /* Intel Box - მაქსიმალური კითხვადობა თეთრი ტექსტით */
    .stInfo {
        border: 1px solid #00FFCC !important;
        background-color: #121517 !important;
        color: #FFFFFF !important;
        font-size: 1.1em;
        line-height: 1.6;
        border-radius: 12px;
        padding: 25px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    }

    /* Footer-ის სტილი */
    .footer-section {
        color: #888888;
        font-size: 0.9em;
        margin-top: 50px;
    }
    a { color: #00FFCC !important; text-decoration: none; }
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
st.markdown(f"<p style='color:#888;'>STATUS: <span style='color:#00FFCC;'>ONLINE</span> | {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>", unsafe_allow_html=True)

mission = st.text_input("DEFINE MISSION:", placeholder="Enter objective (e.g. Find startup partners)...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("PROCESSING VECTORS..."):
            context = f"User: {social_type}, Skills: {skills}."
            is_georgian = any(char in mission for char in "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
            
            if is_georgian:
                prompt = (
                    f"კონტექსტი: {context}. მისია: {mission}. "
                    "მოამზადე მკაცრი სოციალური ბლუპრინტი თბილისისთვის. "
                    "სტრუქტურა: 1. ვენიუს სახელი, 2. ზუსტი წერტილი, 3. სამიზნე პერსონა, "
                    "4. Icebreaker, 5. სტრატეგიული გეგმა, 6. ალბათობის ლოგიკა. "
                    "ტონი: ტაქტიკური. დაიწყე პირდაპირ 'ვენიუს სახელი:'-ით."
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
                    {"role": "system", "content": "You are a senior social strategist. Provide specific, actionable advice. Match the user's language."},
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
                st.error("Connection Failed.")
    else:
        st.warning("MISSION INPUT REQUIRED.")

# --- FOOTER ---
st.write("---")
f1, f2 = st.columns([2, 1])
with f1:
    st.markdown(f"<div class='footer-section'><b>Architect:</b> Ilia Mgeladze<br><b>Inquiries:</b> <a href='mailto:mgeladzeilia39@gmail.com'>mgeladzeilia39@gmail.com</a></div>", unsafe_allow_html=True)
with f2:
    st.markdown("<div style='text-align: right; color: #555; margin-top: 10px;'>V2.9 | SYSTEM OPERATIONAL</div>", unsafe_allow_html=True)
