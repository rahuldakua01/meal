from fastapi.routing import APIRouter
from backend.schemas.user import RegisterUser,LoginUser
from sqlalchemy.orm import Session
from backend.core.dependency import get_db, get_current_user
from fastapi import Depends, HTTPException
from backend.services.user_service import register_user,user_login
from backend.models.user import User
from backend.models.subscription import Subscription


router = APIRouter()



@router.post("/register")
async def register(data:RegisterUser,db:Session=Depends(get_db)):
    return await register_user(data,db)

@router.post("/login")
def login(data:LoginUser,db:Session=Depends(get_db)):
    return user_login(data,db)

@router.get("/me")
def get_me(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == current_user["user_id"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    latest_sub = db.query(Subscription).filter(Subscription.user_id == user.id).order_by(Subscription.end_date.desc()).first()
    
    subscription_info = None
    if latest_sub and user.status == "Active":
        # Parse the plan name if it follows the format tier:preference:meals
        plan_name = latest_sub.meal_plan_name
        tier = plan_name
        preference = "veg"
        meals = ["breakfast"]
        
        if ":" in plan_name:
            parts = plan_name.split(":")
            if len(parts) >= 3:
                tier = parts[0]
                preference = parts[1]
                meals = parts[2].split(",")
                
        subscription_info = {
            "tier": tier,
            "meals": meals,
            "startDate": latest_sub.start_date.strftime("%Y-%m-%d"),
            "status": "active",
            "preference": preference
        }
        
    return {
        "id": str(user.id),
        "name": user.name,
        "email": user.mail,
        "phone": str(user.phone),
        "role": user.role,
        "status": user.status,
        "subscription": subscription_info
    }
