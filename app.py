import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="My Heart For You", page_icon="❤️", layout="wide")

# --- CUSTOM CSS (Cinematic Dark Mode) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    
    /* Elegant Fonts */
    h1, h2, h3, p { font-family: 'Helvetica Neue', sans-serif; color: #ecf0f1; }
    
    /* Custom Slider Styling */
    .stSlider > div > div > div > div { background-color: #ff3333; }
    
    /* Button Styling */
    .stButton>button {
        background-color: transparent;
        color: #ff3333;
        border: 2px solid #ff3333;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        color: white;
        box-shadow: 0px 0px 15px #ff3333;
    }
    
    /* Hide Streamlit Bloat */
    header, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- MATH FUNCTIONS ---

def get_rose_shape(bloom_stage):
    # bloom_stage goes from 0.0 (Bud) to 1.0 (Full Flower)
    
    theta = np.linspace(-2, 15 * np.pi, 800) 
    t_vals = np.linspace(0, 15*np.pi, 800)
    x_vals = np.linspace(0, 1, 50)
    x, t = np.meshgrid(x_vals, t_vals)
    
    p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
    
    # MODIFYING PARAMETERS FOR BLOOMING EFFECT
    # When bloom is low, we squeeze the petals (change u) and pull them up (change z)
    bloom_factor = 0.2 + (bloom_stage * 0.8) # map 0-1 to 0.2-1.0
    
    u = 1 - (1 - np.mod(3.3 * t, 2 * np.pi) / np.pi) ** 4 / 2
    y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p)) * bloom_factor # Expand width
    h = u * (x * np.cos(p) - y * np.sin(p)) 
    
    # Adjust height based on bloom (buds are taller/closed, flowers are wider/flat)
    # If bloom is 0, we stretch Z. If bloom is 1, we keep Z normal.
    z_stretch = 1.5 - (bloom_stage * 0.5)
    
    X = r * np.cos(t)
    Y = r * np.sin(t)
    Z = h * z_stretch

    return X, Y, Z

def get_heart_shape():
    # 3D Heart Parametric Equation
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 16 * np.sin(v) ** 3 * np.sin(u)
    y = 16 * np.sin(v) ** 3 * np.cos(u)
    z = 13 * np.cos(v) - 5 * np.cos(2 * v) - 2 * np.cos(3 * v) - np.cos(4 * v)
    # Meshgrid creates the surface
    u, v = np.meshgrid(u, v)
    X = 16 * np.sin(v) ** 3 * np.sin(u)
    Y = 16 * np.sin(v) ** 3 * np.cos(u)
    Z = 13 * np.cos(v) - 5 * np.cos(2 * v) - 2 * np.cos(3 * v) - np.cos(4 * v)
    return X, Y, Z

# --- APP LAYOUT ---

st.markdown("<h1 style='text-align: center; margin-bottom: 20px;'>THE SHAPE OF MY LOVE</h1>", unsafe_allow_html=True)

# 1. CONTROLS
col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
with col_c2:
    mode = st.radio("Select Form:", ["The Rose", "The Heart"], horizontal=True)

# 2. VISUALIZATION
if mode == "The Rose":
    # Slider for interactivity
    st.markdown("<p style='text-align: center; color: gray; font-size: 14px;'>🌱 Drag the slider to bloom the flower</p>", unsafe_allow_html=True)
    bloom = st.slider("", 0.0, 1.0, 0.1, key="bloom_slider") # Start closed (0.1)
    
    X, Y, Z = get_rose_shape(bloom)
    color_scale = [[0, 'rgb(30,0,0)'], [0.5, 'rgb(180,0,0)'], [1, 'rgb(255,0,50)']]
    
    # Dynamic Caption
    if bloom < 0.3:
        caption = "Just like us... it starts small."
    elif bloom < 0.7:
        caption = "Growing stronger every day..."
    else:
        caption = "Fully bloomed. Just like my love for you. 🌹"
        st.balloons() # Only balloons when fully open!

elif mode == "The Heart":
    X, Y, Z = get_heart_shape()
    color_scale = [[0, 'rgb(50,0,0)'], [0.5, 'rgb(150,0,0)'], [1, 'rgb(220,20,60)']]
    caption = "This heart beats only for you. ❤️"

# 3. RENDER THE PLOT
fig = go.Figure(data=[go.Surface(
    x=X, y=Y, z=Z,
    colorscale=color_scale,
    opacity=1.0, # VELVET TEXTURE (No transparency)
    showscale=False,
    lighting=dict(ambient=0.4, diffuse=0.5, roughness=0.9, specular=0.05, fresnel=0.2)
)])

fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
        bgcolor='#000000',
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
    ),
    paper_bgcolor='#000000',
    margin=dict(l=0, r=0, b=0, t=0),
    height=500
)

st.plotly_chart(fig, use_container_width=True)
st.markdown(f"<h3 style='text-align: center; margin-top: -20px;'>{caption}</h3>", unsafe_allow_html=True)

# 4. FINAL INTERACTION
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("💌 Read the Secret Message"):
    st.markdown("""
    <div style='text-align: center; padding: 20px; border: 1px solid #333; border-radius: 10px;'>
        <p style='font-style: italic; color: #ffcccc;'>
        "I didn't want to just send you a picture.<br>
        I wanted to build something that you could touch and change.<br>
        Because that's what you've done to my life—you touched it, and changed it into something beautiful."
        </p>
    </div>
    """, unsafe_allow_html=True)
