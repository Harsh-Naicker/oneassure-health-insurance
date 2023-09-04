from OneAssureInsurance import users_collection
from OneAssureInsurance.users.utils.pydanticmodels import (
    UserLoginFormPayload,
    UserLoginResponseModel
)
from OneAssureInsurance import ResponseModel
import bcrypt
from flask_jwt_extended import create_access_token

class UserLoginController:
    def __init__(self, validated_form: UserLoginFormPayload) -> None:
        self.validated_form = validated_form
    
    def login_user(self):
        existing_user = users_collection.find_one({"email": self.validated_form.email})

        if existing_user:
            if bcrypt.checkpw(self.validated_form.password.encode('utf-8'), existing_user['password']):
                access_token = create_access_token(identity=existing_user['email'])
                return UserLoginResponseModel(
                        access_token=access_token
                    ).model_dump()
            else:
                return ResponseModel(
                    message="Incorrect password",
                    error=True
                )
        else:
            return ResponseModel(
                message="User does not exist",
                error=True
            ).model_dump()

