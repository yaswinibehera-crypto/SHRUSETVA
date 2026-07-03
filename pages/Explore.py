import streamlit as st
from pathlib import Path

# ---------------------------
# Page Config
# ---------------------------

st.set_page_config(
    page_title="Knowledge Chamber",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------
# Load CSS
# ---------------------------

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

# ---------------------------
# Hero
# ---------------------------

st.markdown("""

<div class="hero">

<h1>Knowledge Chamber</h1>

<h3>
What knowledge would you like to rediscover today?
</h3>

<p class="description">

Ask about traditions, architecture,
medicine, agriculture, rituals,
food preservation, astronomy,
or any wisdom preserved by civilizations.

</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# ---------------------------
# Search Box
# ---------------------------

query = st.text_input(
    "",
    placeholder="Example: Traditional methods of water conservation..."
)

st.write("")

# ---------------------------
# Popular Topics
# ---------------------------

st.markdown(
"<h2 class='section-title'>Explore Popular Topics</h2>",
unsafe_allow_html=True
)

col1,col2,col3=st.columns(3)

with col1:

    if st.button("🌿 Ayurveda"):
        st.session_state.query="Ayurveda"

    if st.button("🏛 Architecture"):
        st.session_state.query="Ancient Architecture"

with col2:

    if st.button("💧 Water Conservation"):
        st.session_state.query="Water Conservation"

    if st.button("🌾 Agriculture"):
        st.session_state.query="Traditional Agriculture"

with col3:

    if st.button("🍯 Traditional Medicine"):
        st.session_state.query="Traditional Medicine"

    if st.button("🔥 Rituals & Practices"):
        st.session_state.query="Rituals"

st.write("")
st.write("")
st.write("")

# ---------------------------
# Begin Expedition
# ---------------------------

if st.button("🚀 Begin Expedition", use_container_width=True):

    if query!="":

        st.session_state.user_query=query

        st.switch_page("pages/Agents.py")

    else:

        st.warning("Please enter a topic to explore.")