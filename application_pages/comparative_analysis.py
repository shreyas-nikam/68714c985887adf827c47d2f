
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_comparative_analysis():
    st.header("Comparative Analysis: Benchmarking Your Firm")
    st.markdown(r"""
**Business Value:**  
Comparative analysis allows an organization to benchmark its operational risk management quality against a peer, standard, or industry average ("benchmark firm"). Decision makers can immediately visualize their strengths and areas for improvement in the four main quality areas:

- Output
- Process
- Audience
- Success

**Technical Details:**  
- This function takes two sets of scores (firm scores and benchmark scores).
- It produces a side-by-side bar chart comparing scores by category.
- This approach closely mirrors market best practices (Handbook Table: `Means of Measurement versus Purpose`) and emphasizes **audience satisfaction** as the most actionable metric.
""")

    def perform_comparative_analysis(firm_scores, benchmark_scores):
        categories = list(firm_scores.keys())
        firm_values = list(firm_scores.values())
        benchmark_values = list(benchmark_scores.values())

        x = np.arange(len(categories))
        width = 0.35

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(x - width/2, firm_values, width, label='Firm', color='#1f77b4')
        ax.bar(x + width/2, benchmark_values, width, label='Benchmark', color='#ff7f0e')

        ax.set_xlabel('Quality Areas', fontsize=12)
        ax.set_ylabel('Scores', fontsize=12)
        ax.set_title('Comparative Analysis of Firm vs Benchmark', fontsize=14)
        ax.set_xticks(x)
        ax.set_xticklabels(categories, fontsize=12)
        ax.legend(fontsize=10)
        plt.tight_layout()
        return fig

    st.subheader("Enter Scores (0-100):")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Your Firm's Scores")
        firm_output = st.number_input("Output (Firm)", min_value=0, max_value=100, value=75, key='f_out', help="Score for the quality of outputs produced.")
        firm_process = st.number_input("Process (Firm)", min_value=0, max_value=100, value=80, key='f_proc', help="Score for the effectiveness of internal processes.")
        firm_audience = st.number_input("Audience (Firm)", min_value=0, max_value=100, value=90, key='f_aud', help="Score for audience satisfaction with risk management.")
        firm_success = st.number_input("Success (Firm)", min_value=0, max_value=100, value=70, key='f_succ', help="Score for overall success in achieving risk management goals.")
        firm_scores = {'Output': firm_output, 'Process': firm_process, 'Audience': firm_audience, 'Success': firm_success}

    with col2:
        st.markdown("### Benchmark Scores")
        bench_output = st.number_input("Output (Benchmark)", min_value=0, max_value=100, value=80, key='b_out', help="Score for benchmark's output quality.")
        bench_process = st.number_input("Process (Benchmark)", min_value=0, max_value=100, value=75, key='b_proc', help="Score for benchmark's process effectiveness.")
        bench_audience = st.number_input("Audience (Benchmark)", min_value=0, max_value=100, value=85, key='b_aud', help="Score for benchmark's audience satisfaction.")
        bench_success = st.number_input("Success (Benchmark)", min_value=0, max_value=100, value=75, key='b_succ', help="Score for benchmark's overall success.")
        benchmark_scores = {'Output': bench_output, 'Process': bench_process, 'Audience': bench_audience, 'Success': bench_success}

    st.pyplot(perform_comparative_analysis(firm_scores, benchmark_scores))
    st.markdown("---")
