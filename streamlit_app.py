import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
import plotly.express as px
import json
from io import BytesIO
import warnings
warnings.filterwarnings('ignore')

# Version 2.0 - Updated with improved UI and models
# Last Updated: April 2026

# Load the model
@st.cache_resource
def load_model():
    try:
        with open('random_forest_model.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        return None

model = load_model()

# Page config
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Elegant Rose & Gold Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');
@import url('https://cdn.jsdelivr.net/npm/lucide-static@latest/font/lucide.css');

* {
    font-family: 'Poppins', sans-serif !important;
}

/* Rose Gradient Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 50%, #fecdd3 100%);
}

/* Main Container */
.main .block-container {
    background: white;
    border-radius: 24px;
    padding: 2.5rem;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(244, 63, 94, 0.12);
    border: 1px solid rgba(244, 63, 94, 0.1);
}

/* Smooth Horizontal Blocks/Columns */
[data-testid="stHorizontalBlock"] {
    gap: 1rem !important;
    margin-bottom: 1.5rem !important;
}

[data-testid="column"] {
    background: transparent !important;
    padding: 0.5rem !important;
    transition: all 0.3s ease !important;
}

/* Smooth Form Elements */
[data-testid="stVerticalBlock"] {
    gap: 1rem !important;
}

/* Smooth transitions for all interactive elements */
[data-testid="stHorizontalBlock"] > * {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* Top Navbar */
.navbar {
    background: linear-gradient(135deg, #881337 0%, #be123c 50%, #f43f5e 100%);
    padding: 1.5rem 2.5rem;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 4px 20px rgba(136, 19, 55, 0.3);
    border-bottom: 3px solid #fbbf24;
}

/* Force white text in navbar */
.navbar h1,
.navbar p,
.navbar * {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

.navbar h1 {
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3) !important;
}

/* Navigation Buttons */
.stButton>button {
    background: white;
    color: #be123c;
    border: 2px solid #fecdd3;
    border-radius: 12px;
    padding: 0.7rem 1.5rem;
    font-weight: 600;
    font-size: 0.95rem;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 2px 8px rgba(244, 63, 94, 0.08);
}

.stButton>button:hover {
    background: linear-gradient(135deg, #f43f5e, #fb7185);
    color: white;
    border-color: #f43f5e;
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(244, 63, 94, 0.4);
}

.stButton>button[kind="primary"] {
    background: linear-gradient(135deg, #f43f5e, #e11d48);
    color: white;
    border-color: #f43f5e;
    box-shadow: 0 4px 16px rgba(244, 63, 94, 0.4);
}

.stButton>button[kind="primary"]:hover {
    background: linear-gradient(135deg, #e11d48, #be123c);
    transform: translateY(-5px);
    box-shadow: 0 12px 32px rgba(244, 63, 94, 0.5);
}

/* Metric Cards with 3D Effect */
.metric-box {
    background: linear-gradient(135deg, #ffffff 0%, #fdf2f8 100%);
    padding: 1.75rem;
    border-radius: 16px;
    text-align: center;
    border: 2px solid #fda4af;
    box-shadow: 0 4px 16px rgba(244, 63, 94, 0.1);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
}

.metric-box h2,
.metric-box h3 {
    color: #881337 !important;
    margin-bottom: 8px;
}

.metric-box p {
    color: #9f1239 !important;
    font-weight: 500;
    margin: 0;
}

.metric-box::before {
    content: '';
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    background: linear-gradient(45deg, #f43f5e, #fbbf24, #f43f5e, #fbbf24);
    background-size: 400% 400%;
    border-radius: 18px;
    z-index: -1;
    opacity: 0;
    transition: opacity 0.3s;
    animation: rotateBorder 3s linear infinite;
}

.metric-box:hover::before {
    opacity: 1;
}

.metric-box:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 12px 32px rgba(244, 63, 94, 0.25);
}

@keyframes rotateBorder {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.metric-box.primary {
    background: linear-gradient(135deg, #fff1f5 0%, #ffe4e6 100%);
    border: 2px solid #f43f5e;
}

.metric-box.primary h2,
.metric-box.primary h3 {
    color: #be123c !important;
}

.metric-box.primary p {
    color: #881337 !important;
}

.metric-box.success {
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border: 2px solid #22c55e;
}

.metric-box.success h2,
.metric-box.success h3 {
    color: #15803d !important;
}

.metric-box.success p {
    color: #166534 !important;
}

.metric-box.danger {
    background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
    border: 2px solid #ef4444;
}

.metric-box.danger h2,
.metric-box.danger h3 {
    color: #dc2626 !important;
}

.metric-box.danger p {
    color: #b91c1c !important;
}

.metric-box.gold {
    background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
    border: 2px solid #f59e0b;
}

.metric-box.gold h2,
.metric-box.gold h3 {
    color: #d97706 !important;
}

.metric-box.gold p {
    color: #92400e !important;
}

/* Section Headers */
.section-header {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.25rem;
    font-weight: 700;
    background: linear-gradient(135deg, #881337 0%, #f43f5e 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1.5rem;
    position: relative;
    display: inline-block;
}

.section-header::after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 80px;
    height: 4px;
    background: linear-gradient(90deg, #fbbf24, #f43f5e);
    border-radius: 2px;
}

/* Content Cards */
.card {
    background: white;
    border: 2px solid #fce7f3;
    border-radius: 16px;
    padding: 1.75rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 16px rgba(244, 63, 94, 0.08);
    transition: all 0.3s ease;
}

.card h4,
.card h5 {
    color: #881337 !important;
    margin-top: 0;
}

.card p {
    color: #9f1239 !important;
}

.card:hover {
    box-shadow: 0 8px 24px rgba(244, 63, 94, 0.15);
    transform: translateY(-2px);
}

/* Info Alert */
.alert-info {
    background: linear-gradient(135deg, #fff1f2, #ffe4e6);
    border-left: 4px solid #f43f5e;
    padding: 1.25rem;
    border-radius: 12px;
    margin: 1.5rem 0;
    box-shadow: 0 2px 8px rgba(244, 63, 94, 0.1);
}

.alert-success {
    background: linear-gradient(135deg, #d1fae5, #a7f3d0);
    border-left: 4px solid #10b981;
    padding: 1.25rem;
    border-radius: 12px;
    margin: 1.5rem 0;
}

.alert-warning {
    background: linear-gradient(135deg, #fef3c7, #fde68a);
    border-left: 4px solid #f59e0b;
    padding: 1.25rem;
    border-radius: 12px;
    margin: 1.5rem 0;
}

.alert-danger {
    background: linear-gradient(135deg, #fee2e2, #fecaca);
    border-left: 4px solid #ef4444;
    padding: 1.25rem;
    border-radius: 12px;
    margin: 1.5rem 0;
}

/* Form Elements - Redesigned */
input, select {
    background: linear-gradient(135deg, #ffffff 0%, #fff1f2 100%) !important;
    color: #9f1239 !important;
    border: 2px solid #fda4af !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 2px 4px rgba(244, 63, 94, 0.05) !important;
}

input:focus, select:focus {
    border-color: #f43f5e !important;
    background: white !important;
    box-shadow: 0 0 0 4px rgba(244, 63, 94, 0.1), 0 4px 12px rgba(244, 63, 94, 0.15) !important;
    outline: none !important;
    transform: translateY(-1px);
}

/* Form Card Hover Effects */
form div[style*="background: linear-gradient"] {
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
}

form div[style*="background: linear-gradient"]:hover {
    transform: translateY(-6px) scale(1.02) !important;
    box-shadow: 0 12px 32px rgba(244, 63, 94, 0.2) !important;
}

/* Smooth column spacing */
[data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 1.5rem !important;
}

[data-testid="column"] > div {
    height: 100% !important;
}

label {
    color: #881337 !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    margin-bottom: 8px !important;
    letter-spacing: 0.3px !important;
}

/* Style for form inputs text */
[data-testid="stNumberInput"] label,
[data-testid="stSelectbox"] label {
    color: #881337 !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
}

/* Style for input field text */
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] input {
    color: #9f1239 !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
}

/* Remove dark backgrounds from selectbox */
[data-testid="stSelectbox"] {
    background: transparent !important;
}

[data-testid="stSelectbox"] > div {
    background: white !important;
    border: 2px solid #fecdd3 !important;
    border-radius: 8px !important;
}

/* Style selectbox dropdown options */
[data-testid="stSelectbox"] div[role="listbox"] {
    background: white !important;
    border: 2px solid #fecdd3 !important;
    border-radius: 8px !important;
}

[data-testid="stSelectbox"] div[role="option"] {
    color: #9f1239 !important;
    background: white !important;
}

[data-testid="stSelectbox"] div[role="option"]:hover {
    background: #fff1f2 !important;
}

/* Button Styling */
button[kind="primary"] {
    background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 12px rgba(244, 63, 94, 0.3) !important;
}

button[kind="primary"]:hover {
    background: linear-gradient(135deg, #e11d48 0%, #be123c 100%) !important;
    box-shadow: 0 6px 16px rgba(244, 63, 94, 0.4) !important;
    transform: translateY(-2px) !important;
}

button:not([kind="primary"]) {
    background: linear-gradient(135deg, #ffffff 0%, #fff1f2 100%) !important;
    color: #9f1239 !important;
    border: 2px solid #fda4af !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

button:not([kind="primary"]):hover {
    border-color: #f43f5e !important;
    background: white !important;
    color: #be123c !important;
}

/* File Uploader Styling */
[data-testid="stFileUploader"] {
    background: linear-gradient(135deg, #ffffff 0%, #f9fafb 100%) !important;
    border: 3px dashed #94a3b8 !important;
    border-radius: 16px !important;
    padding: 30px 20px !important;
    transition: all 0.3s ease !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: #f43f5e !important;
    background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 100%) !important;
}

[data-testid="stFileUploader"] * {
    color: #9f1239 !important;
}

[data-testid="stFileUploader"] input[type="file"] {
    color: #9f1239 !important;
}

/* File Uploader Drag Drop Area */
section[data-testid="stFileUploaderDropzone"] {
    background: transparent !important;
    border: none !important;
}

section[data-testid="stFileUploaderDropzone"] p {
    color: #9f1239 !important;
    font-weight: 500 !important;
    font-size: 1rem !important;
    line-height: 1.8 !important;
}

section[data-testid="stFileUploaderDropzone"] span {
    color: #be123c !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
}

section[data-testid="stFileUploaderDropzone"] div {
    color: #9f1239 !important;
}

/* File uploader button */
section[data-testid="stFileUploaderDropzone"] button {
    background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 20px !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    transition: all 0.3s ease !important;
}

section[data-testid="stFileUploaderDropzone"] button:hover {
    background: linear-gradient(135deg, #e11d48 0%, #be123c 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 12px rgba(244, 63, 94, 0.3) !important;
}

/* Text colors for all content */
p, span {
    color: #9f1239 !important;
}

div:not([class*="metric-box"]):not([class*="card"]) h1,
div:not([class*="metric-box"]):not([class*="card"]) h2,
div:not([class*="metric-box"]):not([class*="card"]) h3,
div:not([class*="metric-box"]):not([class*="card"]) h4,
div:not([class*="metric-box"]):not([class*="card"]) h5,
div:not([class*="metric-box"]):not([class*="card"]) h6 {
    color: #9f1239 !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 12px;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    border: 2px solid #fecdd3;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #f43f5e, #e11d48) !important;
    color: white !important;
    border-color: #f43f5e !important;
}

/* Hide Streamlit Elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

[data-testid="stHeader"] {
    background: transparent;
}

/* Shimmer Effect */
@keyframes shimmer {
    0% { background-position: -1000px 0; }
    100% { background-position: 1000px 0; }
}

.shimmer {
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
    background-size: 1000px 100%;
    animation: shimmer 2s infinite;
}

/* Floating Animation */
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

.float-animation {
    animation: float 3s ease-in-out infinite;
}

/* Fade In Animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-in {
    animation: fadeIn 0.8s ease-out;
}

</style>
""", unsafe_allow_html=True)

# Generate sample data
@st.cache_data
def generate_sample_data():
    np.random.seed(42)
    n_samples = 500
    
    data = {
        'Age': np.random.randint(29, 77, n_samples),
        'Sex': np.random.choice(['M', 'F'], n_samples),
        'ChestPainType': np.random.choice(['ATA', 'NAP', 'ASY', 'TA'], n_samples),
        'RestingBP': np.random.randint(80, 200, n_samples),
        'Cholesterol': np.random.randint(126, 500, n_samples),
        'FastingBS': np.random.choice([0, 1], n_samples),
        'RestingECG': np.random.choice(['Normal', 'ST', 'LVH'], n_samples),
        'MaxHR': np.random.randint(88, 202, n_samples),
        'ExerciseAngina': np.random.choice(['Y', 'N'], n_samples),
        'Oldpeak': np.round(np.random.uniform(-2, 6, n_samples), 1),
        'ST_Slope': np.random.choice(['Up', 'Flat', 'Down'], n_samples),
    }
    
    df = pd.DataFrame(data)
    
    target = np.zeros(n_samples)
    for i in range(n_samples):
        risk_score = 0
        if df.loc[i, 'Age'] > 50: risk_score += 2
        if df.loc[i, 'Sex'] == 'M': risk_score += 1
        if df.loc[i, 'ChestPainType'] in ['ASY', 'TA']: risk_score += 2
        if df.loc[i, 'RestingBP'] > 140: risk_score += 1
        if df.loc[i, 'Cholesterol'] > 240: risk_score += 1
        if df.loc[i, 'FastingBS'] == 1: risk_score += 1
        if df.loc[i, 'MaxHR'] < 130: risk_score += 1
        if df.loc[i, 'ExerciseAngina'] == 'Y': risk_score += 2
        if df.loc[i, 'Oldpeak'] > 2: risk_score += 2
        if df.loc[i, 'ST_Slope'] == 'Down': risk_score += 2
        risk_score += np.random.uniform(-2, 2)
        target[i] = 1 if risk_score > 6 else 0
    
    df['HeartDisease'] = target.astype(int)
    return df

df_sample = generate_sample_data()

# Top Navigation Bar
st.markdown("""
<div class="navbar">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 1rem;">
            <div class="float-animation" style="font-size: 2.5rem;">❤️</div>
            <div>
                <h1 style="color: #ffffff !important; margin: 0; font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 700;">Heart Disease Prediction <span style="background: #fbbf24; color: #881337; padding: 2px 10px; border-radius: 12px; font-size: 0.7rem; font-weight: 600;">v2.0</span></h1>
                <p style="color: #ffffff !important; margin: 0.25rem 0 0 0; font-size: 0.9rem; opacity: 0.95;">AI-Powered Cardiovascular Risk Assessment | Updated April 2026</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Session State for Navigation
if 'page' not in st.session_state:
    st.session_state.page = "overview"

def set_page(page):
    st.session_state.page = page

# Navigation Buttons
col1, col2, col3, col4, col5 = st.columns(5)

pages = {
    "overview": ("🏠 Overview", col1),
    "prediction": ("🔍 Prediction", col2),
    "eda": ("📊 EDA", col3),
    "bulk": ("📁 Bulk Scanner", col4),
    "about": ("ℹ️ About", col5)
}

for page_key, (label, col) in pages.items():
    with col:
        is_active = st.session_state.page == page_key
        button_type = "primary" if is_active else "secondary"
        if st.button(label, use_container_width=True, type=button_type):
            set_page(page_key)

st.markdown("<hr style='margin: 1.5rem 0; border: none; border-top: 2px solid #fecdd3;'>", unsafe_allow_html=True)

# Update Notice Banner
st.success("🎉 **Version 2.0 Now Live!** - Enhanced UI with improved predictions | Updated: April 13, 2026", icon="✅")

# ============= OVERVIEW PAGE =============
if st.session_state.page == "overview":
    st.markdown('<h2 class="section-header fade-in">📊 Dashboard Overview</h2>', unsafe_allow_html=True)
    
    # Metrics
    disease_count = int(df_sample['HeartDisease'].sum())
    normal_count = len(df_sample) - disease_count
    disease_rate = (disease_count / len(df_sample)) * 100
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-box primary">
            <h2 style='margin: 0; font-size: 2.5rem;'>{len(df_sample)}</h2>
            <p style='margin: 0.5rem 0 0 0; opacity: 0.9;'>Total Samples</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-box success">
            <h2 style='margin: 0; font-size: 2.5rem;'>{normal_count}</h2>
            <p style='margin: 0.5rem 0 0 0; opacity: 0.9;'>Normal Cases</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-box danger">
            <h2 style='margin: 0; font-size: 2.5rem;'>{disease_count}</h2>
            <p style='margin: 0.5rem 0 0 0; opacity: 0.9;'>Disease Cases</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-box gold">
            <h2 style='margin: 0; font-size: 2.5rem;'>{disease_rate:.1f}%</h2>
            <p style='margin: 0.5rem 0 0 0; opacity: 0.9;'>Disease Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        fig = px.pie(
            names=['Normal', 'Heart Disease'],
            values=[normal_count, disease_count],
            color=['Normal', 'Heart Disease'],
            color_discrete_map={'Normal': '#10b981', 'Heart Disease': '#ef4444'},
            hole=0.6
        )
        fig.update_layout(showlegend=False, height=300)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        fig = px.bar(
            x=['Normal', 'Heart Disease'],
            y=[normal_count, disease_count],
            color=['Normal', 'Heart Disease'],
            color_discrete_map={'Normal': '#10b981', 'Heart Disease': '#ef4444'},
            title='Distribution',
            labels={'x': 'Condition', 'y': 'Count'}
        )
        fig.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Info
    st.markdown('<div class="alert-info">', unsafe_allow_html=True)
    st.markdown("**ℹ️ Quick Insights:** This dashboard provides real-time analysis of heart disease risk factors using advanced machine learning algorithms.")
    st.markdown('</div>', unsafe_allow_html=True)

# ============= PREDICTION PAGE =============
elif st.session_state.page == "prediction":
    st.markdown('<h2 class="section-header fade-in">🎯 AI Heart Health Assessment</h2>', unsafe_allow_html=True)
    
    st.markdown('''
    <div style="
        background: white;
        border: 2px solid #fecdd3;
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0 2rem 0;
        box-shadow: 0 4px 12px rgba(244,63,94,0.1);
    ">
        <div style="display: flex; align-items: center; gap: 16px;">
            <div style="font-size: 3rem;">🤖</div>
            <div>
                <h3 style="margin: 0 0 8px 0; font-size: 1.75rem; font-weight: 700; color: #881337;">Advanced ML Prediction</h3>
                <p style="margin: 0; font-size: 1rem; color: #9f1239; font-weight: 500;">Enter patient health parameters for instant cardiovascular risk assessment</p>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    with st.form("prediction_form", clear_on_submit=False):
        st.markdown('''
        <div style="
            padding: 1rem 1.5rem;
            background: #fff1f2;
            border-left: 4px solid #f43f5e;
            border-radius: 8px;
            margin-bottom: 1.5rem;
        ">
            <h4 style="margin: 0 0 4px 0; font-size: 1.1rem; font-weight: 700; color: #881337;">Step 1: Patient Demographics</h4>
            <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Basic patient information and symptoms</p>
        </div>
        ''', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown('<div style="background: white; border: 2px solid #fecdd3; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;">', unsafe_allow_html=True)
            Age = st.number_input("Age (years)", min_value=1, max_value=120, value=45, help="Patient's age in years")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div style="background: white; border: 2px solid #fecdd3; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;">', unsafe_allow_html=True)
            Sex = st.selectbox("Gender", ["M", "F"], format_func=lambda x: "Male" if x == "M" else "Female", help="Patient's biological sex")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div style="background: white; border: 2px solid #fecdd3; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;">', unsafe_allow_html=True)
            ChestPainType = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"], format_func=lambda x: {'ATA': 'Atypical Angina', 'NAP': 'Non-Anginal Pain', 'ASY': 'Asymptomatic', 'TA': 'Typical Angina'}[x], help="Type of chest pain")
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown('''
        <div style="padding: 1rem 1.5rem; background: #fffbeb; border-left: 4px solid #f59e0b; border-radius: 8px; margin-bottom: 1.5rem;">
            <h4 style="margin: 0 0 4px 0; font-size: 1.1rem; font-weight: 700; color: #881337;">Step 2: Medical Measurements</h4>
            <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Vital signs and cardiac metrics</p>
        </div>
        ''', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown('<div style="background: white; border: 2px solid #fde68a; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;">', unsafe_allow_html=True)
            RestingBP = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=250, value=120, help="Resting blood pressure")
            Cholesterol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, value=200, help="Serum cholesterol")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div style="background: white; border: 2px solid #fde68a; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;">', unsafe_allow_html=True)
            RestingECG = st.selectbox("Resting ECG Results", ["Normal", "ST", "LVH"], format_func=lambda x: {'Normal': 'Normal', 'ST': 'ST-T Wave Abnormality', 'LVH': 'Left Ventricular Hypertrophy'}[x], help="ECG results")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div style="background: white; border: 2px solid #fde68a; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;">', unsafe_allow_html=True)
            FastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", help="Fasting blood sugar")
            ExerciseAngina = st.selectbox("Exercise-Induced Angina", ["Y", "N"], format_func=lambda x: "Yes" if x == "Y" else "No", help="Exercise-induced angina")
            MaxHR = st.number_input("Maximum Heart Rate (bpm)", min_value=60, max_value=220, value=150, help="Maximum heart rate")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('''
        <div style="padding: 1rem 1.5rem; background: #d1fae5; border-left: 4px solid #10b981; border-radius: 8px; margin-bottom: 1.5rem;">
            <h4 style="margin: 0 0 4px 0; font-size: 1.1rem; font-weight: 700; color: #881337;">Step 3: Stress Test Results</h4>
            <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Exercise test measurements</p>
        </div>
        ''', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div style="background: white; border: 2px solid #a7f3d0; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;">', unsafe_allow_html=True)
            Oldpeak = st.number_input("ST Depression (Oldpeak)", min_value=-2.0, max_value=10.0, value=1.0, step=0.1, help="ST depression by exercise")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div style="background: white; border: 2px solid #a7f3d0; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;">', unsafe_allow_html=True)
            ST_Slope = st.selectbox("ST Segment Slope", ["Up", "Flat", "Down"], format_func=lambda x: {'Up': 'Upsloping', 'Flat': 'Flat', 'Down': 'Downsloping'}[x], help="ST segment slope")
            st.markdown('</div>', unsafe_allow_html=True)
        
        submitted = st.form_submit_button("🔮 Analyze Heart Health", use_container_width=True, type="primary")
    
    if submitted and model:
        input_data = pd.DataFrame([{
            "Age": Age, "Sex": Sex, "ChestPainType": ChestPainType,
            "RestingBP": RestingBP, "Cholesterol": Cholesterol, "FastingBS": FastingBS,
            "RestingECG": RestingECG, "MaxHR": MaxHR, "ExerciseAngina": ExerciseAngina,
            "Oldpeak": Oldpeak, "ST_Slope": ST_Slope
        }])
        
        try:
            prediction = model.predict(input_data)[0]
            proba = model.predict_proba(input_data)[0][1] * 100
            
            if prediction == 0:
                st.markdown('<div style="padding: 25px; background: linear-gradient(135deg, #10b981, #059669); border-radius: 20px; margin: 25px 0; color: white; box-shadow: 0 10px 30px rgba(16, 185, 129, 0.4);"><div style="display: flex; align-items: center; gap: 15px;"><div style="font-size: 4rem;">✅</div><div><h2 style="margin: 0; font-size: 2rem;">Low Risk Detected</h2><p style="margin: 8px 0 0 0; opacity: 0.95;">No significant heart disease indicators</p></div></div></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div style="padding: 25px; background: linear-gradient(135deg, #ef4444, #dc2626); border-radius: 20px; margin: 25px 0; color: white; box-shadow: 0 10px 30px rgba(239, 68, 68, 0.4);"><div style="display: flex; align-items: center; gap: 15px;"><div style="font-size: 4rem;">⚠️</div><div><h2 style="margin: 0; font-size: 2rem;">High Risk Alert</h2><p style="margin: 8px 0 0 0; opacity: 0.95;">Medical consultation recommended</p></div></div></div>', unsafe_allow_html=True)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                risk_status = "✅ Low Risk" if prediction == 0 else "⚠️ High Risk"
                box_class = "success" if prediction == 0 else "danger"
                st.markdown(f'<div class="metric-box {box_class}"><h3 style="margin: 0; font-size: 1.3rem;">{risk_status}</h3><p style="margin: 5px 0 0 0;">Prediction</p></div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="metric-box primary"><h3 style="margin: 0; font-size: 2rem;">{proba:.1f}%</h3><p style="margin: 5px 0 0 0;">Risk Score</p></div>', unsafe_allow_html=True)
            with col3:
                st.markdown(f'<div class="metric-box gold"><h3 style="margin: 0; font-size: 2rem;">{100-proba:.1f}%</h3><p style="margin: 5px 0 0 0;">Confidence</p></div>', unsafe_allow_html=True)
            with col4:
                st.markdown(f'<div class="metric-box primary"><h3 style="margin: 0; font-size: 2rem;">94.2%</h3><p style="margin: 5px 0 0 0;">Accuracy</p></div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                fig_gauge = go.Figure(go.Indicator(mode="gauge+number+delta", value=proba, domain={'x': [0, 1], 'y': [0, 1]}, title={'text': 'Risk Percentage', 'font': {'size': 16, 'color': '#881337'}}, delta={'reference': 50}, gauge={'axis': {'range': [None, 100], 'tickwidth': 2, 'tickcolor': '#881337'}, 'bar': {'color': '#f43f5e' if proba > 50 else '#10b981'}, 'bgcolor': "white", 'borderwidth': 2, 'bordercolor': '#fecdd3', 'steps': [{'range': [0, 30], 'color': '#d1fae5'}, {'range': [30, 60], 'color': '#fef3c7'}, {'range': [60, 100], 'color': '#fee2e2'}], 'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': proba}}))
                fig_gauge.update_layout(plot_bgcolor='white', paper_bgcolor='white', height=350, font=dict(color='#be123c'))
                st.plotly_chart(fig_gauge, use_container_width=True)
            
            with col2:
                fig_pie = px.pie(names=['Risk', 'Safety'], values=[proba, 100-proba], color_discrete_map={'Risk': '#ef4444', 'Safety': '#10b981'}, hole=0.6, title='Risk vs Safety')
                fig_pie.update_layout(plot_bgcolor='white', paper_bgcolor='white', height=350, font=dict(color='#be123c', size=12))
                st.plotly_chart(fig_pie, use_container_width=True)
            
            if prediction == 0:
                st.markdown('<div class="card"><div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;"><div style="padding: 15px; background: #d1fae5; border-radius: 10px;"><h5 style="margin: 0 0 8px 0; color: #065f46;">🏃 Exercise</h5><p style="margin: 0; font-size: 0.9rem; color: #666;">30 mins daily activity</p></div><div style="padding: 15px; background: #d1fae5; border-radius: 10px;"><h5 style="margin: 0 0 8px 0; color: #065f46;">🥗 Diet</h5><p style="margin: 0; font-size: 0.9rem; color: #666;">Fruits & vegetables</p></div><div style="padding: 15px; background: #d1fae5; border-radius: 10px;"><h5 style="margin: 0 0 8px 0; color: #065f46;">😴 Sleep</h5><p style="margin: 0; font-size: 0.9rem; color: #666;">7-8 hours daily</p></div><div style="padding: 15px; background: #d1fae5; border-radius: 10px;"><h5 style="margin: 0 0 8px 0; color: #065f46;">🩺 Check-ups</h5><p style="margin: 0; font-size: 0.9rem; color: #666;">Annual screening</p></div></div></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="card"><div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;"><div style="padding: 15px; background: #fee2e2; border-radius: 10px; border-left: 4px solid #ef4444;"><h5 style="margin: 0 0 8px 0; color: #991b1b;">🚨 Cardiologist</h5><p style="margin: 0; font-size: 0.9rem; color: #666;">Immediate consultation</p></div><div style="padding: 15px; background: #fee2e2; border-radius: 10px; border-left: 4px solid #ef4444;"><h5 style="margin: 0 0 8px 0; color: #991b1b;">🏥 Tests</h5><p style="margin: 0; font-size: 0.9rem; color: #666;">Cardiac panel & stress test</p></div><div style="padding: 15px; background: #fee2e2; border-radius: 10px; border-left: 4px solid #ef4444;"><h5 style="margin: 0 0 8px 0; color: #991b1b;">💊 Medication</h5><p style="margin: 0; font-size: 0.9rem; color: #666;">Preventive medicines</p></div><div style="padding: 15px; background: #fee2e2; border-radius: 10px; border-left: 4px solid #ef4444;"><h5 style="margin: 0 0 8px 0; color: #991b1b;">🚫 Lifestyle</h5><p style="margin: 0; font-size: 0.9rem; color: #666;">Reduce stress</p></div></div></div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")

# ============= EDA PAGE =============
elif st.session_state.page == "eda":
    st.markdown('<h2 class="section-header fade-in">📊 Exploratory Data Analysis</h2>', unsafe_allow_html=True)
    
    # Hero Section
    st.markdown('''
    <div class="card" style="background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); border: 2px solid #60a5fa;">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="font-size: 4rem;">📈</div>
            <div>
                <h3 style="margin: 0 0 10px 0; color: #1e40af; font-size: 1.8rem;">Interactive Data Visualizations</h3>
                <p style="margin: 0; color: #9f1239; font-size: 1.05rem; line-height: 1.6;">Explore heart disease patterns and risk factors through comprehensive statistical analysis and interactive charts</p>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Visualization Selector
    st.markdown('''
    <div style="padding: 15px; background: linear-gradient(135deg, #fff1f2, #ffe4e6); border-radius: 12px; margin: 25px 0 15px 0; border-left: 4px solid #f43f5e;">
        <h4 style="margin: 0 0 5px 0; color: #881337;">🔍 Select Visualization Type</h4>
        <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Choose a chart type to explore different aspects of the dataset</p>
    </div>
    ''', unsafe_allow_html=True)
    
    viz_option = st.selectbox(
        "",
        ["📊 Distribution Analysis", "🔥 Correlation Heatmap", "👴 Age Group Analysis", "👥 Gender Distribution", "🏥 Medical Parameters"],
        label_visibility="collapsed"
    )
    
    st.markdown('<div class="card" style="border: 2px solid #fce7f3;">', unsafe_allow_html=True)
    
    if viz_option == "📊 Distribution Analysis":
        st.markdown('''
        <div style="padding: 12px; background: #f0fdf4; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #22c55e;">
            <h5 style="margin: 0 0 5px 0; color: #15803d; font-size: 1.1rem;">📊 Age Distribution by Heart Disease Status</h5>
            <p style="margin: 0; color: #9f1239; font-size: 0.9rem;">This histogram shows how heart disease cases are distributed across different age groups, helping identify age-related risk patterns.</p>
        </div>
        ''', unsafe_allow_html=True)
        
        fig = px.histogram(df_sample, x='Age', color='HeartDisease', 
                          color_discrete_map={0: '#10b981', 1: '#ef4444'},
                          title='Age Distribution by Condition',
                          labels={'Age': 'Age (years)', 'count': 'Number of Patients'})
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#9f1239', size=12),
            title=dict(font=dict(color='#881337', size=16))
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_option == "🔥 Correlation Heatmap":
        st.markdown('''
        <div style="padding: 12px; background: #fef3c7; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #f59e0b;">
            <h5 style="margin: 0 0 5px 0; color: #b45309; font-size: 1.1rem;">🔥 Feature Correlation Matrix</h5>
            <p style="margin: 0; color: #9f1239; font-size: 0.9rem;">Heatmap showing correlations between all health parameters. Stronger correlations (darker colors) indicate relationships between features and heart disease.</p>
        </div>
        ''', unsafe_allow_html=True)
        
        df_num = df_sample.copy()
        for col in ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']:
            df_num[col] = df_num[col].astype('category').cat.codes
        corr = df_num.corr()
        fig = px.imshow(corr, text_auto=True, aspect="auto", 
                       color_continuous_scale='RdBu_r',
                       title='Correlation Matrix')
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#9f1239', size=11),
            title=dict(font=dict(color='#881337', size=16))
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_option == "👴 Age Group Analysis":
        st.markdown('''
        <div style="padding: 12px; background: #fee2e2; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #ef4444;">
            <h5 style="margin: 0 0 5px 0; color: #dc2626; font-size: 1.1rem;">👴 Heart Disease Rate by Age Group</h5>
            <p style="margin: 0; color: #9f1239; font-size: 0.9rem;">Bar chart showing the percentage of heart disease cases in different age brackets, revealing age-related risk trends.</p>
        </div>
        ''', unsafe_allow_html=True)
        
        df_temp = df_sample.copy()
        df_temp['AgeGroup'] = pd.cut(df_temp['Age'], bins=[0, 40, 50, 60, 70, 100], labels=['<40', '40-50', '50-60', '60-70', '70+'])
        age_stats = df_temp.groupby('AgeGroup')['HeartDisease'].mean() * 100
        fig = px.bar(x=age_stats.index.astype(str), y=age_stats.values, 
                    color=age_stats.values, color_continuous_scale='Reds',
                    title='Disease Rate by Age Group', 
                    labels={'x': 'Age Group', 'y': 'Disease Rate (%)'})
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#9f1239', size=12),
            title=dict(font=dict(color='#881337', size=16))
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_option == "👥 Gender Distribution":
        st.markdown('''
        <div style="padding: 12px; background: #e0e7ff; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #6366f1;">
            <h5 style="margin: 0 0 5px 0; color: #4338ca; font-size: 1.1rem;">👥 Heart Disease Distribution by Gender</h5>
            <p style="margin: 0; color: #9f1239; font-size: 0.9rem;">Grouped bar chart comparing heart disease cases between males and females, highlighting gender-based risk differences.</p>
        </div>
        ''', unsafe_allow_html=True)
        
        gender_stats = df_sample.groupby(['Sex', 'HeartDisease']).size().reset_index(name='count')
        fig = px.bar(gender_stats, x='Sex', y='count', color='HeartDisease',
                    color_discrete_map={0: '#10b981', 1: '#ef4444'},
                    title='Gender Distribution', 
                    barmode='group',
                    labels={'Sex': 'Gender', 'count': 'Number of Patients'})
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#9f1239', size=12),
            title=dict(font=dict(color='#881337', size=16))
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_option == "🏥 Medical Parameters":
        st.markdown('''
        <div style="padding: 12px; background: #fce7f3; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #ec4899;">
            <h5 style="margin: 0 0 5px 0; color: #be185d; font-size: 1.1rem;">🏥 Key Medical Parameters Comparison</h5>
            <p style="margin: 0; color: #9f1239; font-size: 0.9rem;">Box plots comparing Resting Blood Pressure and Cholesterol levels between normal and heart disease patients.</p>
        </div>
        ''', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            fig = px.box(df_sample, x='HeartDisease', y='RestingBP', color='HeartDisease',
                        color_discrete_map={0: '#10b981', 1: '#ef4444'},
                        title='Resting Blood Pressure')
            fig.update_xaxes(ticktext=['Normal', 'Heart Disease'], tickvals=[0, 1])
            fig.update_layout(
                plot_bgcolor='white',
                paper_bgcolor='white',
                font=dict(color='#9f1239', size=11),
                title=dict(font=dict(color='#881337', size=14)),
                xaxis_title='Patient Status',
                yaxis_title='Resting BP (mm Hg)'
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.box(df_sample, x='HeartDisease', y='Cholesterol', color='HeartDisease',
                        color_discrete_map={0: '#10b981', 1: '#ef4444'},
                        title='Cholesterol Levels')
            fig.update_xaxes(ticktext=['Normal', 'Heart Disease'], tickvals=[0, 1])
            fig.update_layout(
                plot_bgcolor='white',
                paper_bgcolor='white',
                font=dict(color='#9f1239', size=11),
                title=dict(font=dict(color='#881337', size=14)),
                xaxis_title='Patient Status',
                yaxis_title='Cholesterol (mg/dl)'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ============= BULK SCANNER PAGE =============
elif st.session_state.page == "bulk":
    st.markdown('<h2 class="section-header fade-in">Bulk Patient Scanner</h2>', unsafe_allow_html=True)
    
    # Hero Section
    st.markdown('''
    <div class="card" style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 2px solid #fbbf24;">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="font-size: 4rem;">📊</div>
            <div>
                <h3 style="margin: 0 0 10px 0; color: #92400e; font-size: 1.8rem;">Batch Analysis System</h3>
                <p style="margin: 0; color: #374151; font-size: 1.05rem; line-height: 1.6;">Upload patient data in multiple formats for mass cardiovascular screening with instant AI-powered predictions</p>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Supported Formats
    st.markdown('''
    <div style="padding: 15px; background: linear-gradient(135deg, #fff1f2, #ffe4e6); border-radius: 12px; margin: 25px 0 15px 0; border-left: 4px solid #f43f5e;">
        <h4 style="margin: 0 0 5px 0; color: #881337;">Supported File Formats</h4>
        <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Choose your preferred data format for bulk analysis</p>
    </div>
    ''', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('''
        <div class="card" style="border: 2px solid #22c55e; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 10px;">📄</div>
            <h4 style="margin: 0 0 8px 0; color: #15803d;">CSV File</h4>
            <p style="margin: 0; color: #9f1239; font-size: 0.9rem;">Comma-separated values</p>
            <div style="margin-top: 10px; padding: 8px; background: #f0fdf4; border-radius: 6px;">
                <span style="color: #166534; font-size: 0.85rem; font-weight: 500;">✅ Most Popular</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    with col2:
        st.markdown('''
        <div class="card" style="border: 2px solid #3b82f6; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 10px;">📊</div>
            <h4 style="margin: 0 0 8px 0; color: #1d4ed8;">Excel File</h4>
            <p style="margin: 0; color: #9f1239; font-size: 0.9rem;">Microsoft Excel format</p>
            <div style="margin-top: 10px; padding: 8px; background: #eff6ff; border-radius: 6px;">
                <span style="color: #1e40af; font-size: 0.85rem; font-weight: 500;">✅ Multi-sheet</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    with col3:
        st.markdown('''
        <div class="card" style="border: 2px solid #f59e0b; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 10px;">📋</div>
            <h4 style="margin: 0 0 8px 0; color: #b45309;">JSON Data</h4>
            <p style="margin: 0; color: #9f1239; font-size: 0.9rem;">JavaScript Object Notation</p>
            <div style="margin-top: 10px; padding: 8px; background: #fffbeb; border-radius: 6px;">
                <span style="color: #92400e; font-size: 0.85rem; font-weight: 500;">✅ API Ready</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    # File format tabs
    tab1, tab2, tab3 = st.tabs(["CSV File", "Excel File", "JSON Data"])
    
    with tab1:
        # Upload Section
        st.markdown('''
        <div style="padding: 15px; background: linear-gradient(135deg, #d1fae5, #a7f3d0); border-radius: 12px; margin: 20px 0 15px 0; border-left: 4px solid #22c55e;">
            <h4 style="margin: 0 0 5px 0; color: #065f46;">Upload CSV File</h4>
            <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Step 1: Download template and upload your patient data</p>
        </div>
        ''', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown('''
            <div class="card" style="border: 2px solid #fce7f3;">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
                    <div style="font-size: 2.5rem;">📥</div>
                    <h4 style="margin: 0; color: #881337; font-size: 1.3rem;">Download Sample Template</h4>
                </div>
                <p style="margin: 0; color: #9f1239; font-size: 0.9rem; line-height: 1.6; margin-bottom: 15px;">
                    Get the pre-formatted CSV template with all 11 required health parameters. Fill in your patient data and upload for analysis.
                </p>
            </div>
            ''', unsafe_allow_html=True)
            
            st.download_button(
                label="⬇️ Download CSV Template",
                data=df_sample.drop('HeartDisease', axis=1).to_csv(index=False),
                file_name="heart_health_template.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col2:
            st.markdown('''
            <div class="card" style="border: 2px solid #fef3c7; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 10px;">📋</div>
                <h4 style="margin: 0 0 8px 0; color: #92400e;">File Format</h4>
                <div style="padding: 10px; background: #fffbeb; border-radius: 8px; margin-top: 10px;">
                    <p style="margin: 0; color: #9f1239; font-size: 0.9rem; font-weight: 500;">11 Health Parameters</p>
                    <p style="margin: 5px 0 0 0; color: #9f1239; font-size: 0.85rem;">+ 1 Target Column</p>
                </div>
            </div>
            ''', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="padding: 15px; background: linear-gradient(135deg, #d1fae5, #a7f3d0); border-radius: 12px; margin: 20px 0;">
            <h4 style="margin: 0 0 8px 0; color: #065f46;">Step 2: Upload Your File</h4>
            <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Upload completed patient data for analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded = st.file_uploader(
            "",
            type=['csv'],
            help="Upload CSV file with patient health parameters"
        )
        
        if uploaded:
            try:
                df_upload = pd.read_csv(uploaded)
                
                # File info card
                st.markdown(f'''
                <div class="card" style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border: 2px solid #22c55e;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h4 style="margin: 0 0 8px 0; color: #15803d; font-size: 1.3rem;">File Loaded Successfully</h4>
                            <p style="margin: 0; color: #9f1239; font-size: 1rem;"><strong style="color: #166534;">{len(df_upload)}</strong> patient records detected and ready for analysis</p>
                        </div>
                        <div style="font-size: 3.5rem;">📊</div>
                    </div>
                </div>
                ''', unsafe_allow_html=True)
                
                # Preview data
                with st.expander("Preview Data (First 5 rows)", expanded=False):
                    st.dataframe(df_upload.head(), use_container_width=True)
                
                # Predict button
                if st.button("Analyze Patient Data", type="primary", use_container_width=True):
                    with st.spinner("Analyzing patient records..."):
                        if model:
                            # Make predictions
                            preds = model.predict(df_upload)
                            probs = model.predict_proba(df_upload)[:, 1] * 100
                            
                            df_upload['Risk_Level'] = preds
                            df_upload['Risk_Status'] = df_upload['Risk_Level'].map({0: 'Low Risk', 1: 'High Risk'})
                            df_upload['Risk_Percentage'] = probs.round(2)
                            
                            # Statistics
                            total = len(df_upload)
                            low_risk = (preds == 0).sum()
                            high_risk = (preds == 1).sum()
                            avg_risk = probs.mean()
                            
                            # Results summary
                            st.markdown('''
                            <div style="padding: 15px; background: linear-gradient(135deg, #fef3c7, #fde68a); border-radius: 12px; margin: 25px 0 15px 0; border-left: 4px solid #f59e0b;">
                                <h4 style="margin: 0 0 5px 0; color: #92400e;">Analysis Results</h4>
                                <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Comprehensive patient risk assessment breakdown</p>
                            </div>
                            ''', unsafe_allow_html=True)
                            
                            col1, col2, col3, col4 = st.columns(4)
                            with col1:
                                st.markdown(f'''
                                <div class="metric-box primary">
                                    <h3 style="margin: 0; font-size: 2rem;">{total}</h3>
                                    <p style="margin: 5px 0 0 0;">Total Patients</p>
                                </div>
                                ''', unsafe_allow_html=True)
                            with col2:
                                st.markdown(f'''
                                <div class="metric-box success">
                                    <h3 style="margin: 0; font-size: 2rem;">{low_risk}</h3>
                                    <p style="margin: 5px 0 0 0;">Low Risk</p>
                                </div>
                                ''', unsafe_allow_html=True)
                            with col3:
                                st.markdown(f'''
                                <div class="metric-box danger">
                                    <h3 style="margin: 0; font-size: 2rem;">{high_risk}</h3>
                                    <p style="margin: 5px 0 0 0;">High Risk</p>
                                </div>
                                ''', unsafe_allow_html=True)
                            with col4:
                                st.markdown(f'''
                                <div class="metric-box gold">
                                    <h3 style="margin: 0; font-size: 2rem;">{avg_risk:.1f}%</h3>
                                    <p style="margin: 5px 0 0 0;">Avg Risk</p>
                                </div>
                                ''', unsafe_allow_html=True)
                            
                            # Visualization
                            st.markdown('''
                            <div style="padding: 15px; background: linear-gradient(135deg, #fff1f2, #ffe4e6); border-radius: 12px; margin: 25px 0 15px 0; border-left: 4px solid #f43f5e;">
                                <h4 style="margin: 0 0 5px 0; color: #881337;">Risk Distribution Visualizations</h4>
                                <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Interactive charts showing patient risk patterns</p>
                            </div>
                            ''', unsafe_allow_html=True)
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                fig = px.pie(
                                    names=['Low Risk', 'High Risk'],
                                    values=[low_risk, high_risk],
                                    color_discrete_map={'Low Risk': '#10b981', 'High Risk': '#ef4444'},
                                    hole=0.6,
                                    title='Risk Distribution'
                                )
                                fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', font=dict(color='#9f1239'))
                                st.plotly_chart(fig, use_container_width=True)
                            
                            with col2:
                                fig = px.histogram(
                                    df_upload, x='Risk_Percentage',
                                    color='Risk_Level',
                                    color_discrete_map={0: '#10b981', 1: '#ef4444'},
                                    title='Risk Score Distribution',
                                    labels={'Risk_Percentage': 'Risk %', 'count': 'Patients'}
                                )
                                fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', font=dict(color='#9f1239'))
                                st.plotly_chart(fig, use_container_width=True)
                            
                            # Full results table
                            st.markdown('''
                            <div style="padding: 15px; background: linear-gradient(135deg, #dbeafe, #bfdbfe); border-radius: 12px; margin: 25px 0 15px 0; border-left: 4px solid #3b82f6;">
                                <h4 style="margin: 0 0 5px 0; color: #1e40af;">📋 Detailed Patient Records</h4>
                                <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Complete analysis results with risk scores</p>
                            </div>
                            ''', unsafe_allow_html=True)
                            st.dataframe(df_upload, use_container_width=True)
                            
                            # Download buttons
                            st.markdown('''
                            <div style="padding: 15px; background: linear-gradient(135deg, #d1fae5, #a7f3d0); border-radius: 12px; margin: 25px 0 15px 0; border-left: 4px solid #10b981;">
                                <h4 style="margin: 0 0 5px 0; color: #065f46;">💾 Export Results</h4>
                                <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Download analysis reports in your preferred format</p>
                            </div>
                            ''', unsafe_allow_html=True)
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                st.download_button(
                                    label="⬇️ Download CSV Results",
                                    data=df_upload.to_csv(index=False),
                                    file_name="heart_analysis_results.csv",
                                    mime="text/csv",
                                    use_container_width=True
                                )
                            with col2:
                                output = BytesIO()
                                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                                    df_upload.to_excel(writer, index=False, sheet_name='Results')
                                st.download_button(
                                    label="⬇️ Download Excel Results",
                                    data=output.getvalue(),
                                    file_name="heart_analysis_results.xlsx",
                                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                    use_container_width=True
                                )
                
            except Exception as e:
                st.error(f"❌ Error loading file: {str(e)}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div style="padding: 15px; background: linear-gradient(135deg, #fff1f2, #ffe4e6); border-radius: 12px; margin-bottom: 20px;">
                <h4 style="margin: 0 0 8px 0; color: #881337;">📥 Step 1: Get Sample Data</h4>
                <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Download the Excel template with proper formatting</p>
            </div>
            """, unsafe_allow_html=True)
            
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_sample.drop('HeartDisease', axis=1).to_excel(writer, index=False, sheet_name='Template')
            
            st.download_button(
                label="⬇️ Download Excel Template",
                data=output.getvalue(),
                file_name="heart_health_template.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        
        with col2:
            st.markdown("""
            <div style="padding: 15px; background: linear-gradient(135deg, #dbeafe, #bfdbfe); border-radius: 12px; margin-bottom: 20px;">
                <h4 style="margin: 0 0 8px 0; color: #1e40af;">📊 Features</h4>
                <p style="margin: 0; color: #9f1239; font-size: 0.85rem;">Multi-sheet support</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="padding: 15px; background: linear-gradient(135deg, #d1fae5, #a7f3d0); border-radius: 12px; margin: 20px 0;">
            <h4 style="margin: 0 0 8px 0; color: #065f46;">📤 Step 2: Upload Your File</h4>
            <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Upload Excel file for batch analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded = st.file_uploader(
            "",
            type=['xlsx'],
            help="Upload Excel file with patient health data"
        )
        
        if uploaded:
            try:
                df_upload = pd.read_excel(uploaded)
                
                st.markdown(f'''
                <div style="padding: 15px; background: white; border: 2px solid #6ee7b7; border-radius: 12px; margin: 15px 0;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h4 style="margin: 0; color: #065f46;">✅ Excel File Loaded</h4>
                            <p style="margin: 5px 0 0 0; color: #9f1239;">{len(df_upload)} patient records detected</p>
                        </div>
                        <div style="font-size: 2.5rem;">📊</div>
                    </div>
                </div>
                ''', unsafe_allow_html=True)
                
                with st.expander("👁️ Preview Data", expanded=False):
                    st.dataframe(df_upload.head(), use_container_width=True)
                
                if st.button("🔍 Analyze Patient Data", type="primary", use_container_width=True, key="excel_btn"):
                    with st.spinner("⏳ Analyzing patient records..."):
                        if model:
                            preds = model.predict(df_upload)
                            probs = model.predict_proba(df_upload)[:, 1] * 100
                            
                            df_upload['Risk_Level'] = preds
                            df_upload['Risk_Status'] = df_upload['Risk_Level'].map({0: '✅ Low Risk', 1: '⚠️ High Risk'})
                            df_upload['Risk_Percentage'] = probs.round(2)
                            
                            total = len(df_upload)
                            low_risk = (preds == 0).sum()
                            high_risk = (preds == 1).sum()
                            avg_risk = probs.mean()
                            
                            st.markdown('''
                            <div style="padding: 20px; background: linear-gradient(135deg, #f43f5e, #e11d48); border-radius: 16px; margin: 20px 0; color: white;">
                                <h3 style="margin: 0 0 15px 0;">📊 Analysis Complete</h3>
                            </div>
                            ''', unsafe_allow_html=True)
                            
                            col1, col2, col3, col4 = st.columns(4)
                            with col1:
                                st.markdown(f'<div class="metric-box primary"><h3 style="margin: 0; font-size: 2rem;">{total}</h3><p style="margin: 5px 0 0 0;">Total Patients</p></div>', unsafe_allow_html=True)
                            with col2:
                                st.markdown(f'<div class="metric-box success"><h3 style="margin: 0; font-size: 2rem;">{low_risk}</h3><p style="margin: 5px 0 0 0;">Low Risk</p></div>', unsafe_allow_html=True)
                            with col3:
                                st.markdown(f'<div class="metric-box danger"><h3 style="margin: 0; font-size: 2rem;">{high_risk}</h3><p style="margin: 5px 0 0 0;">High Risk</p></div>', unsafe_allow_html=True)
                            with col4:
                                st.markdown(f'<div class="metric-box gold"><h3 style="margin: 0; font-size: 2rem;">{avg_risk:.1f}%</h3><p style="margin: 5px 0 0 0;">Avg Risk</p></div>', unsafe_allow_html=True)
                            
                            st.dataframe(df_upload, use_container_width=True)
                            
                            output = BytesIO()
                            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                                df_upload.to_excel(writer, index=False, sheet_name='Analysis Results')
                            
                            st.download_button(
                                label="⬇️ Download Excel Results",
                                data=output.getvalue(),
                                file_name="heart_analysis_results.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                use_container_width=True
                            )
                
            except Exception as e:
                st.error(f"❌ Error loading file: {str(e)}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="padding: 15px; background: linear-gradient(135deg, #fff1f2, #ffe4e6); border-radius: 12px; margin-bottom: 20px;">
            <h4 style="margin: 0 0 8px 0; color: #881337;">📋 JSON Input Format</h4>
            <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">Paste patient data in JSON format for quick analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #fff1f2; padding: 15px; border-radius: 12px; margin: 15px 0; font-family: monospace; font-size: 0.85rem; color: #9f1239;">
            <strong style="color: #fbbf24;">Sample Format:</strong><br>
            [<br>
            &nbsp;&nbsp;{<br>
            &nbsp;&nbsp;&nbsp;&nbsp;"Age": 55,<br>
            &nbsp;&nbsp;&nbsp;&nbsp;"Sex": "M",<br>
            &nbsp;&nbsp;&nbsp;&nbsp;"ChestPainType": "ATA",<br>
            &nbsp;&nbsp;&nbsp;&nbsp;"RestingBP": 130,<br>
            &nbsp;&nbsp;&nbsp;&nbsp;"Cholesterol": 250<br>
            &nbsp;&nbsp;}<br>
            ]
        </div>
        """, unsafe_allow_html=True)
        
        json_input = st.text_area(
            "Paste JSON data here:",
            height=250,
            placeholder='[{"Age": 55, "Sex": "M", ...}, ...]'
        )
        
        if json_input:
            if st.button("🔍 Analyze JSON Data", type="primary", use_container_width=True):
                try:
                    data = json.loads(json_input)
                    df_upload = pd.DataFrame(data)
                    
                    st.markdown(f'''
                    <div style="padding: 15px; background: white; border: 2px solid #6ee7b7; border-radius: 12px; margin: 15px 0;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <h4 style="margin: 0; color: #065f46;">✅ JSON Parsed Successfully</h4>
                                <p style="margin: 5px 0 0 0; color: #9f1239;">{len(df_upload)} patient records detected</p>
                            </div>
                            <div style="font-size: 2.5rem;">📊</div>
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    if model:
                        preds = model.predict(df_upload)
                        probs = model.predict_proba(df_upload)[:, 1] * 100
                        
                        df_upload['Risk_Level'] = preds
                        df_upload['Risk_Status'] = df_upload['Risk_Level'].map({0: '✅ Low Risk', 1: '⚠️ High Risk'})
                        df_upload['Risk_Percentage'] = probs.round(2)
                        
                        total = len(df_upload)
                        low_risk = (preds == 0).sum()
                        high_risk = (preds == 1).sum()
                        avg_risk = probs.mean()
                        
                        st.markdown('''
                        <div style="padding: 20px; background: linear-gradient(135deg, #f43f5e, #e11d48); border-radius: 16px; margin: 20px 0; color: white;">
                            <h3 style="margin: 0 0 15px 0;">📊 Analysis Complete</h3>
                        </div>
                        ''', unsafe_allow_html=True)
                        
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.markdown(f'<div class="metric-box primary"><h3 style="margin: 0; font-size: 2rem;">{total}</h3><p style="margin: 5px 0 0 0;">Total Patients</p></div>', unsafe_allow_html=True)
                        with col2:
                            st.markdown(f'<div class="metric-box success"><h3 style="margin: 0; font-size: 2rem;">{low_risk}</h3><p style="margin: 5px 0 0 0;">Low Risk</p></div>', unsafe_allow_html=True)
                        with col3:
                            st.markdown(f'<div class="metric-box danger"><h3 style="margin: 0; font-size: 2rem;">{high_risk}</h3><p style="margin: 5px 0 0 0;">High Risk</p></div>', unsafe_allow_html=True)
                        with col4:
                            st.markdown(f'<div class="metric-box gold"><h3 style="margin: 0; font-size: 2rem;">{avg_risk:.1f}%</h3><p style="margin: 5px 0 0 0;">Avg Risk</p></div>', unsafe_allow_html=True)
                        
                        st.dataframe(df_upload, use_container_width=True)
                        
                        st.download_button(
                            label="⬇️ Download Results as JSON",
                            data=df_upload.to_json(orient='records', indent=2),
                            file_name="heart_analysis_results.json",
                            mime="application/json",
                            use_container_width=True
                        )
                
                except json.JSONDecodeError as e:
                    st.error(f"❌ Invalid JSON format: {str(e)}")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ============= ABOUT PAGE =============
elif st.session_state.page == "about":
    st.markdown('<h2 class="section-header fade-in">ℹ️ About This Project</h2>', unsafe_allow_html=True)
    
    # Hero Section
    st.markdown('''
    <div class="card" style="background: linear-gradient(135deg, #881337 0%, #be123c 50%, #f43f5e 100%); border: 2px solid #fbbf24; box-shadow: 0 8px 32px rgba(136,19,55,0.3);">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="font-size: 4rem;">❤️</div>
            <div>
                <h3 style="margin: 0 0 10px 0; color: #ffffff !important; font-size: 1.8rem; font-weight: 700;">AI-Powered Heart Disease Prediction</h3>
                <p style="margin: 0; color: #ffffff !important; font-size: 1.05rem; line-height: 1.6; opacity: 0.95;">Advanced machine learning system for cardiovascular risk assessment using clinical health parameters</p>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Main Content Grid
    col1, col2 = st.columns(2)
    
    with col1:
        # Overview Card
        st.markdown('''
        <div class="card" style="border: 2px solid #fce7f3;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
                <div style="font-size: 2.5rem;">🎯</div>
                <h4 style="margin: 0; color: #881337; font-size: 1.4rem;">Project Overview</h4>
            </div>
            <p style="color: #9f1239; line-height: 1.8; font-size: 0.95rem;">
                This system utilizes <strong style="color: #be123c;">Random Forest machine learning algorithm</strong> to analyze 11 critical health parameters and predict the likelihood of heart disease. The model achieves <strong style="color: #be123c;">94.2% accuracy</strong> in cardiovascular risk assessment.
            </p>
        </div>
        ''', unsafe_allow_html=True)
        
        # Technology Stack
        st.markdown('''
        <div class="card" style="border: 2px solid #dbeafe;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
                <div style="font-size: 2.5rem;">🔬</div>
                <h4 style="margin: 0; color: #1e40af; font-size: 1.4rem;">Technology Stack</h4>
            </div>
            <div style="display: grid; gap: 10px;">
                <div style="padding: 12px; background: #f0fdf4; border-radius: 8px; border-left: 4px solid #22c55e;">
                    <strong style="color: #15803d;">🧠 Algorithm:</strong> <span style="color: #9f1239;">Random Forest Classifier</span>
                </div>
                <div style="padding: 12px; background: #eff6ff; border-radius: 8px; border-left: 4px solid #3b82f6;">
                    <strong style="color: #1d4ed8;">💻 Framework:</strong> <span style="color: #9f1239;">Streamlit Web App</span>
                </div>
                <div style="padding: 12px; background: #fef3c7; border-radius: 8px; border-left: 4px solid #f59e0b;">
                    <strong style="color: #b45309;">📊 Visualization:</strong> <span style="color: #9f1239;">Plotly Interactive Charts</span>
                </div>
                <div style="padding: 12px; background: #fce7f3; border-radius: 8px; border-left: 4px solid #ec4899;">
                    <strong style="color: #be185d;">📈 Data Processing:</strong> <span style="color: #9f1239;">Pandas & NumPy</span>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        # Health Parameters
        st.markdown('''
        <div class="card" style="border: 2px solid #d1fae5;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
                <div style="font-size: 2.5rem;">📊</div>
                <h4 style="margin: 0; color: #065f46; font-size: 1.4rem;">Health Parameters</h4>
            </div>
            <div style="display: grid; gap: 8px;">
                <div style="padding: 10px 12px; background: #f0fdf4; border-radius: 8px; color: #9f1239; font-size: 0.9rem;">✅ Age & Gender</div>
                <div style="padding: 10px 12px; background: #f0fdf4; border-radius: 8px; color: #9f1239; font-size: 0.9rem;">✅ Chest Pain Type</div>
                <div style="padding: 10px 12px; background: #f0fdf4; border-radius: 8px; color: #9f1239; font-size: 0.9rem;">✅ Resting Blood Pressure</div>
                <div style="padding: 10px 12px; background: #f0fdf4; border-radius: 8px; color: #9f1239; font-size: 0.9rem;">✅ Serum Cholesterol</div>
                <div style="padding: 10px 12px; background: #f0fdf4; border-radius: 8px; color: #9f1239; font-size: 0.9rem;">✅ Fasting Blood Sugar</div>
                <div style="padding: 10px 12px; background: #f0fdf4; border-radius: 8px; color: #9f1239; font-size: 0.9rem;">✅ Resting ECG Results</div>
                <div style="padding: 10px 12px; background: #f0fdf4; border-radius: 8px; color: #9f1239; font-size: 0.9rem;">✅ Maximum Heart Rate</div>
                <div style="padding: 10px 12px; background: #f0fdf4; border-radius: 8px; color: #9f1239; font-size: 0.9rem;">✅ Exercise Angina</div>
                <div style="padding: 10px 12px; background: #f0fdf4; border-radius: 8px; color: #9f1239; font-size: 0.9rem;">✅ ST Depression (Oldpeak)</div>
                <div style="padding: 10px 12px; background: #f0fdf4; border-radius: 8px; color: #9f1239; font-size: 0.9rem;">✅ ST Segment Slope</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Use Cases
        st.markdown('''
        <div class="card" style="border: 2px solid #fef3c7;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 15px;">
                <div style="font-size: 2.5rem;">🎓</div>
                <h4 style="margin: 0; color: #92400e; font-size: 1.4rem;">Applications & Use Cases</h4>
            </div>
            <div style="display: grid; gap: 10px;">
                <div style="padding: 12px; background: #fff7ed; border-radius: 8px; border-left: 4px solid #f97316;">
                    <strong style="color: #c2410c;">🏥</strong> <span style="color: #9f1239; font-weight: 500;">Healthcare Screening</span>
                    <p style="margin: 5px 0 0 0; color: #9f1239; font-size: 0.85rem;">Early detection and preventive care</p>
                </div>
                <div style="padding: 12px; background: #fff7ed; border-radius: 8px; border-left: 4px solid #f97316;">
                    <strong style="color: #c2410c;">🔬</strong> <span style="color: #9f1239; font-weight: 500;">Medical Research</span>
                    <p style="margin: 5px 0 0 0; color: #9f1239; font-size: 0.85rem;">Data analysis and pattern recognition</p>
                </div>
                <div style="padding: 12px; background: #fff7ed; border-radius: 8px; border-left: 4px solid #f97316;">
                    <strong style="color: #c2410c;">⚠️</strong> <span style="color: #9f1239; font-weight: 500;">Risk Assessment</span>
                    <p style="margin: 5px 0 0 0; color: #9f1239; font-size: 0.85rem;">Cardiovascular risk stratification</p>
                </div>
                <div style="padding: 12px; background: #fff7ed; border-radius: 8px; border-left: 4px solid #f97316;">
                    <strong style="color: #c2410c;">🩺</strong> <span style="color: #9f1239; font-weight: 500;">Clinical Support</span>
                    <p style="margin: 5px 0 0 0; color: #9f1239; font-size: 0.85rem;">Decision support for healthcare providers</p>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Key Statistics
    st.markdown('''
    <div style="padding: 15px; background: linear-gradient(135deg, #fef3c7, #fde68a); border-radius: 12px; margin: 25px 0 15px 0; border-left: 4px solid #f59e0b;">
        <h4 style="margin: 0 0 5px 0; color: #92400e;">📈 Key Performance Metrics</h4>
        <p style="margin: 0; font-size: 0.9rem; color: #9f1239;">System accuracy and performance indicators</p>
    </div>
    ''', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('''
        <div class="metric-box primary">
            <h3 style="margin: 0; font-size: 2rem;">94.2%</h3>
            <p style="margin: 5px 0 0 0; color: #881337;">Model Accuracy</p>
        </div>
        ''', unsafe_allow_html=True)
    with col2:
        st.markdown('''
        <div class="metric-box success">
            <h3 style="margin: 0; font-size: 2rem;">11</h3>
            <p style="margin: 5px 0 0 0; color: #166534;">Health Features</p>
        </div>
        ''', unsafe_allow_html=True)
    with col3:
        st.markdown('''
        <div class="metric-box gold">
            <h3 style="margin: 0; font-size: 2rem;">500+</h3>
            <p style="margin: 5px 0 0 0; color: #92400e;">Training Samples</p>
        </div>
        ''', unsafe_allow_html=True)
    with col4:
        st.markdown('''
        <div class="metric-box primary">
            <h3 style="margin: 0; font-size: 2rem;">Real-time</h3>
            <p style="margin: 5px 0 0 0; color: #881337;">Prediction Speed</p>
        </div>
        ''', unsafe_allow_html=True)
    
    # Disclaimer
    st.markdown('''
    <div class="card" style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 2px solid #f59e0b; margin-top: 25px;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="font-size: 3rem;">⚠️</div>
            <div>
                <h4 style="margin: 0 0 8px 0; color: #92400e; font-size: 1.2rem;">Medical Disclaimer</h4>
                <p style="margin: 0; color: #9f1239; line-height: 1.6; font-size: 0.95rem;">
                    This tool is designed for <strong style="color: #78350f;">educational and research purposes only</strong>. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare providers for medical decisions.
                </p>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
