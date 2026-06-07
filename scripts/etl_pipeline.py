import sqlite3
import pandas as pd
from pathlib import Path

# Database path
db_path = Path("../data/db/bluestock_mf.db")

# Connect to SQLite
conn = sqlite3.connect(db_path)

print("Database connected successfully!")

# Load schema.sql
with open("../sql/schema.sql", "r") as file:
    schema = file.read()

conn.executescript(schema)

print("Tables created successfully!")

# Load datasets
fund_master = pd.read_csv(
    "../data/raw/01_fund_master.csv"
)

clean_nav = pd.read_csv(
    "../data/processed/clean_nav.csv"
)

clean_transactions = pd.read_csv(
    "../data/processed/clean_transactions.csv"
)

clean_performance = pd.read_csv(
    "../data/processed/clean_performance.csv"
)

aum = pd.read_csv(
    "../data/raw/03_aum_by_fund_house.csv"
)

# Prepare dim_fund
dim_fund = fund_master[
    [
        'amfi_code',
        'fund_house',
        'scheme_name',
        'category',
        'sub_category',
        'plan',
        'expense_ratio_pct',
        'risk_category'
    ]
]

# Prepare fact_nav
fact_nav = clean_nav.rename(
    columns={
        'date': 'nav_date'
    }
)

# Prepare fact_transactions
fact_transactions = clean_transactions

# Prepare fact_performance
fact_performance = clean_performance[
    [
        'amfi_code',
        'return_1yr_pct',
        'return_3yr_pct',
        'return_5yr_pct',
        'alpha',
        'beta',
        'sharpe_ratio',
        'sortino_ratio',
        'std_dev_ann_pct',
        'max_drawdown_pct',
        'morningstar_rating'
    ]
]

# Prepare fact_aum
fact_aum = aum.rename(
    columns={
        'quarter': 'date'
    }
)

dim_fund.to_sql(
    'dim_fund',
    conn,
    if_exists='replace',
    index=False
)

fact_nav.to_sql(
    'fact_nav',
    conn,
    if_exists='replace',
    index=False
)

fact_transactions.to_sql(
    'fact_transactions',
    conn,
    if_exists='replace',
    index=False
)

fact_performance.to_sql(
    'fact_performance',
    conn,
    if_exists='replace',
    index=False
)

fact_aum.to_sql(
    'fact_aum',
    conn,
    if_exists='replace',
    index=False
)

print("All datasets loaded successfully!")

tables = [
    'dim_fund',
    'fact_nav',
    'fact_transactions',
    'fact_performance',
    'fact_aum'
]

print("All datasets loaded successfully!")

tables = [
    'dim_fund',
    'fact_nav',
    'fact_transactions',
    'fact_performance',
    'fact_aum'
]

for table in tables:

    count = pd.read_sql_query(
        f"SELECT COUNT(*) AS total FROM {table}",
        conn
    )

    print(
        f"{table}:",
        count['total'][0],
        "rows"
    )

conn.close()

print(
    "Database connection closed."
)