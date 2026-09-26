import pandas as pd

from order_report.processing import (
    calculate_order_values,
    clean_orders,
)


def test_calculate_order_values():
    data = pd.DataFrame(
        {
            "quantity": [2],
            "unit_price": [100],
            "discount": [0.10],
        }
    )

    result = calculate_order_values(data)

    assert result.loc[0, "order_value"] == 200
    assert result.loc[0, "discounted_value"] == 180


def test_clean_orders_converts_returned_to_boolean():
    data = pd.DataFrame(
        {
            "region": [" sweden "],
            "product_category": [" electronics "],
            "quantity": ["2"],
            "unit_price": ["100"],
            "discount": ["0.1"],
            "returned": ["yes"],
        }
    )

    result = clean_orders(data)

    assert result.loc[0, "region"] == "Sweden"
    assert result.loc[0, "product_category"] == "Electronics"
    assert result.loc[0, "quantity"] == 2
    assert result.loc[0, "unit_price"] == 100
    assert result.loc[0, "discount"] == 0.1
    assert bool(result.loc[0, "returned"]) is True


def test_missing_quantity_gets_default_value():
    data = pd.DataFrame(
        {
            "region": ["Sweden"],
            "product_category": ["Electronics"],
            "quantity": [None],
            "unit_price": [100],
            "discount": [0],
            "returned": ["false"],
        }
    )

    result = clean_orders(data)

    assert result.loc[0, "quantity"] == 1