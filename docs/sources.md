# Data Sources & Lineage Documentation

This document maintains the cryptographic provenance, extraction methods, schema attributes, and licensing details for all datasets used in the **IBM Data Analyst Capstone Project**.

---

## 1. Primary Dataset: Stack Overflow Developer Survey (IBM Subset)

* **Source Name**: IBM Skills Network Developer Survey Sample (`m1_survey_data.csv`)
* **Authoritative URL**: `https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv`
* **Original Provenance**: Annual Stack Overflow Developer Survey (2019 sample curated by IBM for Capstone analysis).
* **Role in Project**: Primary dataset for understanding technology usage, career satisfaction, demographics, developer compensation, and future skill aspirations.
* **Format & Size**: CSV format | 28,512,734 bytes (~28.5 MB) | ~11,552 raw records, 85 columns.
* **Acquisition Date**: September 13, 2026
* **Cryptographic Checksum (SHA-256)**:
  `78cedfca3f0a21f78090be1b19f938f605301d08303d90d9e6babbd321563d0f`
* **Storage Location**: `data/raw/m1_survey_data.csv` (Immutable original file).
* **Key Columns**:
  * `Respondent`: Unique survey respondent ID (subject to deduplication audit).
  * `MainBranch`: Professional developer classification.
  * `Country`: Geographic location of respondent.
  * `EdLevel`, `UndergradMajor`: Educational background.
  * `YearsCode`, `YearsCodePro`: Coding experience metrics.
  * `DevType`: Specific developer roles (semicolon-delimited multi-response).
  * `CompTotal`, `CompFreq`, `ConvertedComp`: Raw and normalized annual compensation figures.
  * `LanguageWorkedWith`, `LanguageDesireNextYear`: Current vs. aspirational programming languages.
  * `DatabaseWorkedWith`, `DatabaseDesireNextYear`: Current vs. aspirational databases.
  * `PlatformWorkedWith`, `PlatformDesireNextYear`: Cloud and operating platforms.
  * `WebFrameWorkedWith`, `WebFrameDesireNextYear`: Web frameworks.
  * `DevEnviron`: Integrated development environments (IDEs).
  * `Age`, `Gender`, `WorkWeekHrs`, `WorkLoc`: Demographics and working preferences.

---

## 2. Secondary Dataset: Job Market Demand Postings (API Endpoint)

* **Source Name**: PromptCloud Naukri Job Postings Sample (`jobs.json`)
* **Authoritative URL**: `https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json`
* **Original Provenance**: PromptCloud tech job postings dataset on Kaggle (licensed under Open Public Domain / CC0).
* **Role in Project**: Represents employer hiring demand to cross-examine developer self-reported skills against live market requirements.
* **Format & Size**: JSON Array | 12,878,382 bytes (~12.9 MB) | 27,005 job posting records.
* **Acquisition Date**: September 13, 2026
* **Cryptographic Checksum (SHA-256)**:
  `d527cbb5ac73ab342610559ff4d785e2f3fb0509fa44965b8c4fb3ad842a9139`
* **Storage Location**: `data/raw/jobs.json` (Immutable original file).
* **Key Columns / JSON Keys**:
  * `Id`: Unique job identifier.
  * `Job Title`: Title of advertised position.
  * `Job Experience Required`: Experience bracket required by employer.
  * `Key Skills`: Semicolon/comma-delimited skills keywords (e.g., Python, SQL, Java).
  * `Role Category`: Functional role designation.
  * `Location`: Hiring location.
  * `Functional Area`: Business domain.

---

## 3. Tertiary Dataset: Programming Languages Benchmark (Web Scraping)

* **Source Name**: IBM Skills Network Programming Language Salary & Popularity Benchmark (`Programming_Languages.html`)
* **Authoritative URL**: `https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html`
* **Original Provenance**: Curated HTML benchmark table hosted by IBM Skills Network.
* **Role in Project**: External benchmark to compare surveyed language popularity and compensation against baseline industry averages and learning curves.
* **Format & Size**: HTML | 2,170 bytes | 10 language benchmark records.
* **Acquisition Date**: September 13, 2026
* **Cryptographic Checksum (SHA-256)**:
  `8f6d5aaa3a6fdfd0f3fb0e1b7c976b093b2c33ae301f175b6458b6947763bb56`
* **Storage Location**: `data/raw/Programming_Languages.html` (Immutable original file).
* **Key Fields Extracted via Scraping**:
  * `Language`: Programming language name.
  * `Average Annual Salary`: Baseline market compensation.
  * `Learning Difficulty`: Relative difficulty / barrier to entry.

---

## Data Governance & Reproducibility Policy

1. **Strict Immutability**: All original files in `data/raw/` are read-only inputs. Any transformations, cleaning, imputations, or aggregations must be saved into `data/processed/`.
2. **Deterministic Regeneration**: Running `python src/data_collection.py` verifies or re-acquires all three raw files deterministically against their SHA-256 signatures.
