**AI-Sec: Prompt Injection & Log Auditor**

**Overview**

This is a Python-based security tool designed to audit AI agent logs for potential Prompt Injection attacks. It automates the process of scanning raw log data against a dictionary of known adversarial keywords (e.g., "override", "bypass", "ignore"). This was built to test my knowledge of scripts and interests in the future of AI and Security

 
**Features**


Automated Pattern Matching: Scans logs for high-risk strings used in LLM prompt injection attempts.


Data Normalization: Implements case-insensitive matching to prevent bypasses via capitalization.


Security Reporting: Generates a standalone alerts.txt report for incident response review.


Error Handling: Robust file-system checks to prevent crashes during log ingestion.


**Technical Fundamentals Used**

With open for secure file stream management.


Modular code structure for reusability.


Error Handling: try/except blocks for professional-grade stability.

______________________________________________________________________________________________________
This project is part of my focus on AI Security Engineering and protecting critical LLM infrastructure.

