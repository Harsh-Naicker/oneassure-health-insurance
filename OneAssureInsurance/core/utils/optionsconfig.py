from OneAssureInsurance import insurance_rates_collection

tier_id_list = insurance_rates_collection.distinct("tier_id")
age_list = insurance_rates_collection.distinct("age")
sum_insured_list = insurance_rates_collection.distinct("sum_insured")
tenures_list = insurance_rates_collection.distinct("tenure")

tier_id_options = [
    {"label": str(option), "value": option, "selected": False} for option in tier_id_list
]

age_options = [
    {"label": str(option), "value": option, "selected": False} for option in age_list
]

sum_insured_options = [
    {"label": str(option), "value": option, "selected": False} for option in sum_insured_list
]

tenure_options = [
    {"label": str(option), "value": option, "selected": False} for option in tenures_list
]
