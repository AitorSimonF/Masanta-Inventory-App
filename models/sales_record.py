"""
Sales record model - represents a single transaction
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class SalesRecord:
    """
    Represents a sales transactioin pulled from QuickBooks
    Each sale is one invoice line (SKU + quantity + date)
    """

    # Product Sold
    sku: str

    # Number of units sold in this invoice line
    quantity_sold: int

    # When the sale ocurred
    sale_date: datetime

    # Ooptional QuickBooks details
    invoice_id: Optional[str] = None
    customer_name: Optional[str] = None

    # -------------------------
    # Helpful computed values
    # -------------------------


    @property
    def month_year(self) -> str:
        """
        Returns formatted year-month (YYY-MM)
        Useful for monthly forecasting.
        """
        return self.scale_date.strftime('%Y-%m')

    @property
    def week_number(self) -> int:
        """
        Returns ISO week number.
        Useful for weekly forecasting.
        """

        return self.sale_date.isocalendar()[1]

    # -------------------------
    # Debug output
    # -------------------------

    def __repr__(self) -> str:
        return f"SalesRecord(sku='{self.sku}', qty={self.quantity_sold}, date={self.sale_date.date()})"

    # -------------------------
    # Serialization helpers
    # -------------------------

    def to_dict(self) -> dict:
        """
        Convert SalesRecord -> dictionary.
        Useful for DB/JSON storage.
        """

        return{
            'sku': self.sku,
            'quantity_sold': self.quantity_sold,
            'sale_date': self.sale_date.isoformat(),
            'invoice_id': self.invoice_id,
            'customer_name': self.customer_name
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'SalesRecord':
        """
        Convert dictionary - SalesRecord instance.
        Handles date parsing automtically
        """

        sale_date = data['sale_date']
        
        # If date is stored as string, convert back to datetime
        if isinstance(sale_date, str):
            sale_date = datetime.fromisoformat(sale_date)
        
        return cls(
            sku = data['sku'],
            quantity_sold = data['quantity_sold'],
            sale_date = sale_date,
            invoice_id = data.get('invoice_id'),
            customer_name = data.get('customer_name')
        )
