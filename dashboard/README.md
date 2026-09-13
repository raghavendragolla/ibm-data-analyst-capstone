# Executive Technology Trends Dashboard

This directory contains the interactive dashboard implementation and architecture specifications for the **IBM Data Analyst Capstone Project**.

---

## 1. Local Interactive Dashboard (Streamlit + Plotly + SQLite)

A modern, production-grade business intelligence dashboard connected directly to the normalized relational database (`data/processed/capstone.db`).

### Key Features:
- **Executive KPI Cards**: Real-time indicators for Total Headcount (11,398), Median Annual Salary ($57,744), Top Language (JavaScript), Leading Future Growth Language (Python), and Preferred Future Database (PostgreSQL).
- **Interactive Multi-Level Filtering**: Dynamically segment analysis across **135 Countries** and **3 Work Locations** (Office, Home, Coworking/Other).
- **5 Thematic Tabs**:
  1. `Programming Languages`: Interactive horizontal bar charts comparing current production usage against future developer desire.
  2. `Database Migrations`: Grouped bar charts tracking the structural migration shift from MySQL to PostgreSQL and Redis.
  3. `Supply vs. Demand Gap`: Comparative analysis cross-referencing developer skills against 27,005 live tech job requisitions.
  4. `IDEs & Demographics`: Donut charts for development environments and interactive boxplots for degree compensation.
  5. `Executive Insights & Actions`: C-suite recommendations for hiring, reskilling, and technology modernization.

### How to Run the Dashboard Locally:
From the project root directory, run:
```powershell
.\.venv\Scripts\streamlit.exe run dashboard/app.py
```
*The dashboard will automatically open in your web browser at `http://localhost:8501`.*

---

## 2. IBM Cognos Analytics Capstone Specification

For stakeholders or evaluators reviewing against the original **IBM Cognos Analytics** assignment format, the exact Cognos specification is detailed below:

### Tab 1: Current Technology Usage
- **Widget 1 (Bar Chart)**: Top 10 Languages Worked With (`Language` vs. `Count of Respondent`).
- **Widget 2 (Bar Chart)**: Top 10 Databases Worked With (`Database` vs. `Count of Respondent`).
- **Widget 3 (Donut Chart)**: Top 10 Development Environments (`DevEnviron` vs. `Count of Respondent`).
- **Widget 4 (Column Chart)**: Operating System Adoption (`OpSys` vs. `Count of Respondent`).

### Tab 2: Future Technology Trends
- **Widget 1 (Bar Chart)**: Top 10 Languages Desired Next Year.
- **Widget 2 (Bar Chart)**: Top 10 Databases Desired Next Year.
- **Widget 3 (Line Chart)**: Year-over-Year Momentum for Emerging Languages.

### Tab 3: Demographics & Compensation
- **Widget 1 (Histogram)**: Respondent Age Distribution (`Age` binned into 5-year intervals).
- **Widget 2 (Box Plot)**: Compensation Distribution (`ConvertedComp` grouped by `EdLevel`).
- **Widget 3 (Map / Clustered Bar)**: Top Respondent Geographies (`Country` vs. `Headcount`).
