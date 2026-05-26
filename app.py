import streamlit as st
from streamlit_drawable_canvas import st_canvas
import io

# 1. Page Configuration Framework
st.set_page_config(
    page_title="THE BOARD SOFTWARE | GLOBALINTERNET.PY",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Injection for GlobalInternet.py Dark Theme & Full-Canvas Reset Alignment
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
    
    /* Maximize main block utilization space */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1rem !important;
        max-width: 95% !important;
    }

    /* Force canvas drawing block to align properly without splitting gaps */
    div[data-testid="stCanvas"] {
        margin: 0 auto 15px auto !important;
        background-color: transparent !important;
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
    .instruction-card {
        background-color: #1e293b;
        border-left: 4px solid #38bdf8;
        padding: 12px;
        border-radius: 4px;
        margin-bottom: 15px;
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

# 1. Tool Selection Matrix (NOW INCLUDES 'text' ENGINE OPTION)
drawing_mode = st.sidebar.selectbox(
    "Select Input / Writing Tool:",
    ("freedraw", "line", "rect", "circle", "polygon", "text", "transform"),
    index=0,
    help="freedraw: Draw lines. text: Click on board to type with keyboard. transform: Scale or reposition text/shapes."
)

st.sidebar.markdown("---")

# 2. Advanced Multi-Color Palette Selection Matrix
stroke_color = st.sidebar.color_picker("🎨 Select Pen / Text Color:", "#34d399")

# 3. Dynamic Board Background Color Selection Menu
board_color_name = st.sidebar.selectbox(
    "🧱 Select Board Surface Color:",
    ("Black (Default)", "White Blueprint", "Classic Green Board", "Deep Engineering Blue", "Studio Charcoal Grey"),
    index=0
)

color_map = {
    "Black (Default)": "#000000",
    "White Blueprint": "#ffffff",
    "Classic Green Board": "#064e3b",
    "Deep Engineering Blue": "#1e3a8a",
    "Studio Charcoal Grey": "#334155"
}
bg_color = color_map[board_color_name]

# 4. Thickness & Font Sizing Calibration Slider Node
stroke_width = st.sidebar.slider("✏️ Stroke Thickness / Font Size:", min_value=1, max_value=60, value=18)

st.sidebar.markdown("---")

# =========================================================================
# 📐 GEOMETRIC LEARNING MODULE: 20 SHAPES REFERENCE MATRIX
# =========================================================================
st.sidebar.markdown("## 📐 Kids & Engineering Shape Library")
st.sidebar.caption("Select a shape below to read its structural properties:")

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
    "10. Heptagon": "⦾ A 7-sided polygon. An advanced geometry framework showing how interior angles expand to 900°.",
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
st.sidebar.info(shape_library[selected_shape])

# =========================================================================
# 🎨 CENTRAL INTERACTIVE BOARD CANVAS LAYER
# =========================================================================

canvas_col, metric_col = st.columns([5, 1])

with canvas_col:
    st.markdown(f"### ✏️ Current Lesson Target: **{selected_shape}**")
    
    st.markdown(
        """
        <div class="instruction-card">
            ⌨️ <strong>How to Use Keyboard Typing:</strong> Set your writing tool tool in the sidebar to 
            <strong>'text'</strong>. Click anywhere on the board surface, and a blinking cursor will appear. 
            Type your labels directly from your physical keyboard! Use <strong>'transform'</strong> to resize or reposition them later.
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Executing complete full-coverage canvas core configuration layer
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0.0)",  
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=500,
        width=1000,
        drawing_mode=drawing_mode,
        display_toolbar=True, 
        key=f"engine_board_{bg_color}",
    )

with metric_col:
    st.markdown("#### 📊 Board Matrix")
    if canvas_result.json_data is not None:
        elements_count = len(canvas_result.json_data["objects"])
        st.metric(label="Active Elements", value=str(elements_count))
        
        # Real Hardwired Download Module
        if canvas_result.image_data is not None:
            st.markdown("---")
            st.markdown("##### 💾 Save Blueprint")
            
            img_data = canvas_result.image_data
            try:
                from PIL import Image
                image_pil = Image.fromarray(img_data.astype('uint8'), 'RGBA')
                buffer = io.BytesIO()
                image_pil.save(buffer, format="PNG")
                byte_payload = buffer.getvalue()
                
                st.download_button(
                    label="📥 Save Drawing",
                    data=byte_payload,
                    file_name="globalinternet_board_export.png",
                    mime="image/png",
                    use_container_width=True
                )
            except Exception:
                st.caption("Encoding drawing data...")
        
        st.markdown("---")
        if elements_count > 0:
            st.success("Board Active.")
        else:
            st.markdown('<p class="strong-white-caption">Awaiting input stream layers...</p>', unsafe_allow_html=True)

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
