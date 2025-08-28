from sqlalchemy import Integer, String, Text, Column, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Product_category(Base):
    __tablename__ = "product_categories"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    quantity_in_stock = Column(Integer(), nullable=False)
    description = Column(Text())


    products = relationship('Product', back_populates='category')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('product_categories.id'))
    
    category = relationship('Product_category', back_populates='products')