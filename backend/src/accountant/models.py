from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from auth.models import User
from loan.models import Loan

from database import Base


class Balance(Base):
    __tablename__ = 'balance'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    loan_id = Column(Integer, ForeignKey('loan.id'))
    creation_date = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    # user = relationship('User', back_populates='balance')
