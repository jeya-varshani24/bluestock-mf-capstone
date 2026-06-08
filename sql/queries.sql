SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
    amfi_code,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

SELECT
    transaction_type,
    ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

SELECT
    scheme_name,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

SELECT
    category,
    ROUND(AVG(sharpe_ratio), 2) AS avg_sharpe
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
GROUP BY category;

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY sharpe_ratio DESC
LIMIT 5;

SELECT
    kyc_status,
    COUNT(*) AS investor_count
FROM fact_transactions
GROUP BY kyc_status;

SELECT
    city_tier,
    ROUND(AVG(amount_inr), 2) AS avg_transaction
FROM fact_transactions
GROUP BY city_tier;

SELECT
    state,
    ROUND(SUM(amount_inr), 2) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 5;

