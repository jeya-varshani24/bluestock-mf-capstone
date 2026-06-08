import pandas as pd

performance = pd.read_csv(
    "../data/processed/clean_performance.csv"
)

performance["performance_score"] = (
      performance["return_3yr_pct"] * 0.35
    + performance["return_5yr_pct"] * 0.35
    + performance["sharpe_ratio"] * 15
    + performance["alpha"] * 5
    - performance["expense_ratio_pct"] * 5
)

ranked_funds = performance.sort_values(
    by="performance_score",
    ascending=False
)

ranked_funds.to_csv(
    "../data/processed/fund_rankings.csv",
    index=False
)

print(
    "Fund rankings generated successfully!"
)