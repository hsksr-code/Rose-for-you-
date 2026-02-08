import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Page Configuration for a nice title and icon
st.set_page_config(page_title="For You", page_icon="🌹", layout="centered")

# Custom CSS to hide standard web elements and make it look like a dedicated card
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp {background-color: #000000;} 
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Title Section
st.markdown("<h1 style='text-align: center; color: white;'>Happy Rose Day! 🌹</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ffcccb;'>A mathematical rose that lasts forever.</h3>", unsafe_allow_html=True)

def create_rose():
    # Create the figure
    fig = plt.figure(figsize=(10, 10))
    # Set background to black to match the page
    fig.patch.set_facecolor('black')
    
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')

    # The Math
    [x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi)
    p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
    u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
    y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p))
    h = u * (x * np.cos(p) - y * np.sin(p))

    xx = r * np.cos(t)
    yy = r * np.sin(t)
    zz = h

    # Plot
    surf = ax.plot_surface(xx, yy, zz, rstride=1, cstride=1, 
                           cmap=cm.Reds, linewidth=0, antialiased=True)

    ax.set_axis_off()
    return fig

# Display the rose
with st.spinner("Growing a special rose for you..."):
    fig = create_rose()
    st.pyplot(fig)

# Final message
st.markdown("<p style='text-align: center; color: white; font-style: italic;'>Drag the rose to view it from all angles.</p>", unsafe_allow_html=True)
