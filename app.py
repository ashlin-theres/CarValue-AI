import streamlit as st
from pathlib import Path
import base64

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="CarValue AI | Luxury Edition",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"  # Start with sidebar hidden
)

# ==========================================================
# PATHS
# ==========================================================
BASE_DIR = Path(__file__).parent

# ==========================================================
# IMAGE FUNCTION
# ==========================================================
def get_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

# ==========================================================
# LOAD IMAGES (Safely handled if assets exist)
# ==========================================================
try:
    logo = get_base64(BASE_DIR / "images" / "logo.png")
    predict = get_base64(BASE_DIR / "images" / "predict.png")
    insights = get_base64(BASE_DIR / "images" / "insights.png")
    about = get_base64(BASE_DIR / "images" / "about.png")
except FileNotFoundError:
    # Fallbacks so code doesn't crash if an asset is temporarily missing
    logo = predict = insights = about = ""

# ==========================================================
# PREMIUM BROWN & GOLD LUXURY GLOBAL CSS
# ==========================================================
st.markdown(f"""
<style>
    /* Completely Hide Streamlit Sidebar & Sidebar Toggle Buttons */
    [data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"] {{
        display: none !important;
        width: 0px !important;
    }}
    .stMainBlockContainer {{
        padding-top: 1rem !important;
        max-width: 1200px;
        margin: 0 auto;
    }}

    /* Top Navigation Styling */
    .top-navbar {{
        display: flex;
        justify-content: center;
        gap: 40px;
        padding: 15px 0;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
        margin-bottom: 40px;
    }}
    .nav-item {{
        font-family: 'Georgia', serif;
        font-size: 18px;
        color: #3E2723 !important;
        text-decoration: none !important;
        font-weight: 600;
        letter-spacing: 1px;
        transition: color 0.3s ease;
    }}
    .nav-item:hover {{
        color: #D4AF37 !important;
    }}

    /* Hero Section Luxury Styling */
    .brand-container {{
        text-align: center;
        padding: 20px 0;
    }}
    .luxury-logo {{
        width: 130px;
        height: auto;
        border-radius: 50%;
        border: 3px solid #D4AF37;
        padding: 5px;
        background-color: #FFF;
        box-shadow: 0px 10px 25px rgba(62, 39, 35, 0.15);
    }}
    .app-title {{
        font-family: 'Georgia', serif;
        font-size: 65px;
        font-weight: bold;
        color: #3E2723;
        letter-spacing: 2px;
        margin-top: 15px;
    }}
    .subtitle {{
        font-family: 'Georgia', serif;
        font-style: italic;
        font-size: 24px;
        color: #D4AF37;
        margin-bottom: 25px;
    }}
    .description {{
        font-size: 18px;
        color: #5D4037;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.8;
    }}

    /* Section Headers */
    .section-title {{
        font-family: 'Georgia', serif;
        font-size: 32px;
        color: #3E2723;
        text-align: center;
        letter-spacing: 1px;
        margin: 50px 0 30px 0;
        position: relative;
    }}
    .section-title::after {{
        content: '';
        display: block;
        width: 60px;
        height: 2px;
        background: #D4AF37;
        margin: 10px auto 0 auto;
    }}

    /* Bigger Premium Circle Feature Cards */
    .premium-circle-card {{
        background: radial-gradient(circle, #FFFFFF 60%, #FDFBF7 100%);
        border: 2px solid rgba(212, 175, 55, 0.2);
        border-radius: 50%;
        width: 320px;
        height: 320px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 30px;
        box-shadow: 0px 15px 35px rgba(62, 39, 35, 0.06);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }}
    .premium-circle-card:hover {{
        transform: translateY(-10px);
        border-color: #D4AF37;
        box-shadow: 0px 20px 45px rgba(212, 175, 55, 0.25);
    }}
    .premium-circle-card img {{
        width: 75px;
        height: 75px;
        margin-bottom: 15px;
    }}
    .premium-circle-card h3 {{
        font-family: 'Georgia', serif;
        color: #3E2723;
        font-size: 24px;
        margin: 5px 0;
    }}
    .premium-circle-card p {{
        font-size: 14px;
        color: #745146;
        line-height: 1.5;
    }}

    /* Metric Luxury Grid Cards */
    .luxury-metric-card {{
        background-color: #3E2723;
        border-top: 4px solid #D4AF37;
        padding: 35px 25px;
        border-radius: 4px;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }}
    .luxury-metric-card:hover {{
        transform: translateY(-5px);
    }}
    .luxury-metric-card h2 {{
        font-size: 35px;
        margin-bottom: 10px;
    }}
    .luxury-metric-card h3 {{
        font-family: 'Georgia', serif;
        color: #D4AF37;
        font-size: 22px;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }}
    .luxury-metric-card p {{
        color: #FDFBF7;
        font-size: 15px;
        opacity: 0.85;
        margin: 0;
    }}

    /* Luxury Footer */
    .footer {{
        text-align: center;
        color: #745146;
        font-size: 15px;
        letter-spacing: 1px;
        margin-top: 80px;
        padding: 30px 0;
        border-top: 1px solid rgba(212, 175, 55, 0.15);
    }}
</style>
""", unsafe_allow_html=True)

# Try reading local styles.css if you have secondary rules there
if (BASE_DIR / "styles.css").exists():
    with open(BASE_DIR / "styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ==========================================================
# 📱 TOP NAVIGATION BAR
# ==========================================================
# We construct elegant fallback links. (Note: Streamlit natively requires page links to execute scripts. 
# For true top-nav clicks, we'll place structural page_links side-by-side cleanly inside columns)
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns([3, 1, 1, 1, 3])

with nav_col2:
    st.page_link("pages/Prediction.py", label="PREDICT", icon="🏎️")
with nav_col3:
    st.page_link("pages/Insights.py", label="INSIGHTS", icon="📊")
with nav_col4:
    st.page_link("pages/About.py", label="ABOUT", icon="👤")

st.markdown('<div class="top-navbar"></div>', unsafe_allow_html=True)


# ==========================================================
# 👑 HERO SECTION
# ==========================================================
st.markdown(f"""
<div class="brand-container">
    <img src="data:image/png;base64,{logo}" class="luxury-logo">
    <div class="app-title">CarValue AI</div>
    <div class="subtitle">Discover Your Car's Worth with Distinction</div>
    <div class="description">
        Experience an elite machine learning environment crafted to evaluate your motorcar's accurate valuation instantly. Whether buying, liquidating, or assessing a classic collector asset, calculate your edge effortlessly.
    </div>
</div>

<div class="section-title">Explore Premium Suite Features</div>
""", unsafe_allow_html=True)


# ==========================================================
# ✨ BIGGER PREMIUM FEATURE CIRCLES (3 Columns)
# ==========================================================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="premium-circle-card">
        <img src="data:image/png;base64,{predict}">
        <h3>Valuation</h3>
        <p>Procure real-time algorithmic estimates of your vehicle's marketplace positioning with streamlined accuracy inputs.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="premium-circle-card">
        <img src="data:image/png;base64,{insights}">
        <h3>Intelligence</h3>
        <p>Review systemic microtrends, luxury brand value retention charts, and contextualized market distributions.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="premium-circle-card">
        <img src="data:image/png;base64,{about}">
        <h3>The Engine</h3>
        <p>Uncover the architectural machine learning pipelines and engineering philosophy backing CarValue AI.</p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# 📈 WHY CHOOSE US - LUXURY METRICS SECTION
# ==========================================================
st.markdown('<div class="section-title">The Standard of Excellence</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown("""
    <div class="luxury-metric-card">
        <h2>⏱️</h2>
        <h3>Prestige Speed</h3>
        <p>Bypass heavy computations. Realize absolute data valuations processed globally within milliseconds.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="luxury-metric-card">
        <h2>💎</h2>
        <h3>Proven Integrity</h3>
        <p>Trained over rigorous historical premium datasets ensuring real-world transactional accuracy profiles.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="luxury-metric-card">
        <h2>👑</h2>
        <h3>Elite Utility</h3>
        <p>Curated purposely for strategic market negotiation, asset liquidation choices, and purchasing confidence.</p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# 🎨 FOOTER
# ==========================================================
st.markdown("""
<div class="footer">
    Made with haute couture standards & ❤️ by <b>Ashlin Theres James</b>
</div>
""", unsafe_allow_html=True)