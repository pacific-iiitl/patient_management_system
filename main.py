from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr,AnyUrl, Field, computed_field
from typing import List, Dict, Annotated, Optional, Literal
import json

app=FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="This field contains id of the patient",examples=['p001', 'p002'])]
    name:Annotated[str, Field(..., description="This field contains name of the patient", examples=['Pacific'])]
    city:Annotated[str, Field(..., description="This field contains city of the patient.")]
    age:Annotated[int,Field(..., description="It contains age of the patient in years", gt=0, lt=120)]
    gender:Annotated[Literal['male','female','others'], Field(..., description="Gender of the patient!")]
    height:Annotated[float,Field(..., description="Height of the patient in mtrs", gt=0)]
    weight:Annotated[float, Field(..., gt=0, description="Weight of the patient in kgs")]

    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi<18:
            return "underweight"
        elif self.bmi<25:
            return "Normal"
        else:
            return "Obesse"
#---------------------------------------------------------------------------------------------------
#Creating new pydantic model for update operations
class PatientUpdate(BaseModel):
    name:Annotated[Optional[str], Field(default=None)]
    city:Annotated[Optional[str], Field(default=None)]
    age:Annotated[Optional[int], Field(default=None,gt=0,lt=120)]
    gender:Annotated[Optional[Literal['male','female','others']],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None,gt=0)]
    weight:Annotated[Optional[float],Field(default=None,gt=0)]


def load_data():
    with open("patients.json",'r') as f:
        data=json.load(f)
    return data

def save_data(data):
    with open("patients.json","w")as f:
        json.dump(data,f)



@app.get("/")
def hello():
    return {"message":"Patient Management System API"}

@app.get("/about")
def about():
    return {"message":"A fully functional API to manage your patient records!"}

@app.get("/view")
def view():
    data=load_data()
    return data
@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path(..., description="ID of the patient in the DB",example='p001')):
    #load all the patients
    data=load_data()

    if patient_id in data:
        return data[patient_id]
    # return {"error":"patient not found"}
    raise HTTPException(status_code=404, detail="Patient not found!")

@app.get("/sort")
def sort_patients(sort_by:str=Query(..., description="Sort on the basis of height, weight or BMI"),order:str=Query('asc',description='sort in asc or desc order')):
    valid_fields=['height', 'weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field selected from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail="Invalid order! Select between asc and desc")
    
    data=load_data()
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(), key=lambda x:x.get(sort_by,0),reverse=True)
    return sorted_data

@app.post("/create")
def create_patient(patient:Patient):
    #load existing data
    data=load_data()

    # check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    # new patient add to the database
    data[patient.id]=patient.model_dump(exclude=['id'])

    #save into json file
    save_data(data)
    return JSONResponse(status_code=201, content={"message":"Patient added Succesfully!"})

@app.put("/edit/{patient_id}")
def edit(patient_id:str, patient_update:PatientUpdate):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found!")
    
    existing_patient_info=data[patient_id]

    #converting pydantic object into a dict
    updated_patient_info=patient_update.model_dump(exclude_unset=True)
    
    for key,value in updated_patient_info.items():
        existing_patient_info[key]=value
    
    #existing_patient_info -> pydantic obj -> updated bmi ->verdict
    existing_patient_info['id']=patient_id
    patient_pydantic_obj=Patient(**existing_patient_info)
    #pydantic obj -> dict
    existing_patient_info = patient_pydantic_obj.model_dump(exclude='id')
    #add this dict to data
    data[patient_id]=existing_patient_info
    
    #Save Data
    save_data(data)
    return JSONResponse(status_code=200, content={"message":"patient details updated"})

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id:str):
    #load data
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200, content={'message':f'patient with {patient_id} deleted sucessfully!'})




    

    



