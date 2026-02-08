import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Star Alignment", page_icon="✨", layout="wide")

# --- CUSTOM CSS (Space Theme) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #000005; /* Deepest Space Black */
    }
    
    /* Elegant Space Fonts */
    h1 {
        font-family: 'Courier New', monospace;
        color: #ffffff;
        text-shadow: 0px 0px 10px #ffffff;
    }
    p {
        color: #b0b0b0;
        font-family: 'Helvetica', sans-serif;
    }
    
    /* Custom Slider - Glowing Blue */
    .stSlider > div > div > div > div {
        background-color: #00d2ff;
        box-shadow: 0px 0px 10px #00d2ff;
    }
    
    /* Hide standard UI */
    header, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- MATH: THE GALAXY ROSE ---
def get_galaxy_rose_data(chaos_level):
    # 1. Create the Rose Structure (The "Target" Shape)
    theta = np.linspace(-2, 15 * np.pi, 500) 
    t_vals = np.linspace(0, 15*np.pi, 500)
    x_vals = np.linspace(0, 1, 30)
    x, t = np.meshgrid(x_vals, t_vals)
    
    # Parametric Rose Equations
    p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
    u = 1 - (1 - np.mod(3.3 * t, 2 * np.pi) / np.pi) ** 4 / 2
    y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p))
    h = u * (x * np.cos(p) - y * np.sin(p))
    
    X_target = r * np.cos(t)
    Y_target = r * np.sin(t)
    Z_target = h
    
    # Flatten the arrays to work with particles (points)
    X_flat = X_target.flatten()
    Y_flat = Y_target.flatten()
    Z_flat = Z_target.flatten()
    
    # 2. ADD CHAOS (Based on Slider)
    # If chaos_level is 1.0 (start), points are everywhere.
    # If chaos_level is 0.0 (end), points are exactly on the rose.
    
    # We use a deterministic seed so the "chaos" looks the same every time she opens it
    np.random.seed(42) 
    
    # Random noise for each point
    X_noise = np.random.uniform(-3, 3, size=X_flat.shape)
    Y_noise = np.random.uniform(-3, 3, size=Y_flat.shape)
    Z_noise = np.random.uniform(-3, 3, size=Z_flat.shape)
    
    # Linear Interpolation: Current Position = Target + (Noise * Chaos)
    X_current = X_flat + (X_noise * chaos_level)
    Y_current = Y_flat + (Y_noise * chaos_level)
    Z_current = Z_flat + (Z_noise * chaos_level)
    
    # Color Calculation (Distance from center gives the galaxy gradient)
    # As chaos reduces, colors become more organized
    colors = np.sqrt(X_target.flatten()**2 + Y_target.flatten()**2)

    return X_current, Y_current, Z_current, colors

# --- APP LAYOUT ---

# 1. HEADER
st.markdown("<h1 style='text-align: center; margin-top: 20px;'>THE UNIVERSE ALIGNED</h1>", unsafe_allow_html=True)

# 2. CONTROLS (The "Game")
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Reverse slider: 100% Chaos -> 0% Chaos (Order)
    # She drags from "Chaos" (0) to "Perfection" (100)
    alignment = st.slider("Align the Stars", 0, 100, 0, format="")
    
    # Convert 0-100 scale to 1.0-0.0 chaos factor
    chaos_factor = 1.0 - (alignment / 100.0)

# 3. GENERATE FRAME
X, Y, Z, C = get_galaxy_rose_data(chaos_factor)

# 4. CAPTIONS & EFFECTS
if alignment < 10:
    st.markdown("<p style='text-align: center;'>The universe started in chaos...</p>", unsafe_allow_html=True)
elif alignment < 50:
    st.markdown("<p style='text-align: center;'>But slowly, the stars began to find their place...</p>", unsafe_allow_html=True)
elif alignment < 95:
    st.markdown("<p style='text-align: center;'>Drawing closer, against all odds...</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align: center; color: #00d2ff; font-weight: bold;'>Until they formed the most beautiful thing in existence: YOU.</p>", unsafe_allow_html=True)
    st.balloons() # Celebration!

# 5. RENDER THE GALAXY ROSE
fig = go.Figure(data=[go.Scatter3d(
    x=X, y=Y, z=Z,
    mode='markers',
    marker=dict(
        size=2.5,                # Star size
        color=C,                 # Gradient based on position
        colorscale='Mystic',     # Beautiful Purple/Blue/Pink scale
        opacity=0.8,             # Slight transparency for "glow" look
        showscale=False
    )
)])

# Camera Logic: Auto-rotate ONLY when fully aligned to reward her
camera_eye = dict(x=1.5, y=1.5, z=1.5)

fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
        bgcolor='#000005', # Match background
        camera=dict(eye=camera_eye)
    ),
    paper_bgcolor='#000005',
    margin=dict(l=0, r=0, b=0, t=0),
    height=600,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# 6. HIDDEN LOVE NOTE (Appears only at 100%)
if alignment == 100:
    st.markdown("""
    <div style='text-align: center; margin-top: 20px; padding: 20px; border: 1px solid #333; border-radius: 15px;'>
        <p style='color: white; font-style: italic; font-size: 18px;'>
        "Mathematical probability says we should never have met.<br>
        But just like these stars, everything aligned perfectly.<br>
        <b>Happy Rose Day, My Universe. 🌌</b>"
        </p>
    </div>
    """, unsafe_allow_html=True)
