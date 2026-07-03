import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="SHRUSETVA",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------
from pathlib import Path

def load_css():
    css_path = Path(__file__).parent / "assets" / "style.css"

    with open(css_path, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# Hide Streamlit default menu/footer
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero">

<div class="overlay">

<h1>SHRUSETVA</h1>

<h3>Where Tradition Meets Truth</h3>

<p class="subtitle">
Preserving Humanity's Collective Wisdom through
Multi-Agent AI
</p>

<br>

<p class="description">
Explore how traditional knowledge from civilizations
around the world connects with modern science to solve
today's challenges.
</p>

</div>

</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("🚀 Begin Exploration", use_container_width=True):
        st.switch_page("pages/Explore.py")

st.write("")
st.write("")
st.divider()

# --------------------------------------------------
# ABOUT
# --------------------------------------------------

st.markdown("<h2 class='section-title'>What is SHRUSETVA?</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="about-box">

SHRUSETVA is a Multi-Agent AI platform that collects
traditional knowledge from civilizations across the globe,
compares similar practices, validates them using modern
scientific evidence, and suggests meaningful applications
for today's world.

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# --------------------------------------------------
# THE THREE PILLARS
# --------------------------------------------------

st.markdown("<h2 class='section-title'>The Three Pillars of SHRUSETVA</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="pillar">
        <h3>श्रुति (Shruti)</h3>
        <p>
        The preserved wisdom of humanity—
        knowledge passed through generations,
        traditions, scriptures and lived experience.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="pillar">
        <h3>सेतु (Setu)</h3>
        <p>
        The bridge connecting ancient wisdom
        with modern science through
        autonomous AI research.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="pillar">
        <h3>तत्त्व (Tattva)</h3>
        <p>
        Discovering the fundamental truth
        behind traditions using evidence,
        research and intelligent analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""

<div style="
text-align:center;
margin-top:35px;
margin-bottom:10px;
">

<h2 style="
color:#D4AF37;
font-size:34px;
font-family:Georgia;
">

SHRUSETVA = Shruti • Setu • Tattva

</h2>

<p style="
color:#E8DCC2;
font-size:18px;
max-width:850px;
margin:auto;
line-height:1.8;
">

<b>Shruti</b> preserves humanity's collective wisdom,
<b>Setu</b> bridges ancient knowledge with modern science,
and <b>Tattva</b> uncovers the deeper truth through
Google Gemini-powered Multi-Agent AI.

</p>

</div>

""", unsafe_allow_html=True)

st.write("")
st.divider()

# --------------------------------------------------
# WORKFLOW
# --------------------------------------------------

st.markdown("<h2 class='section-title'>How SHRUSETVA Works</h2>", unsafe_allow_html=True)

st.markdown("""

<div class="workflow">

📝 Ask a Question

⬇️

📚 Knowledge Collection Agent

⬇️

🌍 Civilization Comparison Agent

⬇️

🔬 Scientific Verification Agent

⬇️

💡 Modern Application Agent

⬇️

📄 Final Research Report

</div>

""", unsafe_allow_html=True)