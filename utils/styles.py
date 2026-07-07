import streamlit as st


def load_css():
    st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

.stApp{
    background:#09090b;
    color:white;
}

section[data-testid="stSidebar"]{
    background:#111827;
}

/* ======================================
GLOBAL DESIGN SYSTEM
====================================== */

.block-container{
    padding-top:1.5rem;
    padding-bottom:2rem;
}

h1{
    font-weight:800!important;
    letter-spacing:-0.5px;
}

h2,h3{
    font-weight:700!important;
}

.stButton > button{
    width:100%;
    border-radius:14px;
    border:none;
    padding:12px;
    font-weight:700;
    transition:.25s;
}

.stButton > button:hover{
    transform:translateY(-2px);
}

div[data-testid="stMetric"]{
    background:#18181b;
    border:1px solid #27272a;
    border-radius:18px;
    padding:18px;
}

div[data-testid="stTabs"]{
    margin-top:15px;
}

textarea{
    border-radius:14px!important;
}
/* ---------- Remove top spacing ---------- */

.block-container{
    padding-top:0.3rem !important;
}

section[data-testid="stSidebar"]{
    padding-top:0rem !important;
}

section[data-testid="stSidebar"] > div{
    padding-top:0rem !important;
}
                
</style>
""", unsafe_allow_html=True)