# Interview Preparation Guide: IBM Data Analyst Capstone

This guide prepares you to discuss this project confidently and authoritatively during Data Analyst job interviews.

---

## 1. Project Explanations by Time Horizon

### 30-Second Elevator Pitch
> *"I built an end-to-end Data Analytics project analyzing global technology adoption and labor market demand for an enterprise consulting firm. Working with over 11,000 developer survey records and 27,000 real job postings, I developed an automated ingestion pipeline, engineered a normalized relational database in SQLite, conducted inferential hypothesis testing, and deployed an interactive Streamlit BI dashboard. My analysis identified Python and PostgreSQL as the highest-momentum technologies, while proving that Master's degrees do not command a statistically significant pay premium, helping leadership optimize hiring criteria and reskilling budgets."*

---

### 1-Minute Overview
> *"In this project, I acted as an Associate Data Analyst for a global technology consulting firm. The business problem was identifying which technology skills to prioritize for hiring and internal training, and determining where developer skills diverge from actual employer demand.*
> 
> *I ingested and cryptographically verified three public datasets: an 11,500-record Stack Overflow developer survey, a 27,000-listing tech job postings dataset, and an industry salary benchmark table. After cleaning 154 duplicate respondents and normalizing diverse pay cycles into annual compensation, I decomposed delimited text into first-normal-form relational tables.*
> 
> *Using SQL window functions and CTEs, I discovered that while JavaScript and MySQL lead legacy production, Python is the only top-five language with rising interest (+15.3%) and PostgreSQL is the most-desired database (38.0% of respondents). Using inferential statistics, I ran a Mann-Whitney U test demonstrating that Master's degrees do not yield significantly higher compensation than Bachelor's degrees ($p = 0.068$), and a Welch's t-test showing remote developers log identical hours to in-office staff. Finally, I synthesized these findings into an interactive Streamlit dashboard and an executive strategy report."*

---

### 3-Minute Comprehensive Walkthrough
> *"The objective of this project was to provide executive leadership with a data-driven strategy for talent acquisition and technology consulting roadmaps.*
> 
> *I structured the project following an enterprise analytics lifecycle: Data Collection, Understanding, Wrangling, Relational Modeling, Exploratory Analysis, Hypothesis Testing, Visualization, and Executive Reporting.*
> 
> *During data profiling, I uncovered critical data hygiene issues that would have invalidated downstream metrics if ignored: 154 duplicate respondent IDs, impossible work weeks exceeding 1,000 hours, and severe positive skewness in compensation ($131k mean vs $57k median). I resolved these by deduplicating records, imputing categorical modes, and applying Tukey's Interquartile Range method to isolate 879 high-earning salary outliers beyond the $209,000 fence.*
> 
> *To avoid the anti-pattern of writing complex regex queries against semicolon-delimited text, I redesigned the schema into 1NF normalized tables in SQLite. I then authored 10 production SQL queries using CTEs, window functions like `DENSE_RANK()`, and relational joins across survey skills and employer requisitions.*
> 
> *Next, I conducted formal hypothesis testing. Rather than assuming graduate degrees increase pay, I ran a non-parametric Mann-Whitney U test, which failed to find a statistically significant pay difference between Bachelor's and Master's degree holders ($p = 0.068$). I also tested remote vs. in-office work hours using a Welch's t-test, proving zero productivity loss ($p = 0.272$). Finally, a Chi-Square test ($\chi^2 = 2,692$) proved employee dissatisfaction is the dominant driver of active job hunting.*
> 
> *I packaged the findings into an interactive Streamlit BI application featuring dynamic geographic filters and KPI cards, accompanied by an executive report. My final recommendations advised leadership to remove mandatory Master's degree filters—widening applicant pools by >200%—and launch a dedicated PostgreSQL cloud migration practice to capitalize on enterprise architectural demand."*

---

## 2. Common Technical Interview Questions & Model Answers

### Q1: Why did you choose this project, and what was the business problem?
**Answer**:  
*"I chose this project because it simulates a real-world consulting challenge: how organizations align human capital with technical market shifts. Rather than treating it as an academic exercise, I approached it from the perspective of an enterprise analyst helping executive stakeholders minimize bench idle time and optimize recruiting budgets."*

### Q2: Where did the data come from, and how did you verify its authenticity?
**Answer**:  
*"I utilized three authentic, publicly available datasets from IBM Skills Network and Coursera: a sample of the 2019 Stack Overflow Developer Survey (11,552 raw rows), a dataset of 27,005 tech job postings from PromptCloud/Naukri, and an HTML salary benchmark table. In my data collection script, I computed SHA-256 cryptographic checksums on all raw files to guarantee provenance and source immutability."*

### Q3: What were the most significant data quality issues you discovered?
**Answer**:  
*"The three biggest challenges were:  
1. **Duplicate records**: Exactly 154 rows had duplicate Respondent IDs that would have distorted survey weights.  
2. **Compensation skewness**: Converted compensation had a skewness of 5.38 with salaries reaching $2,000,000, inflating the mean to $131,334 while the median was only $57,744.  
3. **Data-entry errors**: Several respondents reported work weeks up to 1,012 hours (physically impossible in a 168-hour week), requiring domain-specific bounds filtering."*

### Q4: Why did you decompose delimited columns into relational tables?
**Answer**:  
*"In the raw survey, skills were stored as semicolon-delimited strings like `Python;SQL;Java`. Querying this directly in SQL requires computationally expensive `LIKE` or regex operators that violate First Normal Form (1NF). By unnesting them into separate relational junction tables (`respondent_languages`, `respondent_databases`) linked by foreign keys, I achieved sub-second SQL aggregation speed and clean dimensional joins."*

### Q5: What SQL techniques did you demonstrate?
**Answer**:  
*"I authored 10 production queries in SQLite showcasing:  
- **Common Table Expressions (CTEs)** to compute net growth momentum between current and desired skills.  
- **Window Functions** (`DENSE_RANK() OVER`) to rank IDE adoption.  
- **Relational Joins** connecting survey data with job market postings to compute Demand-to-Supply ratios.  
- **Conditional Aggregation** (`CASE WHEN`) to categorize educational tiers and pivot satisfaction matrices."*

### Q6: Why did you use non-parametric tests instead of standard t-tests for compensation?
**Answer**:  
*"A standard two-sample Student's t-test assumes normality. Because compensation is heavily skewed and contains extreme outliers, the normality assumption is violated. Therefore, I utilized the non-parametric Mann-Whitney U test, which compares rank sums rather than means, making it robust against extreme skewness."*

### Q7: What was your most surprising finding?
**Answer**:  
*"The degree attainment test: Master's degree holders in our sample did not earn a statistically significant compensation premium over Bachelor's degree holders ($p = 0.068$). In tech, practical mastery of in-demand stacks and verified project portfolios vastly outweigh formal graduate credentials."*

### Q8: How did you ensure the project is easy for another engineer to reproduce?
**Answer**:  
*"I separated raw data from processed outputs, pinned all dependencies in `requirements.txt`, built modular Python scripts in `src/`, configured `.gitignore` to prevent environment pollution, and provided step-by-step local reproduction instructions in the root `README.md`."*
