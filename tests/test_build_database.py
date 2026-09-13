"""Tests for src/build_database.py -- the script that provisions capstone.db
from sql/schema.sql and the processed CSVs. Uses tiny fixture CSVs written to
a temp directory rather than the real ~24MB database."""

import os
import sqlite3

import pandas as pd
import pytest

from src.build_database import build_database, TABLE_LOAD_ORDER

SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "..", "sql", "schema.sql")

FIXTURE_TABLES = {
    "respondent_demographics.csv": pd.DataFrame({
        "Respondent": [1, 2],
        "MainBranch": ["Developer", "Developer"],
        "Hobbyist": ["Yes", "No"],
        "Employment": ["Employed full-time", "Employed full-time"],
        "Country": ["United States", "India"],
        "Student": ["No", "No"],
        "EdLevel": ["Bachelor's degree", "Master's degree"],
        "UndergradMajor": ["CS", "CS"],
        "OrgSize": ["100 to 499 employees", "20 to 99 employees"],
        "YearsCode": [5, 3],
        "YearsCodePro": [3, 1],
        "CareerSat": ["Very satisfied", "Satisfied"],
        "JobSat": ["Very satisfied", "Satisfied"],
        "WorkLoc": ["Home", "Office"],
        "WorkWeekHrs": [40.0, 45.0],
        "CompFreq": ["Yearly", "Yearly"],
        "CompTotal": [100000.0, 80000.0],
        "ConvertedComp": [100000.0, 80000.0],
        "NormalizedCompensation": [100000.0, 80000.0],
        "Age": [30.0, 28.0],
        "Gender": ["Man", "Woman"],
        "Dependents": ["No", "No"],
    }),
    "respondent_languages.csv": pd.DataFrame({
        "Respondent": [1, 1, 2],
        "Language": ["Python", "SQL", "JavaScript"],
        "Usage_Status": ["Current", "Current", "Desired"],
    }),
    "respondent_databases.csv": pd.DataFrame({
        "Respondent": [1, 2],
        "Database": ["PostgreSQL", "MySQL"],
        "Usage_Status": ["Current", "Current"],
    }),
    "respondent_dev_environments.csv": pd.DataFrame({
        "Respondent": [1, 2],
        "IDE": ["VS Code", "PyCharm"],
    }),
    "respondent_roles.csv": pd.DataFrame({
        "Respondent": [1, 2],
        "Role": ["Data scientist", "Back-end developer"],
    }),
    "job_postings_skills_demand.csv": pd.DataFrame({
        "Technology": ["Python", "SQL"],
        "Posting_Count": [100, 200],
        "Market_Demand_Share_Pct": [10.0, 20.0],
    }),
    "popular_languages_scraped.csv": pd.DataFrame({
        "Rank": [1, 2],
        "Language": ["Python", "JavaScript"],
        "Created_By": ["Guido van Rossum", "Brendan Eich"],
        "Avg_Annual_Salary_USD": [110000.0, 105000.0],
        "Learning_Difficulty": ["Easy", "Easy"],
    }),
}


@pytest.fixture
def processed_dir(tmp_path):
    for filename, df in FIXTURE_TABLES.items():
        df.to_csv(tmp_path / filename, index=False)
    return tmp_path


def test_build_database_creates_all_tables_with_expected_row_counts(processed_dir, tmp_path):
    db_path = tmp_path / "test_capstone.db"
    build_database(schema_path=SCHEMA_PATH, db_path=str(db_path), processed_dir=str(processed_dir))

    assert db_path.exists()
    with sqlite3.connect(db_path) as conn:
        for filename, table_name in TABLE_LOAD_ORDER:
            expected_rows = len(FIXTURE_TABLES[filename])
            actual_rows = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
            assert actual_rows == expected_rows, f"{table_name} row count mismatch"


def test_build_database_is_idempotent_on_rerun(processed_dir, tmp_path):
    db_path = tmp_path / "test_capstone.db"
    build_database(schema_path=SCHEMA_PATH, db_path=str(db_path), processed_dir=str(processed_dir))
    build_database(schema_path=SCHEMA_PATH, db_path=str(db_path), processed_dir=str(processed_dir))

    with sqlite3.connect(db_path) as conn:
        count = conn.execute("SELECT COUNT(*) FROM respondents").fetchone()[0]
    assert count == 2  # schema.sql drops/recreates tables, so no duplication on rerun


def test_build_database_raises_on_missing_csv(tmp_path):
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()
    with pytest.raises(FileNotFoundError):
        build_database(schema_path=SCHEMA_PATH, db_path=str(tmp_path / "x.db"), processed_dir=str(empty_dir))
