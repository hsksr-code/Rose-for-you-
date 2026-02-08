import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Specially For You", page_icon="🌹", layout="wide")

# --- CUSTOM CSS (The "Vibe" Code) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    h1 {
        color: #ff2a2a;
        font-family: 'Courier New', sans-serif;
        font-weight: bold;
        text-shadow: 0px 0px 10px #ff0000;
    }
    .stButton>button {
        background-color: #ff2a2a;
        color: white;
        border-radius: 30px;
        font-size: 24px;
        font-weight: bold;
        padding: 15px 40px;
        border: 2px solid white;
        box-shadow: 0px 0px 20px #ff2a2a;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        background-color: white;
        color: #ff2a2a;
        border: 2px solid #ff2a2a;
    }
    .quote-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff2a2a;
        font-size: 20px;
        color: white;
    }
    /* Hide standard Streamlit overlay */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = "welcome"
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = "Click the button to see why you're amazing... ❤️"

# --- HELPER FUNCTIONS ---

def get_sparkling_rose():
    # 1. THE SURFACE (The Petals)
    theta = np.linspace(-2, 15 * np.pi, 600) 
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

    # 2. THE DEW DROPS (Glitter/Sparkle Effect)
    # We take random points from the rose to add "glitter"
    mask = np.random.rand(*X.shape) > 0.95 # Only 5% of points get glitter
    xs = X[mask]
    ys = Y[mask]
    zs = Z[mask]

    fig = go.Figure()

    # Add the Rose Surface
    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        colorscale=[[0, 'rgb(50,0,0)'], [0.3, 'rgb(200,0,0)'], [0.6, 'rgb(255,50,50)'], [1, 'rgb(255,182,193)']], # Deep Red to Pink
        opacity=0.95,
        showscale=False,
        contours_z=dict(show=True, usecolormap=False, highlightcolor="white", project_z=False)
    ))

    # Add the "Sparkles" (Dew Drops)
    fig.add_trace(go.Scatter3d(
        x=xs, y=ys, z=zs,
        mode='markers',
        marker=dict(
            size=2,
            color='white', # Sparkles are white
            opacity=0.8
        )
    ))

    # Camera and Lighting
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='black',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
        ),
        paper_bgcolor='black',
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )
    return fig

# --- PAGE 1: THE WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 60px;'>🔒 CONFIDENTIAL</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: gray;'>This file is encrypted for one person only.</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Unlock Surprise 🔓"):
            st.session_state.page = "main"
            st.rerun()

# --- PAGE 2: THE MAIN EVENT ---
elif st.session_state.page == "main":
    
    # 1. Balloons + Snow for maximum effect
    st.balloons()
    
    # 2. Title
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>Happy Rose Day! 🌹</h1>", unsafe_allow_html=True)
    
    # 3. Main Layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # The Sparkling Rose
        st.markdown("<h4 style='text-align: center; color: white;'>A Rose That Never Fades</h4>", unsafe_allow_html=True)
        fig = get_sparkling_rose()
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        
        # MUSIC PLAYER - Ed Sheeran: Perfect (Embedded)
        st.markdown("### 🎵 Play Me First")
        st.markdown("""
        <iframe width="100%" height="80" src="https://www.youtube.com/embed/2Vv-BfVoq4g?start=0" 
        title="Ed Sheeran" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen></iframe>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # HIGH ENERGY QUOTES
        reasons = [
            "You aren't just a star, you're the whole damn galaxy. 🌌",
            "If I had a flower for every time I thought of you, I could walk through my garden forever. 🌸",
            "You’re the only person I’d pause my game for. (And you know that's huge!) 🎮",
            "Are you a magician? Because whenever I look at you, everyone else disappears. ✨",
            "My life was black and white until you painted it with color. 🎨",
            "You’re not an option, you’re my priority. Always. 🔥",
            "Forget the butterflies, I feel the whole zoo when I'm with you. 🦁",
            "This code runs on logic, but my heart runs on YOU. ❤️"
        ]
        
        st.markdown("### ⚡ Why you?")
        if st.button("Hit Me! 💥"):
            st.session_state.current_quote = random.choice(reasons)
            st.balloons() # Small celebration every time she clicks!
        
        # The Quote Box
        st.markdown(f"""
        <div class="quote-box">
            {st.session_state.current_quote}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: #333; margin-top: 50px;'>Forever yours.</p>", unsafe_allow_html=True)
