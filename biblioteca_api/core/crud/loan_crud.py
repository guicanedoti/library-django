from models.loan_model import Loan
from schemas.loan_schema import LoanCreate, Loan
from crud.base_crud import CRUDBase

class LoanCRUD(CRUDBase[Loan, LoanCreate, Loan]):
    def __init__(self, model: type[Loan]):
        super().__init__(model)

loan_crud = LoanCRUD(Loan)