from pydantic import BaseModel, validator
from enum import Enum
import typing as t

class ResponseModel(BaseModel):
    message: str
    error: bool = False

class ErrorResponseModel(ResponseModel):
    error: bool = True

class FormElementType(str, Enum):
    TEXT = 'text'
    DROPDOWN = 'dropdown'
    COMPOSITE = 'composite'

class DropDownOption(BaseModel):
    label: str
    value: t.Union[str, int]
    selected: bool

class FormElement(BaseModel):
    label: str
    key: str
    options: t.Optional[t.List[DropDownOption]] = None
    type: FormElementType
    composite_form_elements: t.Optional[t.List["FormElement"]] = None