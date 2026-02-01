from pydantic import BaseModel, Field, field_validator

class CustomerData(BaseModel):
    credit_score: int = Field(..., ge=300, le=850)
    country: str 
    gender: str
    age: int = Field(..., ge=18, le=100)
    tenure: int = Field(..., ge=0)
    balance: float = Field(..., ge=0)
    products_number: int = Field(..., ge=1)
    credit_card: int = Field(..., ge=0, le=1)
    active_member: int = Field(..., ge=0, le=1)
    estimated_salary: float = Field(..., ge=0)

    @field_validator("gender", "country", mode="before")
    @classmethod
    def strip_capitalize(cls, v):
        if isinstance(v, str):
            return v.strip().title()
        return v

    @field_validator("country")
    @classmethod
    def check_country(cls, v):
        if v not in ["France", "Germany", "Spain"]:
            raise ValueError("Country not in the List")
        return v

    @field_validator("gender")
    @classmethod
    def check_gender(cls, v):
        if v not in ["Male", "Female", "Other"]:
            raise ValueError("Invalid gender")
        return v

    @field_validator("tenure")
    @classmethod
    def check_tenure(cls, v, info):
        age = info.data.get("age")
        if age is not None and v > age:
            raise ValueError("Tenure cannot exceed age")
        return v

class PredictionResponse(BaseModel):
    churn: int = Field(..., ge=0, le=1)