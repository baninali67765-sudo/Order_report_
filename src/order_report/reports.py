from pathlib import Path

import pandas as pd


def create_overview(data: pd.DataFrame) -> pd.DataFrame:
    """Skapar översiktsrapport."""

    total_sales = round(
        data["discounted_value"].sum(),
        2,
    )

    number_of_orders = data["order_id"].nunique()
    number_of_returns = int(data["returned"].sum())

    return pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )


def create_grouped_sales_report(
    data: pd.DataFrame,
    group_column: str,
) -> pd.DataFrame:
    """Skapar försäljningsrapport grupperad efter en kolumn."""

    result = (
        data.groupby(
            group_column,
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    result["total_sales"] = (
        result["total_sales"].round(2)
    )

    result["return_rate"] = (
        result["returns"] / result["order_count"]
    ).round(3)

    return (
        result
        .sort_values(
            "total_sales",
            ascending=False,
        )
        .reset_index(drop=True)
    )


def create_returns_by_category(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """Skapar rapport över returer per produktkategori."""

    result = (
        data.groupby(
            "product_category",
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

    result["return_rate"] = (
        result["returns"] / result["order_count"]
    ).round(3)

    return (
        result
        .sort_values(
            "return_rate",
            ascending=False,
        )
        .reset_index(drop=True)
    )


def save_report(
    report: pd.DataFrame,
    output_path: Path,
) -> None:
    """Sparar en rapport till CSV."""
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    report.to_csv(
        output_path,
        index=False,
    )