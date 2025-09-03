from sqlalchemy import Integer, String, Text, Column, ForeignKey, DateTime, Boolean, Numeric, create_engine, event, CheckConstraint
from sqlalchemy.orm import relationship, declarative_base, sessionmaker, attributes

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
    ordered_products = relationship('Order_items', back_populates='product_order')

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
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    status = Column(String, default='Not Delivered', nullable=False)
    products = relationship('Product', back_populates='orders')
    supplier = relationship('Suppliers', back_populates='orders')

    __table_args__ = (
        CheckConstraint(status.in_(['Delivered', 'Not Delivered'])),
    )
    

class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    address = Column(String)
    customer_orders = relationship('Orders', back_populates='customers_order')

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'),nullable=False)
    order_date = Column(DateTime, nullable=False)
    order_status = Column(String, default='Not Delivered', nullable=False)
    customers_order = relationship('Customers', back_populates='customer_orders')
    order_items = relationship('Order_items', back_populates='items_order')

    __table_args__ = (
        CheckConstraint(order_status.in_(['Delivered', 'Not Delivered'])),
    )

class Order_items(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer)
    items_order = relationship('Orders', back_populates='order_items')
    product_order = relationship('Product', back_populates="ordered_products")


@event.listens_for(Orders.order_status, 'set')
def handle_customer_order_status_change(target, value, oldvalue, initiator):
    """
    Subtracts product quantity from stock in Product_category
    when a customer order status changes to 'Delivered'.
    """
    if value == 'Delivered' and oldvalue != 'Delivered':
        local_session = Session()
        try:
            target = local_session.merge(target) 
            order_items = local_session.query(Order_items).filter_by(order_id=target.id).all()
            
            for item in order_items:
                product = local_session.query(Product).filter_by(id=item.product_id).first()
                if product and product.category: 
                    category = product.category
                    if category.quantity_in_stock >= item.quantity:
                        category.quantity_in_stock -= item.quantity
                        print(f"(-) Subtracted {item.quantity} of {product.name} "
                              f"(Category: {category.name}) for Order ID {target.id}. "
                              f"New stock: {category.quantity_in_stock}")
                    else:
                        print(f"Not enough stock for {product.name} "
                              f"(Category: {category.name}). Current stock: {category.quantity_in_stock}, "
                              f"ordered: {item.quantity}")
            
            local_session.commit()
        except Exception as e:
            local_session.rollback()
            print(f"Error updating stock for customer order {target.id}: {e}")
        finally:
            local_session.close()


@event.listens_for(Supply_orders.status, 'set')
def handle_supply_order_status_change(target, value, oldvalue, initiator):
    """
    Adds product quantity to stock in Product_category
    when a supply order status changes to 'Delivered'.
    """
    if value == 'Delivered' and oldvalue != 'Delivered':
        local_session = Session()
        try:
            target = local_session.merge(target) 
            product = local_session.query(Product).filter_by(id=target.product_id).first()
            if product and product.category:
                category = product.category
                category.quantity_in_stock += target.quantity
                print(f"(+) Added {target.quantity} of {product.name} "
                      f"(Category: {category.name}) for Supply Order ID {target.id}. "
                      f"New stock: {category.quantity_in_stock}")
            local_session.commit()
        except Exception as e:
            local_session.rollback()
            print(f"Error updating stock for supply order {target.id}: {e}")
        finally:
            local_session.close()



    
engine = create_engine("sqlite:///company_system.db")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()