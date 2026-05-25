import streamlit as st
from streamlit_drawable_canvas import st_canvas

# 1. Page Configuration Framework
st.set_page_config(
    page_title="THE BOARD SOFTWARE | GLOBALINTERNET.PY",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Injection for GlobalInternet.py Dark Theme & High-Contrast White Text
st.markdown(
    """
    <style>
    /* Global App Background and Base Contrast */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .main-title {
        text-align: center;
        font-weight: 800;
        font-size: 2.5rem;
        background: linear-gradient(90deg, #38bdf8, #34d399, #fbbf24);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px;
        letter-spacing: 1px;
    }
    .sub-title {
        text-align: center;
        font-size: 1rem;
        color: #94a3b8;
        margin-bottom: 4px;
    }
    .author-credentials {
        text-align: center;
        font-size: 0.95rem;
        color: #e2e8f0;
        font-weight: 500;
        margin-bottom: 25px;
    }
    .author-credentials a {
        color: #38bdf8 !important;
        text-decoration: none;
    }
    div[data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    
    /* Strong White Metric Text Overrides */
    div[data-testid="stMetricLabel"] > div {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    div[data-testid="stMetricValue"] > div {
        color: #ffffff !important;
        font-weight: 800 !important;
    }
    
    /* High-Contrast Custom Classes */
    .strong-white-caption {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.875rem;
        margin-top: 4px;
    }
    .strong-white-footer {
        text-align: center; 
        margin-top: 40px; 
        font-size: 0.85rem; 
        color: #ffffff !important; 
        font-weight: 600 !important;
        border-top: 1px solid #334155; 
        padding-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App UI Header Nodes
st.markdown('<h1 class="main-title">THE BOARD SOFTWARE</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="sub-title">Engineered by GlobalInternet.py | Advanced Multi-Touch & Stylus Canvas Core</h3>', unsafe_allow_html=True)

# Personal Information Metadata Injection Layer
st.markdown(
    '<div class="author-credentials">'
    'Built by <strong>Gesner Deslandes</strong> &nbsp;|&nbsp; '
    '📥 Phone: <strong>(509)-47385663</strong> &nbsp;|&nbsp; '
    '✉️ Email: <a href="mailto:deslandes78@gmail.com"><strong>deslandes78@gmail.com</strong></a>'
    '</div>', 
    unsafe_allow_html=True
)

# =========================================================================
# 🎛️ SIDEBAR CONTROL FRAMEWORK
# =========================================================================
st.sidebar.markdown("## 🛠️ Board Controls")
st.sidebar.markdown("---")

# 1. Tool Selection Matrix
drawing_mode = st.sidebar.selectbox(
    "Select Input / Writing Tool:",
    ("freedraw", "line", "rect", "circle", "transform"),
    index=0,
    help="Use 'freedraw' to write with fingers, pens, or pencils. Use 'transform' to select, scale, move, or delete elements."
)

st.sidebar.markdown("---")

# 2. Advanced Multi-Color Palette Selection Matrix
stroke_color = st.sidebar.color_picker("🎨 Select Pen / Pencil Color:", "#34d399")

# 3. Dynamic Board Background Color Configurations
bg_color = st.sidebar.color_picker("🧱 Select Board Background Color:", "#111827")

st.sidebar.markdown("---")

# 4. Thickness Calibration Slider Node
stroke_width = st.sidebar.slider("✏️ Line / Stroke Thickness:", min_value=1, max_value=40, value=5)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Quick User Guide:")
st.sidebar.info(
    "👉 **To Write/Draw:** Set tool to **'freedraw'** and use any finger, stylus, pen, or pencil directly on the surface canvas.\n\n"
    "👉 **To Erase/Delete:** Switch tool to **'transform'**. Click on any specific line or text element you drew to highlight it, then press the **Delete or Backspace** key on your physical keyboard to wipe it out cleanly!"
)

# =========================================================================
# 🎨 CENTRAL INTERACTIVE BOARD CANVAS LAYER
# =========================================================================

# Responsive structural columns layout
canvas_col, metric_col = st.columns([5, 1])

with canvas_col:
    # Drawing Canvas Initialization Matrix
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0.0)",  # Keep interior shapes hollow/transparent
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=550,
        drawing_mode=drawing_mode,
        display_toolbar=True, # Provides built-in Undo/Redo/Trash actions at canvas base
        key="global_board_engine",
    )

with metric_col:
    st.markdown("#### 📊 Board Data")
    if canvas_result.json_data is not None:
        # Pull dynamic canvas elements length directly from underlying JSON engine matrix
        elements_count = len(canvas_result.json_data["objects"])
        
        # Displays "Active Elements" and the raw count string in pure high-contrast bold white
        st.metric(label="Active Elements", value=str(elements_count))
        
        if elements_count > 0:
            st.success("Board Engine Active.")
            st.markdown('<p class="strong-white-caption">Use the toolbar icons below the board to quickly undo strokes or wipe the panel clear.</p>', unsafe_allow_html=True)
        else:
            # Displays "Board is clear. Awaiting input stream..." in strong bold white HTML formatting
            st.markdown('<p class="strong-white-caption">Board is clear. Awaiting input stream...</p>', unsafe_allow_html=True)

# =========================================================================
# 📜 SYSTEM FOOTER BASE NODE
# =========================================================================
st.markdown(
    """
    <div class="strong-white-footer">
        © 2026 GLOBALINTERNET.PY | Global Software Architectures & Technology Innovation.
    </div>
    """,
    unsafe_allow_html=True
)
