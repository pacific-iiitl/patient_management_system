# Patient Management System API

A modern RESTful API for managing patient records, built using **FastAPI** and **Pydantic v2**. This project allows users to create, read, update, and sort patient data, with automatic calculation of BMI and health verdict for each patient. It is suitable for learning backend API practices and rapid prototyping for healthcare or medical data management.

---

## Features

- **Add and view patients:** Easily register new patients and view their detailed data
- **Update patient information:** Edit existing records quickly via PUT endpoints
- **Automatic BMI calculation:** BMI is recalculated after every create or update, based on height and weight
- **Health verdict assessment:** Patients automatically get a health verdict (`Underweight`, `Normal`, `Obese`) based on BMI
- **Sort and filter:** List patients sorted by height, weight, or BMI (ascending or descending)
- **OpenAPI interactive docs:** Built-in documentation at `/docs` for exploring and testing API endpoints
- **Robust data validation:** Strong type checking and field constraints using Pydantic
- **Simple file-based data storage:** JSON file is used for persistent storage—no external DB needed

---

## Technology Stack

- Python 3.8+
- FastAPI
- Pydantic v2
- Uvicorn (development server)

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>.git
cd <YOUR_REPO_NAME>
```

### Set Up a Virtual Environment

```bash
python -m venv myenv
# On Unix or MacOS
source myenv/bin/activate
# On Windows
myenv\Scriptsctivate
```

### Install Dependencies

```bash
pip install fastapi uvicorn pydantic
```

### Run the Server

```bash
uvicorn main:app --reload
```

Open your browser at [http://localhost:8000/docs](http://localhost:8000/docs) to view and interact with the API documentation.

---

## Example API Endpoints

| Method | URL Path                   | Purpose                        |
|--------|----------------------------|--------------------------------|
| GET    | `/`                        | Welcome message                |
| GET    | `/about`                   | Project information            |
| GET    | `/view`                    | List all patients              |
| GET    | `/patient/{patient_id}`    | Retrieve a patient by ID       |
| POST   | `/create`                  | Add a new patient              |
| PUT    | `/edit/{patient_id}`       | Edit an existing patient       |
| GET    | `/sort`                    | Sort patients by height/weight/BMI |

---

## Patient Data Format

Each patient record is stored in `patients.json`:
```json
{
  "p001": {
    "name": "Smith",
    "city": "Delhi",
    "age": 40,
    "gender": "male",
    "height": 1.70,
    "weight": 70,
    "bmi": 24.2,
    "verdict": "Normal"
  }
}
```

---

## Computed Fields & Validation

- **BMI** (`bmi`): Automatically computed as (weight / height^2) (kg/m²)
- **Verdict** (`verdict`):  
    - Underweight if BMI < 18  
    - Normal if 18 ≤ BMI < 25  
    - Obese if BMI ≥ 25
- All fields are validated for types and ranges (e.g., age > 0 and < 120, height and weight > 0).

---

## Contribution

Contributions, improvements, and bug reports are welcome!  
Open an issue or submit a pull request to get started.

---

## License

MIT License
