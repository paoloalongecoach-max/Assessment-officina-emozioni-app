import streamlit as st
import pandas as pd
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Officina delle Emozioni - Check-up",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ASSETS PATHS (RELATIVE FOR DEPLOYMENT) ---
# Ensure we map the correct image based on the score
def get_car_image(score):
    if score <= 3:
        return "assets/car_perfect.png"
    elif score <= 6:
        return "assets/car_scratched.png"
    elif score <= 8:
        return "assets/car_damaged.png"
    else:
        return "assets/car_wrecked.png"

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Dark Premium Theme */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #FFFFFF !important;
    }
    h1 { font-weight: 800; letter-spacing: -1px; }
    
    /* General Text */
    p, div, label, span {
        color: #FFFFFF !important;
    }

    /* Streamlit specific overrides for labels */
    .stMarkdown, .stSlider > label, .stSelectbox > label, .stMultiSelect > label, .stRadio > label {
        color: #FFFFFF !important;
    }
    
    .stCaption {
        color: #E0E0E0 !important; /* Slightly distinct but bright */
    }

    /* Custom Cards */
    .metric-card {
        background-color: #1E1E1E;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF4B4B !important; /* Keep score red */
    }
    .metric-label {
        font-size: 1rem;
        color: #FFFFFF !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Slider Customization */
    .stSlider > div > div > div > div {
        background-color: #FF4B4B;
    }
    
    /* Button Customization (Standard Buttons) */
    .stButton > button {
        width: 100%;
        background-color: #FF4B4B;
        color: white !important;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ff1f1f;
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.4);
    }

    /* Link Button Customization (for direct links) */
    .stLinkButton > a {
        width: 100%;
        background-color: #FF4B4B !important;
        color: white !important;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .stLinkButton > a:hover {
        background-color: #ff1f1f !important;
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.4);
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
col_logo, col_title = st.columns([1, 5])

with col_logo:
    logo_path = "assets/logo_paolo_alonge.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=150)

with col_title:
    st.title("Officina delle Emozioni®")
    st.markdown("##### *di Paolo Alonge - Coach Gestione Rabbia e Stress*")
    
    st.markdown("### 🔧 Diagnostica Ingegneristica dello Stress")
    st.markdown("""
    **Sei stanco di conflitti familiari e stress da lavoro?**
    
    Spesso ignoriamo i segnali di allarme finché non esce il fumo dal cofano.
    Compila questa scheda tecnica per capire se stai solo "correndo troppo" o se rischi di fondere il motore. 
    """)

st.markdown("---")

# --- MAIN FORM ---
col_form, col_visual = st.columns([1.5, 1], gap="large")

with col_form:
    st.markdown("#### 📋 Scheda Tecnica")
    
    # SEZIONE 1: IL MOTORE (Carico Mentale)
    st.markdown("##### 1. REGIME DEL MOTORE (Carico Mentale)")
    st.info("A quanti 'giri' sta andando la tua mente in questo periodo?")
    rpms = st.slider(
        "RPM (Giri al minuto)", 
        min_value=0, max_value=12, value=4, 
        help="0=Spento, 6=Crociera, 12=Zona Rossa (Burnout)"
    )
    
    if rpms <= 4:
        motore_score = 2
        motore_msg = "Regime ottimale. Il motore gira rotondo."
    elif rpms <= 8:
        motore_score = 6
        motore_msg = "Regime alto. Consumo elevato di carburante."
    else:
        motore_score = 10
        motore_msg = "ZONA ROSSA. Rischio fusione guarnizione testata."
        
    st.caption(f"Status Motore: *{motore_msg}*")
    st.markdown("---")

    # SEZIONE 2: RADIATORE (Rabbia e Reattività)
    st.markdown("##### 2. TEMPERATURA RADIATORE (Reattività Emotiva)")
    st.info("Quanto ci metti a 'bollire' quando qualcosa va storto in famiglia o al lavoro?")
    
    temp_val = st.select_slider(
        "Livello di guardia",
        options=["Freddo (Distaccato)", "Normale (Gestibile)", "Caldo (Irritabile)", "Bollente (Esplosivo)"],
        value="Normale (Gestibile)"
    )
    
    # Mapping for calculation
    temp_map = {"Freddo (Distaccato)": 2, "Normale (Gestibile)": 4, "Caldo (Irritabile)": 7, "Bollente (Esplosivo)": 10}
    radiatore_score = temp_map[temp_val]
    st.markdown("---")

    # SEZIONE 3: SOSPENSIONI E INGRANAGGI (Somatizzazione e Tenuta)
    st.markdown("##### 3. INTEGRITÀ TELAIO (Sintomi Fisici)")
    sintomi = st.multiselect(
        "Quali 'cigolii' senti nella carrozzeria?",
        [
            "Insonnia / Sonno disturbato",
            "Tensione muscolare (collo/schiena)",
            "Mal di testa frequente",
            "Gastrite / Reflusso",
            "Stanchezza cronica al risveglio",
            "Fame nervosa"
        ]
    )
    # Score basato sul numero di sintomi pesati
    telaio_score = min(len(sintomi) * 2, 10)
    
    # Calculate Overall Health
    total_score = (motore_score + radiatore_score + telaio_score) / 3

with col_visual:
    st.markdown("#### 📊 Risultato Diagnostica")
    
    # Determine Status
    if total_score <= 3:
        status_color = "#00cc66" # Green
        status_text = "OTTIME CONDIZIONI"
        advice = "Continua così. Fai solo manutenzione ordinaria."
    elif total_score <= 6:
        status_color = "#ff9933" # Orange
        status_text = "USURA EVIDENTE"
        advice = "Consigliato un check-up per evitare danni seri."
    elif total_score <= 8:
        status_color = "#ff3300" # Red
        status_text = "DANNI STRUTTURALI"
        advice = "FERMATI. La macchina non è sicura. Serve intervento immediato."
    else:
        status_color = "#990000" # Dark Red
        status_text = "RELITTO IN FIAMME"
        advice = "Chiama il carro attrezzi. Non sei in grado di guidare."

    # Dynamic Card
    st.markdown(f"""
        <div class="metric-card" style="border-left: 5px solid {status_color};">
            <div class="metric-label">Indice di Usura</div>
            <div class="metric-value" style="color: {status_color};">{total_score:.1f}/10</div>
            <h3 style="color: {status_color}; margin: 10px 0;">{status_text}</h3>
            <p style="color: #FFFFFF; font-style: italic;">"{advice}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("###") # Spacer
    
    # Car Image
    image_path = get_car_image(total_score)
    if os.path.exists(image_path):
        st.image(image_path, width="stretch", caption=f"Rappresentazione visiva dello stato attuale")
        # Wait, the logs showed "Please replace replace `use_container_width` with `width`".
        # I should fix that to avoid warnings.
    else:
        st.error(f"Immagine non trovata: {image_path}. Verificare la cartella 'assets'.")

    # Radar Chart
    st.markdown("### 📡 Telemetria")
    chart_data = pd.DataFrame({
        "Sistemi": ["Motore (Carico)", "Radiatore (Rabbia)", "Telaio (Corpo)"],
        "Stress %": [motore_score * 10, radiatore_score * 10, telaio_score * 10]
    })
    st.bar_chart(chart_data.set_index("Sistemi"), color=status_color)

# --- CTA SECTION ---
st.markdown("---")
col_cta_left, col_cta_center, col_cta_right = st.columns([1, 2, 1])

with col_cta_center:
    if total_score > 4:
        st.error("⚠️ ATTENZIONE: La spia avaria motore è accesa.")
        # Direct link button as requested
        st.link_button("📅 PRENOTA UNA CONSULENZA CON L'ING. PAOLO ALONGE", "https://paoloalonge.it/prenota/")
    else:
        st.success("✅ Sistemi nominali. Mantieni questo assetto!")
