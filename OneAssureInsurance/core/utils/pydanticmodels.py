from pydantic import BaseModel, validator
from enum import Enum
import typing as t
from OneAssureInsurance.basepydanticmodels import ResponseModel

from OneAssureInsurance.core.utils.optionsconfig import (
    tier_id_options,
    age_options,
    sum_insured_options,
    tenure_options,
)

from OneAssureInsurance import FormElementType, FormElement

# Pydantic models for validating input data
class MemberType(str, Enum):
    ADULT = 'adult'
    CHILD = 'child'

class FamilyMemberDetails(BaseModel):
    type: MemberType
    name: t.Optional[str]
    age: int

class PremiumRateQuery(BaseModel):
    family_member_details: t.List[FamilyMemberDetails]
    city_tier: int
    tenure: int
    cover_amount: int
    
    @validator("family_member_details", pre=True, always=True)
    def sort_list(cls, value):
        if value is not None:
            # Sorts list in descending order of age
            return sorted(value, key=lambda d: d['age'], reverse=True) 
        else:
            return []

class PlanPurchasePayload(PremiumRateQuery):
    premium_rate: float

class PlanDetails(PlanPurchasePayload):
    order_id: str

class PlanPurchaseResponse(ResponseModel):
    message: str = "Plan purchased successfully!"
    plan_details: PlanDetails

class PremiumRateResponse(BaseModel):
    premium_rate: float

class PremiumInquiryFormConfig(BaseModel):
    form_elements: t.List = [
        FormElement(
            label="Family members",
            key="family_member_details",
            type=FormElementType.COMPOSITE.value,
            composite_form_elements=[
                FormElement(
                    label="Name",
                    key="name",
                    type=FormElementType.TEXT.value,
                ),
                FormElement(
                    label="Type",
                    key="type",
                    options=[
                        {
                            "label": "Adult", 
                            "value": "adult", 
                            "selected": False
                        },
                        {
                            "label": "Child", 
                            "value": "child", 
                            "selected": False
                        }
                    ],
                    type=FormElementType.DROPDOWN.value
                ),
                FormElement(
                    label="Age",
                    key="age",
                    options=age_options,
                    type=FormElementType.DROPDOWN.value
                )
            ]
        ),
        FormElement(
            label="City Tier",
            key="city_tier",
            options=tier_id_options,
            type=FormElementType.DROPDOWN.value
        ),
        FormElement(
            label="Sum to be insured",
            key="cover_amount",
            options=sum_insured_options,
            type=FormElementType.DROPDOWN.value
        ),
        FormElement(
            label="Tenure",
            key="tenure",
            options=tenure_options,
            type=FormElementType.DROPDOWN.value
        )
    ]