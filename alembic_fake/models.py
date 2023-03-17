from sqlalchemy import Column, Integer, String

from fake_database import Base_fake


class Loan(Base_fake):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    passport = Column(String, nullable=False)
    period = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
