import pandas as pd
import pytest

from order_report.validation import (
    validate_columns,
    validate_not_empty,
)


def test_validate_columns_accepts_required_columns():
    columns = [
        "order_id",
        "order_date",
        "customer_id",
        "region",
        "product_category",
        "quantity",
        "unit_price",
        "discount",
        "returned",
    ]

    data = pd.DataFrame(columns=columns)

    validate_columns(data)


def test_validate_columns_raises_error_when_column_is_missing():
    data = pd.DataFrame(
        {
            "order_id": [1],
            "region": ["Sweden"],
        }
    )

    with pytest.raises(ValueError, match="Obligatoriska kolumner saknas"):
        validate_columns(data)


def test_validate_not_empty_raises_error_for_empty_data():
    data = pd.DataFrame()

    with pytest.raises(
        ValueError,
        match="Datafilen innehåller inga rader",
    ):
        validate_not_empty(data)