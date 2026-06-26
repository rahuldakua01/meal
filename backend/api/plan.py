from fastapi import APIRouter,Form,Depends
from sqlalchemy.orm import Session
from backend.core.dependency import get_db
from backend.services.plan_service import plan,update,get_plans
from backend.core.dependency import admin_requird
from backend.schemas.subscription_plan import PlanCreated



router = APIRouter(prefix="/plan" , tags=["Plan"])


@router.post("/add_plan")
def add_plan(
    data : PlanCreated,
    current_user : Session=Depends(admin_requird),
    db:Session=Depends(get_db)
):
    

    return plan(
        name = data.name,
        price = data.price,
        db = db
    )


@router.patch("/update_plan/{plan_name}")
def update_plan(
        plan_name:str,
        price: int = Form(...),
        current_user:Session=Depends(admin_requird),
        db:Session=Depends(get_db)
    ):
    return update(name=plan_name,price = price,db=db)


@router.get("/get_plans")
def fetch_all_plans(db:Session=Depends(get_db)):
    return get_plans(db)
