import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="For My Valentine", page_icon="🌹", layout="wide")

# --- CUSTOM CSS (The "Make it Pretty" Code) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    h1 {
        color: #ff4b4b;
        font-family: 'Courier New', sans-serif;
        text-shadow: 2px 2px 4px #000000;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 30px;
        font-size: 20px;
        padding: 15px 30px;
        border: 2px solid white;
        box-shadow: 0px 0px 10px #ff4b4b;
    }
    .stButton>button:hover {
        background-color: white;
        color: #ff4b4b;
        border: 2px solid #ff4b4b;
    }
    /* Hide standard Streamlit overlay */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = "welcome"

# --- HELPER FUNCTIONS ---

def get_rose_figure():
    # High-Definition Mathematical Rose
    theta = np.linspace(-2, 15 * np.pi, 600)  # Resolution
    
    # The Rose Mathematics (Parametric Equations)
    # [x, t] setup
    x = np.linspace(0, 1, 30)
    t = np.linspace(0, 15*np.pi, 600)
    x, t = np.meshgrid(x, t)
    
    p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
    u = 1 - (1 - np.mod(3.3 * t, 2 * np.pi) / np.pi) ** 4 / 2
    y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p))
    h = u * (x * np.cos(p) - y * np.sin(p))

    X = r * np.cos(t)
    Y = r * np.sin(t)
    Z = h

    # Create Plotly 3D Surface
    fig = go.Figure(data=[go.Surface(
        x=X, y=Y, z=Z,
        colorscale=[[0, 'rgb(100,0,0)'], [0.5, 'rgb(200,0,0)'], [1, 'rgb(255,50,50)']], # Deep Red Gradient
        opacity=0.9,
        showscale=False,
        contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True)
    )])

    # Style the "Camera" and Lighting
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='black'
        ),
        paper_bgcolor='black',
        margin=dict(l=0, r=0, b=0, t=0),
        scene_camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)) # Initial view angle
    )
    return fig

def typewriter(text):
    """Effect to type out text letter by letter"""
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f"<h3 style='color: white; text-align: center;'>{typed_text}</h3>", unsafe_allow_html=True)
        time.sleep(0.05)
    return placeholder

# --- PAGE 1: THE WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>💌 You Have a Delivery</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        # Using a form to center the button perfectly
        if st.button("Open Gift 🎁"):
            st.session_state.page = "main"
            st.rerun()

# --- PAGE 2: THE ROSE & INTERACTION ---
elif st.session_state.page == "main":
    
    # 1. The Celebration Effect
    st.balloons()

    # 2. Title
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>Happy Rose Day! 🌹</h1>", unsafe_allow_html=True)
    
    # 3. Two Columns: Rose on Left, Love Letter/Reasons on Right
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Render the High-Quality Plotly Rose
        fig = get_rose_figure()
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<p style='text-align: center; color: gray;'>Use your mouse to rotate and zoom into the petals.</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### Why this rose?", unsafe_allow_html=True)
        st.info("Because real flowers fade, but this code runs forever. Just like my feelings for you.")
        
        st.markdown("---")
        
        # INTERACTIVE: "Reasons I Love You" Generator
        if 'reason' not in st.session_state:
            st.session_state.reason = "Click the button below..."
            
        reasons = [
            "Your smile makes my day brighter.",
            "You are smarter than you think.",
            "The way you laugh is my favorite sound.",
            "You support me like no one else.",
            "You are simply beautiful, inside and out.",
            "Coding this was hard, but you are worth it.",
            "I love how kind you are to others."
        ]
        
        st.markdown("### ✨ Remind me why I'm special?")
        if st.button("Tell me a reason ❤️"):
            st.session_state.reason = random.choice(reasons)
        
        # Display the reason nicely
        st.success(f"💖 {st.session_state.reason}")

    # 4. Music Player (Hidden or visible)
    # You can change this URL to any song she likes!
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3", start_time=0)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>Made with ❤️ and Python</p>", unsafe_allow_html=True)
        
