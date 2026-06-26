from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend.models.sunscription_plan import Plan



def plan(name,price,db:Session):
    existing_plan = db.query(Plan).filter(Plan.plan_name == name).first()
    

    if existing_plan:
        raise HTTPException(
            status_code= 410,
            detail="Plan already Exist"
        )
    
    plan = Plan(
        plan_name = name,
        price = price
    )

    db.add(plan)
    db.commit()
    db.refresh(plan)

    return {"Message" : "Plan added Successfully"}


def update(name,price,db:Session):
    plan = db.query(Plan).filter(Plan.plan_name == name).first()

    if not plan:
        raise HTTPException(
            status_code=404,
            detail="Plan not Found"
        )
    
    plan.price = price

    db.commit()

    return {"Message" : "Plan updated"}


def get_plans(db: Session):
    return db.query(Plan).all()
