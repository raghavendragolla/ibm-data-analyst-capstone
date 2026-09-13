"""
Database Provisioning Module for IBM Data Analyst Capstone Project.

Builds `data/processed/capstone.db` from scratch by:
1. Executing `sql/schema.sql` (DDL: tables, keys, indexes).
2. Loading each normalized CSV in `data/processed/` into its matching table.

This is the missing link between the wrangling stage (`src/data_cleaning.py`,
which produces the normalized CSVs) and the SQL analytics stage (`sql/analysis.sql`,
`src/analysis.py`, `dashboard/app.py`), all of which assume `capstone.db` already
exists. Run this after `data_cleaning.py` (or anytime the CSVs change) to
(re)generate the database deterministically.
"""

import os
import sqlite3
import pandas as pd

SCHEMA_PATH = "sql/schema.sql"
DB_PATH = "data/processed/capstone.db"
PROCESSED_DIR = "data/processed"

# Maps each processed CSV to its destination table. Order matters: parent
# `respondents` must load before the child tables that reference it via FK.
TABLE_LOAD_ORDER = [
    ("respondent_demographics.csv", "respondents"),
    ("respondent_languages.csv", "respondent_languages"),
    ("respondent_databases.csv", "respondent_databases"),
    ("respondent_dev_environments.csv", "respondent_dev_environments"),
    ("respondent_roles.csv", "respondent_roles"),
    ("job_postings_skills_demand.csv", "job_postings_demand"),
    ("popular_languages_scraped.csv", "programming_languages_benchmark"),
]


def build_database(
    schema_path: str = SCHEMA_PATH,
    db_path: str = DB_PATH,
    processed_dir: str = PROCESSED_DIR,
) -> None:
    """Recreate `capstone.db` from `schema.sql` and the processed CSVs."""
    missing = [
        csv_name
        for csv_name, _ in TABLE_LOAD_ORDER
        if not os.path.exists(os.path.join(processed_dir, csv_name))
    ]
    if missing:
        raise FileNotFoundError(
            f"Missing processed CSV(s): {missing}. "
            "Run `python src/data_cleaning.py` first."
        )

    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = OFF;")
        conn.executescript(schema_sql)

        for csv_name, table_name in TABLE_LOAD_ORDER:
            df = pd.read_csv(os.path.join(processed_dir, csv_name))
            df.to_sql(table_name, conn, if_exists="append", index=False)
            print(f"Loaded {len(df):,} rows into `{table_name}` from {csv_name}")

        conn.execute("PRAGMA foreign_keys = ON;")
        conn.commit()

    print(f"\nDatabase successfully provisioned at: {db_path}")


if __name__ == "__main__":
    print("--- Provisioning Relational SQLite Database ---")
    build_database()
