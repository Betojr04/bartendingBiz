from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.booking_service import save_booking

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@main.route("/book", methods=["POST"])
def book():
    data = {
        "full_name": request.form.get("full_name"),
        "email": request.form.get("email"),
        "phone": request.form.get("phone"),
        "event_type": request.form.get("event_type"),
        "event_date": request.form.get("event_date"),
        "event_time": request.form.get("event_time"),
        "guests": request.form.get("guests"),
        "budget": request.form.get("budget"),
        "addons": request.form.getlist("addons"),  # ✅ Handles multiple add-ons
        "notes": request.form.get("notes"),
    }

    save_booking(data)
    flash("Your booking request was submitted successfully!", "success")
    return redirect(url_for("main.home"))
