from enum import Enum

class BookStatus(str, Enum):
    available = "available"
    on_loan = "on_loan"
    reserved = "reserved"
    damaged = "damaged"