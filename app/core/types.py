from dataclasses import dataclass
import datetime
from enum import IntEnum


class State(IntEnum):
    ADD_RECORD = 0


@dataclass
class Record:
    category: str
    name: str
    ammount: int | float
    date: datetime.date = datetime.date.today()
    comment: str = ''
    
    def __str__(self):
        return ', '.join(
            [f'{fn}: {getattr(self, fn)}' for fn in self.__dataclass_fields__.keys()]
        )
    
    def values(self):
        return self.__dataclass_fields__.values()
