# Global Technology Trends & Skills Intelligence: End-to-End Data Analytics Capstone

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SQLite%20%7C%20ANSI--SQL-lightgrey.svg)](https://www.sqlite.org/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ibm-capstone.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![IBM Capstone](https://img.shields.io/badge/Certification-IBM%20Data%20Analyst%20Professional-blueviolet.svg)](https://www.coursera.org/professional-certificates/ibm-data-analyst)
[![CI](https://github.com/raghavendragolla/ibm-data-analyst-capstone/actions/workflows/ci.yml/badge.svg)](https://github.com/raghavendragolla/ibm-data-analyst-capstone/actions/workflows/ci.yml)

A professional, portfolio-grade Data Analytics capstone project modeled on the **IBM Data Analyst Professional Certificate Capstone Project**. This repository evaluates global technology trends, programming language adoption, database migration patterns, compensation benchmarks, and labor market supply/demand dynamics across **11,398 developer survey responses** and **27,005 live tech job postings**.

---

## 📑 Table of Contents
- [Executive Overview](#executive-overview)
- [Business Problem & Objectives](#business-problem--objectives)
- [Datasets & Cryptographic Provenance](#datasets--cryptographic-provenance)
- [Tools & Technology Stack](#tools--technology-stack)
- [End-to-End Analytical Workflow](#end-to-end-analytical-workflow)
- [Key Findings & Strategic Insights](#key-findings--strategic-insights)
- [Actionable Business Recommendations](#actionable-business-recommendations)
- [Interactive Dashboard](#interactive-dashboard)
- [Project Repository Structure](#project-repository-structure)
- [How to Reproduce & Run Locally](#how-to-reproduce--run-locally)
- [Methodological Limitations](#methodological-limitations)
- [Author & Contact](#author--contact)

---

## Executive Overview

Global IT and management consulting organizations face rapid shifts in technology ecosystems. Misaligned talent acquisition and internal training result in costly bench idle time, misallocated hiring budgets, and talent attrition. 

This project bridges the gap between **developer skill supply** and **real employer labor demand**, delivering data-driven recommendations for executive stakeholders (CTO, Talent Acquisition, and Learning & Development).

### Key Takeaways at a Glance:
- **Language Momentum**: JavaScript (76.2%) and SQL (62.3%) anchor enterprise production, while **Python** represents the premier growth engine (+46.0% net desire expansion).
- **The Database Shift**: While MySQL leads current deployments (48.0%), **PostgreSQL surges to #1** in future developer desire (38.0%), with Redis (29.2%) and MongoDB (32.0%) capturing caching and NoSQL demand.
- **Tooling Standard**: **Visual Studio Code** dominates engineering environments with **58.3%** adoption.
- **Academic Degree Premium Debunked**: A non-parametric **Mann-Whitney U Test** ($p = 0.0676$) confirms **no statistically significant difference** in compensation between Bachelor's ($60.5k median) and Master's ($57.7k median) degree holders.
- **Remote Work Commitment**: A two-sample **Welch's t-test** ($p = 0.2719$) proves remote developers work identical hours (41.1 hrs/wk) to in-office employees (40.9 hrs/wk).

---

## Business Problem & Objectives

Our client, a multinational IT consulting firm, needs objective data to guide its FY2026–FY2027 technology strategy.

### Core Analytical Objectives:
1. Identify dominant programming languages, databases, and development tooling.
2. Determine emerging future technologies showing the highest adoption momentum.
3. Cross-examine developer capabilities against 27,005 active job listings to pinpoint the market skills gap.
4. Statistically evaluate compensation distributions and demographic determinants.
5. Provide actionable recommendations for recruitment screening, upskilling, and client advisory.

---

## Datasets & Cryptographic Provenance

All data used in this capstone originates from authentic, verified public datasets:

| Dataset | Provenance & Endpoint | Records & Format | SHA-256 Checksum |
| :--- | :--- | :--- | :--- |
| **Developer Survey** | IBM Skills Network / Stack Overflow 2019 Survey Sample | 11,552 raw records, 85 columns (CSV) | `78cedfca3f0a21f78090be1b...` |
| **Job Market Demand** | PromptCloud Naukri Job Postings (Public Domain) | 27,005 job listings (JSON) | `d527cbb5ac73ab34261055...` |
| **Salary Benchmarks** | IBM Skills Network HTML Benchmark Table | 10 language benchmarks (HTML) | `8f6d5aaa3a6fdfd0f3fb0e...` |

*Full schema definitions and field descriptions are documented in [`docs/data_dictionary.md`](docs/data_dictionary.md) and [`docs/sources.md`](docs/sources.md).*

---

## Tools & Technology Stack

- **Core Analytics**: Python 3.10+, Pandas, NumPy, SciPy (Inferential Statistics)
- **Data Engineering**: BeautifulSoup (Web Scraping), Requests, Regular Expressions (Word Boundaries)
- **Database**: SQLite 3, ANSI-SQL (Window Functions, CTEs, Relational 1NF Modeling)
- **Visualization**: Matplotlib, Seaborn, Plotly Express
- **Dashboarding**: Streamlit (Interactive Multi-Tab App) + IBM Cognos Analytics Specifications
- **Testing & CI**: Pytest unit tests (`tests/`) + GitHub Actions (`.github/workflows/ci.yml`)
- **Version Control**: Git, GitHub

---

## End-to-End Analytical Workflow

```
[Phase 2: Acquisition] ──> Cryptographic download & SHA-256 validation (src/data_collection.py)
       │
[Phase 3: Understanding] ─> Column profiling & data dictionary creation (notebooks/01)
       │
[Phase 4: Extraction] ───> API simulation & BeautifulSoup DOM scraping (notebooks/02)
       │
[Phase 5: Cleaning] ─────> Deduplication (154 dropped) & Mode Imputation (src/data_cleaning.py)
       │
[Phase 6: Wrangling] ────> Comp normalization ($100k median) & 1NF decomposition (notebooks/03)
       │
[Phase 7: SQL Modeling] ─> Relational database provisioning (src/build_database.py) & 10 analytical queries (sql/)
       │
[Phase 8: EDA] ──────────> IQR outlier detection (879 outliers) & skewness analysis (notebooks/04)
       │
[Phase 9: Statistics] ───> Mann-Whitney U, Welch t-test, and Chi-Square testing (notebooks/05)
       │
[Phase 10: Visuals] ─────> 8 publication-grade figures exported (visualizations/)
       │
[Phase 11: Dashboard] ───> Multi-tab interactive Streamlit application (dashboard/app.py)
       │
[Phase 12-14: Synthesis] > Executive Report (reports/) & Presentation Slide Deck (presentation/)
```

---

## Key Findings & Strategic Insights

### 1. Programming Languages: The Growth Engine
- **Current Production Leaders**: JavaScript (8,687), HTML/CSS (7,830), and SQL (7,106).
- **Emerging Momentum**: Python surges by **+46.0% net interest** (from 4,542 active users to 6,630 desired users).
- **Declining Adoption**: PHP (-50.0%), Java (-34.5%), and VBA (-76.3%) suffer steep drops in future interest.

### 2. Database Architectures: The Open-Source Migration
- While MySQL leads current deployments (48.0%), **PostgreSQL is the #1 desired database (38.0%)**, reflecting a corporate shift away from legacy commercial systems toward open-source relational engines.
- In-memory caching and document stores (**Redis at 29.2%** and **MongoDB at 32.0%**) dominate future architectural stack designs.

### 3. Supply vs. Market Demand Reality
- Comparing survey capabilities against 27,005 job postings reveals that **SQL (8.2%)** and **JavaScript (8.3%)** represent the highest absolute volume of job requisitions. Foundational SQL remains the single most non-negotiable data skill in enterprise hiring.

### 4. Compensation Skewness & Outliers
- `ConvertedComp` has a severe positive skewness of 5.38. The mean ($131,334) is distorted by 879 high-earner outliers earning above the $209,698 Tukey fence (up to $2.0M).
- When outliers are filtered, the normalized mean drops to $59,883, aligning closely with the $57,744 median.
- **Correlation with Overtime**: Correlation between weekly work hours and pay is virtually zero ($r = 0.05$). Technical specialization, not overtime hours, dictates market compensation.

### 5. Inferential Statistics: Validating Talent Assumptions
- **Degree Premium Test (Mann-Whitney U)**: $U = 7,097,773.0, p = 0.0676$. Fail to reject $H_0$. Master's degrees do not provide a statistically significant pay premium over Bachelor's degrees.
- **Remote Work Hours Test (Welch's t-Test)**: $t = 1.0988, p = 0.2719$. Fail to reject $H_0$. Remote developers log identical weekly hours (41.1 hrs) to in-office developers (40.9 hrs).
- **Retention Test (Chi-Square $\chi^2$)**: $\chi^2 = 2,692.38, p < 0.0001$. Reject $H_0$. Dissatisfied engineers are over 5x more likely to actively hunt for external jobs.

---

## Actionable Business Recommendations

### For the Chief Technology Officer (CTO):
1. **Launch a PostgreSQL & Cloud Modernization Practice**: Create packaged migration services to help enterprise clients migrate from legacy commercial databases (Oracle, SQL Server) to managed PostgreSQL and Redis.
2. **Standardize on VS Code Tooling**: Mandate VS Code as the default engineering environment across internal teams to lower licensing costs and accelerate onboarding.

### For Talent Acquisition & Human Resources:
1. **Remove Mandatory Master's Degree Requirements**: Eliminate graduate degree filters from job postings to expand applicant pools by >200% without sacrificing technical competence.
2. **Standardize SQL & Python Technical Screening**: Screen all data and software engineering candidates for relational query writing and Python automation scripting.

### For Learning & Development (L&D):
1. **Reallocate Training Budgets into Python & TypeScript**: Shift 50% of legacy Java/PHP training funds into full-stack modern web and Python data engineering tracks.
2. **Conduct Proactive Retention Check-Ins**: Leverage quarterly engagement pulses to address developer dissatisfaction early, mitigating expensive talent attrition.

---

## Interactive Dashboard

The repository includes a production-grade **Streamlit & Plotly BI Dashboard** connected to `data/processed/capstone.db`:

```powershell
# Launch the dashboard locally
.\.venv\Scripts\streamlit.exe run dashboard/app.py
```

### Dashboard Features:
- **KPI Overview**: Real-time indicators for Headcount, Median Pay, Top Language, Top Database, and Top IDE.
- **Interactive Multi-Level Filtering**: Dynamic filtering by Country (135 nations) and Work Location.
- **5 Comprehensive Tabs**: Languages, Database Migrations, Labor Demand Gap, IDEs/Demographics, and Executive Actions.
- **IBM Cognos Architecture Guide**: Documented in [`dashboard/README.md`](dashboard/README.md).

---

## Project Repository Structure

```
IBM-Data-Analyst-Capstone/
│
├── README.md                                  <- Executive project summary (this document)
├── requirements.txt                            <- Pinned environment dependencies
├── .gitignore                                  <- Clean Git ignore rules (no .venv, cache, or raw/processed data)
│
├── .github/workflows/
│   └── ci.yml                                  <- GitHub Actions: installs deps & runs the test suite
│
├── tests/                                      <- Pytest unit tests for src/ (fixtures, no large data needed)
│   ├── test_data_cleaning.py
│   ├── test_analysis.py
│   └── test_build_database.py
│
├── data/
│   ├── raw/                                    <- Immutable raw datasets (SHA-256 verified, gitignored)
│   │   ├── m1_survey_data.csv                  <- Primary developer survey (28.5 MB)
│   │   ├── jobs.json                           <- 27,005 tech job postings (12.9 MB)
│   │   └── Programming_Languages.html          <- Scraped benchmark table
│   ├── processed/                              <- Cleaned, wrangled & 1NF normalized tables (gitignored)
│   │   ├── capstone.db                         <- Relational SQLite database (built by src/build_database.py)
│   │   ├── cleaned_survey_data.csv             <- Deduplicated & imputed master dataset
│   │   ├── respondent_demographics.csv         <- Core demographic & compensation table
│   │   ├── respondent_languages.csv            <- 1NF normalized languages table
│   │   ├── respondent_databases.csv            <- 1NF normalized databases table
│   │   ├── respondent_dev_environments.csv     <- 1NF normalized IDEs table
│   │   ├── respondent_roles.csv                <- 1NF normalized roles table
│   │   ├── job_postings_skills_demand.csv      <- Skill counts from 27k job postings
│   │   └── popular_languages_scraped.csv       <- Cleaned language salary benchmarks
│   └── README.md                               <- Data governance and immutability policy
│
├── notebooks/                                  <- Executable narrative Jupyter Notebooks
│   ├── 01_data_understanding.ipynb             <- Schema profiling & initial assessment
│   ├── 02_data_collection.ipynb                <- API querying & BeautifulSoup web scraping
│   ├── 03_data_wrangling.ipynb                 <- Deduplication, imputation & normalization
│   ├── 04_exploratory_data_analysis.ipynb      <- IQR outlier analysis & distributions
│   ├── 05_statistical_analysis.ipynb           <- Mann-Whitney U, t-test & Chi-Square
│   └── 06_data_visualization.ipynb             <- Publication-grade figures & storytelling
│
├── src/                                        <- Modular, reusable Python source code
│   ├── __init__.py
│   ├── data_collection.py                      <- Ingestion, API extraction & web scraping
│   ├── data_cleaning.py                        <- Cleaning, imputation & 1NF decomposition
│   ├── build_database.py                       <- Provisions capstone.db from schema.sql + processed CSVs
│   └── analysis.py                             <- Statistical & aggregation functions
│
├── sql/                                        <- Relational database scripts
│   ├── schema.sql                              <- DDL table definitions, keys & indexes
│   └── analysis.sql                            <- 10 enterprise SQL analytical queries
│
├── visualizations/                             <- High-resolution exported figures (300 DPI)
│   ├── 01_top_languages_current_vs_desired.png
│   ├── 02_top_databases_migration_shift.png
│   ├── 03_ide_popularity_ranking.png
│   ├── 04_compensation_distribution_and_outliers.png
│   ├── 05_skills_labor_demand_gap.png
│   ├── 06_compensation_by_education.png
│   ├── 07_correlation_heatmap.png
│   └── 08_work_location_and_experience.png
│
├── dashboard/
│   ├── app.py                                  <- Interactive Streamlit BI application
│   └── README.md                               <- App guide & IBM Cognos specification
│
├── reports/
│   └── final_report.md                         <- Comprehensive 17-section executive report
│
├── presentation/
│   └── presentation_outline.md                 <- 15-slide executive presentation briefing
│
└── docs/
    ├── data_dictionary.md                      <- Full schema & column definitions
    ├── project_plan.md                         <- Lifecycle milestone progress tracker
    └── sources.md                              <- Cryptographic lineage & licensing info
```

---

## How to Reproduce & Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/raghavendragolla/ibm-data-analyst-capstone.git
cd ibm-data-analyst-capstone
```

### 2. Set Up Virtual Environment & Install Dependencies
```bash
python -m venv .venv
# On Windows:
.\.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the Automated Ingestion, Cleaning & Database Pipeline
```bash
# Acquire raw datasets & extract job market demand
python src/data_collection.py

# Clean data, normalize compensation & generate 1NF tables
python src/data_cleaning.py

# Provision the relational SQLite database from schema.sql + processed CSVs
python src/build_database.py
```
`data/raw/` and `data/processed/` (including `capstone.db`) are gitignored and
regenerated by these three scripts — see [`data/README.md`](data/README.md).

### 4. Launch the Interactive Dashboard
```bash
streamlit run dashboard/app.py
```

---

## Methodological Limitations
1. **Survey Self-Selection**: Stack Overflow survey respondents disproportionately represent proactive, English-speaking developers.
2. **Cross-Sectional Timing**: Data captures a single survey cycle; future desires represent developer intentions rather than contracted corporate migrations.
3. **Currency Conversions**: Annual compensation figures in USD reflect prevailing exchange rates at the time of collection.

---

## Author & Contact

**Raghavendra Golla**  
*Data Analyst | Python | SQL | Business Intelligence*  
- **GitHub**: [github.com/raghavendragolla](https://github.com/raghavendragolla)  
- **LinkedIn**: [linkedin.com/in/raghavendragolla](https://www.linkedin.com)  
- **Portfolio**: [raghavendragolla.github.io](https://raghavendragolla.github.io)
