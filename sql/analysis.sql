-- =============================================================================
-- SQL Analytical Queries: Technology Trends & Skills Intelligence
-- IBM Data Analyst Capstone Project
-- Engine: SQLite / ANSI SQL Compatible
-- Database: data/processed/capstone.db
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Query 1: Top 10 Most Popular Programming Languages Currently in Production
-- Business Question: What languages dominate current developer workflows?
-- -----------------------------------------------------------------------------
SELECT 
    Language,
    COUNT(Respondent) AS Developer_Count,
    ROUND((COUNT(Respondent) * 100.0 / (SELECT COUNT(*) FROM respondents)), 2) AS Adoption_Rate_Pct
FROM respondent_languages
WHERE Usage_Status = 'Current'
GROUP BY Language
ORDER BY Developer_Count DESC
LIMIT 10;

-- -----------------------------------------------------------------------------
-- Query 2: Top 10 Most Desired Programming Languages for Next Year
-- Business Question: What programming skills represent emerging future demand?
-- -----------------------------------------------------------------------------
SELECT 
    Language,
    COUNT(Respondent) AS Desired_Count,
    ROUND((COUNT(Respondent) * 100.0 / (SELECT COUNT(*) FROM respondents)), 2) AS Desired_Rate_Pct
FROM respondent_languages
WHERE Usage_Status = 'Desired'
GROUP BY Language
ORDER BY Desired_Count DESC
LIMIT 10;

-- -----------------------------------------------------------------------------
-- Query 3: Programming Language Momentum & Growth Ratio (CTE Analysis)
-- Business Question: Which languages are growing in developer interest vs. losing momentum?
-- Note: FULL OUTER JOIN requires SQLite >= 3.39; emulated below with
-- LEFT JOIN + UNION so this runs on any SQLite/ANSI-SQL engine.
-- -----------------------------------------------------------------------------
WITH CurrentLang AS (
    SELECT Language, COUNT(Respondent) AS Current_Users
    FROM respondent_languages
    WHERE Usage_Status = 'Current'
    GROUP BY Language
),
DesiredLang AS (
    SELECT Language, COUNT(Respondent) AS Desired_Users
    FROM respondent_languages
    WHERE Usage_Status = 'Desired'
    GROUP BY Language
),
Combined AS (
    SELECT
        c.Language AS Language,
        COALESCE(c.Current_Users, 0) AS Current_Users,
        COALESCE(d.Desired_Users, 0) AS Desired_Users
    FROM CurrentLang c
    LEFT JOIN DesiredLang d ON c.Language = d.Language
    UNION
    SELECT
        d.Language AS Language,
        COALESCE(c.Current_Users, 0) AS Current_Users,
        COALESCE(d.Desired_Users, 0) AS Desired_Users
    FROM DesiredLang d
    LEFT JOIN CurrentLang c ON c.Language = d.Language
)
SELECT
    Language,
    Current_Users,
    Desired_Users,
    (Desired_Users - Current_Users) AS Net_Interest_Delta,
    ROUND(((Desired_Users * 1.0 / NULLIF(Current_Users, 0)) - 1.0) * 100, 2) AS Growth_Momentum_Pct
FROM Combined
WHERE Current_Users >= 500 OR Desired_Users >= 500
ORDER BY Growth_Momentum_Pct DESC;

-- -----------------------------------------------------------------------------
-- Query 4: Top 10 Production Databases Currently in Use
-- Business Question: Which database technologies anchor backend enterprise systems?
-- -----------------------------------------------------------------------------
SELECT 
    Database,
    COUNT(Respondent) AS Active_Deployments,
    ROUND((COUNT(Respondent) * 100.0 / (SELECT COUNT(*) FROM respondents)), 2) AS Market_Share_Pct
FROM respondent_databases
WHERE Usage_Status = 'Current'
GROUP BY Database
ORDER BY Active_Deployments DESC
LIMIT 10;

-- -----------------------------------------------------------------------------
-- Query 5: Top 10 Emerging Databases Desired for Future Adoption
-- Business Question: Which databases should our data architecture team evaluate for modern pipelines?
-- -----------------------------------------------------------------------------
SELECT 
    Database,
    COUNT(Respondent) AS Aspirational_Adoptions,
    ROUND((COUNT(Respondent) * 100.0 / (SELECT COUNT(*) FROM respondents)), 2) AS Aspiration_Share_Pct
FROM respondent_databases
WHERE Usage_Status = 'Desired'
GROUP BY Database
ORDER BY Aspirational_Adoptions DESC
LIMIT 10;

-- -----------------------------------------------------------------------------
-- Query 6: Development Environments (IDEs) Ranking (Window Functions)
-- Business Question: What development tooling should be standardized across engineering teams?
-- -----------------------------------------------------------------------------
SELECT 
    DENSE_RANK() OVER (ORDER BY COUNT(Respondent) DESC) AS IDE_Rank,
    IDE,
    COUNT(Respondent) AS User_Count,
    ROUND((COUNT(Respondent) * 100.0 / (SELECT COUNT(*) FROM respondents)), 2) AS Adoption_Pct
FROM respondent_dev_environments
GROUP BY IDE
ORDER BY IDE_Rank ASC
LIMIT 10;

-- -----------------------------------------------------------------------------
-- Query 7: Compensation Benchmarking Across Educational Attainment Levels
-- Business Question: Does formal graduate education correspond to higher median pay in tech?
-- -----------------------------------------------------------------------------
SELECT 
    CASE 
        WHEN EdLevel LIKE '%Bachelor%' THEN 'Bachelor''s Degree'
        WHEN EdLevel LIKE '%Master%' THEN 'Master''s Degree'
        WHEN EdLevel LIKE '%Doctoral%' OR EdLevel LIKE '%Other doctoral%' THEN 'Doctorate (Ph.D.)'
        WHEN EdLevel LIKE '%Some college%' THEN 'Some College / Non-Degree'
        WHEN EdLevel LIKE '%Secondary%' THEN 'Secondary School'
        WHEN EdLevel LIKE '%Associate%' THEN 'Associate Degree'
        ELSE 'Other / Professional'
    END AS Education_Tier,
    COUNT(Respondent) AS Sample_Size,
    ROUND(AVG(ConvertedComp), 2) AS Mean_Compensation_USD,
    ROUND(AVG(WorkWeekHrs), 1) AS Avg_Weekly_Hours
FROM respondents
WHERE ConvertedComp IS NOT NULL AND ConvertedComp > 0
GROUP BY Education_Tier
ORDER BY Mean_Compensation_USD DESC;

-- -----------------------------------------------------------------------------
-- Query 8: Supply vs. Demand Gap Analysis (Survey Adoption vs. Employer Requisitions)
-- Business Question: Are developers over-investing in skills that employers are not hiring for?
-- -----------------------------------------------------------------------------
WITH DeveloperSkills AS (
    SELECT 
        Language AS Technology,
        COUNT(Respondent) AS Developer_Count,
        ROUND((COUNT(Respondent) * 100.0 / (SELECT COUNT(*) FROM respondents)), 2) AS Dev_Adoption_Pct
    FROM respondent_languages
    WHERE Usage_Status = 'Current'
    GROUP BY Language
)
SELECT 
    d.Technology,
    d.Developer_Count,
    d.Dev_Adoption_Pct,
    j.Posting_Count AS Job_Postings_Count,
    j.Market_Demand_Share_Pct,
    ROUND((j.Market_Demand_Share_Pct / NULLIF(d.Dev_Adoption_Pct, 0)), 2) AS Demand_to_Supply_Ratio
FROM DeveloperSkills d
INNER JOIN job_postings_demand j ON LOWER(d.Technology) = LOWER(j.Technology)
ORDER BY j.Posting_Count DESC;

-- -----------------------------------------------------------------------------
-- Query 9: Work Location Preferences and Average Hours by Employment Type
-- Business Question: What is the distribution of remote vs. office work models?
-- -----------------------------------------------------------------------------
SELECT 
    WorkLoc AS Working_Location,
    Employment,
    COUNT(Respondent) AS Headcount,
    ROUND(AVG(WorkWeekHrs), 1) AS Avg_Work_Week_Hours,
    ROUND(AVG(Age), 1) AS Avg_Age
FROM respondents
WHERE WorkWeekHrs BETWEEN 10 AND 100
GROUP BY WorkLoc, Employment
ORDER BY Headcount DESC;

-- -----------------------------------------------------------------------------
-- Query 10: Career Satisfaction vs. Job Satisfaction Cross-Tabulation
-- Business Question: How do career contentment and workplace satisfaction correlate?
-- -----------------------------------------------------------------------------
SELECT 
    CareerSat AS Career_Satisfaction,
    COUNT(CASE WHEN JobSat LIKE '%satisfied%' THEN 1 END) AS Satisfied_With_Job,
    COUNT(CASE WHEN JobSat LIKE '%dissatisfied%' THEN 1 END) AS Dissatisfied_With_Job,
    COUNT(CASE WHEN JobSat LIKE '%Neither%' THEN 1 END) AS Neutral_Job_Sat,
    COUNT(*) AS Total_Respondents
FROM respondents
WHERE CareerSat IS NOT NULL AND JobSat IS NOT NULL
GROUP BY CareerSat
ORDER BY Total_Respondents DESC;
