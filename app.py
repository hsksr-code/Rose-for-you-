import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# --- PAGE SETUP ---
st.set_page_config(page_title="A Surprise For You", page_icon="🌹", layout="centered")

# Custom CSS to make it look elegant and hide the menu
st.markdown("""
    <style>
    .stApp {background-color: #0e1117;}
    h1 {color: #ff4b4b; font-family: 'Helvetica', sans-serif;}
    .stButton>button {
        background-color: #ff4b4b; 
        color: white; 
        border-radius: 20px;
        padding: 10px 24px;
        font-size: 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ffcccb;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE (To track if she clicked the button) ---
if 'revealed' not in st.session_state:
    st.session_state.revealed = False

# --- THE ROSE FUNCTION ---
def draw_rose(color_map):
    fig = plt.figure(figsize=(8, 8))
    fig.patch.set_facecolor('#0e1117') # Match background
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#0e1117')

    # The Mathematics
    [x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi)
    p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
    u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
    y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p))
    h = u * (x * np.cos(p) - y * np.sin(p))

    xx = r * np.cos(t)
    yy = r * np.sin(t)
    zz = h

    # Plot surface with selected color
    ax.plot_surface(xx, yy, zz, rstride=1, cstride=1, cmap=color_map, linewidth=0, antialiased=True)
    ax.set_axis_off()
    return fig

# --- THE APP LOGIC ---

if not st.session_state.revealed:
    # Phase 1: The Mystery
    st.markdown("<br><br><br>", unsafe_allow_html=True) # Spacing
    st.markdown("<h1 style='text-align: center;'>Hey, I made something for you...</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>It took some coding and math, but you deserve the effort.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Click to Reveal Surprise 🎁"):
            st.session_state.revealed = True
            st.rerun() # Refresh to show phase 2

else:
    # Phase 2: The Reveal
    st.balloons() # DIGITAL BALLOONS ANIMATION!
    
    st.markdown("<h1 style='text-align: center;'>Happy Rose Day! 🌹</h1>", unsafe_allow_html=True)
    
    # Interactive Color Picker
    st.markdown("<p style='text-align: center; color: white;'>Customize your rose:</p>", unsafe_allow_html=True)
    color_choice = st.select_slider(
        "Choose a color:",
        options=["Red", "Pink", "Purple", "Blue", "Gold"],
        value="Red"
    )

    # Map text choices to Matplotlib Colormaps
    colormap_dict = {
        "Red": cm.Reds,
        "Pink": cm.RdPu,
        "Purple": cm.BuPu,
        "Blue": cm.Blues,
        "Gold": cm.Wistia
    }

    # Draw the rose
    with st.spinner("Generating your unique flower..."):
        fig = draw_rose(colormap_dict[color_choice])
        st.pyplot(fig)

    st.markdown(f"<h3 style='text-align: center; color: white;'>This rose is defined by math, so it will never die. Just like my love for you.</h3>", unsafe_allow_html=True)
                    
