import datetime
from enum import Enum
from pydantic import BaseModel, Field, field_validator, validator
from typing import Optional


class Gender(Enum):
    male = "M"
    female = "F"
    undefined = "U"


class ClientType(Enum):
    fl = 1
    ip = 2
    ul = 3


class RequestLoginPass(BaseModel):
    login: str
    password: str = Field(alias="pass")


class ExistingCertsInFNS(BaseModel):
    sn: str
    issued: str


# TODO разбить модель на данные и обвязку запроса
class RequestInfo(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    middleName: Optional[str]

    headPosition: Optional[str]
    headFirstName: Optional[str]
    headLastName: Optional[str]
    headMiddleName: Optional[str]

    company: Optional[str]
    companyFull: Optional[str]

    position: Optional[str]
    department: Optional[str]

    identificationDocumentType: Optional[int]
    passportSerial: Optional[str]
    passportNumber: Optional[str]
    passportDate: Optional[datetime.date]
    passportDivision: Optional[str]
    passportCode: Optional[str]

    idSmevMvd: Optional[str]
    idSmevEGRUL: Optional[str]
    idSmevEGRIP: Optional[str]
    idSmevINNFL: Optional[str]
    idSmevSNILS: Optional[str]

    birthDate: Optional[datetime.date]
    gender: Optional[Gender]

    inn: Optional[str]
    personInn: Optional[str]
    ogrn: Optional[str]
    ogrnip: Optional[str]
    kpp: Optional[str]

    snils: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    companyPhone: Optional[str]

    country: Optional[str]
    region: Optional[int]
    city: Optional[str]
    address: Optional[str]
    index: Optional[str]

    type: Optional[ClientType]
    products: Optional[list[int]]
    offerJoining: Optional[bool]
    regionLaw: Optional[int]
    cityLaw: Optional[str]
    addressLaw: Optional[str]
    createDate: Optional[datetime.datetime]  # '2022-12-28T11:16:19.0328713'

    comment: Optional[str]
    identificationKind: Optional[int]
    forInfoSys: Optional[str]
    managerComment: Optional[str]
    basisOfActs: Optional[str]
    checkCertInFNSStatus: Optional[int]
    fnsCode: Optional[str]
    existingCertsInFNS: Optional[list[ExistingCertsInFNS]]

    @field_validator("createDate", mode="before")
    def parse_date_time(cls, value):
        return datetime.datetime.strptime(value, "%d.%m.%Y %H:%M:%S")

    @field_validator("passportDate", "birthDate", mode="before")
    def parse_date(cls, value):
        return datetime.datetime.strptime(value, "%d.%m.%Y").date()

    @field_validator("phone", mode="before")
    def parse_int_to_str(cls, value):
        return str(value)

    @field_validator("snils", mode="before")
    def format_snils(cls, value):
        str_digits = "".join(char for char in value if char.isdigit())
        if len(str_digits) != 11:
            raise ValueError(f'Ошибка в формате snils : "{str_digits}"')
        return f"{str_digits[:3]}-{str_digits[3:6]}-{str_digits[6:9]} {str_digits[9:]}"


class Attachment:
    def _attachment_content_save(self, content: str, filename: str):
        try:
            with open(filename, "w") as f:
                f.write(content)
                return True, filename
        except Exception as e:
            raise e
            # return False, None

    def download(self, filename: str = None):
        return self._attachment_content_save(
            content=self.contentBase64, filename=filename or self.name
        )
