import pandas as pd

ranked_funds = pd.read_csv(
    "../data/processed/fund_rankings.csv"
)

risk = input(
    "Enter risk level (Low/Moderate/High): "
)

risk = risk.lower()

if risk == "low":

    result = ranked_funds.nsmallest(
        5,
        "beta"
    )

elif risk == "moderate":

    result = ranked_funds[
        (ranked_funds["beta"] >= 0.8)
        &
        (ranked_funds["beta"] < 1.0)
    ].head(5)

else:

    result = ranked_funds.nlargest(
        5,
        "beta"
    )

print(
    result[
        [
            "scheme_name",
            "performance_score",
            "beta"
        ]
    ]
)