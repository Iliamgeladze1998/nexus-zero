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

# UI: V4.2-ის იდენტური დიზაინი (არაფერი შეცვლილა)
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        background-image: 
            linear-gradient(rgba(37, 99, 235, 0.08) 1px, transparent 1px),
            linear-gradient(90deg, rgba(37, 99, 235, 0.08) 1px, transparent 1px) !important;
        background-size: 30px 30px !important;
    }
    div[data-testid="stTextInput"] div[data-testid="stMarkdownContainer"] p { display: none !important; }
    .st-emotion-cache-1pxm8yv { display: none !important; }
    h1 { color: #1E3A8A !important; font-weight: 800 !important; }
    p, label { color: #000000 !important; font-weight: 700 !important; }
    @media (max-width: 768px) {
        .main .block-container { padding: 1rem !important; }
        h1 { font-size: 1.6rem !important; }
    }
    .stButton>button {
        width: 100% !important;
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
        height: 3.5em;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# --- TIME ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
timestamp = datetime.now(tbilisi_tz).strftime('%H:%M')

# --- HEADER ---
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.caption(f"STATUS: ONLINE | TIME: {timestamp}")
st.write("---")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    social_type = st.select_slider("Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    asset_options = [
        "Tech/AI", "Crypto/Web3", "Business/Sales", "Finance/Trading", 
        "Marketing/PR", "Real Estate", "Creative/Art", "Education", 
        "Legal/Gov", "Health/Sport", "E-commerce", "Charisma", "Capital",
        "Event Planning", "Psychology", "Design/UI-UX"
    ]
    skills = st.multiselect("Assets:", asset_options)

mission = st.text_input("MISSION:", placeholder="e.g. I want to find a business partner...")

if st.button("EXECUTE ALIGNMENT"):
    if mission:
        with st.spinner("SCANNING GRID..."):
            prompt = f"""
            Mission: {mission}. Profile: {social_type}. Assets: {skills}.
            Create a tactical plan for Tbilisi. 
            STRICT RULES:
            1. Tell the user EXACTLY where to go, WHEN (best time), and WHAT to do there.
            2. At the end, write exactly 'LOCATION: [Place Name]'.
            """
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "system", "content": "You are a direct, tactical social engineer in Tbilisi. No fluff. Just actions and locations."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.4
            }
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                st.session_state['result'] = result
                
                st.info(result)
                
                # Maps Logic
                if "LOCATION:" in result:
                    loc_name = result.split("LOCATION:")[1].split("\n")[0].strip()
                    maps_url = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(loc_name + ' Tbilisi')}"
                    st.link_button(f"📍 OPEN {loc_name.upper()} ON MAPS", maps_url)

                # PDF Button
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, txt=result.encode('latin-1', 'replace').decode('latin-1'))
                st.download_button("📥 DOWNLOAD PDF DOSSIER", data=pdf.output(dest='S'), file_name="nexus_strategy.pdf")

            except Exception as e:
                st.error(f"Grid Error: {e}")

# --- FOOTER ---
st.write("---")
with st.expander("⚖️ LEGAL & PRIVACY"):
    st.caption("Nexus Zero Protocol. Developed by Ilia Mgeladze.")

st.markdown(f"**Architect:** Ilia Mgeladze")
st.markdown(f"**Inquiries:** [mgeladzeilia39@gmail.com](mailto:mgeladzeilia39@gmail.com)")
