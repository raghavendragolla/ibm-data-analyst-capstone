"""Tests for src/analysis.py statistical and IQR helper functions."""

import numpy as np
import pandas as pd
import pytest

from src.analysis import (
    perform_iqr_outlier_analysis,
    run_degree_compensation_test,
    run_remote_work_hours_test,
    run_job_satisfaction_chi2_test,
)


def test_iqr_outlier_analysis_flags_known_upper_outlier():
    # 1..10 plus one extreme outlier (100).
    series = pd.Series(list(range(1, 11)) + [100])
    result = perform_iqr_outlier_analysis(series)
    assert result["n_total"] == 11
    assert result["n_upper_outliers"] == 1
    assert result["n_lower_outliers"] == 0
    # Trimmed mean should be pulled back toward the un-inflated median.
    assert result["mean_trimmed"] < result["mean_original"]


def test_iqr_outlier_analysis_drops_nans():
    series = pd.Series([1.0, 2.0, 3.0, np.nan, 4.0, 5.0])
    result = perform_iqr_outlier_analysis(series)
    assert result["n_total"] == 5


@pytest.fixture
def compensation_df():
    return pd.DataFrame({
        "EdLevel": ["Bachelor's degree"] * 5 + ["Master's degree"] * 5,
        "ConvertedComp": [50000, 55000, 60000, 62000, 58000, 90000, 95000, 88000, 92000, 91000],
    })


def test_degree_compensation_test_detects_significant_gap(compensation_df):
    result = run_degree_compensation_test(compensation_df)
    assert result["sample_bachelor"] == 5
    assert result["sample_master"] == 5
    assert result["median_master"] > result["median_bachelor"]
    # With cleanly separated distributions this small, the U-test should find significance.
    assert result["statistically_significant"] is True


@pytest.fixture
def work_hours_df():
    rng = np.random.default_rng(seed=42)
    home = rng.normal(loc=40, scale=2, size=200)
    office = rng.normal(loc=40, scale=2, size=200)
    return pd.DataFrame({
        "WorkLoc": ["Home"] * 200 + ["Office"] * 200,
        "WorkWeekHrs": np.concatenate([home, office]),
    })


def test_remote_work_hours_test_no_difference_when_distributions_match(work_hours_df):
    result = run_remote_work_hours_test(work_hours_df)
    assert result["sample_home"] == 200
    assert result["sample_office"] == 200
    # Same underlying distribution -> should not find a significant difference.
    assert result["statistically_significant"] is False


def test_remote_work_hours_test_excludes_out_of_range_values():
    df = pd.DataFrame({
        "WorkLoc": ["Home", "Home", "Office", "Office"],
        "WorkWeekHrs": [40, 200, 40, 5],  # 200 and 5 fall outside the 10-80 valid range
    })
    result = run_remote_work_hours_test(df)
    assert result["sample_home"] == 1
    assert result["sample_office"] == 1


@pytest.fixture
def satisfaction_df():
    return pd.DataFrame({
        "JobSat": (["Very satisfied"] * 40 + ["Very dissatisfied"] * 40),
        "JobSeek": (["I am not interested in new job opportunities"] * 35
                     + ["I am actively looking for a job"] * 5
                     + ["I am actively looking for a job"] * 35
                     + ["I am not interested in new job opportunities"] * 5),
    })


def test_job_satisfaction_chi2_test_finds_association(satisfaction_df):
    result = run_job_satisfaction_chi2_test(satisfaction_df)
    assert result["sample_size"] == 80
    assert result["statistically_significant"] is True
