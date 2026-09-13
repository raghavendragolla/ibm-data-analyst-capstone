"""Tests for src/data_cleaning.py using small synthetic fixtures (no dependency
on the real 28MB survey dataset)."""

import pandas as pd
import pytest

from src.data_cleaning import build_normalized_relational_tables, clean_raw_survey_data

RAW_COLUMNS = [
    "Respondent", "EdLevel", "WorkLoc", "CompFreq", "CompTotal",
    "LanguageWorkedWith", "LanguageDesireNextYear",
    "DatabaseWorkedWith", "DatabaseDesireNextYear",
    "DevEnviron", "DevType",
]

RAW_ROWS = [
    # (Respondent, EdLevel, WorkLoc, CompFreq, CompTotal, LangWorked, LangDesire, DbWorked, DbDesire, DevEnviron, DevType)
    [1, "Bachelor's degree", "Home", "Yearly", 100000, "Python;SQL", "Python;Go", "PostgreSQL", "PostgreSQL", "VS Code", "Data scientist"],
    [2, "Master's degree", None, "Monthly", 5000, "JavaScript", "TypeScript", "MySQL", "MongoDB", "PyCharm", "Back-end developer"],
    [3, None, "Office", "Weekly", 1000, "Java", "Python", None, "Redis", "VS Code", "Back-end developer"],
    [3, None, "Office", "Weekly", 1000, "Java", "Python", None, "Redis", "VS Code", "Back-end developer"],  # exact + Respondent duplicate
    [4, "Bachelor's degree", "Office", "Yearly", 90000, "Python", "Rust", "MySQL", "Redis", "VS Code", "Data scientist"],
]


@pytest.fixture
def raw_csv(tmp_path):
    path = tmp_path / "raw.csv"
    pd.DataFrame(RAW_ROWS, columns=RAW_COLUMNS).to_csv(path, index=False)
    return path


def test_deduplicates_on_respondent(raw_csv, tmp_path):
    df_clean, metrics = clean_raw_survey_data(
        raw_csv_path=str(raw_csv), output_clean_csv=str(tmp_path / "clean.csv")
    )
    assert metrics["initial_rows"] == 5
    assert metrics["cleaned_rows"] == 4
    assert metrics["respondent_duplicates_removed"] == 1
    assert df_clean["Respondent"].is_unique


def test_mode_imputation_fills_missing_categoricals(raw_csv, tmp_path):
    df_clean, metrics = clean_raw_survey_data(
        raw_csv_path=str(raw_csv), output_clean_csv=str(tmp_path / "clean.csv")
    )
    assert df_clean["WorkLoc"].isna().sum() == 0
    assert df_clean["EdLevel"].isna().sum() == 0
    # Office is the mode among {Home, Office} once the duplicate is dropped.
    assert metrics["workloc_imputed_value"] == "Office"


@pytest.mark.parametrize(
    "freq, total, expected_annual",
    [("Yearly", 100000, 100000), ("Monthly", 5000, 60000), ("Weekly", 1000, 52000)],
)
def test_compensation_normalized_to_annual(raw_csv, tmp_path, freq, total, expected_annual):
    df_clean, _ = clean_raw_survey_data(
        raw_csv_path=str(raw_csv), output_clean_csv=str(tmp_path / "clean.csv")
    )
    row = df_clean[(df_clean["CompFreq"] == freq) & (df_clean["CompTotal"] == total)]
    assert row["NormalizedCompensation"].iloc[0] == expected_annual


def test_output_csv_is_written(raw_csv, tmp_path):
    output_path = tmp_path / "clean.csv"
    clean_raw_survey_data(raw_csv_path=str(raw_csv), output_clean_csv=str(output_path))
    assert output_path.exists()


def test_unnests_semicolon_delimited_languages_into_current_and_desired(raw_csv, tmp_path):
    df_clean, _ = clean_raw_survey_data(
        raw_csv_path=str(raw_csv), output_clean_csv=str(tmp_path / "clean.csv")
    )
    tables = build_normalized_relational_tables(df_clean, output_dir=str(tmp_path))
    languages = tables["languages"]

    # Respondent 1 worked with Python and SQL, desires Python and Go.
    resp1 = languages[languages["Respondent"] == 1]
    current = set(resp1[resp1["Usage_Status"] == "Current"]["Language"])
    desired = set(resp1[resp1["Usage_Status"] == "Desired"]["Language"])
    assert current == {"Python", "SQL"}
    assert desired == {"Python", "Go"}


def test_unnested_tables_are_written_to_disk(raw_csv, tmp_path):
    df_clean, _ = clean_raw_survey_data(
        raw_csv_path=str(raw_csv), output_clean_csv=str(tmp_path / "clean.csv")
    )
    build_normalized_relational_tables(df_clean, output_dir=str(tmp_path))
    for fname in [
        "respondent_demographics.csv", "respondent_languages.csv",
        "respondent_databases.csv", "respondent_dev_environments.csv",
        "respondent_roles.csv",
    ]:
        assert (tmp_path / fname).exists()
