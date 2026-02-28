import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# Custom CSS for Professional Minimalist Neon UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'JetBrains Mono', monospace;
        background-color: #050505;
    }
    .stButton>button {
        border: 1px solid #ff00ff !important;
        background-color: transparent !important;
        color: #ff00ff !important;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
        height: 3.5em;
    }
    .stButton>button:hover {
        background-color: #ff00ff !important;
        color: white !important;
        box-shadow: 0 0 20px #ff00ff;
    }
    .stInfo {
        border: 1px solid #00ffcc !important;
        background-color: #0a0a0a !important;
        color: #e0e0e0 !important;
        font-size: 1.05em;
    }
    .stTextInput>div>div>input {
        background-color: #111 !important;
        color: #00ffcc !important;
        border: 1px solid #333 !important;
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
    if st.button("RESET SESSION"):
        st.rerun()

# --- MAIN INTERFACE ---
st.title("⚡ NEXUS ZERO: TBILISI GRID")
st.write(f"STATUS: ONLINE | {datetime.now().strftime('%Y-%m-%d %H:%M')}")

mission = st.text_input("DEFINE MISSION:", placeholder="მაგ: მინდა ვიპოვო პარტნიორი სტარტაპისთვის...")

if st.button("EXECUTE STRATEGIC ALIGNMENT"):
    if mission:
        with st.spinner("ANALYZING SOCIAL VECTORS..."):
            context = f"User: {social_type}, Skills: {skills}."
            
            # ენის დეტექტორი
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
                    {"role": "system", "content": "You are a senior social strategist. You provide high-level, tactical advice for Tbilisi. Be specific, never generic."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                
                try:
                    # ლოკაციის ამოღება Google Maps-ისთვის
                    venue_name = result.split('\n')[0].split(':')[1].strip()
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
                st.error("System Override Failed. Check connection.")
    else:
        st.warning("MISSION INPUT REQUIRED.")

st.write("---")
st.markdown("<div style='text-align: right; color: #555;'>V2.5 | SYSTEM OPERATIONAL</div>", unsafe_allow_html=True)
