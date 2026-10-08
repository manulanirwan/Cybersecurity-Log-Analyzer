# Cybersecurity Log Analyzer 🛡️

An AI-powered log analysis tool that parses raw server logs, identifies suspicious threat patterns, maps them to MITRE ATT&CK tactics, and exports executive-ready PDF security advisories.

## Key Features

- **Automated Threat Detection**: Detects brute-force attacks, unauthorized access, privilege escalation, and suspicious anomalies.
- **Contextual AI Reasoning**: Explains *what happened*, *why it is suspicious*, and assigns severity levels (Critical, High, Medium, Low).
- **Indicators of Compromise (IOCs)**: Extracts attacker IPs, targeted usernames, timestamps, and attack vectors.
- **Actionable Defense Recommendations**: Provides clear, step-by-step mitigation instructions (e.g., firewall IP blocking, enforcing SSH keys, configuring Fail2ban).
- **One-Click PDF Export**: Generates executive-ready PDF security reports using ReportLab.

## Repository Structure

```
Cybersecurity-Log-Analyzer/
├── app.py                 # Streamlit web interface
├── core/
│   ├── __init__.py
│   ├── analyzer.py        # AI threat analysis engine (OpenAI LLM)
│   └── reporter.py        # PDF report generator (ReportLab)
├── samples/
│   └── sample_auth.log    # Sample authentication log for testing
├── requirements.txt       # Python package dependencies
└── README.md              # Project documentation
```

## Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/manulanirwan/Cybersecurity-Log-Analyzer.git
   cd Cybersecurity-Log-Analyzer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## Sample Workflow

1. Upload `.log` or `.txt` file (e.g., `samples/sample_auth.log`).
2. Provide OpenAI API Key in the sidebar.
3. Click **Analyze Logs** to get real-time AI security findings.
4. Export the comprehensive **Security Report PDF**.

## License

This project is open-source under the MIT License.
