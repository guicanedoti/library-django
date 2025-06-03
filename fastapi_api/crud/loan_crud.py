from fastapi_api.models.loan_model import Loan as LoanModel
from fastapi_api.schemas.loan_schema import LoanCreate, Loan as LoanSchema
from fastapi_api.crud.base_crud import CRUDBase

class LoanCRUD(CRUDBase[LoanModel, LoanCreate, LoanSchema]):
    pass

loan_crud = LoanCRUD(LoanModel)
