from datetime import datetime
from sqlalchemy.orm import Session
from backend.models.meal import Meal1,Meal2,Meal3


def get_today_menu(db: Session):
    today = datetime.now().strftime("%A")

    breakfast = db.query(Meal1).filter(Meal1.day == today).all()
    lunch = db.query(Meal2).filter(Meal2.day == today).all()
    dinner = db.query(Meal3).filter(Meal3.day == today).all()

    return {
        "Day": today,
        "Breakfast": [
            {
                "name": meal.name,
                "category": meal.category,
                "image": meal.image
            }
            for meal in breakfast
        ],
        "Lunch": [
            {
                "name": meal.name,
                "category": meal.category,
                "image": meal.image
            }
            for meal in lunch
        ],
        "Dinner": [
            {
                "name": meal.name,
                "category": meal.category,
                "image": meal.image
            }
            for meal in dinner
        ]
    }


def get_day_menu(day: str, db: Session):

    breakfast = db.query(Meal1).filter(Meal1.day == day).all()
    lunch = db.query(Meal2).filter(Meal2.day == day).all()
    dinner = db.query(Meal3).filter(Meal3.day == day).all()

    return {
        "Day": day,

        "Breakfast": [
            {
                "name": meal.name,
                "category": meal.category,
                "image": meal.image
            }
            for meal in breakfast
        ],

        "Lunch": [
            {
                "name": meal.name,
                "category": meal.category,
                "image": meal.image
            }
            for meal in lunch
        ],

        "Dinner": [
            {
                "name": meal.name,
                "category": meal.category,
                "image": meal.image
            }
            for meal in dinner
        ]
    }


def get_weekly_menu(db: Session):
    breakfasts = db.query(Meal1).all()
    lunches = db.query(Meal2).all()
    dinners = db.query(Meal3).all()

    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    weekly = {day: {} for day in days}

    def map_type(cat: str):
        if not cat:
            return "veg"
        c = cat.lower().replace("-", "")
        return "veg" if "veg" in c and "non" not in c else "nonveg"

    for meal in breakfasts:
        day_key = meal.day.lower()
        if day_key in weekly:
            t = map_type(meal.category)
            key = "breakfastVeg" if t == "veg" else "breakfastNonVeg"
            weekly[day_key][key] = {
                "name": meal.name,
                "description": meal.description or "",
                "calories": meal.calories or 0,
                "image": meal.image or "",
                "type": t
            }

    for meal in lunches:
        day_key = meal.day.lower()
        if day_key in weekly:
            t = map_type(meal.category)
            key = "lunchVeg" if t == "veg" else "lunchNonVeg"
            weekly[day_key][key] = {
                "name": meal.name,
                "description": meal.description or "",
                "calories": meal.calories or 0,
                "image": meal.image or "",
                "type": t
            }

    for meal in dinners:
        day_key = meal.day.lower()
        if day_key in weekly:
            t = map_type(meal.category)
            key = "dinnerVeg" if t == "veg" else "dinnerNonVeg"
            weekly[day_key][key] = {
                "name": meal.name,
                "description": meal.description or "",
                "calories": meal.calories or 0,
                "image": meal.image or "",
                "type": t
            }

    return weekly
