
from sqlalchemy import Column, Integer, String
from database.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(255))
    price = Column(Integer)
    quantity = Column(Integer)