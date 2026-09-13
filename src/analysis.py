"""
Analysis Module for IBM Data Analyst Capstone Project.

Contains reusable analytical calculations, SQL query helpers,
and inferential statistical hypothesis testing routines.
"""

import sqlite3
from typing import Dict, Tuple, Optional
import pandas as pd
import numpy as np
from scipy import stats


def query_top_technologies(
    db_path: str,
    tech_type: str = "language",
    status: str = "Current",
    top_n: int = 10
) -> pd.DataFrame:
    """
    Query top technologies by developer adoption count from relational SQLite database.
    
    Args:
        db_path: Path to capstone.db.
        tech_type: 'language' or 'database'.
        status: 'Current' or 'Desired'.
        top_n: Number of records to return.
        
    Returns:
        DataFrame with columns [Technology, Developer_Count, Adoption_Share_Pct].
    """
    table_name = f"respondent_{tech_type}s"
    col_name = "Language" if tech_type == "language" else "Database"
    
    query = f"""
    SELECT 
        {col_name} AS Technology,
        COUNT(Respondent) AS Developer_Count,
        ROUND((COUNT(Respondent) * 100.0 / (SELECT COUNT(*) FROM respondents)), 2) AS Adoption_Share_Pct
    FROM {table_name}
    WHERE Usage_Status = ?
    GROUP BY {col_name}
    ORDER BY Developer_Count DESC
    LIMIT ?;
    """
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query, conn, params=(status, top_n))
    return df


def calculate_technology_momentum(db_path: str, tech_type: str = "language") -> pd.DataFrame:
    """
    Calculate net momentum and percent growth ratio comparing Current usage to Desired future adoption.
    """
    table_name = f"respondent_{tech_type}s"
    col_name = "Language" if tech_type == "language" else "Database"
    
    # FULL OUTER JOIN requires SQLite >= 3.39 (mid-2022) and isn't available on
    # every deployment target. Emulated here with LEFT JOIN + UNION so the
    # query runs on any SQLite/ANSI-SQL engine.
    query = f"""
    WITH Curr AS (
        SELECT {col_name} AS Tech, COUNT(*) AS Current_Count
        FROM {table_name} WHERE Usage_Status = 'Current' GROUP BY {col_name}
    ),
    Des AS (
        SELECT {col_name} AS Tech, COUNT(*) AS Desired_Count
        FROM {table_name} WHERE Usage_Status = 'Desired' GROUP BY {col_name}
    ),
    Combined AS (
        SELECT
            c.Tech AS Technology,
            COALESCE(c.Current_Count, 0) AS Current_Users,
            COALESCE(d.Desired_Count, 0) AS Desired_Users
        FROM Curr c
        LEFT JOIN Des d ON c.Tech = d.Tech
        UNION
        SELECT
            d.Tech AS Technology,
            COALESCE(c.Current_Count, 0) AS Current_Users,
            COALESCE(d.Desired_Count, 0) AS Desired_Users
        FROM Des d
        LEFT JOIN Curr c ON c.Tech = d.Tech
    )
    SELECT
        Technology,
        Current_Users,
        Desired_Users,
        (Desired_Users - Current_Users) AS Net_Interest_Delta,
        ROUND(((Desired_Users * 1.0 / NULLIF(Current_Users, 0)) - 1.0) * 100, 2) AS Growth_Momentum_Pct
    FROM Combined
    WHERE Current_Users >= 300 OR Desired_Users >= 300
    ORDER BY Growth_Momentum_Pct DESC;
    """
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query, conn)
    return df


def perform_iqr_outlier_analysis(series: pd.Series) -> Dict[str, float]:
    """
    Compute Tukey's Interquartile Range (IQR) fences and classify upper/lower outliers.
    """
    clean_s = series.dropna()
    q1 = float(clean_s.quantile(0.25))
    q3 = float(clean_s.quantile(0.75))
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    
    outliers_upper = clean_s[clean_s > upper_fence]
    outliers_lower = clean_s[clean_s < lower_fence]
    filtered_series = clean_s[(clean_s >= lower_fence) & (clean_s <= upper_fence)]
    
    return {
        "n_total": len(clean_s),
        "q1": q1,
        "median_original": float(clean_s.median()),
        "mean_original": float(clean_s.mean()),
        "q3": q3,
        "iqr": iqr,
        "lower_fence": lower_fence,
        "upper_fence": upper_fence,
        "n_upper_outliers": len(outliers_upper),
        "n_lower_outliers": len(outliers_lower),
        "median_trimmed": float(filtered_series.median()),
        "mean_trimmed": float(filtered_series.mean())
    }


def run_degree_compensation_test(df: pd.DataFrame) -> Dict[str, any]:
    """
    Perform Mann-Whitney U test comparing Bachelor's vs. Master's degree compensation.
    """
    bach = df[df["EdLevel"].str.contains("Bachelor", na=False)]["ConvertedComp"].dropna()
    mast = df[df["EdLevel"].str.contains("Master", na=False)]["ConvertedComp"].dropna()
    
    u_stat, u_pval = stats.mannwhitneyu(mast, bach, alternative="two-sided", method="asymptotic")
    
    return {
        "test_name": "Mann-Whitney U Test (Degree Compensation)",
        "sample_bachelor": len(bach),
        "median_bachelor": float(bach.median()),
        "sample_master": len(mast),
        "median_master": float(mast.median()),
        "u_statistic": float(u_stat),
        "p_value": float(u_pval),
        "statistically_significant": bool(u_pval < 0.05)
    }


def run_remote_work_hours_test(df: pd.DataFrame) -> Dict[str, any]:
    """
    Perform Welch's two-sample t-test comparing Remote (Home) vs. Office weekly hours.
    """
    hrs_home = df[(df["WorkLoc"] == "Home") & (df["WorkWeekHrs"].between(10, 80))]["WorkWeekHrs"].dropna()
    hrs_off = df[(df["WorkLoc"] == "Office") & (df["WorkWeekHrs"].between(10, 80))]["WorkWeekHrs"].dropna()
    
    t_stat, p_val = stats.ttest_ind(hrs_home, hrs_off, equal_var=False)
    
    return {
        "test_name": "Welch's Two-Sample t-Test (Work Location Hours)",
        "sample_home": len(hrs_home),
        "mean_home_hours": float(hrs_home.mean()),
        "sample_office": len(hrs_off),
        "mean_office_hours": float(hrs_off.mean()),
        "t_statistic": float(t_stat),
        "p_value": float(p_val),
        "statistically_significant": bool(p_val < 0.05)
    }


def run_job_satisfaction_chi2_test(df: pd.DataFrame) -> Dict[str, any]:
    """
    Perform Pearson's Chi-Square test of independence between JobSat and JobSeek.
    """
    df_sub = df[["JobSat", "JobSeek"]].dropna()
    contingency = pd.crosstab(df_sub["JobSat"], df_sub["JobSeek"])

    chi2, p_val, dof, _ = stats.chi2_contingency(contingency)

    return {
        "test_name": "Chi-Square Test of Independence (Job Satisfaction vs. Job Seeking)",
        "sample_size": int(len(df_sub)),
        "chi2_statistic": float(chi2),
        "degrees_of_freedom": int(dof),
        "p_value": float(p_val),
        "statistically_significant": bool(p_val < 0.05),
        "contingency_table": contingency,
    }


if __name__ == "__main__":
    import os
    db = "data/processed/capstone.db"
    if os.path.exists(db):
        print("Top 5 Languages Current:")
        print(query_top_technologies(db, "language", "Current", 5))
        print("\nLanguage Momentum:")
        print(calculate_technology_momentum(db, "language").head(5))
