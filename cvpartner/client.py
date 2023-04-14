import pydantic
import requests

import config
from cvpartner.types.cv import CVResponse
from cvpartner.types.user_list import UserListResponse


base_url = f"https://{config.cvpartner_domain}/api"


def search_users(cvpartner_api_key: str):
    headers = {"Authorization": f"Bearer {cvpartner_api_key}"}
    url = f"{base_url}/v2/users/search"
    params: dict[str, int | bool | str] = {
        "from": 0,
        "size": 10,
        "sort_by": "email",
        "deactivated": False,
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        user_data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Couldn't decode response from CVPartner:\n" + response.text)
        raise

    try:
        return pydantic.parse_obj_as(UserListResponse, user_data)
    except pydantic.ValidationError:
        print("Couldn't parse response from CVPartner:\n" + response.text)
        raise


def find_user_id(email: str, cvpartner_api_key: str) -> tuple[str, str]:
    headers = {"Authorization": f"Bearer {cvpartner_api_key}"}
    url = f"{base_url}/v1/users/find?email={email}"
    response = requests.get(url, headers=headers)
    try:
        user_data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Couldn't decode response from CVPartner:\n" + response.text)
        raise

    user_id = user_data["user_id"]
    cv_id = user_data["default_cv_id"]
    return user_id, cv_id


def query_cv(user_id: str, cv_id: str, cvpartner_api_key: str) -> CVResponse:
    headers = {"Authorization": f"Bearer {cvpartner_api_key}"}
    url = f"{base_url}/v3/cvs/{user_id}/{cv_id}"
    response = requests.get(url, headers=headers)
    try:
        cv_data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Couldn't decode response from CVPartner:\n" + response.text)
        raise

    try:
        cv = CVResponse(**cv_data)
    except pydantic.errors.JsonError as e:
        print("Couldn't parse response from CVPartner:\n" + str(e))
        raise

    return cv
