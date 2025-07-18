
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we explore various operational risk measurement approaches and provide interactive tools for data validation, comparative analysis, risk profile visualization, and cost variability analysis.

formulae, explanations, tables, etc.
""")

page = st.sidebar.selectbox(label="Navigation", options=["Data Loading & Summary", "Comparative Analysis", "Risk Profile Grid", "Cost Variability Analysis", "Additional Visualizations"])
if page == "Data Loading & Summary":
    from application_pages.data_loading import run_data_loading
    run_data_loading()
elif page == "Comparative Analysis":
    from application_pages.comparative_analysis import run_comparative_analysis
    run_comparative_analysis()
elif page == "Risk Profile Grid":
    from application_pages.risk_profile import run_risk_profile
    run_risk_profile()
elif page == "Cost Variability Analysis":
    from application_pages.cost_variability import run_cost_variability
    run_cost_variability()
elif page == "Additional Visualizations":
    from application_pages.additional_visualizations import run_additional_visualizations
    run_additional_visualizations()


# License
st.caption('''
---
## QuantUniversity License

© QuantUniversity 2025  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@quantuniversity.com](mailto:info@quantuniversity.com)
''')
