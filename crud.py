from sqlalchemy.orm import Session
from datetime import datetime

from models import Customer, Package, Shipment, Tracking


# CUSTOMER

def create_customer(db: Session, customer):
    obj = Customer(**customer.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


# PACKAGE

def create_package(db: Session, package):

    customer = db.query(Customer).filter(
        Customer.id == package.customer_id
    ).first()

    if not customer:
        raise Exception("Customer not found")

    if package.weight <= 0:
        raise Exception("Weight must be greater than 0")

    obj = Package(**package.dict())

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


# SHIPMENT

def create_shipment(db: Session, shipment):

    obj = Shipment(
        package_id=shipment.package_id,
        status="Pending"
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


def update_shipment_status(
    db: Session,
    shipment_id: int,
    status: str
):

    shipment = db.query(Shipment).filter(
        Shipment.id == shipment_id
    ).first()

    if not shipment:
        return None

    if shipment.status == "Delivered":
        raise Exception(
            "Delivered shipment cannot be modified"
        )

    shipment.status = status

    db.commit()
    db.refresh(shipment)

    return shipment


# TRACKING

def create_tracking(db: Session, tracking):

    existing = db.query(Tracking).filter(
        Tracking.tracking_id == tracking.tracking_id
    ).first()

    if existing:
        raise Exception("Tracking ID already exists")

    obj = Tracking(**tracking.dict())

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


def update_tracking_location(
    db: Session,
    tracking_id: str,
    location: str
):

    tracking = db.query(Tracking).filter(
        Tracking.tracking_id == tracking_id
    ).first()

    if not tracking:
        return None

    tracking.current_location = location
    tracking.updated_time = datetime.utcnow()

    db.commit()
    db.refresh(tracking)

    return tracking