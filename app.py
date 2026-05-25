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

# 1. Tool Selection Matrix (Expanded with direct shape generation tools)
drawing_mode = st.sidebar.selectbox(
    "Select Input / Writing Tool:",
    ("freedraw", "line", "rect", "circle", "polygon", "transform"),
    index=0,
    help="freedraw: Freehand lines. rect/circle/polygon: Automatically generate vector shapes on drag. transform: Select, resize, or delete elements."
)

st.sidebar.markdown("---")

# 2. Advanced Multi-Color Palette Selection Matrix
stroke_color = st.sidebar.color_picker("🎨 Select Pen / Pencil Color:", "#34d399")

# 3. Dynamic Board Background Color Configurations
bg_color = st.sidebar.color_picker("🧱 Select Board Background Color:", "#111827")

# 4. Thickness Calibration Slider Node
stroke_width = st.sidebar.slider("✏️ Line / Stroke Thickness:", min_value=1, max_value=40, value=5)

st.sidebar.markdown("---")

# =========================================================================
# 📐 GEOMETRIC LEARNING MODULE: 20 SHAPES REFERENCE MATRIX
# =========================================================================
st.sidebar.markdown("## 📐 Kids & Engineering Shape Library")
st.sidebar.caption("Select a shape below to read its structural properties. Set your writing tool above to generate shapes on the board:")

# Structured mapping array containing exactly 20 essential geometric shapes
shape_library = {
    "1. Triangle (Equilateral)": "🔺 3 equal sides and 3 equal 60° internal angles. Use 'polygon' or 'line' tool to plot your points.",
    "2. Right Triangle": "📐 3 sides, featuring exactly one 90° right angle. Essential for building construction layouts.",
    "3. Square": "⏹️ 4 equal straight sides and 4 perfect 90° right angles. Use the 'rect' tool to draw perfectly symmetrical boxes.",
    "4. Rectangle": "▱ 4 sides where opposite sides are equal lengths. Use the 'rect' tool to stretch out width vs height ratios.",
    "5. Circle": "⚪ A perfectly round loop with 0 corners. Use the 'circle' tool to automatically expand from a central point.",
    "6. Oval / Ellipse": "🥚 An elongated, smooth curving egg shape with two distinct focal geometric axes.",
    "7. Semicircle": "🌗 Exactly half of a circle, composed of a flat straight diameter baseline line and a curved top arc.",
    "8. Pentagon": "⬟ A 5-sided polygon with 5 interior angles adding up to 540°. Set tool to 'polygon' to link 5 joints.",
    "9. Hexagon": "⬢ A 6-sided polygon. This shape is incredibly common in engineering honeycomb structures.",
    "10. Heptagon": "⬦ A 7-sided polygon. An advanced geometry framework showing how interior angles expand to 900°.",
    "11. Octagon": "🛑 An 8-sided geometric polygon. Instantly recognizable to children as the universal shape of a stop sign.",
    "12. Nonagon": "🔶 A 9-sided polygon containing 9 individual corner angles summing to exactly 1260°.",
    "13. Decagon": "🌟 A 10-sided polygon. Ideal for teaching structural decimal groupings to young mathematics students.",
    "14. Parallelogram": "💎 A 4-sided flat quadrilateral where the opposite sides are completely parallel to each other.",
    "15. Trapezoid": "📐 A 4-sided shape possessing only one single pair of parallel horizontal lines.",
    "16. Rhombus / Diamond": "♦️ A 4-sided diamond shape where all 4 edges are identical lengths, but corners are skewed.",
    "17. Crescent": "🌙 A distinct curved crescent silhouette formed by a circular shape being intersected by another curve.",
    "18. Star (5-Pointed)": "⭐ A beautiful 10-sided star shape built out of alternating interior and exterior acute angles.",
    "19. Heart": "❤️ A symmetrical, recognizable decorative shape containing two round upper lobes meeting at a sharp bottom corner point.",
    "20. Cube Structure": "📦 A 3D dimensional presentation displaying 6 identical square flat faces, 12 edges, and 8 corner vertices."
}

selected_shape = st.sidebar.selectbox("Choose Shape Template:", list(shape_library.keys()))

# Interactive blueprint details box for instructional delivery
st.sidebar.info(shape_library[selected_shape])

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Quick User Guide:")
st.sidebar.info(
    "👉 **To Automatically Generate Shapes:** Change the tool above to **'rect'** for rectangles/squares, **'circle'** for circles, or **'polygon'** for multi-sided items like triangles.\n\n"
    "👉 **To Erase/Delete:** Switch tool to **'transform'**. Click on any specific element you drew to highlight it, then press the **Delete or Backspace** key on your keyboard to wipe it cleanly!"
)

# =========================================================================
# 🎨 CENTRAL INTERACTIVE BOARD CANVAS LAYER
# =========================================================================

# Responsive structural columns layout
canvas_col, metric_col = st.columns([5, 1])

with canvas_col:
    # Display the targeted instruction header based on active drop-down selection
    st.markdown(f"### ✏️ Current Lesson Target: **{selected_shape}**")
    
    # Drawing Canvas Initialization Matrix
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0.0)",  # Keep interior shapes hollow/transparent for blueprint looks
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
