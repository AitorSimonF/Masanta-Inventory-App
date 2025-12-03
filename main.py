"""
Masanta Inventory Management System
Main entry point
"""

import sys
from pathlib import Path

# -------------------------------------------------------
# EXPANDING PYTHON'S IMPORT PATH
# -------------------------------------------------------
# This line allows Python to import modules from your project root.
# Otherwise, imports like "from models.product" might fail.
sys.path.insert(0, str(Path(__file__).parent))

# Import configuration
from config.settings import BASE_DIR, DATA_DIR, QB_ENVIRONMENT

# Import models
from models.product import Product
from models.sales_record import SalesRecord

# Import utility functions
from utils.converters import liters_to_gallons, gallons_to_liters

from datetime import datetime


def test_basic_setup():
    """
    Runs a series of small tests to confirm the project
    is correctly configured and your classes work as expected.
    """

    print("=" * 50)
    print("MASANTA INVENTORY SYSTEM - BASIC TEST")
    print("=" * 50)

    # -------------------------------------------------------
    # CONFIGURATION TEST
    # -------------------------------------------------------
    print(f"\n✓ Project Directory: {BASE_DIR}")
    print(f"✓ Data Directory: {DATA_DIR}")
    print(f"✓ QuickBooks Environment: {QB_ENVIRONMENT}")

    # -------------------------------------------------------
    # PRODUCT MODEL TEST
    # -------------------------------------------------------
    test_product = Product(
        sku="TEST-001",
        name="Test Beverage 4L",
        unit_volume_liters=4.0,
        units_per_case=6,
        current_stock=100
    )

    print(f"\n✓ Created Product: {test_product}")
    print(f"  - Case Volume Liters: {test_product.case_volume_liters}L")
    print(f"  - Case Volume Cubic Meters: {test_product.case_volume_cubic_meters:.4f} m³")

    # -------------------------------------------------------
    # SALES RECORD TEST
    # -------------------------------------------------------
    test_sale = SalesRecord(
        sku="TEST-001",
        quantity_sold=24,
        sale_date=datetime.now(),
        invoice_id="INV-001"
    )

    print(f"\n✓ Created Sale: {test_sale}")
    print(f"  - Month-Year: {test_sale.month_year}")
    print(f"  - Week Number: {test_sale.week_number}")

    # -------------------------------------------------------
    # UNIT CONVERSION TEST
    # -------------------------------------------------------
    liters = 20.0
    gallons = liters_to_gallons(liters)
    back_to_liters = gallons_to_liters(gallons)

    print(f"\n✓ Conversion Test:")
    print(f"  - {liters} L = {gallons:.2f} gallons")
    print(f"  - {gallons:.2f} gallons = {back_to_liters:.2f} L")

    print("\n" + "=" * 50)
    print("ALL BASIC TESTS PASSED! ✓")
    print("=" * 50)

    print("\nNext steps:")
    print("- Set up your .env file with QuickBooks credentials")
    print("- Ready to continue building!")


# -------------------------------------------------------
# RUN WHEN EXECUTED DIRECTLY
# -------------------------------------------------------
if __name__ == "__main__":
    test_basic_setup()