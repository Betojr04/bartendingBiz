from app.models import Booking
from app import db


def save_booking(data):
    addons = ", ".join(data.get("addons", [])) if data.get("addons") else None

    booking = Booking(
        full_name=data["full_name"],
        email=data["email"],
        phone=data["phone"],
        event_type=data["event_type"],
        event_date=data["event_date"],
        event_time=data["event_time"],
        guests=data["guests"],
        budget=data["budget"],
        addons=addons,
        notes=data.get("notes", ""),
    )
    db.session.add(booking)
    db.session.commit()
