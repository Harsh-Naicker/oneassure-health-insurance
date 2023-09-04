from OneAssureInsurance import users_collection
from OneAssureInsurance.users.utils.pydanticmodels import (
    UserRegistrationFormPayload
)
from OneAssureInsurance import ResponseModel
from datetime import datetime
import bcrypt

class UserRegistrationController:
    def __init__(self, validated_form: UserRegistrationFormPayload) -> None:
        self.validated_form = validated_form
    
    def register_user(self):
        existing_user = users_collection.find_one({"email": self.validated_form.email})

        if existing_user:
            return ResponseModel(
                message="User with this email already exists"
            ).model_dump()

        hashed_password = bcrypt.hashpw(
            self.validated_form.password2.encode('utf-8'), 
            bcrypt.gensalt()
        )

        users_collection.insert_one({
                'name': self.validated_form.full_name, 
                'email': self.validated_form.email, 
                'password': hashed_password,
                'created_at': datetime.now()
            }
        )

        return ResponseModel(
            message="User created successfully"
        ).model_dump()

