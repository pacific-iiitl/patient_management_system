from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Address(BaseModel):
    
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name: str
    gender:str
    # email:EmailStr
    # weight:float
    # height:float
    age:str
    address: Address

address_dict={'city':'gurgaon','state':'haryana','pin':'232110'}
address1=Address(**address_dict)

patient_dict={'name':'pankaj','gender':'male','age':'23','address':address1}
patient1=Patient(**patient_dict)
print(patient1)