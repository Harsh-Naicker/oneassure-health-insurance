# OneAssure Fullstack SDE Hiring Assignment
This is the backend repository of the SDE hiring asignment administered by OneAssure.

## Deployed Website
[https://oneassure-health-insurance-fe-demo.onrender.com/](https://oneassure-health-insurance-fe-demo.onrender.com/)

## Installation steps
1. Clone the repository
2. Create a virtualenv or a conda env using python=3.9 and run `pip install -r requirements.txt`

## Running the project
Run command: `python app.py`

## Project Overview
1. Project has been written by keeping MVC architecture in mind
2. Database used is MongoDB
    - Collections inside the DB are: `Users`, `InsuranceRates` and `Purchases`
3. The frontend for this project is server driven, hence all the form elements to be used on FE are planned and sent from the BE
4. User authentication has been implemented using JWT token based approached
5. Pydantic models have been used extensively for data validation across the endpoints

## API Glossary
1. `/get-registration-form-config/` [GET]
    - Returns the form config for the registration process
2. `/register-user/` [POST]
    - Endpoint to register a user
3. `/get-login-form-config/` [GET]
    - Returns the form config for the logic process
4. `/login-user/` [POST]
    - Endpoint to login a user
5. `/is-user-logged-in/` [GET]
    - Endpoint to determine if user is still logged in by validating the `access_token`
6. `/get-premium-rate-form-config/` [GET]
    - Returns the form config for the premium rate inquiry process
7. `/get-premium-rate/` [POST]
    - Returns the evaluated premium rate for the given family member details and other paramaters.
8. `/purchase-insurance-plan/` [POST]
    - Marks a plan as purchased at the evaluated premium rate.
