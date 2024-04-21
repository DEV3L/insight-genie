from dataclasses import dataclass
from datetime import datetime


@dataclass(kw_only=True)
class ContentData:
    id: int
    title: str
    body: str
    date: datetime
