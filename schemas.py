from pydantic import BaseModel
from datetime import datetime


class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str


class PackageCreate(BaseModel):
    package_name: str
    weight: float
    package_type: str
    customer_id: int


class ShipmentCreate(BaseModel):
    package_id: int


class ShipmentStatus(BaseModel):
    status: str


class TrackingCreate(BaseModel):
    tracking_id: str
    shipment_id: int
    current_location: str


class TrackingLocation(BaseModel):
    current_location: str