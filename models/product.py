""" 
Product model - represents a single product in inventory
"""

from dataclasses import dataclass
from typing import Optional

# dataclass automatically generates:
# - __init__
# - __repr__
# - comparison methods
# making it PERFECT for simple data storage objects 

@dataclass
class Product:
    """
    Represents a product in the Masanta Inventory System. 
    This essentially a "row" in your product database.
    """

    sku: str        # Unique product code (e.g., M15W50-20L)
    name: str       # Human-readable product name

    # Volume of ONE UNIT in liters (e.g., 20L bucket)
    unit_volume_liters: float

    # Some products are sold in boxes (e.g., 4 bottles per box)
    qb_item_id: Optional[str] = None

    # Cuttent stock count (units, not cases)
    current_stock: int = 0

    # Reorder point (units) - calculated later based on sales
    reorder_point: int = 0

    # -------------------------
    # Computed Values (dynamic)
    # -------------------------

    @property
    def case_volume_liters(self) -> float:
        """
        Total volume of ONE BOX in liters.
        For example:
        4L/unit x 4 units per case = 16 liters per case
        """

        return self.unit_volume_liters * self.units_per_case

    @property
    def case_volume_cubic_meters(self) -> float:
        """
        Convert liters to cubic meters.
        1000 liters = 1 m^3
        """

        return self.case_volume_liters / 1000

    # -------------------------
    # Useful overrides
    # -------------------------

    def __repr__(self) -> str:
        """ Human-readable output for debugging."""
        return f"Product(sku='{self.sku}', name='{self.name}', stock={self.current_stock})"
    
    # -------------------------
    # Serialization helpers
    # -------------------------

    def to_dict(self) -> dict:
        """
        Convert Product -> dictionary.
        Useful for JSON or database storage
        """
        return {
            'sku': self.sku,
            'name': self.name,
            'unit_volume_liters': self.units_volume_liters,
            'units_per_case': self.units_per_case,
            'qb_item_id': self.qb_item_id,
            'current_stock': self.current_stock,
            'reorder_point': self.reorder_point
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Product':
        """
        Convert dictionary -> Product instance.
        Useful when loading from JSON/db
        """
        return cls(
            sku = data['sku'],
            name = data['name'],
            unit_volume_liters = data['unit_volume_liters'],
            units_per_case = data.get('units_per_case', 1),
            qb_item_id = data.get('qb_item_id'),
            current_stock = data.get('current_stock', 0),
            reorder_point = data.get('reorder_point', 0)
        )