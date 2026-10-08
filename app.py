import streamlit as st
import os
from core.analyzer import LogAnalyzer
from core.reporter import PDFReportGenerator

st.set_page_config(page_title="Cybersecurity Log Analyzer", page_icon="🛡️", layout="wide")

st.title("🛡️ Cybersecurity Log Analyzer")
st.markdown("Upload raw system or application log files to automatically detect threats and generate a PDF security advisory.")

api_key = st.sidebar.text_input("OpenAI API Key", type="password")

uploaded_file = st.file_uploader("Upload Log File (.log, .txt)", type=["log", "txt"])

if uploaded_file and api_key:
    log_text = uploaded_file.read().decode("utf-8")
    
    with st.expander("Raw Log Preview", expanded=False):
        st.code(log_text[:2000] + ("\n..." if len(log_text) > 2000 else ""), language="text")

    if st.button("Analyze Logs"):
        with st.spinner("Analyzing threat patterns and generating insights..."):
            try:
                analyzer = LogAnalyzer(api_key=api_key)
                result = analyzer.analyze_logs(log_text)

                st.subheader("Analysis Findings")
                col1, col2 = st.columns(2)
                col1.metric("Threat Detected", "Yes" if result.get("threat_detected") else "No")
                col2.metric("Severity Level", result.get("severity", "N/A"))

                st.write("**Primary Threat:**", result.get("primary_threat"))
                st.write("**Summary:**", result.get("summary"))
                st.write("**Suspicion Analysis:**", result.get("suspicion_reason"))

                st.subheader("Recommended Remediation")
                for action in result.get("recommended_actions", []):
                    st.write(f"- {action}")

                # PDF Generation
                pdf_buffer = PDFReportGenerator.create_report(result)
                st.download_button(
                    label="📄 Download Security Report (PDF)",
                    data=pdf_buffer,
                    file_name="security_analysis_report.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")
elif not api_key:
    st.info("Please enter your OpenAI API key in the sidebar to proceed.")
