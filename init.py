"""
FipiranFunds - A Python library for fetching Iranian fund data.

Author: Kimia Salehy Delarestaghy
Email: kimiaslhd@gmail.com
LinkedIn: https://www.linkedin.com/in/kimia-salehy-delarestaghy/
"""

from .core import export_fund_data
from .api import *

__version__ = "0.1.0"
__author__ = "Kimia Salehy Delarestaghy"
__email__ = "kimiaslhd@gmail.com"
__all__ = ["export_fund_data"]