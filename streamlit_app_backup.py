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

# Clean Professional Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Inter', sans-serif !important;
}

/* Clean White Background */
[data-testid="stAppViewContainer"] {
    background: #f5f7fa;
}

/* Main Container */
.main .block-container {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    margin-top: 1.5rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

/* Top Navbar */
.navbar {
    background: white;
    padding: 1.25rem 2rem;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    border-bottom: 1px solid #e2e8f0;
}

/* Navigation Buttons */
.nav-button {
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    border: 2px solid #e2e8f0;
    background: white;
    color: #4a5568;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
}

.nav-button:hover {
    border-color: #4299e1;
    color: #4299e1;
    transform: translateY(-2px);
}

.nav-button.active {
    background: #4299e1;
    border-color: #4299e1;
    color: white;
}

/* Metric Cards */
.metric-box {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.metric-box.primary {
    background: linear-gradient(135deg, #4299e1, #3182ce);
    color: white;
    border: none;
}

.metric-box.success {
    background: linear-gradient(135deg, #48bb78, #38a169);
    color: white;
    border: none;
}

.metric-box.danger {
    background: linear-gradient(135deg, #f56565, #e53e3e);
    color: white;
    border: none;
}

.metric-box.info {
    background: linear-gradient(135deg, #ed8936, #dd6b20);
    color: white;
    border: none;
}

/* Section Headers */
.section-header {
    font-size: 1.75rem;
    font-weight: 700;
    color: #2d3748;
    margin-bottom: 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 3px solid #4299e1;
}

/* Content Cards */
.card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

/* Info Alert */
.alert-info {
    background: #ebf8ff;
    border-left: 4px solid #4299e1;
    padding: 1rem 1.25rem;
    border-radius: 8px;
    margin: 1rem 0;
}

.alert-success {
    background: #f0fff4;
    border-left: 4px solid #48bb78;
    padding: 1rem 1.25rem;
    border-radius: 8px;
    margin: 1rem 0;
}

.alert-warning {
    background: #fffaf0;
    border-left: 4px solid #ed8936;
    padding: 1rem 1.25rem;
    border-radius: 8px;
    margin: 1rem 0;
}

.alert-danger {
    background: #fff5f5;
    border-left: 4px solid #f56565;
    padding: 1rem 1.25rem;
    border-radius: 8px;
    margin: 1rem 0;
}

/* Buttons */
.stButton>button {
    background: #4299e1;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.65rem 1.5rem;
    font-weight: 600;
    transition: all 0.2s;
}

.stButton>button:hover {
    background: #3182ce;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(66, 153, 225, 0.3);
}

/* Form Elements */
input, select {
    border: 2px solid #e2e8f0 !important;
    border-radius: 8px !important;
    transition: all 0.2s !important;
}

input:focus, select:focus {
    border-color: #4299e1 !important;
    box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.1) !important;
}

label {
    color: #4a5568 !important;
    font-weight: 600 !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-weight: 600;
}

/* Hide Streamlit Elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

[data-testid="stHeader"] {
    background: transparent;
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
        <div style="display: flex; align-items: center; gap: 0.75rem;">
            <div style="font-size: 1.75rem;">❤️</div>
            <div>
                <h1 style="color: #2d3748; margin: 0; font-size: 1.4rem; font-weight: 700;">Heart Disease Prediction System</h1>
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

st.markdown("<hr style='margin: 1.5rem 0; border: none; border-top: 2px solid #e2e8f0;'>", unsafe_allow_html=True)

# ============= OVERVIEW PAGE =============
if st.session_state.page == "overview":
    st.markdown('<h2 class="section-header">📊 Dashboard Overview</h2>', unsafe_allow_html=True)
    
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
        <div class="metric-box info">
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
            color_discrete_map={'Normal': '#48bb78', 'Heart Disease': '#f56565'},
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
            color_discrete_map={'Normal': '#48bb78', 'Heart Disease': '#f56565'},
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
    st.markdown('<h2 class="section-header">🔍 Heart Disease Prediction</h2>', unsafe_allow_html=True)
    
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("#### 👤 Patient Information")
            Age = st.number_input("Age", min_value=1, max_value=120, value=30)
            Sex = st.selectbox("Sex", ["M", "F"])
            ChestPainType = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("#### 🩺 Medical Vitals")
            RestingBP = st.number_input("Resting BP (mm Hg)", min_value=0, max_value=250, value=120)
            Cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
            FastingBS = st.selectbox("Fasting BS > 120 mg/dl", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("#### 💓 Cardiac Metrics")
            RestingECG = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
            MaxHR = st.number_input("Max Heart Rate", min_value=60, max_value=220, value=150)
            ExerciseAngina = st.selectbox("Exercise Angina", ["Y", "N"], format_func=lambda x: "Yes" if x == "Y" else "No")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("#### 📊 Test Results")
            Oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
            ST_Slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])
            st.markdown('</div>', unsafe_allow_html=True)
        
        submitted = st.form_submit_button("🔮 Predict Now", use_container_width=True)
    
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
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if prediction == 0:
                    st.markdown(f'<div class="metric-box success"><h2 style="margin:0">✅</h2><p>Low Risk</p></div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="metric-box danger"><h2 style="margin:0">⚠️</h2><p>High Risk</p></div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="metric-box primary"><h2 style="margin:0">{proba:.1f}%</h2><p>Risk Level</p></div>', unsafe_allow_html=True)
            with col3:
                st.markdown(f'<div class="metric-box info"><h2 style="margin:0">{100-proba:.1f}%</h2><p>Confidence</p></div>', unsafe_allow_html=True)
            
            if prediction == 0:
                st.markdown('<div class="alert-success">✅ **Good News:** No significant heart disease detected. Maintain a healthy lifestyle!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="alert-danger">⚠️ **Warning:** High risk detected. Please consult a cardiologist immediately.</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")

# ============= EDA PAGE =============
elif st.session_state.page == "eda":
    st.markdown('<h2 class="section-header">📊 Exploratory Data Analysis</h2>', unsafe_allow_html=True)
    
    viz_option = st.selectbox(
        "Select Visualization:",
        ["Distribution", "Correlation", "Age Analysis", "Gender Analysis", "Medical Parameters"],
        label_visibility="collapsed"
    )
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    if viz_option == "Distribution":
        fig = px.histogram(df_sample, x='Age', color='HeartDisease', 
                          color_discrete_map={0: '#48bb78', 1: '#f56565'},
                          title='Age Distribution by Condition')
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_option == "Correlation":
        df_num = df_sample.copy()
        for col in ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']:
            df_num[col] = df_num[col].astype('category').cat.codes
        corr = df_num.corr()
        fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r')
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_option == "Age Analysis":
        df_temp = df_sample.copy()
        df_temp['AgeGroup'] = pd.cut(df_temp['Age'], bins=[0, 40, 50, 60, 70, 100], labels=['<40', '40-50', '50-60', '60-70', '70+'])
        age_stats = df_temp.groupby('AgeGroup')['HeartDisease'].mean() * 100
        fig = px.bar(x=age_stats.index.astype(str), y=age_stats.values, 
                    color=age_stats.values, color_continuous_scale='Reds',
                    title='Disease Rate by Age Group', labels={'x': 'Age Group', 'y': 'Rate (%)'})
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_option == "Gender Analysis":
        gender_stats = df_sample.groupby(['Sex', 'HeartDisease']).size().reset_index(name='count')
        fig = px.bar(gender_stats, x='Sex', y='count', color='HeartDisease',
                    color_discrete_map={0: '#48bb78', 1: '#f56565'},
                    title='Gender Distribution', barmode='group')
        st.plotly_chart(fig, use_container_width=True)
    
    elif viz_option == "Medical Parameters":
        col1, col2 = st.columns(2)
        with col1:
            fig = px.box(df_sample, x='HeartDisease', y='RestingBP', color='HeartDisease',
                        color_discrete_map={0: '#48bb78', 1: '#f56565'},
                        title='Resting BP')
            fig.update_xaxes(ticktext=['Normal', 'Disease'], tickvals=[0, 1])
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.box(df_sample, x='HeartDisease', y='Cholesterol', color='HeartDisease',
                        color_discrete_map={0: '#48bb78', 1: '#f56565'},
                        title='Cholesterol')
            fig.update_xaxes(ticktext=['Normal', 'Disease'], tickvals=[0, 1])
            st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ============= BULK SCANNER PAGE =============
elif st.session_state.page == "bulk":
    st.markdown('<h2 class="section-header">📁 Bulk Prediction Scanner</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📄 CSV", "📊 Excel", "📋 JSON"])
    
    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.download_button(
            label="📥 Download Sample CSV",
            data=df_sample.drop('HeartDisease', axis=1).to_csv(index=False),
            file_name="sample_data.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        uploaded = st.file_uploader("Upload CSV", type=['csv'])
        if uploaded:
            df_upload = pd.read_csv(uploaded)
            st.success(f"✅ Loaded {len(df_upload)} records")
            
            if st.button("Predict All", type="primary", use_container_width=True):
                if model:
                    preds = model.predict(df_upload)
                    df_upload['Prediction'] = preds
                    df_upload['Status'] = df_upload['Prediction'].map({0: 'Low Risk', 1: 'High Risk'})
                    st.dataframe(df_upload, use_container_width=True)
                    
                    st.download_button(
                        label="📥 Download Results",
                        data=df_upload.to_csv(index=False),
                        file_name="results.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_sample.drop('HeartDisease', axis=1).to_excel(writer, index=False)
        
        st.download_button(
            label="📥 Download Sample Excel",
            data=output.getvalue(),
            file_name="sample_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
        
        uploaded = st.file_uploader("Upload Excel", type=['xlsx'])
        if uploaded:
            df_upload = pd.read_excel(uploaded)
            st.success(f"✅ Loaded {len(df_upload)} records")
            
            if st.button("Predict All", type="primary", use_container_width=True, key="excel_pred"):
                if model:
                    preds = model.predict(df_upload)
                    df_upload['Prediction'] = preds
                    df_upload['Status'] = df_upload['Prediction'].map({0: 'Low Risk', 1: 'High Risk'})
                    st.dataframe(df_upload, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.download_button(
            label="📥 Download Sample JSON",
            data=json.dumps(df_sample.drop('HeartDisease', axis=1).to_dict(orient='records'), indent=2),
            file_name="sample_data.json",
            mime="application/json",
            use_container_width=True
        )
        
        uploaded = st.file_uploader("Upload JSON", type=['json'])
        if uploaded:
            df_upload = pd.DataFrame(json.load(uploaded))
            st.success(f"✅ Loaded {len(df_upload)} records")
            
            if st.button("Predict All", type="primary", use_container_width=True, key="json_pred"):
                if model:
                    preds = model.predict(df_upload)
                    df_upload['Prediction'] = preds
                    df_upload['Status'] = df_upload['Prediction'].map({0: 'Low Risk', 1: 'High Risk'})
                    st.dataframe(df_upload, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ============= ABOUT PAGE =============
elif st.session_state.page == "about":
    st.markdown('<h2 class="section-header">ℹ️ About This Project</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 🎯 Overview")
        st.markdown("""
        AI-powered heart disease prediction system using machine learning.
        Analyzes 11 clinical parameters to assess cardiovascular risk.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 🔬 Technology")
        st.markdown("- **Algorithm:** Random Forest Classifier")
        st.markdown("- **Framework:** Streamlit")
        st.markdown("- **Visualization:** Plotly")
        st.markdown('- **Data Processing:** Pandas')
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 📊 Features")
        st.markdown("- Age, Sex, Chest Pain Type")
        st.markdown("- Resting BP, Cholesterol")
        st.markdown("- Max Heart Rate, ECG Results")
        st.markdown("- Exercise Angina, ST Slope")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 🎓 Use Cases")
        st.markdown("- Healthcare screening")
        st.markdown("- Medical research")
        st.markdown("- Risk assessment")
        st.markdown("- Clinical support")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="alert-warning">', unsafe_allow_html=True)
    st.markdown("**⚠️ Disclaimer:** For educational purposes only. Always consult medical professionals for diagnosis.")
    st.markdown('</div>', unsafe_allow_html=True)
