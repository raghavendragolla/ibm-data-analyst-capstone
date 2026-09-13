-- =============================================================================
-- Database Schema Definitions (DDL)
-- IBM Data Analyst Capstone Project
-- Engine: SQLite / ANSI SQL Compatible
-- Database: data/processed/capstone.db
-- =============================================================================

DROP TABLE IF EXISTS respondent_languages;
DROP TABLE IF EXISTS respondent_databases;
DROP TABLE IF EXISTS respondent_dev_environments;
DROP TABLE IF EXISTS respondent_roles;
DROP TABLE IF EXISTS job_postings_demand;
DROP TABLE IF EXISTS programming_languages_benchmark;
DROP TABLE IF EXISTS respondents;

-- -----------------------------------------------------------------------------
-- 1. Core Respondents Table (1NF Demographics & Normalized Compensation)
-- -----------------------------------------------------------------------------
CREATE TABLE respondents (
    Respondent INTEGER PRIMARY KEY,
    MainBranch TEXT,
    Hobbyist TEXT,
    Employment TEXT,
    Country TEXT,
    Student TEXT,
    EdLevel TEXT,
    UndergradMajor TEXT,
    OrgSize TEXT,
    YearsCode INTEGER,
    YearsCodePro INTEGER,
    CareerSat TEXT,
    JobSat TEXT,
    WorkLoc TEXT,
    WorkWeekHrs REAL,
    CompFreq TEXT,
    CompTotal REAL,
    ConvertedComp REAL,
    NormalizedCompensation REAL,
    Age REAL,
    Gender TEXT,
    Dependents TEXT
);

-- -----------------------------------------------------------------------------
-- 2. Respondent Languages Junction Table (1NF Normalized)
-- -----------------------------------------------------------------------------
CREATE TABLE respondent_languages (
    Respondent INTEGER,
    Language TEXT NOT NULL,
    Usage_Status TEXT NOT NULL CHECK(Usage_Status IN ('Current', 'Desired')),
    PRIMARY KEY (Respondent, Language, Usage_Status),
    FOREIGN KEY (Respondent) REFERENCES respondents (Respondent) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 3. Respondent Databases Junction Table (1NF Normalized)
-- -----------------------------------------------------------------------------
CREATE TABLE respondent_databases (
    Respondent INTEGER,
    Database TEXT NOT NULL,
    Usage_Status TEXT NOT NULL CHECK(Usage_Status IN ('Current', 'Desired')),
    PRIMARY KEY (Respondent, Database, Usage_Status),
    FOREIGN KEY (Respondent) REFERENCES respondents (Respondent) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 4. Respondent Development Environments (IDEs) Table
-- -----------------------------------------------------------------------------
CREATE TABLE respondent_dev_environments (
    Respondent INTEGER,
    IDE TEXT NOT NULL,
    PRIMARY KEY (Respondent, IDE),
    FOREIGN KEY (Respondent) REFERENCES respondents (Respondent) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 5. Respondent Roles Table
-- -----------------------------------------------------------------------------
CREATE TABLE respondent_roles (
    Respondent INTEGER,
    Role TEXT NOT NULL,
    PRIMARY KEY (Respondent, Role),
    FOREIGN KEY (Respondent) REFERENCES respondents (Respondent) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 6. Job Market Demand Benchmark Table
-- -----------------------------------------------------------------------------
CREATE TABLE job_postings_demand (
    Technology TEXT PRIMARY KEY,
    Posting_Count INTEGER NOT NULL,
    Market_Demand_Share_Pct REAL NOT NULL
);

-- -----------------------------------------------------------------------------
-- 7. Programming Languages Salary Benchmark Table
-- -----------------------------------------------------------------------------
CREATE TABLE programming_languages_benchmark (
    Rank INTEGER PRIMARY KEY,
    Language TEXT UNIQUE NOT NULL,
    Created_By TEXT,
    Avg_Annual_Salary_USD REAL NOT NULL,
    Learning_Difficulty TEXT
);

-- -----------------------------------------------------------------------------
-- Performance Indexes for Fast Analytical Joins and Aggregations
-- -----------------------------------------------------------------------------
CREATE INDEX idx_lang_name_status ON respondent_languages (Language, Usage_Status);
CREATE INDEX idx_db_name_status ON respondent_databases (Database, Usage_Status);
CREATE INDEX idx_ide_name ON respondent_dev_environments (IDE);
CREATE INDEX idx_role_name ON respondent_roles (Role);
CREATE INDEX idx_resp_country ON respondents (Country);
CREATE INDEX idx_resp_comp ON respondents (NormalizedCompensation);
