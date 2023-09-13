from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fantasy_name = Column(String(200))
    rut = Column(String(200))
    business_name = Column(String(200))
    nickname = Column(String(200))
    contact_name = Column(String(200))
    phone = Column(String(200))
    email = Column(String(200))
    adress = Column(String(200))
    commune = Column(String(200))
    payment_method = Column(String(200))

    sales = relationship("Sale", back_populates="client")
