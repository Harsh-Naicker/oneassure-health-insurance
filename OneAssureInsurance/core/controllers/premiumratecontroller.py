from OneAssureInsurance.core.utils.pydanticmodels import (
    PremiumRateQuery, 
    PremiumRateResponse
)
from OneAssureInsurance import insurance_rates_collection

class PremiumRateController:
    def __init__(self, query: PremiumRateQuery) -> None:
        self.query = query
        self.tenure = query.tenure
        self.city_tier = query.city_tier
        self.sum_insured = query.cover_amount
        self.num_family_members = len(self.query.family_member_details)
    
    def get_response(self):
        rate = 0

        for index in range(self.num_family_members):
            detail = self.query.family_member_details[index]

            # Mongo Query
            rate_card = insurance_rates_collection.find_one({
                "tenure": self.tenure,
                "tier_id": self.city_tier,
                "age": detail.age,
                "sum_insured": self.sum_insured,
            })

            if rate_card is not None:
                if self.num_family_members == 1:
                    rate += rate_card['rate'] * 0.5
                else:
                    if index != 0:
                        rate += rate_card['rate'] * 0.5
                    else:
                        rate += rate_card['rate']
        
        return PremiumRateResponse(premium_rate=rate).dict()
