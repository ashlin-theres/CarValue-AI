import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 120

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="CarValue AI | Advanced Insights",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# LOAD CSS
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

# 🔥 Divider line (same as home)
st.markdown('<div class="top-navbar"></div>', unsafe_allow_html=True)

# ==========================================================
# LOAD DATA
# ==========================================================
df = pd.read_csv("data/Used_Car_Price_Prediction.csv")
sns.set_style("darkgrid")

# ==========================================================
# HEADER
# ==========================================================
st.markdown("""
<div class="section-title">📊 Advanced EDA Insights Engine</div>
<div class="description">
Explore how different factors influence used car prices using data-driven visual analysis.
</div>
""", unsafe_allow_html=True)

# ==========================================================
# SMALL PLOT FUNCTION
# ==========================================================
def small_plot():
    return plt.subplots(figsize=(5, 3))

# ==========================================================
# 1. YEAR vs PRICE
# ==========================================================
st.markdown("## 📅 Manufacturing Year vs Sale Price")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    fig, ax = small_plot()
    sns.scatterplot(data=df, x="yr_mfr", y="sale_price", ax=ax)
    ax.set_title("Year vs Price")
    st.pyplot(fig, use_container_width=False)

# ==========================================================
# 2. KMS RUN vs PRICE
# ==========================================================
st.markdown("## 🚗 Kilometers Driven vs Sale Price")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    fig, ax = small_plot()
    sns.scatterplot(data=df, x="kms_run", y="sale_price", ax=ax)
    ax.set_title("KMs vs Price")
    st.pyplot(fig, use_container_width=False)

# ==========================================================
# 3. FUEL TYPE
# ==========================================================
st.markdown("## ⛽ Fuel Type Impact")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    fig, ax = small_plot()
    sns.boxplot(data=df, x="fuel_type", y="sale_price", ax=ax)
    ax.set_title("Fuel Type vs Price")
    ax.tick_params(axis='x', rotation=20)
    st.pyplot(fig, use_container_width=False)

# ==========================================================
# 4. TRANSMISSION
# ==========================================================
st.markdown("## ⚙️ Transmission Impact")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    fig, ax = small_plot()
    sns.boxplot(data=df, x="transmission", y="sale_price", ax=ax)
    ax.set_title("Transmission vs Price")
    st.pyplot(fig, use_container_width=False)

# ==========================================================
# 5. CORRELATION HEATMAP
# ==========================================================
st.markdown("## 🔥 Feature Correlation Heatmap")

numeric_df = df.select_dtypes(include=["number"])

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(numeric_df.corr(), annot=False, cmap="coolwarm", ax=ax)
    ax.set_title("Feature Correlation")
    st.pyplot(fig, use_container_width=False)

# ==========================================================
# SUMMARY
# ==========================================================
st.markdown("""
---
### 👑 AI Insight Summary

- Newer cars have higher resale value  
- Higher kilometers reduce price significantly  
- Fuel type strongly impacts pricing  
- Transmission type affects valuation  
- Strong correlations improve ML model performance  

💡 These insights help improve CarValue AI prediction accuracy.
""")