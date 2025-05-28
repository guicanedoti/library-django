from models.loan_model import Loan as LoanModel
from schemas.loan_schema import LoanCreate, Loan as LoanSchema
from crud.base_crud import CRUDBase

class LoanCRUD(CRUDBase[LoanModel, LoanCreate, LoanSchema]):
    pass

loan_crud = LoanCRUD(LoanModel)
