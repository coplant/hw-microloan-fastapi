from datetime import datetime
from sqlalchemy import Column, Integer, TIMESTAMP, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Loan(Base):
    __tablename__ = 'loan'
    id = Column(Integer, primary_key=True)
    creation_date = Column(TIMESTAMP, default=datetime.utcnow)
    end_date = Column(TIMESTAMP, default=None)
    period = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String, default='В обработке')
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', back_populates='loan')
