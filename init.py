"""Fipiran Funds - A library for fetching Iranian fund data."""

__version__ = "0.1.0"
__author__ = "K.Salehi"
__description__ = "A Python library for fetching Iranian fund data from Fipiran API"

from .core import export_fund_data
from .api import *

__all__ = ['export_fund_data'] 
