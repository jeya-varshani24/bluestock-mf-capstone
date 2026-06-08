# Data Dictionary

This document describes the datasets and database tables used in the Bluestock Mutual Fund Analytics Platform project.

## dim_fund

Source: 01_fund_master.csv

* amfi_code (TEXT): Unique AMFI scheme identifier.
* fund_house (TEXT): Name of the asset management company.
* scheme_name (TEXT): Official name of the mutual fund scheme.
* category (TEXT): Broad fund category such as Equity or Debt.
* sub_category (TEXT): Specific fund classification such as Large Cap or Liquid Fund.
* plan (TEXT): Type of investment plan (Direct or Regular).
* expense_ratio_pct (REAL): Annual expense ratio charged by the fund.
* risk_category (TEXT): Risk classification assigned to the scheme.

---

## fact_nav

Source: clean_nav.csv

* amfi_code (TEXT): AMFI code associated with the scheme.
* nav_date (DATE): Date on which the NAV was recorded.
* nav (REAL): Net Asset Value of the scheme on the specified date.

---

## fact_transactions

Source: clean_transactions.csv

* investor_id (TEXT): Unique identifier assigned to an investor.
* transaction_date (DATE): Date of the transaction.
* amfi_code (TEXT): Mutual fund scheme involved in the transaction.
* transaction_type (TEXT): Type of transaction (SIP, Lumpsum, Redemption).
* amount_inr (REAL): Transaction amount in Indian Rupees.
* state (TEXT): State of residence of the investor.
* city (TEXT): City of the investor.
* city_tier (TEXT): Classification of the city as T30 or B30.
* age_group (TEXT): Age bracket of the investor.
* gender (TEXT): Gender of the investor.
* annual_income_lakh (REAL): Annual income of the investor in lakhs.
* payment_mode (TEXT): Mode used to complete the transaction.
* kyc_status (TEXT): KYC verification status of the investor.

---

## fact_performance

Source: clean_performance.csv

* amfi_code (TEXT): AMFI scheme identifier.
* return_1yr_pct (REAL): One-year return percentage.
* return_3yr_pct (REAL): Three-year CAGR percentage.
* return_5yr_pct (REAL): Five-year CAGR percentage.
* alpha (REAL): Excess return generated over the benchmark.
* beta (REAL): Sensitivity of the fund relative to market movements.
* sharpe_ratio (REAL): Risk-adjusted return measure.
* sortino_ratio (REAL): Downside risk-adjusted return measure.
* std_dev_ann_pct (REAL): Annualized standard deviation of returns.
* max_drawdown_pct (REAL): Maximum decline from the peak value.
* morningstar_rating (INTEGER): Fund rating on a scale of 1 to 5.

---

## fact_aum

Source: 03_aum_by_fund_house.csv

* fund_house (TEXT): Name of the asset management company.
* date (DATE): Reporting period for AUM values.
* aum_crore (REAL): Assets Under Management reported in crore rupees.

---

## Data Sources

* AMFI India
* mfapi.in
* Bluestock Fintech Capstone datasets
 