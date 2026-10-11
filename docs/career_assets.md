# Career & Portfolio Assets: IBM Data Analyst Capstone

This document provides tailored resume bullets, a LinkedIn project launch post, and portfolio website showcase copy based strictly on the actual implementation and verified results of this project.

---

## 1. Resume Bullet Points

### Bullet Option 1 (Full Analytics Lifecycle Focus):
- **Engineered an end-to-end analytics pipeline** analyzing 11,398 developer survey records and 27,005 job postings using Python (Pandas, SciPy) and SQLite, finding that Python is the only top-five language with rising developer interest (+15.3%) and that PostgreSQL is the most-desired database (38.0% of respondents).

### Bullet Option 2 (Statistical Rigor & Data Engineering Focus):
- **Architected a 1NF normalized relational database** with SQL window functions and CTEs; performed inferential hypothesis testing (Mann-Whitney U, Welch's t-test, Chi-Square), validating that remote developers deliver equal work hours ($p = 0.272$) and disproving degree salary premiums ($p = 0.068$).

### Bullet Option 3 (Business Impact & BI Dashboard Focus):
- **Built an interactive multi-tab Streamlit BI dashboard** with dynamic geographic and working-model filters; translated data findings into an executive strategy report advising C-suite stakeholders on workforce reskilling and skill-first hiring.

---

## 2. LinkedIn Project Launch Post

```markdown
🚀 Excited to share my latest portfolio project: Global Technology Trends & Skills Intelligence!

As part of the IBM Data Analyst Professional Certificate Capstone, I built an end-to-end data analytics project evaluating how developer technology adoption compares with real employer labor market demand.

Key Highlights of the Project:
📊 Multi-Source Pipeline: Ingested and cryptographically verified 11,398 developer survey records, 27,005 live tech job postings, and industry salary benchmarks.
🧹 Data Hygiene & Engineering: Resolved 154 duplicate submissions, addressed right-skewed compensation ($131k mean vs $57k median) via Tukey's IQR outlier fences, and normalized delimited survey strings into 1NF relational tables in SQLite.
🔍 Advanced SQL Analytics: Authored 10 enterprise SQL queries utilizing CTEs, window functions (DENSE_RANK), and relational joins to calculate skill supply vs. demand ratios.
🧪 Inferential Statistics: Conducted Mann-Whitney U, Welch's t-test, and Chi-Square tests—statistically proving that remote engineers work identical weekly hours to in-office staff (p = 0.272) and debunking the assumption that Master's degrees command an automatic pay premium in software roles (p = 0.068).
📈 Interactive BI Dashboard: Developed a multi-tab Streamlit application with live geographic filters and executive KPI metrics.

💡 Core Takeaway: Python (the only top-five language with rising interest, +15.3%) and PostgreSQL (the most-desired database, 38.0%) are key growth areas, while SQL and JavaScript remain the non-negotiable anchor skills demanded by employers.

Check out the full open-source repository, code, and executive briefing on GitHub:
👉 https://github.com/raghavendragolla/ibm-data-analyst-capstone

#DataAnalytics #Python #SQL #DataScience #Streamlit #BusinessIntelligence #Portfolio #IBM #DataVisualization
```

---

## 3. Portfolio Website Showcase Copy

### Project Card:
- **Title**: Global Technology Trends & Skills Intelligence
- **Category**: Data Analytics & Business Intelligence
- **Tools**: Python, Pandas, SQLite, SciPy, Streamlit, Plotly, Seaborn
- **Short Summary**: End-to-end analytics evaluating 11,000+ developer profiles and 27,000+ job listings to identify technology momentum, supply-demand gaps, and compensation benchmarks for enterprise consulting leadership.

### Project Overview Modal:
- **Problem**: Global consulting firms face costly bench downtime and misaligned hiring budgets due to rapid shifts in technology ecosystems.
- **Approach**: Built reproducible data collection scripts, cleaned data with IQR outlier detection, normalized delimited text into relational tables in SQLite, tested hypotheses with Mann-Whitney U and Chi-Square tests, and created an interactive Streamlit BI application.
- **Result**: Proved that Master's degrees do not grant a significant salary premium ($p = 0.068$) and showed that Python's desired user count grows by 15.3% while PostgreSQL is the most-desired database (38.0%), providing C-suite stakeholders with clear roadmaps for hiring and reskilling.
