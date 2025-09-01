"""
Minimal seed script to populate the database with test data

"""

from datetime import datetime
from db.models import session, Suppliers, Product_category, Product, Customers, Orders, Order_items, Supply_orders

def seed():
    # --- Suppliers ---
    s1 = Suppliers(name="ElectroHub Ltd", email="sales@electrohub.com", phone="0711223344", address="Nairobi")
    s2 = Suppliers(name="Appliance World", email="info@applianceworld.com", phone="0799887766", address="Mombasa")
    session.add_all([s1, s2])
    session.commit()

    # --- Categories ---
    c1 = Product_category(name="Televisions", quantity_in_stock=0, description="Smart TVs")
    c2 = Product_category(name="Refrigerators", quantity_in_stock=0, description="Home fridges")
    session.add_all([c1, c2])
    session.commit()

    # --- Products ---
    p1 = Product(name="Sony Bravia 50-inch", brand="Sony", price=55000.00, availability=True, category_id=c1.id, description="4K HDR Smart TV")
    p2 = Product(name="Samsung Double-door Fridge", brand="Samsung", price=72000.00, availability=True, category_id=c2.id, description="500L fridge")
    session.add_all([p1, p2])
    session.commit()

    # --- Customers ---
    cust1 = Customers(first_name="Alice", last_name="Mwangi", email="alice@test.com", phone="0722334455", address="Nairobi")
    cust2 = Customers(first_name="Brian", last_name="Otieno", email="brian@test.com", phone="0733445566", address="Kisumu")
    session.add_all([cust1, cust2])
    session.commit()

    # --- Orders + Items ---
    o1 = Orders(customer_id=cust1.id, order_date=datetime.now(), order_status="Not Delivered")
    session.add(o1)
    session.commit()

    oi1 = Order_items(order_id=o1.id, product_id=p1.id, quantity=1)
    session.add(oi1)
    session.commit()

    # --- Supply Orders ---
    so1 = Supply_orders(product_id=p1.id, quantity=10, supplier_id=s1.id, status="Delivered")
    so2 = Supply_orders(product_id=p2.id, quantity=5, supplier_id=s2.id, status="Not Delivered")
    session.add_all([so1, so2])
    session.commit()


if __name__ == "__main__":
    seed()
