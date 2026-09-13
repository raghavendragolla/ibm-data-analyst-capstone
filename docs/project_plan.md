# Project Plan & Milestones: IBM Data Analyst Capstone

This document tracks the phased lifecycle and completion status of the **IBM Data Analyst Capstone Project**.

---

## Project Status: 100% Completed (Portfolio & Publication Ready)

- [x] **Phase 0: Project Research & Blueprint Alignment**
  - Authoritative IBM Capstone curriculum scope established
  - Project blueprint approved with data governance commitments
- [x] **Phase 1: Project Architecture & Environment Setup**
  - Repository structure created with separation of concerns (`data/`, `notebooks/`, `src/`, `sql/`, `visualizations/`, `dashboard/`, `reports/`, `presentation/`, `docs/`)
  - Virtual environment (`.venv`) configured with pinned `requirements.txt`
  - Git repository initialized and linked to GitHub remote
- [x] **Phase 2: Authentic Dataset Acquisition & Verification**
  - Developer survey (`m1_survey_data.csv`, 28.5 MB) downloaded from IBM Skills Network
  - Labor market postings (`jobs.json`, 12.9 MB) and benchmark table (`Programming_Languages.html`, 2.1 KB) acquired
  - SHA-256 cryptographic verification and lineage recorded in `docs/sources.md`
- [x] **Phase 3: Data Understanding & Initial Quality Assessment**
  - Audited 85 attributes, memory footprint, and data types
  - Identified 154 duplicate respondent records and severe compensation right-skewness
  - Exhaustive data dictionary compiled in `docs/data_dictionary.md`
  - Runnable audit notebook created in `notebooks/01_data_understanding.ipynb`
- [x] **Phase 4: Data Collection Demonstrations (APIs & Web Scraping)**
  - BeautifulSoup HTML parser engineered for salary benchmarks
  - Regex word-boundary API simulation across 27,005 job postings
  - Output tables generated in `data/processed/` and documented in `notebooks/02_data_collection.ipynb`
- [x] **Phase 5: Data Cleaning & Quality Audit**
  - Removed 154 duplicate submissions (retaining 11,398 unique respondents)
  - Mode imputation executed for `WorkLoc` ('Office') and `EdLevel`
  - UTF-8 non-ASCII encoding repairs applied in `src/data_cleaning.py`
- [x] **Phase 6: Data Wrangling & 1NF Normalization**
  - Harmonized compensation cycles to annual `NormalizedCompensation` (Median = $100,000)
  - Unnested multi-response delimited strings into 5 relational tables in `data/processed/`
  - Documented wrangling pipeline in `notebooks/03_data_wrangling.ipynb`
- [x] **Phase 7: Relational Database Modeling & SQL Analytics**
  - Provisioned SQLite database (`data/processed/capstone.db`) with keys and indexes (`sql/schema.sql`), built deterministically via `src/build_database.py`
  - Authored 10 enterprise SQL queries with CTEs and window functions in `sql/analysis.sql`
- [x] **Phase 8: Exploratory Data Analysis (EDA)**
  - Evaluated distribution skewness (5.38) and 5-number summaries
  - Isolated 879 high-earning salary outliers via Tukey's IQR fences ($209,698 fence)
  - Completed narrative analysis in `notebooks/04_exploratory_data_analysis.ipynb`
- [x] **Phase 9: Inferential Statistics & Hypothesis Testing**
  - Mann-Whitney U test confirmed no statistically significant degree pay premium ($p = 0.068$)
  - Welch's t-test proved remote developers work equal hours to in-office staff ($p = 0.272$)
  - Chi-Square test proved dissatisfaction directly drives active job seeking ($\chi^2 = 2,692, p < 0.0001$)
  - Analysis documented in `notebooks/05_statistical_analysis.ipynb`
- [x] **Phase 10: Production Visualizations & Data Storytelling**
  - 8 high-resolution 300-DPI charts exported to `visualizations/`
  - Documented narrative storytelling framework in `notebooks/06_data_visualization.ipynb`
- [x] **Phase 11: Interactive Executive BI Dashboard**
  - Built multi-tab interactive Streamlit & Plotly BI application (`dashboard/app.py`)
  - Documented local run instructions and IBM Cognos Analytics specifications in `dashboard/README.md`
- [x] **Phase 12: Business Insights & Strategic Recommendations**
  - Synthesized evidence-based strategic roadmaps for CTO, HR, and L&D
- [x] **Phase 13: Comprehensive Final Report**
  - 17-section executive report authored in `reports/final_report.md`
- [x] **Phase 14: Presentation Slide Deck**
  - 15-slide executive presentation briefing prepared in `presentation/presentation_outline.md`
- [x] **Phase 15: GitHub README & Repository Polish**
  - Recruiter-grade root `README.md` with badges, architecture, workflow, and instructions
- [x] **Phase 16–18: Career Integration & Interview Preparation**
  - 30-sec, 1-min, and 3-min interview pitches and 8 detailed technical Q&As in `docs/interview_preparation.md`
  - Action-oriented resume bullet points and LinkedIn project launch post in `docs/career_assets.md`
