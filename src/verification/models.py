from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base


class Passport(Base):
    __tablename__ = "passport"
    id = Column(Integer, primary_key=True)
    number = Column(String(120), unique=True, nullable=False)
    filename = Column(String)
    content_type = Column(String)
    data = Column(LargeBinary)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="passport", lazy=False)
