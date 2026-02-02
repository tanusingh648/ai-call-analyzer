from pydantic import BaseModel
from datetime import datetime

class CallEvent(BaseModel):
    number: str
    risk: int
    action: str
    time: datetime
