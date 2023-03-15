from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, MetaData
from sqlalchemy.orm import relationship

from database import Base
from loan.models import Loan
from verification.models import Passport


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    role_id = Column(Integer, ForeignKey("role.id"))
    # role = relationship("Role", back_populates="user", foreign_keys="User.role_id", passive_deletes=True)
    # passport_id = Column(Integer, ForeignKey("passport.id"))
    passport = relationship("Passport", back_populates="user", lazy=False, uselist=False, passive_deletes=True)
    loan = relationship("Loan", back_populates="user", lazy=False, passive_deletes=True)
