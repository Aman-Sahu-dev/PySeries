from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from expense_tracker.models.category import category

@dataclass
class expence:
    amount: Decimal
    category: category
    description: str
    date: date
    id: int | None
