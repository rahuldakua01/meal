from backend.db.base import Base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship

class Plan(Base):
    __tablename__ = "plan"

    id = Column(Integer,primary_key=True,index=True)
    plan_name = Column(String,nullable=False)
    price = Column(Integer,nullable=False)

    subscriptions = relationship(
        "Subscription",
        back_populates="plan"
    )
