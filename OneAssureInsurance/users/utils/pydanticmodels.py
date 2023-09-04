from pydantic import BaseModel, validator, root_validator
from OneAssureInsurance import ResponseModel
import typing as t

from OneAssureInsurance import FormElement, FormElementType

class UserRegistrationFormPayload(BaseModel):
    full_name: str
    email: str
    password1: str
    password2: str

    @root_validator(pre=True)
    def root_validate(cls, values):
        if not (values['password1'] == values['password2']):
            raise ValueError("Both passwords must match")
        return values

class UserLoginFormPayload(BaseModel):
    email: str
    password: str

class UserRegistrationFormConfig(BaseModel):
    form_fields: t.List[FormElement] = [
        FormElement(
            label="Full name",
            key="full_name",
            type=FormElementType.TEXT.value
        ),
        FormElement(
            label="Email",
            key="email",
            type=FormElementType.TEXT.value
        ),
        FormElement(
            label="Password",
            key="password1",
            type=FormElementType.TEXT.value
        ),
        FormElement(
            label="Re-enter Password",
            key="password2",
            type=FormElementType.TEXT.value
        )
    ]

class UserLoginFormConfig(BaseModel):
    form_fields: t.List[FormElement] = [
        FormElement(
            label="Email",
            key="email",
            type=FormElementType.TEXT.value
        ),
        FormElement(
            label="Password",
            key="password",
            type=FormElementType.TEXT.value
        ),
    ]

class UserLoginResponseModel(ResponseModel):
    message: str = "User logged in successfully"
    access_token: str


