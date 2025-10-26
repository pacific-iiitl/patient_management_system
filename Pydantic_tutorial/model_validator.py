from pydantic import BaseModel, Field, AnyUrl, EmailStr, field_validator, model_validator
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):
    name:str
    email:EmailStr
    age: int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("patients elder than 60 must have emergency contact")
        return model


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Information Inserted!")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Updated!")


patient_info={"name":"nitish","age":70,'email':'abc@icici.com',"weight":75.2,'height':1.2,"linkedin_url":"https://adfasd.com","married":True,"allergies":['pollen','dust'],"contact_details":{'email':'abc@gmail.com','phone':'242442','emergency':'2423444'}}

patient1=Patient(**patient_info)    #Object Creation-> Validation-> Type Coercion

update_patient_data(patient1)