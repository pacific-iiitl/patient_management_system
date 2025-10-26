from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):
    '''This class uses field value to calculate value for new field on the go. (Dynamic Initialization of BMI)'''
    name:str
    email:EmailStr
    age:int
    weight:float    #kgs
    height:float    #mtr
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field
    # @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Information Inserted!")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('BMI',patient.bmi)
    print(patient.allergies)
    print("Updated!")


patient_info={"name":"nitish","age":70,'email':'abc@icici.com',"weight":75.2,'height':1.2,"linkedin_url":"https://adfasd.com","married":True,"allergies":['pollen','dust'],"contact_details":{'email':'abc@gmail.com','phone':'242442','emergency':'2423444'}}

patient1=Patient(**patient_info)    #Object Creation-> Validation-> Type Coercion

update_patient_data(patient1)