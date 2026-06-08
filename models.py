from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(30), unique=True)
    phone = Column(String(20))
    address = Column(String(100))

    packages = relationship("Package", back_populates="customer")


class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    package_name = Column(String(50))
    weight = Column(Float)
    package_type = Column(String(45))

    customer_id = Column(Integer, ForeignKey("customers.id"))

    customer = relationship("Customer", back_populates="packages")


class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)

    package_id = Column(Integer, ForeignKey("packages.id"))
    status = Column(String(50), default="Pending")


class Tracking(Base):
    __tablename__ = "tracking"

    id = Column(Integer, primary_key=True, index=True)

    tracking_id = Column(String(30), unique=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id"))
    current_location = Column(String(50))

    updated_time = Column(
        DateTime,
        default=datetime.utcnow
    )