from pydantic import BaseModel
from pydantic.networks import EmailStr

# {
#     "id": "110010986932044647324",
#     "email": "21038@hyundai.hs.kr",
#     "verified_email": True,
#     "name": "11002김동현",
#     "given_name": "김동현",
#     "family_name": "11002",
#     "picture": "https://lh3.googleusercontent.com/a/AATXAJzusswNrgMRPLv_SRxTBQ2kxJtpB_ZCcTjKHk-z=s96-c",
#     "locale": "ko",
#     "hd": "hyundai.hs.kr"
# }


class User(BaseModel):
    id: str
    email: EmailStr
    full_name: str
    name: str
    student_id: str
    is_student: bool
    grade: int
    classnum: int
    number: int


def parse_google_response(data: dict) -> dict:
    user: dict = dict()
    user["id"] = data.get("id")
    user["email"] = data.get("email")
    user["full_name"] = data.get("name")
    user["name"] = data.get("given_name")
    user["student_id"] = data.get("family_name")
    user["is_student"] = True if user["student_id"].isnumeric() else False
    user["grade"] = int(user["student_id"][0]) if user["is_student"] else 0
    user["classnum"] = int(user["student_id"][1:3]) if user["is_student"] else 0
    user["number"] = int(user["student_id"][3:5]) if user["is_student"] else 0
    return user
