from crypt import methods
from flask import request, Response, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from pydantic import ValidationError
from OneAssureInsurance.core.utils.pydanticmodels import (
    PremiumInquiryFormConfig,
    PremiumRateQuery,
    PlanPurchasePayload,
)
from OneAssureInsurance import (
    ErrorResponseModel,
    users_collection
)
from OneAssureInsurance.core.controllers.premiumratecontroller import (
    PremiumRateController
)
from OneAssureInsurance.core.controllers.planpurchasecontroller import (
    PlanPurchaseController
)
from pymongo.errors import (
    ConnectionFailure, 
    NetworkTimeout, 
    ExecutionTimeout, 
    ServerSelectionTimeoutError
)

core=Blueprint('core', __name__)

@core.route('/get-premium-rate/', methods=['POST'])
@jwt_required()
def get_premium_rate():
    try:
        current_user_email = get_jwt_identity()
        current_user = users_collection.find_one({"email": current_user_email})

        if current_user:
            data = request.json
            query = PremiumRateQuery(**data)

            controller = PremiumRateController(query)
            return controller.get_response()
        else:
            return Response(
                ErrorResponseModel(
                    message="Invalid user"
                ),
                status=400
            )
    except ValidationError as e:
        return Response(
            ErrorResponseModel(
                message="Information provided is not in the correct format"
            ).model_dump(),
            status=400
        )

@core.route('/get-premium-rate-form-config/', methods=['GET'])
@jwt_required()
def get_form_options_config():
    try:
        current_user_email = get_jwt_identity()
        current_user = users_collection.find_one({"email": current_user_email})

        if current_user:
            return PremiumInquiryFormConfig().model_dump()
        return Response(
            ErrorResponseModel(
                message="User does not exist"
            ).model_dump(),
            status=400
        )
    except (ServerSelectionTimeoutError, ConnectionFailure, NetworkTimeout, ExecutionTimeout) as e:
        return Response(
            ErrorResponseModel(
                message="Something went wrong, please try again in some time"
            ).model_dump(),
            status=500
        )

@core.route('/purchase-insurance-plan/', methods=['POST'])
@jwt_required()
def purchase_insurance_plan():
    try:
        current_user_email = get_jwt_identity()
        current_user = users_collection.find_one({"email": current_user_email})
        if current_user:
            data = request.json
            payload = PlanPurchasePayload(**data)
            controller = PlanPurchaseController(payload, current_user_email)

            return controller.purchase_plan()
        else:
            return Response(
                ErrorResponseModel(
                    message="Invalid user"
                ),
                status=400
            )

    except ValidationError as e:
        return Response(
            ErrorResponseModel(
                message="Information provided is not in the correct format"
            ).model_dump(),
            status=400
        )