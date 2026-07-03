import streamlit as st
from pathlib import Path
import time

from agents.orchestrator import SHRUSETVAOrchestrator

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Council of Agents",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------
# LOAD CSS
# ---------------------------------

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

# ---------------------------------
# HEADER
# ---------------------------------

st.markdown("""
<div class="hero">

<h1>⚜️ Council of SHRUSETVA</h1>

<h3>The Council of Wisdom is Investigating Your Question</h3>

<p class="description">
Each specialist AI agent is independently examining your topic before
combining its findings into one comprehensive research report.
</p>

</div>
""", unsafe_allow_html=True)

query = st.session_state.get("user_query", "")

if query == "":
    st.error("No query found.")
    st.stop()

st.markdown("### 📜 Research Topic")
st.success(query)

st.write("")

if st.button("🚀 Convene the Council", use_container_width=True):

    progress = st.progress(0)

    status = st.empty()

    agents = [

        ("📚 Knowledge Collection Agent",
         "Searching ancient texts and traditional wisdom..."),

        ("🌍 Civilization Comparison Agent",
         "Comparing practices across civilizations..."),

        ("🔬 Scientific Verification Agent",
         "Examining modern scientific evidence..."),

        ("⚖️ Evidence Evaluation Agent",
         "Determining credibility and confidence..."),

        ("💡 Modern Application Agent",
         "Finding practical applications..."),

        ("📄 Report Generation Agent",
         "Compiling the Wisdom Report...")
    ]

    for i, (title, desc) in enumerate(agents):

        status.markdown(f"""
### {title}

*{desc}*
""")

        time.sleep(1)

        progress.progress((i + 1) / len(agents))

    status.success("🏛️ Council deliberation completed successfully!")

    with st.spinner("Generating Wisdom Report..."):

        orchestrator = SHRUSETVAOrchestrator()

        result = orchestrator.run(query)

        st.session_state["report"] = result

    time.sleep(1)

    st.switch_page("pages/Report.py")