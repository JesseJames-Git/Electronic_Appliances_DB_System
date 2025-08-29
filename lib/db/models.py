from sqlalchemy import Integer, String, Text, Column, ForeignKey, DateTime, Boolean, Numeric
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
    brand = Column(String, nullable=False)
    price = Column(Numeric(5,2), nullable=False)
    availability = Column(Boolean, nullable=False)
    category_id = Column(Integer, ForeignKey('product_categories.id'))
    description = Column(Text)
    
    category = relationship('Product_category', back_populates='products')
    orders = relationship('Supply_orders', back_populates='products')
    ordered_products = relationship('Orders')

class Suppliers(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    address = Column(String)

    orders = relationship('Supply_orders', back_populates='supplier')

class Supply_orders(Base):
    __tablename__ = 'supply_orders'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    products = relationship('Product', back_populates='orders')
    suppliers = relationship('Suppliers', back_populates='orders')

class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    address = Column(String)

    customer_orders = relationship('Orders', back_populates='customers')

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'),nullable=False)
    order_date = Column(DateTime, nullable=False)
    order_status = Column(Boolean, nullable=False)

    customers = relationship('Customers', back_populates='customer_orders')
    
    
    
