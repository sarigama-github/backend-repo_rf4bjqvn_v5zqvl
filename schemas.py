"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (you can keep them for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# OxySPA B2B Lead schema (this will create a "lead" collection)
class Lead(BaseModel):
    company_name: str = Field(..., min_length=2, max_length=200, description="Company or property name")
    contact_name: str = Field(..., min_length=2, max_length=120, description="Primary contact full name")
    email: EmailStr = Field(..., description="Business email")
    phone: Optional[str] = Field(None, max_length=30, description="Phone number")
    country: Optional[str] = Field(None, max_length=80, description="Country")
    city: Optional[str] = Field(None, max_length=80, description="City")
    spa_count: Optional[int] = Field(None, ge=1, le=5000, description="Number of pools/spas managed")
    current_chemicals: Optional[Literal["chlorine", "bromine", "mixed", "other", "none"]] = Field(
        None, description="Current disinfection approach"
    )
    monthly_chemical_cost: Optional[float] = Field(None, ge=0, description="Estimated monthly spend on chemicals (USD)")
    pain_points: Optional[str] = Field(None, max_length=1000, description="Key challenges with current solution")
    message: Optional[str] = Field(None, max_length=1500, description="Additional notes or requirements")
    consent: bool = Field(True, description="Consent to be contacted and store data")
    source: Optional[str] = Field("landing", description="Lead source identifier")
