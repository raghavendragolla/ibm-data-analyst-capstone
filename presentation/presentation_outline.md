# Executive Presentation Deck: Global Technology Trends & Skills Intelligence

**Course**: IBM Data Analyst Professional Certificate Capstone Project  
**Presenter**: Raghavendra Golla | Associate Data Analyst  
**Audience**: Executive Leadership (CTO, VP of HR, L&D Director)  
**Format**: 15-Slide Professional Briefing  

---

### Slide 1: Title Slide
* **Headline**: Global Technology Trends & Workforce Skills Intelligence
* **Subhead**: Data-Driven Talent Strategy for Enterprise Consulting
* **Presenter**: Raghavendra Golla, Associate Data Analyst
* **Date**: September 2026

---

### Slide 2: The Business Problem
* **Context**: Rapid technical evolution creates severe skill shortages in enterprise consulting.
* **Core Challenge**: Misalignment between developer adoption, employer job demand, and training investments.
* **Financial Risk**: High cost of unbillable talent bench, misaligned hiring budgets, and unwanted attrition.

---

### Slide 3: Project Objectives
* **Map Current Adoption**: Identify dominant languages, databases, and IDEs across 11,398 engineers.
* **Forecast Future Demand**: Track aspirational technology adoption to guide FY2026–2027 strategy.
* **Bridge the Skills Gap**: Cross-examine developer capabilities against 27,005 active job postings.
* **Statistical Validation**: Test pay equity across education tiers and evaluate remote work productivity.

---

### Slide 4: Data Architecture & Sources
* **Developer Survey Sample**: 11,398 unique responses from the Stack Overflow survey (IBM subset).
* **Labor Market Postings**: 27,005 live job listings from PromptCloud / Naukri dataset (Public Domain).
* **Industry Salary Benchmark**: Curated salary and learning difficulty web-scraped benchmark table.
* **Reproducibility**: Cryptographic SHA-256 validation across all source datasets.

---

### Slide 5: Data Hygiene & Wrangling Pipeline
* **Deduplication**: Eliminated 154 duplicate submissions; protected statistical sample integrity.
* **Mode Imputation**: Imputed missing categorical records (`WorkLoc` = Office, `EdLevel` = Bachelor's).
* **Compensation Harmonization**: Converted weekly/monthly cycles to `NormalizedCompensation` (Median = $100k).
* **1NF Normalization**: Decomposed delimited strings into 5 relational tables linked by `Respondent ID`.

---

### Slide 6: Programming Languages: The Growth Engine
* **Current Enterprise Leaders**: JavaScript (76.2%), HTML/CSS (68.7%), SQL (62.3%).
* **Rising Interest Among Mainstream Languages**: **Python** is the only one of the five most-used languages whose desired users exceed current users (4,542 → 5,239, +15.3%).
* **Fading Momentum**: PHP (-50.0%), Java (-34.5%), and VBA (-76.3%) experience sharp decline in desire.
* **Key Takeaway**: Enterprise engagements require dual-competency engineers: Web (JS/TS) + Data/Backend (Python).

---

### Slide 7: Database Systems: The Open-Source Migration
* **Current Deployments**: MySQL leads active production environments (48.0%), followed by SQL Server (36.1%).
* **The Modernization Shift**: **PostgreSQL emerges as the #1 desired database (38.0%)**, overtaking MySQL.
* **Caching & NoSQL Surge**: High future demand for **MongoDB (32.0%)** and **Redis (29.2%)**.
* **Key Takeaway**: Enterprise architecture is transitioning from legacy commercial RDBMS to cloud-native PostgreSQL.

---

### Slide 8: Development Environments (IDEs): Tooling Dominance
* **Industry Standard**: **Visual Studio Code** commands **58.3%** developer adoption.
* **Runner-Up Tooling**: Visual Studio (35.3%), Notepad++ (30.2%), IntelliJ (27.2%), Vim (26.7%).
* **Strategic Takeaway**: Standardizing internal development tooling on VS Code eliminates proprietary license costs.

---

### Slide 9: Skills Gap: Developer Supply vs. Market Demand
* **High-Demand Anchor Skills**: SQL appears in 8.2% and JavaScript in 8.3% of 27,000+ job requisitions.
* **The Over-Investment Risk**: High developer supply in C++ and C# with lower relative job posting shares.
* **Key Takeaway**: Technical screening must verify practical SQL query proficiency as a prerequisite for all technical roles.

---

### Slide 10: Compensation Reality & Outlier Analysis
* **Statistical Skew**: Mean salary ($131,334) is inflated >2.2x over the Median ($57,744).
* **IQR Outlier Detection**: 879 respondents earn above the $209,698 upper fence (up to $2,000,000).
* **Post-Outlier Baseline**: Trimming outliers normalizes the mean to $59,883.
* **Key Takeaway**: Executive salary budgeting must rely on Median compensation to avoid distorted forecasts.

---

### Slide 11: Inferential Statistics: Debunking Degree Bias
* **Hypothesis Test (Mann-Whitney U)**: Bachelor's ($60.5k median) vs. Master's ($57.7k median).
* **Test Result**: $U = 7.09M, \quad p = 0.0676 > 0.05$ (Fail to Reject $H_0$).
* **Finding**: Master's degree holders do **not** earn a statistically significant compensation premium.
* **Executive Action**: Eliminate mandatory Master's degree requirements to widen the hiring pool by >200%.

---

### Slide 12: Remote Work Productivity & Employee Retention
* **Productivity Test (Welch's t-Test)**: Remote (41.1 hrs/wk) vs. Office (40.9 hrs/wk), $p = 0.272$.
  * *Result*: Remote work delivers identical weekly hours; no loss of productivity.
* **Retention Test (Chi-Square $\chi^2$)**: $\chi^2 = 2,692.38, \quad p < 0.0001$.
  * *Result*: Dissatisfaction directly drives active job seeking (5x increase in active hunting).
* **Executive Action**: Flexible remote policies safeguard talent against expensive market churn.

---

### Slide 13: Executive BI Dashboard Overview
* **Platform**: Interactive Streamlit & Plotly BI application (`dashboard/app.py`).
* **KPI Header**: Real-time metrics for Headcount (11,398), Median Pay ($57.7k), and Top Growth Technologies.
* **Filtering**: Live segmentation across 135 countries and 3 working models.
* **Architecture Companion**: Full IBM Cognos Analytics specification documented in `dashboard/README.md`.

---

### Slide 14: Strategic Recommendations Roadmap
* **CTO Office**:
  1. Build a *PostgreSQL & Redis Cloud Migration Practice* for enterprise client advisory.
  2. Standardize enterprise development environments on Visual Studio Code.
* **Talent Acquisition**:
  1. Shift from credential-first to skill-first screening (drop graduate degree filters).
  2. Test foundational SQL and Python in all candidate evaluations.
* **Learning & Development**:
  1. Transition training investments from legacy Java/PHP into Python, TypeScript, and Cloud architectures.
  2. Conduct quarterly developer satisfaction surveys to prevent costly talent turnover.

---

### Slide 15: Conclusion & Q&A
* **Summary**: Evidence-based analysis replaces intuition with rigorous data intelligence across 11k+ developers and 27k+ job postings.
* **Repository**: Full code, notebooks, SQL scripts, and documentation available on GitHub.
* **Discussion**: Open for questions and implementation planning.
