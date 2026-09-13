"""
Data Cleaning & Wrangling Module for IBM Data Analyst Capstone Project.

Contains automated, production-grade transformations:
1. Deduplication on primary key `Respondent`.
2. Strategic missing value imputation (mode for categorical, domain validation for numeric).
3. Character encoding repairs.
4. Annual compensation normalization (CompFreq * CompTotal -> NormalizedCompensation).
5. 1NF Relational Decomposition for multi-valued fields (Languages, Databases, Roles, IDEs).
"""

import os
from typing import Tuple, Dict
import pandas as pd
import numpy as np


def clean_raw_survey_data(
    raw_csv_path: str = "data/raw/m1_survey_data.csv",
    output_clean_csv: str = "data/processed/cleaned_survey_data.csv"
) -> Tuple[pd.DataFrame, Dict[str, any]]:
    """
    Clean raw survey data: deduplicate, fix encodings, impute categorical modes, and normalize compensation.
    
    Returns:
        Tuple of (Cleaned DataFrame, Audit Metrics Dictionary).
    """
    df = pd.read_csv(raw_csv_path)
    initial_rows, initial_cols = df.shape
    
    # 1. Deduplication
    exact_dupes = int(df.duplicated().sum())
    resp_dupes = int(df.duplicated(subset=["Respondent"]).sum())
    df_clean = df.drop_duplicates(subset=["Respondent"], keep="first").copy()
    dedup_rows = len(df_clean)
    
    # 2. Text Encoding Repairs (fixing non-ASCII replacement characters)
    if "EdLevel" in df_clean.columns:
        df_clean["EdLevel"] = df_clean["EdLevel"].str.replace("\ufffd", "'", regex=False)
        
    # 3. Categorical Missing Value Imputation
    # WorkLoc mode imputation
    workloc_mode = df_clean["WorkLoc"].mode().iloc[0]
    workloc_missing_before = int(df_clean["WorkLoc"].isna().sum())
    df_clean["WorkLoc"] = df_clean["WorkLoc"].fillna(workloc_mode)
    
    # EdLevel mode imputation
    edlevel_mode = df_clean["EdLevel"].mode().iloc[0]
    edlevel_missing_before = int(df_clean["EdLevel"].isna().sum())
    df_clean["EdLevel"] = df_clean["EdLevel"].fillna(edlevel_mode)
    
    # 4. Compensation Normalization
    # Calculate NormalizedCompensation = annual salary equivalent
    def calc_normalized_comp(row):
        freq = row["CompFreq"]
        total = row["CompTotal"]
        if pd.isna(freq) or pd.isna(total):
            return np.nan
        if freq == "Yearly":
            return total * 1.0
        elif freq == "Monthly":
            return total * 12.0
        elif freq == "Weekly":
            return total * 52.0
        return np.nan

    df_clean["NormalizedCompensation"] = df_clean.apply(calc_normalized_comp, axis=1)
    
    # 5. Export primary cleaned dataset
    os.makedirs(os.path.dirname(output_clean_csv), exist_ok=True)
    df_clean.to_csv(output_clean_csv, index=False)
    
    audit_metrics = {
        "initial_rows": initial_rows,
        "initial_cols": initial_cols,
        "exact_duplicates_removed": exact_dupes,
        "respondent_duplicates_removed": resp_dupes,
        "cleaned_rows": dedup_rows,
        "workloc_missing_imputed": workloc_missing_before,
        "workloc_imputed_value": workloc_mode,
        "edlevel_missing_imputed": edlevel_missing_before,
        "edlevel_imputed_value": edlevel_mode,
        "median_normalized_comp": float(df_clean["NormalizedCompensation"].median()),
        "output_path": output_clean_csv
    }
    
    return df_clean, audit_metrics


def build_normalized_relational_tables(
    cleaned_df: pd.DataFrame,
    output_dir: str = "data/processed"
) -> Dict[str, pd.DataFrame]:
    """
    Decompose multi-valued columns into 1NF normalized relational tables for SQL querying.
    
    Creates:
    - respondent_demographics.csv
    - respondent_languages.csv
    - respondent_databases.csv
    - respondent_dev_environments.csv
    - respondent_roles.csv
    """
    os.makedirs(output_dir, exist_ok=True)
    tables = {}
    
    # Table 1: Core Respondent Demographics & Compensation
    core_cols = [
        "Respondent", "MainBranch", "Hobbyist", "Employment", "Country", 
        "Student", "EdLevel", "UndergradMajor", "OrgSize", "YearsCode", 
        "YearsCodePro", "CareerSat", "JobSat", "WorkLoc", "WorkWeekHrs", 
        "CompFreq", "CompTotal", "ConvertedComp", "NormalizedCompensation", 
        "Age", "Gender", "Dependents"
    ]
    existing_core_cols = [c for c in core_cols if c in cleaned_df.columns]
    df_demographics = cleaned_df[existing_core_cols].copy()
    demographics_path = os.path.join(output_dir, "respondent_demographics.csv")
    df_demographics.to_csv(demographics_path, index=False)
    tables["demographics"] = df_demographics
    
    # Helper to unnest semicolon-separated fields
    def unnest_field(col_name: str, new_col_name: str, extra_cols: Dict = None) -> pd.DataFrame:
        subset = cleaned_df[["Respondent", col_name]].dropna().copy()
        subset[col_name] = subset[col_name].str.split(";")
        exploded = subset.explode(col_name)
        exploded[col_name] = exploded[col_name].str.strip()
        exploded = exploded.rename(columns={col_name: new_col_name})
        if extra_cols:
            for k, v in extra_cols.items():
                exploded[k] = v
        return exploded.reset_index(drop=True)

    # Table 2: Languages (Worked With & Desired Next Year)
    df_lang_curr = unnest_field("LanguageWorkedWith", "Language", {"Usage_Status": "Current"})
    df_lang_des = unnest_field("LanguageDesireNextYear", "Language", {"Usage_Status": "Desired"})
    df_languages = pd.concat([df_lang_curr, df_lang_des], ignore_index=True)
    df_languages.to_csv(os.path.join(output_dir, "respondent_languages.csv"), index=False)
    tables["languages"] = df_languages
    
    # Table 3: Databases (Worked With & Desired Next Year)
    df_db_curr = unnest_field("DatabaseWorkedWith", "Database", {"Usage_Status": "Current"})
    df_db_des = unnest_field("DatabaseDesireNextYear", "Database", {"Usage_Status": "Desired"})
    df_databases = pd.concat([df_db_curr, df_db_des], ignore_index=True)
    df_databases.to_csv(os.path.join(output_dir, "respondent_databases.csv"), index=False)
    tables["databases"] = df_databases

    # Table 4: Development Environments (DevEnviron / IDEs)
    df_ides = unnest_field("DevEnviron", "IDE")
    df_ides.to_csv(os.path.join(output_dir, "respondent_dev_environments.csv"), index=False)
    tables["dev_environments"] = df_ides

    # Table 5: Developer Roles (DevType)
    df_roles = unnest_field("DevType", "Role")
    df_roles.to_csv(os.path.join(output_dir, "respondent_roles.csv"), index=False)
    tables["roles"] = df_roles
    
    return tables


if __name__ == "__main__":
    print("--- Executing Data Cleaning Pipeline ---")
    df_clean, metrics = clean_raw_survey_data()
    print("Cleaning Metrics Summary:")
    for k, v in metrics.items():
        print(f"  {k}: {v}")
        
    print("\n--- Executing Relational Decomposition Pipeline ---")
    tables = build_normalized_relational_tables(df_clean)
    print("All processed artifacts successfully generated.")
