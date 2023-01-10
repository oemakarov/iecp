import datetime
from enum import Enum 
from pydantic import BaseModel, Field, validator
from typing import Optional



class Gender(Enum):
    male = 'M'
    female = 'F'
    undefined = 'U'


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
    passportDate: Optional[str]
    passportDivision: Optional[str]
    passportCode: Optional[str]
    
    idSmevMvd: Optional[str]
    idSmevEGRUL: Optional[str]
    idSmevEGRIP: Optional[str]
    idSmevINNFL: Optional[str]
    idSmevSNILS: Optional[str]
    
    birthDate: Optional[str]
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

    @validator('createDate', pre=True)
    def parse_date_time(cls, value):
        return datetime.datetime.strptime(value, '%d.%m.%Y %H:%M:%S')


class Attachment():
    def _attachment_content_save(self, content: str, filename: str):
        try:
            with open(filename, 'w') as f:
                f.write(content)
                return True, filename
        except Exception as e:
            raise e
            # return False, None

    def download(self, filename:str=None):
        return self._attachment_content_save(content=self.contentBase64, 
                                            filename=filename or self.name)

