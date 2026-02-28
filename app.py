import streamlit as st
import requests
from datetime import datetime
import urllib.parse

# --- CONFIGURATION ---
# იყენებს Streamlit-ის Secrets-ს უსაფრთხოებისთვის
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
    
    # აქტივების სია
    asset_list = [
        "Tech/Dev", "Crypto/Web3", "Business/Sales", "Finance/Investment",
        "Creative/Design", "Art/Culture", "Real Estate", "Marketing/PR",
        "Capital", "Charisma", "Education/Academic"
    ]
    skills = st.multiselect("Available Assets:", asset_list)
    
    st.write("---")
    # დააბრუნა Privacy და Legal სექცია
    with st.expander("⚖️ LEGAL & PRIVACY"):
        st.caption("Nexus Zero Protocol. Encrypted session. Developed by Ilia Mgeladze.")
    
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
            
            # ენის ჭკვიანი დეტექტორი
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
                    {"role": "system", "content": "You are a senior social strategist. Respond strictly in the language used by the user. Be tactical and specific."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3 # სიზუსტისთვის
            }
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                
                try:
                    # ლოკაციის ამოღება რუკისთვის
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

# --- FOOTER (შენი სახელით და მეილით) ---
st.write("---")
f1, f2 = st.columns([2, 1])
with f1:
    st.markdown("**Architect:** Ilia Mgeladze")
    st.markdown(f"**Inquiries:** [Mgeladzeilia39@gmail.com](mailto:Mgeladzeilia39@gmail.com)")
with f2:
    st.markdown("<div style='text-align: right; color: #555;'>V2.6 | SYSTEM OPERATIONAL</div>", unsafe_allow_html=True)
