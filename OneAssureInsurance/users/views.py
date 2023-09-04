from flask import request, Response, Blueprint
from pydantic import ValidationError
from OneAssureInsurance import (
    ErrorResponseModel,
    users_collection
)
from OneAssureInsurance.users.utils.pydanticmodels import (
    UserRegistrationFormPayload,
    UserRegistrationFormConfig,
    UserLoginFormPayload,
    UserLoginFormConfig,
)
from OneAssureInsurance.users.controllers.userregistrationcontroller import (
    UserRegistrationController
)
from OneAssureInsurance.users.controllers.userlogincontroller import (
    UserLoginController
)
from flask_jwt_extended import jwt_required, get_jwt_identity

users = Blueprint('users', __name__)

@users.route('/get-registration-form-config/', methods=['GET'])
def get_registration_form_config():
    return UserRegistrationFormConfig().model_dump()

@users.route('/register-user/', methods=['POST'])
def register_user():
    try:
        data = request.json
        validated_form = UserRegistrationFormPayload(**data)
        controller = UserRegistrationController(validated_form)

        return controller.register_user()

    except (ValidationError, ValueError) as e:
        return Response(
            ErrorResponseModel(
                message="Invalid user data"
            ),
            status=400
        )

@users.route('/get-login-form-config/', methods=['GET'])
def get_login_form_config():
    return UserLoginFormConfig().model_dump()


@users.route('/login-user/', methods=['POST'])
def login_user():
    try:
        data = request.json
        validated_form = UserLoginFormPayload(**data)
        controller = UserLoginController(validated_form)

        return controller.login_user()

    except (ValidationError, ValueError) as e:
        return Response(
            ErrorResponseModel(
                message="Invalid user data"
            ),
            status=400
        )

@users.route('/is-user-logged-in/', methods=['GET'])
@jwt_required()
def is_user_logged_in():
    current_user_email = get_jwt_identity()
    current_user = users_collection.find_one({"email": current_user_email})

    if current_user is not None:
        return {"is_logged_in": True }
    return {"is_logged_in": False }