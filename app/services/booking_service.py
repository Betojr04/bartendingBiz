from app import db
from app.models import Booking


def save_booking(data):
    booking = Booking(
        full_name=data.get("full_name"),
        email=data.get("email"),
        phone=data.get("phone"),
        event_type=data.get("event_type"),
        event_date=data.get("event_date"),
        event_time=data.get("event_time"),
        guests=int(data.get("guests")),
        budget=data.get("budget"),
        notes=data.get("notes"),
    )
    db.session.add(booking)
    db.session.commit()
    return booking
