import streamlit as st
from pathlib import Path

# --------------------------
# PAGE CONFIG
# --------------------------

st.set_page_config(
    page_title="Wisdom Report",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------
# LOAD CSS
# --------------------------

css_path = Path(__file__).parent.parent / "assets" / "style.css"

with open(css_path, encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# --------------------------
# GET REPORT
# --------------------------

report = st.session_state.get("report", None)
query = st.session_state.get("user_query", "")

if report is None:
    st.error("No report found.")
    st.stop()

data = report["report"]

# --------------------------
# HEADER
# --------------------------

st.markdown("""
<div class="hero">

<h1>Wisdom Report</h1>

<h3>Research completed by SHRUSETVA</h3>

</div>
""", unsafe_allow_html=True)

st.write("")

st.markdown(f"""
<div class="about-box">

<h2 style="color:#D4AF37;">📜 Research Question</h2>

<p style="font-size:22px;">
{query}
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# --------------------------
# Traditional Knowledge
# --------------------------

st.markdown(
"<h2 class='section-title'>📚 Traditional Knowledge</h2>",
unsafe_allow_html=True
)

st.markdown(f"""
<div class="about-box">

{data["traditional_knowledge"]["traditional_knowledge"]}

</div>
""", unsafe_allow_html=True)

st.divider()

# --------------------------
# Civilization Comparison
# --------------------------

st.markdown(
"<h2 class='section-title'>🌍 Across Civilizations</h2>",
unsafe_allow_html=True
)

st.markdown(f"""
<div class="about-box">

{data["civilization_comparison"]["comparison"]}

</div>
""", unsafe_allow_html=True)

st.divider()

# --------------------------
# Scientific Validation
# --------------------------

st.markdown(
"<h2 class='section-title'>🔬 Scientific Evidence</h2>",
unsafe_allow_html=True
)

st.markdown(f"""
<div class="about-box">

{data["scientific_validation"]["evidence"]}

</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown(
"<h2 class='section-title'>⚖️ Evidence Evaluation</h2>",
unsafe_allow_html=True
)

st.markdown(f"""
<div class="about-box">

{data["evidence_evaluation"]["evaluation"]}

</div>
""", unsafe_allow_html=True)

# --------------------------
# Modern Applications
# --------------------------

st.markdown(
"<h2 class='section-title'>💡 Modern Applications</h2>",
unsafe_allow_html=True
)

st.markdown(f"""
<div class="about-box">

{data["modern_applications"]["applications"]}

</div>
""", unsafe_allow_html=True)

st.divider()

# --------------------------
# Explore Again
# --------------------------

if st.button("🔍 Explore Another Topic", use_container_width=True):

    st.switch_page("pages/Explore.py")