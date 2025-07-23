from datetime import datetime
from app import db


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    event_date = db.Column(db.String(20), nullable=False)
    event_time = db.Column(db.String(20), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
