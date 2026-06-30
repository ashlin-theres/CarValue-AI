import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import base64
import time

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="CarValue AI | Prediction",
    page_icon="🚗",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# LOAD CSS & GLOBAL FONT OVERRIDES
# ==========================================================

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Comprehensive global CSS override to catch every single input field label
st.markdown(
    """
    <style>
    /* Force every single input label, text question, and widget title to white */
    label,
    .stWidgetLabel,
    div[data-testid="stWidgetLabel"] p,
    .stSlider p,
    .stNumberInput label,
    .stSelectbox label,
    div[data-testid="stSliderText"] p,
    div[class*="stSelectbox"] label p,
    div[class*="stNumberInput"] label p,
    div[class*="stSlider"] label p {
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# LOAD MODEL
# ==========================================================

import requests
import joblib

MODEL_URL = "https://huggingface.co/ashlintheres4/carvalue-ai-model/resolve/main/carvalue_pipeline.pkl"
MODEL_PATH = "carvalue_pipeline.pkl"

def load_model():
    response = requests.get(MODEL_URL)
    with open(MODEL_PATH, "wb") as f:
        f.write(response.content)

    return joblib.load(MODEL_PATH)

model = load_model()

# ==========================================================
# LOAD DATA
# ==========================================================

df = pd.read_csv(
    BASE_DIR / "data" / "Used_Car_Price_Prediction.csv"
)

# ==========================================================
# IMAGE FUNCTION
# ==========================================================

def image64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

car = image64(BASE_DIR / "images" / "car.png")

# ==========================================================
# NAVIGATION
# ==========================================================

nav1, nav2, nav3, nav4, nav5 = st.columns([2,1,1,1,2])

with nav1:
    st.page_link("app.py", label="HOME", icon="🏠")

with nav2:
    st.page_link("pages/Prediction.py", label="PREDICT", icon="🚗")

with nav3:
    st.page_link("pages/Insights.py", label="INSIGHTS", icon="📊")

with nav4:
    st.page_link("pages/About.py", label="ABOUT", icon="👤")

st.markdown(
    '<div class="top-navbar"></div>',
    unsafe_allow_html=True
)

# ==========================================================
# HERO
# ==========================================================

st.markdown("""
<div class="section-title" style="color:#FFD700; text-align:center; font-family:Cinzel; font-size:40px; font-weight:bold;">
Predict Your Car Value
</div>
<div class="description" style="color:#FFFFFF; text-align:center; font-size:18px; margin-top:10px;">
Discover the estimated market value of your vehicle using its specifications and current market trends.
</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# FORM CONTAINER
# ==========================================================

st.markdown("""
<div style="
background:rgba(255,255,255,.05);
border:1px solid rgba(212,175,55,.35);
border-radius:25px;
padding:35px;
margin-top:10px;
box-shadow:0 12px 30px rgba(0,0,0,.30);
">
<h2 style="
text-align:center;
color:#FFD700;
font-family:Cinzel;
margin-bottom:25px;
">
Vehicle Information
</h2>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# INPUTS
# ==========================================================

left, right = st.columns(2)

with left:
    make = st.selectbox(
        "Manufacturer",
        sorted(df["make"].dropna().astype(str).unique())
    )

    filtered_models = df[df["make"] == make]["model"].dropna().astype(str).unique()
    model_name = st.selectbox(
        "Model",
        sorted(filtered_models)
    )

    yr_mfr = st.slider(
        "Manufacturing Year",
        2000,
        2025,
        2020
    )

    kms_run = st.number_input(
        "Kilometers Driven",
        0,
        500000,
        30000,
        step=1000
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        sorted(df["fuel_type"].dropna().astype(str).unique())
    )

    transmission = st.selectbox(
        "Transmission",
        sorted(df["transmission"].dropna().astype(str).unique())
    )

with right:
    city = st.selectbox(
        "City",
        sorted(df["city"].dropna().astype(str).unique())
    )

    body_type = st.selectbox(
        "Body Type",
        sorted(df["body_type"].dropna().astype(str).unique())
    )

    total_owners = st.selectbox(
        "Number of Owners",
        sorted(df["total_owners"].dropna().astype(str).unique())
    )

    assured_buy = st.selectbox(
        "Assured Buy",
        sorted(df["assured_buy"].dropna().astype(str).unique())
    )

    warranty_avail = st.selectbox(
        "Warranty Available",
        sorted(df["warranty_avail"].dropna().astype(str).unique())
    )

    fitness_certificate = st.selectbox(
        "Fitness Certificate",
        sorted(df["fitness_certificate"].dropna().astype(str).unique())
    )

    car_rating = st.selectbox(
        "Vehicle Rating",
        sorted(df["car_rating"].dropna().astype(str).unique())
    )

st.write("")
st.write("")

predict = st.button(
    "Predict Car Value",
    use_container_width=True
)

# ==========================================================
# PREDICTION & OUTPUTS
# ==========================================================

if predict:

    # ------------------------------------------------------
    # PREMIUM CAR ANIMATION
    # ------------------------------------------------------
    st.markdown(
        f"""
        <style>
        .road{{
            width:100%;
            height:170px;
            overflow:hidden;
            position:relative;
            margin-top:25px;
            margin-bottom:25px;
            border-bottom:4px dashed rgba(255,215,0,.35);
        }}
        .moving-car{{
            position:absolute;
            width:230px;
            top:20px;
            animation:drive 3.2s linear forwards;
        }}
        @keyframes drive{{
            from{{left:-250px;}}
            to{{left:110%;}}
        }}
        .loading-title{{
            text-align:center;
            color:#FFD700;
            font-size:30px;
            font-family:Cinzel;
            margin-bottom:20px;
        }}
        </style>
        <div class="loading-title">
        Analysing Your Vehicle...
        </div>
        <div class="road">
        <img src="data:image/png;base64,{car}" class="moving-car">
        </div>
        """,
        unsafe_allow_html=True
    )

    progress = st.progress(0)

    for i in range(101):
        time.sleep(0.02)
        progress.progress(i)

    # ------------------------------------------------------
    # MODEL INFERENCE
    # ------------------------------------------------------
    sample = pd.DataFrame({
        "yr_mfr":[yr_mfr],
        "fuel_type":[fuel_type],
        "kms_run":[kms_run],
        "city":[city],
        "body_type":[body_type],
        "transmission":[transmission],
        "assured_buy":[assured_buy],
        "make":[make],
        "model":[model_name],
        "total_owners":[total_owners],
        "car_rating":[car_rating],
        "fitness_certificate":[fitness_certificate],
        "warranty_avail":[warranty_avail]
    })

    raw_prediction = model.predict(sample)[0]
    prediction = float(raw_prediction)

    progress.empty()

    # ------------------------------------------------------
    # RESULT CARD
    # ------------------------------------------------------
    st.markdown(
        f"""
        <div style="
        background:linear-gradient(135deg,#D4AF37,#F7E29B);
        border-radius:25px;
        padding:40px;
        text-align:center;
        color:#2C1810;
        box-shadow:0 15px 35px rgba(0,0,0,.35);
        margin-top:20px;
        ">
        <h1 style="margin-bottom:10px; color:#2C1810; font-weight:bold;">
        Estimated Market Value
        </h1>
        <h1 style="font-size:60px; color:#2C1810; font-weight:bold;">
        ₹ {prediction:,.0f}
        </h1>
        <p style="font-size:20px; color:#2C1810;">
        Based on the specifications you provided.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    # ==========================================================
    # VEHICLE SUMMARY
    # ==========================================================
    st.markdown("""
    <div class="section-title" style="color:#FFD700; font-size:28px; font-family:Cinzel; margin-bottom:15px; font-weight:bold;">
    Vehicle Summary
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="metric-card" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,215,0,0.2); padding:20px; border-radius:15px; margin-bottom:15px;">
            <h3 style="color:#B0B0B0; font-size:14px; margin:0; text-transform:uppercase; letter-spacing:1px;">Manufacturer</h3>
            <h2 style="color:#FFFFFF; font-size:24px; margin:5px 0 0 0; font-weight:600;">{str(make).title()}</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,215,0,0.2); padding:20px; border-radius:15px; margin-bottom:15px;">
            <h3 style="color:#B0B0B0; font-size:14px; margin:0; text-transform:uppercase; letter-spacing:1px;">Model</h3>
            <h2 style="color:#FFFFFF; font-size:24px; margin:5px 0 0 0; font-weight:600;">{str(model_name).title()}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,215,0,0.2); padding:20px; border-radius:15px; margin-bottom:15px;">
            <h3 style="color:#B0B0B0; font-size:14px; margin:0; text-transform:uppercase; letter-spacing:1px;">Manufacturing Year</h3>
            <h2 style="color:#FFFFFF; font-size:24px; margin:5px 0 0 0; font-weight:600;">{yr_mfr}</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,215,0,0.2); padding:20px; border-radius:15px; margin-bottom:15px;">
            <h3 style="color:#B0B0B0; font-size:14px; margin:0; text-transform:uppercase; letter-spacing:1px;">Kilometers Driven</h3>
            <h2 style="color:#FFFFFF; font-size:24px; margin:5px 0 0 0; font-weight:600;">{kms_run:,}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,215,0,0.2); padding:20px; border-radius:15px; margin-bottom:15px;">
            <h3 style="color:#B0B0B0; font-size:14px; margin:0; text-transform:uppercase; letter-spacing:1px;">Fuel Type</h3>
            <h2 style="color:#FFFFFF; font-size:24px; margin:5px 0 0 0; font-weight:600;">{str(fuel_type).title()}</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,215,0,0.2); padding:20px; border-radius:15px; margin-bottom:15px;">
            <h3 style="color:#B0B0B0; font-size:14px; margin:0; text-transform:uppercase; letter-spacing:1px;">Transmission</h3>
            <h2 style="color:#FFFFFF; font-size:24px; margin:5px 0 0 0; font-weight:600;">{str(transmission).title()}</h2>
        </div>
        """, unsafe_allow_html=True)

    # ==========================================================
    # PRICE CATEGORY
    # ==========================================================
    st.write("")
    st.markdown("""
    <div class="section-title" style="color:#FFD700; font-size:28px; font-family:Cinzel; margin-bottom:15px; font-weight:bold;">
    Price Category
    </div>
    """, unsafe_allow_html=True)

    if prediction < 300000.0:
        level = 25
        category = "Budget Vehicle"
    elif prediction < 700000.0:
        level = 50
        category = "Mid-Range Vehicle"
    elif prediction < 1500000.0:
        level = 75
        category = "Premium Vehicle"
    else:
        level = 100
        category = "Luxury Vehicle"

    st.progress(level)

    st.markdown(
        f"""
        <h2 style="text-align:center; color:#FFD700; font-family:Cinzel; margin-top:10px; font-weight:bold;">
        {category}
        </h2>
        """,
        unsafe_allow_html=True
    )

    # ==========================================================
    # QUICK INSIGHTS
    # ==========================================================
    st.write("")
    st.markdown("""
    <div class="section-title" style="color:#FFD700; font-size:28px; font-family:Cinzel; margin-bottom:15px; font-weight:bold;">
    Vehicle Insights
    </div>
    """, unsafe_allow_html=True)

    a, b, c = st.columns(3)

    with a:
        st.info(f"📍 **City**\n\n{str(city).title()}")

    with b:
        st.info(f"👤 **Owners**\n\n{total_owners}")

    with c:
        st.info(f"⭐ **Condition**\n\n{str(car_rating).title()}")

    # ==========================================================
    # BUY / SELL SUGGESTION
    # ==========================================================
    st.write("")
    st.markdown("""
    <div class="section-title" style="color:#FFD700; font-size:28px; font-family:Cinzel; margin-bottom:15px; font-weight:bold;">
    Recommendation
    </div>
    """, unsafe_allow_html=True)

    if prediction >= 1500000.0:
        st.success("Excellent resale value. Your vehicle falls into the Luxury segment.")
    elif prediction >= 700000.0:
        st.success("Your vehicle has a strong market value and is competitively priced.")
    elif prediction >= 300000.0:
        st.warning("Your vehicle has an average resale value. Regular maintenance can improve buyer confidence.")
    else:
        st.error("This vehicle belongs to the budget segment. Maintaining service records can help improve resale value.")


# ==========================================================
# STATIC LOWER PAGE CONTENT
# ==========================================================

# ==========================================================
# THANK YOU CARD
# ==========================================================
st.markdown("""
<div style="
margin-top:40px;
padding:30px;
border-radius:20px;
text-align:center;
background:rgba(255,255,255,.05);
border:1px solid rgba(212,175,55,.35);
">
<h2 style="color:#FFD700; font-family:Cinzel; font-weight:bold;">
Thank You for Using CarValue AI
</h2>
<p style="font-size:18px; color:#FFFFFF; margin-top:10px;">
We hope this valuation helps you make better buying and selling decisions.
</p>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================
st.write("")
st.write("")

st.markdown("""
<div class="footer" style="text-align:center; color:#B0B0B0; font-size:14px; margin-top:20px;">
CarValue AI © 2026
<br>
Designed & Developed by <b style="color:#FFFFFF;">Ashlin Theres James</b>
</div>
""", unsafe_allow_html=True)