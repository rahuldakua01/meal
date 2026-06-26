from backend.models.subscription import Subscription
from backend.models.user import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta



def create_subscribe(data,current_user, db: Session):

    user = db.query(User).filter(User.id == current_user["user_id"]).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if user.status == "Active":
        raise HTTPException(
            status_code=400,
            detail="User already has an active subscription"
        )

    subscription = Subscription(
        user_id=user.id,
        meal_plan_name=data.meal_plan_name,
        price = data.price,
        plan_id = data.plan_id,
        start_date=datetime.utcnow(),
        end_date=datetime.utcnow() + timedelta(days=30),
    )

    db.add(subscription)

    user.status = "Active"

    db.commit()
    db.refresh(subscription)


    return {
        "message": "Subscription created successfully",
        "subscription_id": subscription.id
    }


def expire_subscriptions(db:Session):

    expired = db.query(Subscription).filter(
        Subscription.end_date < datetime.utcnow()
    ).all()

    for sub in expired:
        sub.user.status = "Non-Active"

    db.commit()
