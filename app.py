import streamlit as st
import requests
from datetime import datetime
import pytz
from fpdf import FPDF

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="NEXUS ZERO PRO", page_icon="🎯", layout="wide")

# UI (დიზაინი უცვლელია, როგორც გინდოდა)
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
    h1 { color: #1E3A8A !important; font-weight: 800 !important; }
    .stButton>button { width: 100% !important; background-color: #2563EB !important; color: white !important; border-radius: 12px; font-weight: bold; height: 3.5em; border: none !important; }
</style>
""", unsafe_allow_html=True)

# --- PDF GENERATOR FUNCTION ---
def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=text.encode('latin-1', 'replace').decode('latin-1'))
    return pdf.output(dest='S')

# --- HEADER ---
tbilisi_tz = pytz.timezone('Asia/Tbilisi')
timestamp = datetime.now(tbilisi_tz).strftime('%H:%M')
st.title("🎯 NEXUS ZERO: TBILISI GRID")
st.caption(f"STATUS: ONLINE | TIME: {timestamp}")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    social_type = st.select_slider("Profile:", options=["Introvert", "Balanced", "Extrovert"])
with col2:
    asset_options = ["Tech/AI", "Crypto/Web3", "Business", "Finance", "Marketing", "Real Estate", "Creative/Art", "Charisma", "Capital"]
    skills = st.multiselect("Assets:", asset_options)

mission = st.text_input("MISSION:", placeholder="e.g. I want to find a business partner...")

if st.button("EXECUTE ALIGNMENT"):
    if mission:
        with st.spinner("SCANNING GRID..."):
            # ვავალებთ AI-ს კონკრეტულ ლოკაციებს და რუკას
            prompt = f"""
            Mission: {mission}. Profile: {social_type}. Assets: {skills}. 
            Provide a tactical strategy for Tbilisi. 
            MUST INCLUDE: At least 2 specific physical locations in Tbilisi with Google Maps search links.
            """
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
            data = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "system", "content": "You are a Tbilisi-based strategic advisor. Be specific about locations."}, {"role": "user", "content": prompt}], "temperature": 0.3}
            
            try:
                response = requests.post(GROQ_URL, headers=headers, json=data)
                result = response.json()["choices"][0]["message"]["content"]
                st.session_state['result'] = result
                st.info(result)
            except:
                st.error("Grid Error.")

# --- PDF DOWNLOAD SECTION ---
if 'result' in st.session_state:
    pdf_data = create_pdf(st.session_state['result'])
    st.download_button(
        label="📥 Download Strategy as PDF",
        data=pdf_data,
        file_name=f"Nexus_Strategy_{timestamp}.pdf",
        mime="application/pdf"
    )

st.write("---")
st.markdown(f"**Architect:** Ilia Mgeladze | **Inquiries:** mgeladzeilia39@gmail.com")
