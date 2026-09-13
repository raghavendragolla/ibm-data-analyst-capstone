"""
Data Collection Module for IBM Data Analyst Capstone Project.

Provides automated, reproducible functions to:
1. Acquire raw datasets from authoritative IBM endpoints with SHA-256 verification.
2. Query and aggregate job postings by key skills (API simulation / labor demand extraction).
3. Web-scrape HTML tables with BeautifulSoup to extract programming language benchmarks.
"""

import os
import re
import json
import hashlib
import urllib.request
from typing import Dict, List, Optional
import pandas as pd
from bs4 import BeautifulSoup


DATASET_SOURCES = {
    "survey_data": {
        "filename": "m1_survey_data.csv",
        "url": "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv",
        "expected_min_bytes": 28_000_000,
        # Recorded in docs/sources.md at initial acquisition time.
        "expected_sha256": "78cedfca3f0a21f78090be1b19f938f605301d08303d90d9e6babbd321563d0f",
    },
    "jobs_data": {
        "filename": "jobs.json",
        "url": "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json",
        "expected_min_bytes": 12_000_000,
        "expected_sha256": "d527cbb5ac73ab342610559ff4d785e2f3fb0509fa44965b8c4fb3ad842a9139",
    },
    "languages_scraped": {
        "filename": "Programming_Languages.html",
        "url": "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html",
        "expected_min_bytes": 2_000,
        "expected_sha256": "8f6d5aaa3a6fdfd0f3fb0e1b7c976b093b2c33ae301f175b6458b6947763bb56",
    },
}


def compute_sha256(filepath: str) -> str:
    """Compute cryptographic SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def download_file(url: str, target_path: str, chunk_size: int = 1024 * 1024) -> int:
    """Download remote endpoint with streaming buffer."""
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    total_bytes = 0
    with urllib.request.urlopen(req) as response, open(target_path, "wb") as out_file:
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            out_file.write(chunk)
            total_bytes += len(chunk)
    return total_bytes


def acquire_all_raw_datasets(target_dir: str = "data/raw", force: bool = False) -> Dict[str, Dict]:
    """Download and cryptographically verify all official IBM raw datasets.

    Raises:
        ValueError: If a file's computed SHA-256 does not match the hash
            recorded in `DATASET_SOURCES` (and documented in docs/sources.md).
    """
    results = {}
    for key, info in DATASET_SOURCES.items():
        filepath = os.path.join(target_dir, info["filename"])
        if os.path.exists(filepath) and not force:
            status = "cached"
        else:
            download_file(info["url"], filepath)
            status = "downloaded"

        actual_sha256 = compute_sha256(filepath)
        expected_sha256 = info.get("expected_sha256")
        if expected_sha256 and actual_sha256 != expected_sha256:
            raise ValueError(
                f"SHA-256 mismatch for {info['filename']}: "
                f"expected {expected_sha256}, got {actual_sha256}. "
                "The source file may have changed or downloaded corrupted -- "
                "investigate before trusting downstream results."
            )

        results[key] = {
            "filepath": filepath,
            "size_bytes": os.path.getsize(filepath),
            "sha256": actual_sha256,
            "status": status,
        }
    return results


def extract_job_demand_by_technologies(
    jobs_filepath: str = "data/raw/jobs.json",
    technologies: Optional[List[str]] = None,
    output_csv: Optional[str] = "data/processed/job_postings_skills_demand.csv"
) -> pd.DataFrame:
    """
    Simulate API skill queries across the 27,005 job postings dataset to quantify labor market demand.
    
    Args:
        jobs_filepath: Path to jobs.json.
        technologies: List of technology skill keywords to query.
        output_csv: Path to export aggregated demand CSV.
        
    Returns:
        DataFrame with Skill and Posting_Count columns.
    """
    if technologies is None:
        technologies = [
            "Python", "SQL", "Java", "JavaScript", "C++", "C#", 
            "R", "PHP", "Go", "Swift", "Ruby", "TypeScript",
            "PostgreSQL", "MySQL", "Oracle", "MongoDB", "SQL Server",
            "AWS", "Azure", "Docker", "Kubernetes", "Git"
        ]
        
    with open(jobs_filepath, "r", encoding="utf-8") as f:
        jobs_data = json.load(f)
        
    df_jobs = pd.DataFrame(jobs_data)
    total_postings = len(df_jobs)
    
    records = []
    for tech in technologies:
        # Regex matching word boundary to avoid false positives (e.g., 'R' matching inside 'Ruby')
        pattern = rf"\b{re.escape(tech)}\b"
        count = df_jobs["Key Skills"].str.contains(pattern, case=False, na=False, regex=True).sum()
        pct = (count / total_postings) * 100
        records.append({
            "Technology": tech,
            "Posting_Count": int(count),
            "Market_Demand_Share_Pct": round(pct, 2)
        })
        
    demand_df = pd.DataFrame(records).sort_values(by="Posting_Count", ascending=False).reset_index(drop=True)
    
    if output_csv:
        os.makedirs(os.path.dirname(output_csv), exist_ok=True)
        demand_df.to_csv(output_csv, index=False)
        print(f"Labor demand dataset saved to: {output_csv}")
        
    return demand_df


def scrape_programming_languages_benchmark(
    html_filepath: str = "data/raw/Programming_Languages.html",
    output_csv: Optional[str] = "data/processed/popular_languages_scraped.csv"
) -> pd.DataFrame:
    """
    Web-scrape programming language compensation benchmarks from local or remote HTML table.
    
    Args:
        html_filepath: Path to Programming_Languages.html.
        output_csv: Path to export scraped benchmark CSV.
        
    Returns:
        Cleaned benchmark DataFrame.
    """
    with open(html_filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    table = soup.find("table")
    rows = table.find_all("tr")
    
    header = [th.get_text().strip() for th in rows[0].find_all(["th", "td"])]
    data_rows = []
    for tr in rows[1:]:
        cols = [td.get_text().strip() for td in tr.find_all("td")]
        if cols:
            data_rows.append(cols)
            
    df = pd.DataFrame(data_rows, columns=header)
    
    # Rename and clean columns
    col_map = {
        "No.": "Rank",
        "Language": "Language",
        "Created By": "Created_By",
        "Average Annual Salary": "Avg_Annual_Salary_USD",
        "Learning Difficulty": "Learning_Difficulty"
    }
    df = df.rename(columns={k: v for k, v in col_map.items() if k in df.columns})
    
    # Clean salary column: strip $, commas and cast to float
    if "Avg_Annual_Salary_USD" in df.columns:
        df["Avg_Annual_Salary_USD"] = (
            df["Avg_Annual_Salary_USD"]
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .astype(float)
        )
        
    if "Rank" in df.columns:
        df["Rank"] = df["Rank"].astype(int)
        
    df = df.sort_values(by="Avg_Annual_Salary_USD", ascending=False).reset_index(drop=True)
    
    if output_csv:
        os.makedirs(os.path.dirname(output_csv), exist_ok=True)
        df.to_csv(output_csv, index=False)
        print(f"Scraped benchmark dataset saved to: {output_csv}")
        
    return df


if __name__ == "__main__":
    print("--- Executing Data Collection Pipelines ---")
    acquire_all_raw_datasets()
    df_demand = extract_job_demand_by_technologies()
    print("\nTop 10 In-Demand Skills from Job Postings:")
    print(df_demand.head(10).to_string(index=False))
    
    print("\n--- Scraping Language Benchmark Table ---")
    df_bench = scrape_programming_languages_benchmark()
    print(df_bench.to_string(index=False))
