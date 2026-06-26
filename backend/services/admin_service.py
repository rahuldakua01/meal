from backend.models.user import User
from sqlalchemy.orm import Session
from backend.models.subscription import Subscription

def get_active_users(db: Session):
    students = db.query(User).filter(User.role == "user").all()
    result = []

    for user in students:
        latest_subscription = db.query(Subscription).filter(Subscription.user_id == user.id).order_by(Subscription.end_date.desc()).first()

        sub_info = None
        if latest_subscription and user.status == "Active":
            # The subscription format in DB is serialized e.g.: "premium:nonveg:breakfast,lunch,dinner"
            parts = latest_subscription.meal_plan_name.split(":")
            tier = parts[0] if len(parts) > 0 else "base"
            pref = parts[1] if len(parts) > 1 else "veg"
            meals = parts[2].split(",") if len(parts) > 2 else []

            sub_info = {
                "tier": tier,
                "meals": meals,
                "startDate": latest_subscription.start_date.strftime("%Y-%m-%d") if latest_subscription.start_date else "",
                "status": "active",
                "preference": pref
            }

        result.append({
            "id": str(user.id),
            "name": user.name,
            "email": user.mail,
            "phone": str(user.phone),
            "role": "user",
            "status": user.status,
            "subscription": sub_info
        })

    return result
