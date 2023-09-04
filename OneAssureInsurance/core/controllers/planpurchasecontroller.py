from flask_login import user_accessed
from OneAssureInsurance.core.utils.pydanticmodels import (
    PlanPurchasePayload,
    PlanPurchaseResponse,
    PlanDetails
)
from OneAssureInsurance import purchases_collection
from datetime import datetime
import uuid

class PlanPurchaseController:
    def __init__(self, payload: PlanPurchasePayload, user: str) -> None:
        self.payload = payload
        self.user = user
    
    def purchase_plan(self):
        mongo_payload = {
            'order_id': str(uuid.uuid1()),
            'premium_rate': self.payload.premium_rate,
            'cover_amount': self.payload.cover_amount,
            'family_member_details': [member.model_dump() for member in self.payload.family_member_details],
            "city_tier": self.payload.city_tier,
            "tenure": self.payload.tenure,
            'purchased_at': datetime.now(),
            "user": self.user,
        }
        purchases_collection.insert_one(mongo_payload)

        mongo_payload.pop("user")

        return PlanPurchaseResponse(
            plan_details=PlanDetails(**mongo_payload)
        ).model_dump()
