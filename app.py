import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# --- PAGE CONFIGURATION (Clean & Elegant) ---
st.set_page_config(page_title="For You", page_icon="🌹", layout="wide")

# --- CUSTOM CSS (The "Velvet" Vibe) ---
st.markdown("""
    <style>
    /* 1. Background: Deep Matte Black */
    .stApp {
        background-color: #050505;
    }
    
    /* 2. Typography: Elegant Serif Fonts */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif; 
        color: #e0e0e0;
        font-weight: 400;
        letter-spacing: 2px;
    }
    
    /* 3. The Button: Minimalist & Classy */
    .stButton>button {
        background-color: transparent;
        color: #ff3333;
        border: 2px solid #ff3333;
        border-radius: 5px;
        padding: 10px 30px;
        font-family: 'Courier New', monospace;
        text-transform: uppercase;
        letter-spacing: 3px;
        transition: all 0.4s ease;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        color: black;
        box-shadow: 0px 0px 20px rgba(255, 51, 51, 0.4);
    }
    
    /* 4. Progress Bar Styling */
    .stProgress > div > div > div > div {
        background-color: #ff3333;
    }
    
    /* Hide standard Streamlit elements */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'decrypted' not in st.session_state:
    st.session_state.decrypted = False

# --- HELPER FUNCTIONS ---

def get_velvet_rose():
    # 1. THE GEOMETRY
    theta = np.linspace(-2, 15 * np.pi, 800) 
    x = np.linspace(0, 1, 50) # Higher resolution for smoothness
    t = np.linspace(0, 15*np.pi, 800)
    x, t = np.meshgrid(x, t)
    
    p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
    u = 1 - (1 - np.mod(3.3 * t, 2 * np.pi) / np.pi) ** 4 / 2
    y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p))
    h = u * (x * np.cos(p) - y * np.sin(p))

    X = r * np.cos(t)
    Y = r * np.sin(t)
    Z = h

    # 2. THE MATERIAL (Velvet Effect)
    fig = go.Figure(data=[go.Surface(
        x=X, y=Y, z=Z,
        # Deep Crimson Gradient (Dark to Light Red)
        colorscale=[[0, 'rgb(30,0,0)'], [0.4, 'rgb(100,0,0)'], [1, 'rgb(220,20,60)']], 
        opacity=1.0, # 100% Opaque (No transparency)
        showscale=False,
        
        # LIGHTING: This creates the "Velvet" texture
        lighting=dict(
            ambient=0.3,      # Low ambient light for drama
            diffuse=0.6,      # Soft spread of light
            roughness=0.9,    # High roughness = Velvet/Cloth (not shiny plastic)
            specular=0.05,    # Low shine (matte finish)
            fresnel=0.1       # Slight rim lighting
        ),
        lightposition=dict(x=0, y=0, z=100) # Light from directly above
    )])

    # Camera and Background
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='#050505',
            camera=dict(eye=dict(x=1.6, y=1.6, z=1.6))
        ),
        paper_bgcolor='#050505',
        margin=dict(l=0, r=0, b=0, t=0),
    )
    return fig

# --- MAIN LAYOUT ---

# 1. Elegant Header
st.markdown("<h1 style='text-align: center; margin-bottom: 50px;'>THE ALGORITHM OF LOVE</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    # 2. The Velvet Rose
    fig = get_velvet_rose()
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<p style='text-align: center; color: #444; font-size: 12px; letter-spacing: 2px;'>INTERACTIVE 3D RENDER</p>", unsafe_allow_html=True)

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if not st.session_state.decrypted:
        # Phase 1: The "Code" View
        st.markdown("""
        <div style='font-family: "Courier New"; color: #00ff00; opacity: 0.7; font-size: 14px;'>
        > INCOMING TRANSMISSION...<br>
        > SENDER: [YOUR NAME]<br>
        > STATUS: ENCRYPTED 🔒<br>
        > CONTENT-TYPE: PURE_EMOTION<br>
        <br>
        01001000 01100101 01100001 01110010 01110100<br>
        01100010 01100101 01100001 01110100 00101110<br>
        01100101 01111000 01100101 00100000 01110010<br>
        01110101 01101110 01101110 01101001 01101110<br>
        01100111...
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("RUN DECRYPTION"):
            # The "Hacker" Loading Effect
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(100):
                time.sleep(0.02) # Speed of loading
                progress_bar.progress(i + 1)
                if i < 40:
                    status_text.text(f"Decrypting binary... {i}%")
                elif i < 80:
                    status_text.text(f"Translating feelings to words... {i}%")
                else:
                    status_text.text(f"Unlocking heart... {i}%")
            
            st.session_state.decrypted = True
            st.rerun()

    else:
        # Phase 2: The Decrypted Message (Elegant)
        st.balloons() # The only "fun" element allowed, serving as celebration
        
        st.markdown("""
        <div style='border-left: 3px solid #ff3333; padding-left: 20px;'>
            <h3 style='color: white;'>Decryption Complete.</h3>
            <p style='color: #cccccc; font-size: 18px; line-height: 1.6; font-family: "Georgia", serif;'>
            "I wanted to give you something that lasts longer than a real flower.<br><br>
            This code, like my care for you, has no expiration date. 
            It doesn't wither, it doesn't fade, and it's built to stand the test of time.<br><br>
            <b>You are the most special variable in my life's equation.</b>"
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.success("Message Successfully Delivered 🌹")
