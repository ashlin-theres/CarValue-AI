import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="CarValue AI | About",
    page_icon="👤",
    layout="wide"
)

# ==========================================================
# LOAD GLOBAL CSS
# ==========================================================
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==========================================================
# NAVIGATION BAR
# ==========================================================
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns([2, 1, 1, 1, 2])

with nav_col1:
    st.page_link("app.py", label="HOME", icon="🏠")

with nav_col2:
    st.page_link("pages/Prediction.py", label="PREDICT", icon="🏎️")

with nav_col3:
    st.page_link("pages/Insights.py", label="INSIGHTS", icon="📊")

with nav_col4:
    st.page_link("pages/About.py", label="ABOUT", icon="👤")

# ==========================================================
# NAVIGATION DIVIDER (SAME AS HOME PAGE)
# ==========================================================
st.markdown('<div class="top-navbar"></div>', unsafe_allow_html=True)

# ==========================================================
# HERO SECTION
# ==========================================================
st.markdown("""
<div class="section-title">👤 About CarValue AI</div>

<div class="description">
CarValue AI is an intelligent car valuation platform designed to estimate the
fair market price of used vehicles instantly using machine learning predictions.
<br><br>
It helps buyers and sellers make faster, smarter, and more confident decisions
in the used car market.
</div>
""", unsafe_allow_html=True)

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================
st.markdown("""
## 🚗 Project Overview

CarValue AI is an **AI-powered car price prediction system** built using Machine Learning.

It analyzes key vehicle attributes such as manufacturing year, mileage, fuel type,
transmission, brand, and ownership history to estimate a realistic resale value.

The goal is to reduce uncertainty in used car pricing and improve decision-making.
""")

# ==========================================================
# HOW IT WORKS
# ==========================================================
st.markdown("""
## ⚙️ How It Works

1. User enters car details (brand, year, kilometers, etc.)
2. Data is processed and encoded
3. Machine learning model predicts price
4. Final estimated value is displayed instantly
""")

# ==========================================================
# MACHINE LEARNING MODEL
# ==========================================================
st.markdown("""
## 🤖 Machine Learning Model

The system uses a **Random Forest Regressor**, a powerful ML algorithm that combines
multiple decision trees for more accurate predictions.

### 📊 Model Performance:
- MAE: **41358.56**
- RMSE: **71875.72**
- R² Score: **0.9257**

These results show strong predictive performance on real-world used car data.
""")

# ==========================================================
# FEATURES USED
# ==========================================================
st.markdown("""
## 📊 Key Features Used

- Manufacturing Year
- Kilometers Driven
- Fuel Type
- Transmission Type
- Car Brand & Model
- Ownership Count
- Vehicle Condition Indicators
""")

# ==========================================================
# TECH STACK
# ==========================================================
st.markdown("""
## ⚙️ Tech Stack

- Python 🐍  
- Streamlit  
- Pandas & NumPy  
- Scikit-learn (ML)  
- Matplotlib & Seaborn  
- Joblib (Model Saving)  
""")

# ==========================================================
# VISION
# ==========================================================
st.markdown("""
## 🎯 Vision

To build a simple, intelligent AI system that brings transparency to the used car market
and helps users make confident pricing decisions.
""")

# ==========================================================
# CREATOR
# ==========================================================
st.markdown("""
## 👤 Creator

**Ashlin Theres James**  
B.Tech Student | AI & Data Science Enthusiast  

Building practical AI solutions that simplify real-world problems using data and code.
""")

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("""
---
<div style="text-align:center; color:#FFD700; font-size:14px;">
Built with ❤️ using Machine Learning & Streamlit
</div>
""", unsafe_allow_html=True)