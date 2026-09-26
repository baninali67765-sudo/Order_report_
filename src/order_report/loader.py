import logging
from pathlib import Path

import pandas as pd

from .validation import validate_columns, validate_not_empty

logger = logging.getLogger(__name__)


def load_orders(input_path: Path) -> pd.DataFrame:
    """Läser orderdata från en CSV-fil och validerar grundstrukturen."""
    if not input_path.exists():
        raise FileNotFoundError(
            f"Datafilen kunde inte hittas: {input_path}"
        )

    data = pd.read_csv(input_path)

    validate_columns(data)
    validate_not_empty(data)

    logger.info("Läste in %d rader från %s", len(data), input_path)

    return data