import json
import os
from openai import OpenAI

class LogAnalyzer:
    def __init__(self, api_key: str = None):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))

    def analyze_logs(self, log_contents: str) -> dict:
        prompt = f"""
You are a Senior Cybersecurity Incident Response Analyst. 
Analyze the following log snippet and identify potential security threats, anomalies, or suspicious activities.

Log Snippet:
```
{log_contents}
```

Provide your assessment strictly in JSON format with the following keys:
- "threat_detected": boolean
- "primary_threat": string (e.g., "Possible SSH Brute-Force Attack")
- "severity": string ("Low", "Medium", "High", "Critical")
- "mitre_attack_id": string (e.g., "T1110 - Brute Force")
- "summary": string (Brief narrative of what happened)
- "suspicion_reason": string (Why this behavior indicates malicious intent)
- "indicators_of_compromise": list of strings (IPs, usernames, timestamps)
- "recommended_actions": list of strings (Actionable defensive steps)

Return raw JSON only. Do not wrap in markdown block formatting.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )

        content = response.choices[0].message.content.strip()
        
        if content.startswith("```json"):
            content = content[7:-3].strip()
        elif content.startswith("```"):
            content = content[3:-3].strip()

        return json.loads(content)
