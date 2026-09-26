import logging
from pathlib import Path

from .config import ReportConfig
from .loader import load_orders
from .processing import (
    calculate_order_values,
    clean_orders,
)
from .reports import (
    create_grouped_sales_report,
    create_overview,
    create_returns_by_category,
    save_report,
)


def configure_logging() -> None:
    """Konfigurerar programmets logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )


def run(config: ReportConfig) -> None:
    """Kör hela orderrapporteringen."""

    logger = logging.getLogger(__name__)

    logger.info("Startar orderrapport")

    data = load_orders(config.input_path)

    data = clean_orders(data)
    data = calculate_order_values(data)

    config.output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    overview = create_overview(data)
    save_report(
        overview,
        config.output_dir / "overview.csv",
    )

    category_report = create_grouped_sales_report(
        data,
        "product_category",
    )
    save_report(
        category_report,
        config.output_dir / "sales_by_category.csv",
    )

    region_report = create_grouped_sales_report(
        data,
        "region",
    )
    save_report(
        region_report,
        config.output_dir / "sales_by_region.csv",
    )

    returns_report = create_returns_by_category(data)
    save_report(
        returns_report,
        config.output_dir / "returns_by_category.csv",
    )

    logger.info(
        "Rapporter sparade i %s",
        config.output_dir,
    )
    logger.info("Orderrapport klar")


def main() -> None:
    """Programmets startpunkt."""

    configure_logging()

    config = ReportConfig(
        input_path=Path("data/orders.csv"),
        output_dir=Path("output"),
    )

    try:
        run(config)
    except (FileNotFoundError, ValueError) as error:
        logging.getLogger(__name__).error("%s", error)
        raise SystemExit(1)


if __name__ == "__main__":
    main()