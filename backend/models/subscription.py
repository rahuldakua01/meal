from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db.base import Base


class Subscription(Base):

    __tablename__ = "subscriptions"

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    meal_plan_name = Column(String,nullable=False)
    price = Column(Integer)
    start_date = Column(DateTime,default=datetime.utcnow)
    end_date = Column(DateTime)


    plan_id = Column(Integer, ForeignKey("plan.id"), nullable=True)

    user = relationship(
        "User",
        back_populates="subscriptions"
    )
    plan = relationship(
        "Plan",
        back_populates="subscriptions"
    )

