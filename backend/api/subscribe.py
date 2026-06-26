from fastapi import APIRouter,Depends
from backend.core.dependency import get_db
from sqlalchemy.orm import Session
from backend.services.subscription_service import create_subscribe
from backend.core.dependency import user_requird
from backend.schemas.subscribe import SubscriptionCreate




router = APIRouter(prefix="/subscribe", tags=["Subscribe"])


@router.post("/subscription")
def sub(data:SubscriptionCreate ,current_user : Session=Depends(user_requird), db:Session=Depends(get_db)):
    return create_subscribe(data,current_user,db)


# @router.patch("/renew")
# def renew_plan(data, current_user : Session=Depends(user_requird),db:Session=Depends(get_db)):
#     return renew(data,db)
