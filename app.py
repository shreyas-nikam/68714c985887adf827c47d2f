
import streamlit as st

st.set_page_config(page_title="Risk Governance Navigator", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we will explore the Risk Governance Lab 2 application. This application is designed to help you understand and visualize the effects of different governance styles and the effectiveness of VSM components on risk mitigation and operational efficiency.
""")

page = st.sidebar.selectbox(label="Navigation", options=["Overview", "Simulation", "About"])

if page == "Overview":
    from application_pages.overview import run_overview
    run_overview()
elif page == "Simulation":
    from application_pages.simulation import run_simulation
    run_simulation()
elif page == "About":
    from application_pages.about import run_about
    run_about()
