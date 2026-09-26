import pandas as pd


REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
}


def validate_columns(data: pd.DataFrame) -> None:
    """Kontrollerar att alla obligatoriska kolumner finns."""
    missing = REQUIRED_COLUMNS - set(data.columns)

    if missing:
        raise ValueError(
            f"Obligatoriska kolumner saknas: {sorted(missing)}"
        )


def validate_not_empty(data: pd.DataFrame) -> None:
    """Kontrollerar att datafilen inte är tom."""
    if data.empty:
        raise ValueError("Datafilen innehåller inga rader.")