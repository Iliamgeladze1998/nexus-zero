import streamlit as st
import requests
from datetime import datetime
import urllib.parse
import pytz
from fpdf import FPDF

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI: სუფთა დიზაინი + ტექსტის გარანტირებული ხილვადობა
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        background-image: 
            linear-gradient(rgba(37, 99, 235, 0.08) 1px, transparent 1px),
            linear-gradient(90deg, rgba(37, 99, 235, 0.08) 1px, transparent 1px) !important;
        background-size: 30px 30px !important;
    }
    
    /* გარანტირებული შავი ტექსტი Expander-ში (რომ მობილურზე არ გაქრეს) */
    [data-testid="stExpander"] div[role="button"] p, 
    [data-testid="stExpander"] .stMarkdown p {
        color: #000000 !important;
        font-weight: 700 !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    /* Press Enter Fix */
    div[data-testid="stTextInput"] div[data-testid="stMarkdownContainer"] p,
    .st-emotion-cache-1pxm8yv, .st-emotion-cache-1p78y8e, .st-emotion-cache-6q9sum,
    section[data-testid="stTextInput"] small {
        display: none !important;
    }

    h1 { color: #1E3A8A !important; font-weight: 800 !important; }
    p, label { color: #000000 !important; font-weight: 700 !important; }

    .stButton>button {
        width: 100% !important;
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
        height: 3.5em;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER & GUIDE ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")

# ჩამოსაშლელი ინსტრუქცია - ახლა უკვე გარანტირებულად გამოჩნდება
with st.expander("📖 HOW IT WORKS / ინსტრუქცია"):
    st.markdown("""
    1. **Profile:** მიუთითე შენი სოციალური ენერგიის დონე.
    2. **Assets:** მონიშნე შენი ძლიერი მხარეები და უნარები.
    3. **Mission:** ჩაწერე კონკრეტული მიზანი (მაგ: პარტნიორის პოვნა).
    4. **Execute:** მიიღე სტრატეგიული გეგმა, ლოკაცია და დრო.
    """)

tbilisi_tz = pytz.timezone('Asia/Tbilisi')
timestamp = datetime.now(tbilisi_tz).strftime('%H:%M')
st.caption(f"STATUS: ONLINE | TIME: {timestamp}")
st.write("---")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    social_type = st.select_slider("Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    asset_options = ["Tech/AI", "Crypto/Web3", "Business/Sales", "Finance", "Marketing", "Real Estate", "Creative/Art", "Charisma", "Psychology"]
    skills = st.multiselect("Assets:", asset_options)

mission = st.text_input("MISSION:", placeholder="e.g. I want to find a business partner...")

if st.button("EXECUTE ALIGNMENT"):
    if mission:
        with st.spinner("SCANNING GRID..."):
            prompt = f"Mission: {mission}. Profile: {social_type}. Assets: {skills}. Tactical Tbilisi strategy. End with 'FINAL_DESTINATION: Venue Name'."
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "system", "content": "You are a tactical advisor. Be precise."}, {"role": "user", "content": prompt}], "temperature": 0.4}
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                st.info(result)
                
                if "FINAL_DESTINATION:" in result:
                    loc_name = result.split("FINAL_DESTINATION:")[1].strip()
                    maps_url = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(loc_name + ' Tbilisi')}"
                    st.link_button(f"📍 NAVIGATE TO {loc_name.upper()}", maps_url)

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, txt=result.encode('latin-1', 'replace').decode('latin-1'))
                st.download_button("📥 DOWNLOAD PDF DOSSIER", data=bytes(pdf.output(dest='S')), file_name="nexus_strategy.pdf")
            except Exception as e:
                st.error(f"Grid Error: {e}")

# --- FOOTER ---
st.write("---")
# ქვედა ჩამოსაშლელი (Legal)
with st.expander("⚖️ LEGAL & PRIVACY"):
    st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")

st.markdown(f"**Architect:** Ilia Mgeladze")
st.markdown(f"**Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
