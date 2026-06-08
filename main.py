from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import Customer, Package, Shipment, Tracking
from schemas import *
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Courier Tracking System")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CUSTOMER APIs

@app.post("/customers")
def add_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return crud.create_customer(db, customer)


@app.get("/customers")
def get_customers(
    db: Session = Depends(get_db)
):
    return db.query(Customer).all()


# PACKAGE APIs

@app.post("/packages")
def add_package(
    package: PackageCreate,
    db: Session = Depends(get_db)
):
    return crud.create_package(db, package)


@app.get("/packages")
def get_packages(
    db: Session = Depends(get_db)
):
    return db.query(Package).all()


# SHIPMENT APIs

@app.post("/shipments")
def add_shipment(
    shipment: ShipmentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_shipment(db, shipment)


@app.put("/shipments/{shipment_id}")
def update_status(
    shipment_id: int,
    data: ShipmentStatus,
    db: Session = Depends(get_db)
):
    return crud.update_shipment_status(
        db,
        shipment_id,
        data.status
    )


@app.get("/shipments")
def get_shipments(
    db: Session = Depends(get_db)
):
    return db.query(Shipment).all()


# TRACKING APIs

@app.post("/tracking")
def add_tracking(
    tracking: TrackingCreate,
    db: Session = Depends(get_db)
):
    return crud.create_tracking(db, tracking)


@app.get("/track/{tracking_id}")
def track_package(
    tracking_id: str,
    db: Session = Depends(get_db)
):

    tracking = db.query(Tracking).filter(
        Tracking.tracking_id == tracking_id
    ).first()

    if not tracking:
        raise HTTPException(
            status_code=404,
            detail="Tracking ID not found"
        )

    return tracking


@app.put("/track/{tracking_id}")
def update_location(
    tracking_id: str,
    data: TrackingLocation,
    db: Session = Depends(get_db)
):
    return crud.update_tracking_location(
        db,
        tracking_id,
        data.current_location
    )