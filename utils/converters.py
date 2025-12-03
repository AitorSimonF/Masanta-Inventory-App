"""
Utility functions for unit conversions
"""

# These functions exist so you can:
# - Convert product sizes
# - Calculate container volumes
# - Standardize measurements for forecasting and container packing

def liters_to_gallons(liters: float) -> float:
    """Convert liters → US gallons"""
    return liters * 0.264172


def gallons_to_liters(gallons: float) -> float:
    """Convert US gallons → liters"""
    return gallons * 3.78541


def liters_to_cubic_meters(liters: float) -> float:
    """Convert liters → cubic meters (1000L = 1m³)"""
    return liters / 1000


def cubic_meters_to_liters(cubic_meters: float) -> float:
    """Convert cubic meters → liters"""
    return cubic_meters * 1000


def cubic_feet_to_cubic_meters(cubic_feet: float) -> float:
    """Convert ft³ → m³"""
    return cubic_feet * 0.0283168


def cubic_meters_to_cubic_feet(cubic_meters: float) -> float:
    """Convert m³ → ft³"""
    return cubic_meters * 35.3147


# Quick lookup table for algorithms
CONVERSIONS = {
    'liter_to_gallon': 0.264172,
    'gallon_to_liter': 3.78541,
    'liter_to_m3': 0.001,
    'm3_to_liter': 1000,
    'ft3_to_m3': 0.0283168,
    'm3_to_ft3': 35.3147
}