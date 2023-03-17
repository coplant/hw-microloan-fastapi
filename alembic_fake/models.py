import sys
from inspect import getsourcefile
from os.path import abspath
from pathlib import Path

from sqlalchemy import Column, Integer, String, Boolean

sys.path.append(str(Path(__file__).parents[1]))
sys.path.append("..")

from fake_database import Base_fake


class FakeUser(Base_fake):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    passport = Column(String, nullable=False)
    period = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    is_active = Column(Boolean)
