import streamlit as st
import requests
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
import base64
from io import StringIO
import warnings
warnings.filterwarnings('ignore')

# Load the model and preprocessor
@st.cache_resource
def load_model():
    try:
        with open('random_forest_model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except:
        return None

@st.cache_resource
def load_preprocessor():
    try:
        with open('preprocessor.pkl', 'rb') as f:
            preprocessor = pickle.load(f)
        return preprocessor
    except:
        return None

model = load_model()
preprocessor = load_preprocessor()

# Page config
st.set_page_config(
    page_title="Heart Disease AI",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

[data-testid="stHeader"] {
    background: rgba(255, 255, 255, 0);
}

.main-card {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    margin-bottom: 1.5rem;
}

.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1.5rem;
    border-radius: 15px;
    text-align: center;
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    transition: transform 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
}

.section-title {
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1.5rem;
}

.info-box {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
    border-left: 4px solid #667eea;
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
}

.success-gradient {
    background: linear-gradient(135deg, #11998e, #38ef7d);
    padding: 1.5rem;
    border-radius: 15px;
    color: white;
    text-align: center;
}

.danger-gradient {
    background: linear-gradient(135deg, #eb3349, #f45c43);
    padding: 1.5rem;
    border-radius: 15px;
    color: white;
    text-align: center;
}

.stButton>button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 12px;
    padding: 0.75rem 2rem;
    font-size: 1rem;
    font-weight: 600;
    border: none;
    transition: all 0.3s ease;
}

/* Top Navigation Bar */
[data-testid="stSidebar"] {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 80px !important;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%) !important;
    z-index: 999;
    padding: 0 2rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

[data-testid="stSidebarContent"] {
    display: flex;
    flex-direction: row !important;
    align-items: center;
    justify-content: space-between;
    height: 80px;
    padding-top: 0 !important;
}

[data-testid="stSidebar"] .stRadio {
    display: flex;
    flex-direction: row !important;
    gap: 1rem;
}

[data-testid="stSidebar"] label {
    color: white !important;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    transition: all 0.3s ease;
    margin: 0;
}

[data-testid="stSidebar"] label:hover {
    background: rgba(102, 126, 234, 0.3);
    transform: translateY(-2px);
}

/* Hide default sidebar toggle */
button[kind="header"] {
    display: none;
}

/* Adjust main content for top navbar */
.main .block-container {
    margin-top: 100px !important;
    padding-top: 2rem;
}

/* Sidebar heading */
[data-testid="stSidebar"] h2 {
    font-size: 1.5rem !important;
    margin: 0;
}

[data-testid="stSidebar"] p {
    display: none;
}

/* Navigation items horizontal */
[data-testid="stSidebar"] > div {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 0.5rem;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
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
            <div style="font-size: 2rem;">❤️</div>
            <div>
                <h2 style="color: #2d3748; margin: 0; font-size: 1.6rem; font-weight: 700;">Heart Disease Prediction</h2>
                <p style="color: #718096; margin: 0.25rem 0 0 0; font-size: 0.85rem;">AI-Powered Cardiovascular Risk Assessment</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Page Navigation using session state
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Overview"

def set_page(page):
    st.session_state.page = page

# Create navigation buttons
col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 2])

with col1:
    if st.button("🏠 Overview", use_container_width=True, type="primary" if st.session_state.page == "🏠 Overview" else "secondary"):
        set_page("🏠 Overview")

with col2:
    if st.button("🔍 Prediction", use_container_width=True, type="primary" if st.session_state.page == "🔍 Single Prediction" else "secondary"):
        set_page("🔍 Single Prediction")

with col3:
    if st.button("📊 EDA", use_container_width=True, type="primary" if st.session_state.page == "📊 EDA & Analytics" else "secondary"):
        set_page("📊 EDA & Analytics")

with col4:
    if st.button("📁 Bulk Scanner", use_container_width=True, type="primary" if st.session_state.page == "📁 Bulk Scanner" else "secondary"):
        set_page("📁 Bulk Scanner")

with col5:
    if st.button("ℹ️ About", use_container_width=True, type="primary" if st.session_state.page == "ℹ️ About" else "secondary"):
        set_page("ℹ️ About")

st.markdown("<hr style='margin: 1rem 0 2rem 0; border: none; border-top: 2px solid rgba(102, 126, 234, 0.3);'>", unsafe_allow_html=True)

# Get current page
page = st.session_state.page

# ============= OVERVIEW PAGE =============
if page == "🏠 Overview":
    st.markdown('<h1 class="section-title" style="text-align: center; color: white;">❤️ Heart Disease Prediction System</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-size: 1.1rem; margin-bottom: 2rem;'>AI-Powered Cardiovascular Risk Assessment & Analytics Platform</p>", unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    disease_count = int(df_sample['HeartDisease'].sum())
    normal_count = len(df_sample) - disease_count
    disease_rate = (disease_count / len(df_sample)) * 100
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style='margin: 0; font-size: 2.5rem;'>{len(df_sample):,}</h3>
            <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem;'>Total Samples</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style='background: linear-gradient(135deg, #11998e, #38ef7d);'>
            <h3 style='margin: 0; font-size: 2.5rem;'>{normal_count:,}</h3>
            <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem;'>Normal Cases</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card" style='background: linear-gradient(135deg, #eb3349, #f45c43);'>
            <h3 style='margin: 0; font-size: 2.5rem;'>{disease_count:,}</h3>
            <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem;'>Disease Cases</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card" style='background: linear-gradient(135deg, #f093fb, #f5576c);'>
            <h3 style='margin: 0; font-size: 2.5rem;'>{disease_rate:.1f}%</h3>
            <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem;'>Disease Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main Features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="main-card">
            <h3 style='color: #667eea;'>🎯 Project Highlights</h3>
            <ul style='line-height: 2; color: #333;'>
                <li><strong>Machine Learning:</strong> Random Forest Classifier</li>
                <li><strong>Accuracy:</strong> High-performance predictive model</li>
                <li><strong>Features:</strong> 11 clinical parameters analyzed</li>
                <li><strong>Real-time:</strong> Instant predictions & analytics</li>
                <li><strong>Bulk Processing:</strong> CSV, Excel, JSON support</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="main-card">
            <h3 style='color: #667eea;'>📊 Analytics Features</h3>
            <ul style='line-height: 2; color: #333;'>
                <li><strong>Interactive Visualizations:</strong> Plotly & Matplotlib</li>
                <li><strong>Correlation Analysis:</strong> Feature relationships</li>
                <li><strong>Risk Factor Analysis:</strong> Age, gender, symptoms</li>
                <li><strong>Distribution Charts:</strong> Medical parameters</li>
                <li><strong>Statistical Insights:</strong> Data-driven patterns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown("<h3 class='section-title' style='color: white; text-align: center; margin-top: 2rem;'>📈 Quick Statistics</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fig = px.pie(
            names=['Normal', 'Heart Disease'],
            values=[normal_count, disease_count],
            color=['Normal', 'Heart Disease'],
            color_discrete_map={'Normal': '#38ef7d', 'Heart Disease': '#f45c43'},
            hole=0.6
        )
        fig.update_layout(
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', size=14)
        )
        fig.update_annotations(font_color='white')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        age_stats = df_sample.groupby('HeartDisease')['Age'].mean()
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Normal', 'Heart Disease'],
            y=[age_stats[0], age_stats[1]],
            marker_color=['#38ef7d', '#f45c43'],
            text=[f'{age_stats[0]:.1f}', f'{age_stats[1]:.1f}'],
            textposition='auto'
        ))
        fig.update_layout(
            title='Average Age by Condition',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=350
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        gender_stats = df_sample.groupby(['Sex', 'HeartDisease']).size().reset_index(name='count')
        fig = px.bar(
            gender_stats,
            x='Sex',
            y='count',
            color='HeartDisease',
            barmode='group',
            color_discrete_map={0: '#38ef7d', 1: '#f45c43'},
            labels={'count': 'Count', 'Sex': 'Gender', 'HeartDisease': 'Condition'}
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=350
        )
        st.plotly_chart(fig, use_container_width=True)

# ============= SINGLE PREDICTION PAGE =============
elif page == "🔍 Single Prediction":
    st.markdown('<h1 class="section-title" style="text-align: center; color: white;">🔍 Single Patient Prediction</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; margin-bottom: 2rem;'>Enter patient details for instant AI-powered heart disease risk assessment</p>", unsafe_allow_html=True)
    
    # Prediction form
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("<h4 style='color: #667eea;'>👤 Demographics</h4>", unsafe_allow_html=True)
            Age = st.number_input("Age (years)", min_value=1, max_value=120, value=30)
            Sex = st.selectbox("Sex", ["M", "F"])
            ChestPainType = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("<h4 style='color: #667eea;'>🩺 Vitals</h4>", unsafe_allow_html=True)
            RestingBP = st.number_input("Resting BP (mm Hg)", min_value=0, max_value=250, value=120)
            Cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
            FastingBS = st.selectbox("Fasting BS > 120 mg/dl", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("<h4 style='color: #667eea;'>💓 Cardiac Metrics</h4>", unsafe_allow_html=True)
            RestingECG = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
            MaxHR = st.number_input("Max Heart Rate", min_value=60, max_value=220, value=150)
            ExerciseAngina = st.selectbox("Exercise Angina", ["Y", "N"], format_func=lambda x: "Yes" if x == "Y" else "No")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("<h4 style='color: #667eea;'>📊 Test Results</h4>", unsafe_allow_html=True)
            Oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
            ST_Slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])
            st.markdown("</div>", unsafe_allow_html=True)
        
        submitted = st.form_submit_button("🔮 Predict Now", use_container_width=True)
    
    if submitted:
        if model is None:
            st.error("❌ Model not found. Please train the model first.")
        else:
            input_data = {
                "Age": int(Age),
                "Sex": Sex,
                "ChestPainType": ChestPainType,
                "RestingBP": int(RestingBP),
                "Cholesterol": int(Cholesterol),
                "FastingBS": int(FastingBS),
                "RestingECG": RestingECG,
                "MaxHR": int(MaxHR),
                "ExerciseAngina": ExerciseAngina,
                "Oldpeak": float(Oldpeak),
                "ST_Slope": ST_Slope
            }
            
            try:
                input_df = pd.DataFrame([input_data])
                prediction = model.predict(input_df)[0]
                prediction_proba = model.predict_proba(input_df)[0]
                
                # Display results
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if prediction == 1:
                        st.markdown(f"""
                        <div class="danger-gradient">
                            <h2 style='margin: 0;'>⚠️ High Risk</h2>
                            <p style='margin: 0.5rem 0 0 0;'>Heart Disease Detected</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="success-gradient">
                            <h2 style='margin: 0;'>✅ Low Risk</h2>
                            <p style='margin: 0.5rem 0 0 0;'>No Heart Disease</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                with col2:
                    risk_pct = prediction_proba[1] * 100
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3 style='margin: 0; font-size: 2rem;'>{risk_pct:.1f}%</h3>
                        <p style='margin: 0.5rem 0 0 0;'>Risk Probability</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    confidence = max(prediction_proba) * 100
                    st.markdown(f"""
                    <div class="metric-card" style='background: linear-gradient(135deg, #f093fb, #f5576c);'>
                        <h3 style='margin: 0; font-size: 2rem;'>{confidence:.1f}%</h3>
                        <p style='margin: 0.5rem 0 0 0;'>Model Confidence</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Risk factors
                if prediction == 1:
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("<h3 style='color: #eb3349;'>📋 Risk Factors Detected:</h3>", unsafe_allow_html=True)
                    
                    risk_factors = []
                    if Age > 50: risk_factors.append("• Age > 50 years")
                    if Sex == 'M': risk_factors.append("• Male gender")
                    if ChestPainType in ['ASY', 'TA']: risk_factors.append(f"• {ChestPainType} chest pain type")
                    if RestingBP > 140: risk_factors.append("• High blood pressure (>140)")
                    if Cholesterol > 240: risk_factors.append("• High cholesterol (>240)")
                    if ExerciseAngina == 'Y': risk_factors.append("• Exercise-induced angina")
                    if Oldpeak > 2: risk_factors.append("• High ST depression (>2)")
                    
                    for factor in risk_factors:
                        st.warning(factor)
                    
                    st.error("⚠️ **Recommendation:** Please consult with a cardiologist for comprehensive evaluation.")
                else:
                    st.success("✅ **Good News!** No significant signs of heart disease detected. Continue maintaining a healthy lifestyle!")
                    
            except Exception as e:
                st.error(f"❌ Prediction error: {e}")

# ============= EDA & ANALYTICS PAGE =============
elif page == "📊 EDA & Analytics":
    st.markdown('<h1 class="section-title" style="text-align: center; color: white;">📊 Exploratory Data Analysis</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; margin-bottom: 2rem;'>Comprehensive statistical analysis and visualizations</p>", unsafe_allow_html=True)
    
    # Summary Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Samples", f"{len(df_sample):,}")
    with col2:
        st.metric("Features", "11")
    with col3:
        st.metric("Disease Cases", f"{int(df_sample['HeartDisease'].sum()):,}")
    with col4:
        st.metric("Disease Rate", f"{(df_sample['HeartDisease'].mean()*100):.1f}%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Visualization Selection
    viz_type = st.selectbox(
        "Select Visualization:",
        ["📊 Distribution Analysis", "🔥 Correlation Heatmap", "📈 Feature Importance", 
         "⚠️ Risk Factor Analysis", "👥 Age & Gender Analysis", "🏥 Medical Parameters"],
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    sns.set_style("whitegrid")
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    
    if viz_type == "📊 Distribution Analysis":
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.pie(
                df_sample['HeartDisease'].value_counts().reset_index(),
                values='count',
                names='HeartDisease',
                title='Target Variable Distribution',
                color='HeartDisease',
                color_discrete_map={0: '#38ef7d', 1: '#f45c43'},
                hole=0.5
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.histogram(
                df_sample,
                x='Age',
                color='HeartDisease',
                title='Age Distribution by Condition',
                color_discrete_map={0: '#38ef7d', 1: '#f45c43'},
                barmode='overlay',
                opacity=0.7
            )
            fig.update_layout(showlegend=True)
            st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "🔥 Correlation Heatmap":
        df_numeric = df_sample.copy()
        for col in ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']:
            df_numeric[col] = df_numeric[col].astype('category').cat.codes
        
        corr_matrix = df_numeric.corr()
        
        fig = px.imshow(
            corr_matrix,
            text_auto=True,
            aspect="auto",
            color_continuous_scale='RdBu_r',
            title='Feature Correlation Matrix'
        )
        fig.update_layout(height=700)
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "📈 Feature Importance":
        if model:
            try:
                feature_names = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']
                cat_features = preprocessor.transformers_[1][2]
                if hasattr(cat_features, 'get_feature_names_out'):
                    cat_feature_names = cat_features.get_feature_names_out(['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope'])
                    all_features = feature_names + list(cat_feature_names)
                else:
                    all_features = feature_names + ['Sex_M', 'ChestPainType_ATA', 'ChestPainType_NAP', 
                                                   'ChestPainType_ASY', 'RestingECG_Normal', 
                                                   'RestingECG_ST', 'ExerciseAngina_Y', 'ST_Slope_Up', 'ST_Slope_Flat']
                
                rf_model = model.named_steps['classifier']
                importances = rf_model.feature_importances_
                
                importance_df = pd.DataFrame({
                    'Feature': all_features[:len(importances)],
                    'Importance': importances
                }).sort_values('Importance', ascending=True).tail(15)
                
                fig = px.bar(
                    importance_df,
                    x='Importance',
                    y='Feature',
                    orientation='h',
                    title='Top 15 Feature Importance',
                    color='Importance',
                    color_continuous_scale='Viridis'
                )
                fig.update_layout(height=600)
                st.plotly_chart(fig, use_container_width=True)
            except:
                st.warning("Feature importance not available")
    
    elif viz_type == "⚠️ Risk Factor Analysis":
        df_temp = df_sample.copy()
        df_temp['AgeGroup'] = pd.cut(df_temp['Age'], bins=[0, 35, 45, 55, 65, 100], 
                                     labels=['<35', '35-45', '45-55', '55-65', '65+'])
        
        col1, col2 = st.columns(2)
        
        with col1:
            age_disease = df_temp.groupby('AgeGroup')['HeartDisease'].mean() * 100
            fig = px.bar(
                x=age_disease.index.astype(str),
                y=age_disease.values,
                title='Disease Rate by Age Group',
                labels={'x': 'Age Group', 'y': 'Disease Rate (%)'},
                color=age_disease.values,
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            chest_pain = df_temp[df_temp['HeartDisease']==1]['ChestPainType'].value_counts()
            fig = px.pie(
                values=chest_pain.values,
                names=chest_pain.index,
                title='Chest Pain Type Distribution (Disease Cases)',
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "👥 Age & Gender Analysis":
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.box(
                df_sample,
                x='HeartDisease',
                y='Age',
                color='HeartDisease',
                title='Age Distribution by Condition',
                color_discrete_map={0: '#38ef7d', 1: '#f45c43'},
                points='all'
            )
            fig.update_xaxes(ticktext=['Normal', 'Disease'], tickvals=[0, 1])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            gender_disease = df_sample.groupby(['Sex', 'HeartDisease']).size().reset_index(name='count')
            fig = px.bar(
                gender_disease,
                x='Sex',
                y='count',
                color='HeartDisease',
                barmode='group',
                title='Gender Distribution',
                color_discrete_map={0: '#38ef7d', 1: '#f45c43'}
            )
            st.plotly_chart(fig, use_container_width=True)
    
    elif viz_type == "🏥 Medical Parameters":
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.box(
                df_sample,
                x='HeartDisease',
                y='RestingBP',
                color='HeartDisease',
                title='Resting Blood Pressure',
                color_discrete_map={0: '#38ef7d', 1: '#f45c43'}
            )
            fig.update_xaxes(ticktext=['Normal', 'Disease'], tickvals=[0, 1])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.box(
                df_sample,
                x='HeartDisease',
                y='Cholesterol',
                color='HeartDisease',
                title='Cholesterol Levels',
                color_discrete_map={0: '#38ef7d', 1: '#f45c43'}
            )
            fig.update_xaxes(ticktext=['Normal', 'Disease'], tickvals=[0, 1])
            st.plotly_chart(fig, use_container_width=True)

# ============= BULK SCANNER PAGE =============
elif page == "📁 Bulk Scanner":
    st.markdown('<h1 class="section-title" style="text-align: center; color: white;">📁 Bulk Prediction Scanner</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; margin-bottom: 2rem;'>Upload multiple patient records for batch processing</p>", unsafe_allow_html=True)
    
    # File format tabs
    tab1, tab2, tab3 = st.tabs(["📄 CSV Upload", "📊 Excel Upload", "📋 JSON Upload"])
    
    with tab1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.header("📄 Upload CSV File")
        
        # Sample download
        st.download_button(
            label="📥 Download Sample CSV",
            data=df_sample.drop('HeartDisease', axis=1).to_csv(index=False),
            file_name="sample_heart_data.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'], key="csv_uploader")
        
        if uploaded_file is not None:
            try:
                df_upload = pd.read_csv(uploaded_file)
                st.success(f"✅ Successfully loaded {len(df_upload)} records")
                
                # Show preview
                st.subheader("📊 Data Preview")
                st.dataframe(df_upload.head(10), use_container_width=True)
                
                if st.button("🔮 Predict All Records", use_container_width=True, type="primary"):
                    if model:
                        predictions = model.predict(df_upload)
                        probabilities = model.predict_proba(df_upload)[:, 1]
                        
                        df_upload['Prediction'] = predictions
                        df_upload['Risk_Probability'] = (probabilities * 100).round(2)
                        df_upload['Status'] = df_upload['Prediction'].map({0: 'Low Risk', 1: 'High Risk'})
                        
                        # Results summary
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Total Processed", len(df_upload))
                        with col2:
                            st.metric("Low Risk", (df_upload['Prediction']==0).sum())
                        with col3:
                            st.metric("High Risk", (df_upload['Prediction']==1).sum())
                        
                        st.dataframe(df_upload, use_container_width=True)
                        
                        # Download results
                        csv_results = df_upload.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Results",
                            data=csv_results,
                            file_name="prediction_results.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                    else:
                        st.error("❌ Model not found")
            except Exception as e:
                st.error(f"❌ Error reading CSV: {e}")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.header("📊 Upload Excel File")
        
        # Sample download
        from io import BytesIO
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_sample.drop('HeartDisease', axis=1).to_excel(writer, index=False, sheet_name='Sample Data')
        
        st.download_button(
            label="📥 Download Sample Excel",
            data=output.getvalue(),
            file_name="sample_heart_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
        
        uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx', 'xls'], key="excel_uploader")
        
        if uploaded_file is not None:
            try:
                df_upload = pd.read_excel(uploaded_file)
                st.success(f"✅ Successfully loaded {len(df_upload)} records")
                
                st.subheader("📊 Data Preview")
                st.dataframe(df_upload.head(10), use_container_width=True)
                
                if st.button("🔮 Predict All Records", use_container_width=True, type="primary", key="excel_predict"):
                    if model:
                        predictions = model.predict(df_upload)
                        probabilities = model.predict_proba(df_upload)[:, 1]
                        
                        df_upload['Prediction'] = predictions
                        df_upload['Risk_Probability'] = (probabilities * 100).round(2)
                        df_upload['Status'] = df_upload['Prediction'].map({0: 'Low Risk', 1: 'High Risk'})
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Total Processed", len(df_upload))
                        with col2:
                            st.metric("Low Risk", (df_upload['Prediction']==0).sum())
                        with col3:
                            st.metric("High Risk", (df_upload['Prediction']==1).sum())
                        
                        st.dataframe(df_upload, use_container_width=True)
                        
                        output = BytesIO()
                        with pd.ExcelWriter(output, engine='openpyxl') as writer:
                            df_upload.to_excel(writer, index=False, sheet_name='Predictions')
                        
                        st.download_button(
                            label="📥 Download Results",
                            data=output.getvalue(),
                            file_name="prediction_results.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True
                        )
                    else:
                        st.error("❌ Model not found")
            except Exception as e:
                st.error(f"❌ Error reading Excel: {e}")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.header("📋 Upload JSON File")
        
        # Sample download
        json_sample = df_sample.drop('HeartDisease', axis=1).to_dict(orient='records')
        st.download_button(
            label="📥 Download Sample JSON",
            data=json.dumps(json_sample, indent=2),
            file_name="sample_heart_data.json",
            mime="application/json",
            use_container_width=True
        )
        
        uploaded_file = st.file_uploader("Choose a JSON file", type=['json'], key="json_uploader")
        
        if uploaded_file is not None:
            try:
                json_data = json.load(uploaded_file)
                df_upload = pd.DataFrame(json_data)
                st.success(f"✅ Successfully loaded {len(df_upload)} records")
                
                st.subheader("📊 Data Preview")
                st.dataframe(df_upload.head(10), use_container_width=True)
                
                if st.button("🔮 Predict All Records", use_container_width=True, type="primary", key="json_predict"):
                    if model:
                        predictions = model.predict(df_upload)
                        probabilities = model.predict_proba(df_upload)[:, 1]
                        
                        df_upload['Prediction'] = predictions
                        df_upload['Risk_Probability'] = (probabilities * 100).round(2)
                        df_upload['Status'] = df_upload['Prediction'].map({0: 'Low Risk', 1: 'High Risk'})
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Total Processed", len(df_upload))
                        with col2:
                            st.metric("Low Risk", (df_upload['Prediction']==0).sum())
                        with col3:
                            st.metric("High Risk", (df_upload['Prediction']==1).sum())
                        
                        st.dataframe(df_upload, use_container_width=True)
                        
                        json_results = df_upload.to_dict(orient='records')
                        st.download_button(
                            label="📥 Download Results",
                            data=json.dumps(json_results, indent=2),
                            file_name="prediction_results.json",
                            mime="application/json",
                            use_container_width=True
                        )
                    else:
                        st.error("❌ Model not found")
            except Exception as e:
                st.error(f"❌ Error reading JSON: {e}")
        
        st.markdown("</div>", unsafe_allow_html=True)

# ============= ABOUT PAGE =============
elif page == "ℹ️ About":
    st.markdown('<h1 class="section-title" style="text-align: center; color: white;">ℹ️ About This Project</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="main-card">
            <h3 style='color: #667eea;'>🎯 Project Overview</h3>
            <p style='color: #555; line-height: 1.8;'>
                This AI-powered Heart Disease Prediction system leverages advanced machine learning 
                algorithms to assess cardiovascular risk based on clinical parameters. Built for 
                healthcare professionals and researchers, it provides instant, data-driven insights 
                to support medical decision-making.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="main-card">
            <h3 style='color: #667eea;'>🔬 Technology Stack</h3>
            <ul style='line-height: 2.2; color: #555;'>
                <li><strong>ML Algorithm:</strong> Random Forest Classifier</li>
                <li><strong>Frontend:</strong> Streamlit Framework</li>
                <li><strong>Data Processing:</strong> Pandas, NumPy</li>
                <li><strong>Visualization:</strong> Plotly, Matplotlib, Seaborn</li>
                <li><strong>Model Serialization:</strong> Pickle</li>
                <li><strong>Preprocessing:</strong> Scikit-learn Pipeline</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="main-card">
            <h3 style='color: #667eea;'>📊 Features Analyzed</h3>
            <ul style='line-height: 2.2; color: #555;'>
                <li><strong>Demographics:</strong> Age, Sex</li>
                <li><strong>Symptoms:</strong> Chest Pain Type (ATA, NAP, ASY, TA)</li>
                <li><strong>Vitals:</strong> Resting BP, Cholesterol, Max Heart Rate</li>
                <li><strong>Test Results:</strong> Fasting Blood Sugar, Resting ECG</li>
                <li><strong>ECG Metrics:</strong> Oldpeak (ST depression), ST Slope</li>
                <li><strong>Exercise Response:</strong> Exercise Induced Angina</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="main-card">
            <h3 style='color: #667eea;'>🎓 Use Cases</h3>
            <ul style='line-height: 2.2; color: #555;'>
                <li>Healthcare screening programs</li>
                <li>Medical research & analytics</li>
                <li>Patient risk assessment</li>
                <li>Clinical decision support</li>
                <li>Academic presentations</li>
                <li>Population health studies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Model Performance
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="main-card">
        <h3 style='color: #667eea; text-align: center;'>📈 Model Architecture</h3>
        <div style='display: flex; justify-content: space-around; margin-top: 2rem;'>
            <div style='text-align: center;'>
                <h2 style='color: #667eea; margin: 0;'>Random Forest</h2>
                <p style='color: #888;'>Ensemble Learning</p>
            </div>
            <div style='text-align: center;'>
                <h2 style='color: #667eea; margin: 0;'>100</h2>
                <p style='color: #888;'>Estimators</p>
            </div>
            <div style='text-align: center;'>
                <h2 style='color: #667eea; margin: 0;'>11</h2>
                <p style='color: #888;'>Features</p>
            </div>
            <div style='text-align: center;'>
                <h2 style='color: #667eea; margin: 0;'>Pipeline</h2>
                <p style='color: #888;'>Preprocessing + ML</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Important Note
    st.markdown("""
    <div class="info-box">
        <h4 style='color: #667eea; margin-top: 0;'>⚠️ Medical Disclaimer</h4>
        <p style='color: #555; line-height: 1.8;'>
            This tool is designed for <strong>educational and research purposes only</strong>. 
            All predictions should be validated by qualified medical professionals. 
            Do not use this system as a sole basis for medical diagnosis or treatment decisions.
            Always consult with healthcare providers for proper medical evaluation.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Developer Info
    st.markdown("""
    <div class="main-card" style='text-align: center;'>
        <h3 style='color: #667eea;'>👨‍💻 Built With ❤️</h3>
        <p style='color: #888; font-size: 1.1rem;'>
            Heart Disease Prediction System v2.0<br>
            <em>Advanced Machine Learning for Healthcare</em>
        </p>
    </div>
    """, unsafe_allow_html=True)
