# def insert_patient_data(name:str, age:int) -> None: #type hinting
#     #Type Validation
#     if type(name)==str and type(age)==int:
#         #Data Validation
#         if age<0:
#             raise ValueError("Age can't be negative!")
#         else:
#             print(name)
#             print(age)
#             print("inserted into database")
#     else:
#         raise TypeError("Incorrect data type!")
# insert_patient_data('nitish','thirty')
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    # name:str=Field(max_length=50)
    name:Annotated[str,Field(max_length=50,title="Name of Patient",description="Give the name of the patient in less than 50 chars",examples=["Pacific","Atul"])]
    age: int=Field(gt=0,lt=120)
    email:EmailStr
    linkedin_url:AnyUrl
    weight:Annotated[float,Field(gt=0,strict=True)]
    # married:bool
    married:Annotated[bool,Field(default=None, description="Is the patient married or not!")]
    allergies:Annotated[Optional[List[str]], Field(default=None,max_length=5)]
    contact_details:Dict[str,str]

    #Data Validation
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']

        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("not a valid domain")
        return value
    
    #Data Transformation
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    #Field Validation in "BEFORE MODE"
    @field_validator('age',mode='before')
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")




def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Information Inserted!")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Updated!")


patient_info={"name":"nitish","age":30,'email':'abc@icici.com',"weight":75.2,"linkedin_url":"https://adfasd.com","married":True,"allergies":['pollen','dust'],"contact_details":{'email':'abc@gmail.com','phone':'242442'}}

patient1=Patient(**patient_info)    #Object Creation-> Validation-> Type Coercion

update_patient_data(patient1)

