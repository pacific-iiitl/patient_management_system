from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Address(BaseModel):
    
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name: str
    gender:str='Male'
    # email:EmailStr
    # weight:float
    # height:float
    age:str
    address: Address

address_dict={'city':'gurgaon','state':'haryana','pin':'232110'}
address1=Address(**address_dict)

# patient_dict={'name':'pankaj','gender':'male','age':'23','address':address1}
patient_dict={'name':'pankaj','age':'23','address':address1}
patient1=Patient(**patient_dict)
# print(patient1)

# temp=patient1.model_dump()  #{'name': 'pankaj', 'gender': 'male', 'age': '23', 'address': {'city': 'gurgaon', 'state': 'haryana', 'pin': '232110'}} \n <class 'dict'>
# temp=patient1.model_dump_json() #{"name":"pankaj","gender":"male","age":"23","address":{"city":"gurgaon","state":"haryana","pin":"232110"}} \n <class 'str'>
# temp=patient1.model_dump(include=['name','age'])    #{'name': 'pankaj', 'age': '23'}
# temp=patient1.model_dump(exclude={'address':['state']}) #{'name': 'pankaj', 'gender': 'male', 'age': '23', 'address': {'city': 'gurgaon', 'pin': '232110'}}\n <class 'dict'>
temp=patient1.model_dump(exclude_unset=True) #{'name': 'pankaj', 'age': '23', 'address': {'city': 'gurgaon', 'state': 'haryana', 'pin': '232110'}}\n <class 'dict'>

print(temp)
print(type(temp))