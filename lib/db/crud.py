from models import Supply_orders, Suppliers, Product_category, Product, Customers, Orders, Order_items, session
from sqlalchemy import event
from sqlalchemy.orm import attributes

def add_supply_order (product_id, quantity, supplier_id ):
    new_supply_order = Supply_orders(product_id = product_id, quantity=quantity, supplier_id=supplier_id)
    session.add(new_supply_order)
    session.commit()

def add_supplier(name, email, phone, address):
    new_supplier = Suppliers(name=name, email=email, phone=phone, address=address)
    session.add(new_supplier)
    session.commit()

def add_product_category(name, quantity_in_stock, description):
    new_product_category = Product_category(name=name, quantity_in_stock=quantity_in_stock, description=description)
    session.add(new_product_category)
    session.commit()

@event.listens_for(Orders.order_status,'set')
def stock_tracker(target, value)

def add_product(name, brand, price, availability, category_id, description):
    new_product  = Product(name=name, brand=brand, price=price, availability=availability, category_id=category_id, description=description)
    session.add(new_product)
    session.commit()

def add_customer(first_name, last_name, email, phone, address):
    new_customer = Customers(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address)
    session.add(new_customer)
    session.commit()

def add_order(customer_id, order_date, order_status):
    new_order = Orders(customer_id=customer_id, order_date=order_date, order_status=order_status)
    session.add(new_order)
    session.commit()

def add_order_item(order_id, product_id, quantity):
    new_order_item = Order_items(order_id=order_id, product_id=product_id, quantity=quantity)
    session.add(new_order_item)
    session.commit()