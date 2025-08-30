from models import Supply_orders, Suppliers, Product_category, Product, Customers, Orders, Order_items, session

# -------------------------------------------------Supply_orders CRUD-----------------------------------------------------------

def add_supply_order (product_id, quantity, supplier_id, status ):
    new_supply_order = Supply_orders(product_id = product_id, quantity=quantity, supplier_id=supplier_id, status=status)
    session.add(new_supply_order)
    session.commit()

def get_all_supply_orders():
    return session.query(Supply_orders).all

def update_order_status(supply_order_id, new_order_status):
    order = session.query(Supply_orders).filter_by(id=supply_order_id).first()

    if order:
        order.status = new_order_status
        session.commit()
        print(f"Order status of supply order with ID {supply_order_id} has been updated successfully.")
    else:
        print(f"Supply order with ID {supply_order_id} has not been updated. Ensure ID is correct")

def delete_supply_order(supply_order_id):
    order = session.query(Supply_orders).filter_by(id=supply_order_id).first()

    if order:
        session.delete(order)
        session.commit()
        print(f"Supply order deleted succesfully")
    else:
        print(f"Supply order has not been deleted. Ensure ID is valid")



# ---------------------------------------------------Suppliers CRUD-------------------------------------------------------------
def add_supplier(name, email, phone, address):
    new_supplier = Suppliers(name=name, email=email, phone=phone, address=address)
    session.add(new_supplier)
    session.commit()

def get_suppliers():
    return session.query(Suppliers).all

def delete_supplier(supplier_id):
    supplier = session.query(Suppliers).filter_by(id=supplier_id).first()

    if supplier:
        session.delete(supplier)
        session.commit()
        print(f"Supplier with ID {supplier_id} has been deleted successfully")
    else:
        print(f"Supplier has not been deleted. Ensure ID is valid")



# ---------------------------------------------------Product_category CRUD-----------------------------------------------------
def add_product_category(name, quantity_in_stock, description):
    new_product_category = Product_category(name=name, quantity_in_stock=quantity_in_stock, description=description)
    session.add(new_product_category)
    session.commit()

def get_product_categories():
    return session.query(Product_category).all

def delete_product_category(product_category_id):
    category = session.query(Product_category).filter_by(id=product_category_id).first()

    if category:
        session.delete(category)
        session.commit()
        print(f"Category with ID {product_category_id} has been deleted successfully")
    else:
        print(f"Category has not been deleted. Ensure ID is valid")



# ----------------------------------------------------Product CRUD-------------------------------------------------------------
def add_product(name, brand, price, availability, category_id, description):
    new_product = Product(name=name, brand=brand, price=price, availability=availability, category_id=category_id, description=description)
    session.add(new_product)
    session.commit()

def get_product():
    return session.query()



# ------------------------------------------------------Customers CRUD---------------------------------------------------------
def add_customer(first_name, last_name, email, phone, address):
    new_customer = Customers(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address)
    session.add(new_customer)
    session.commit()



# -------------------------------------------------------Orders CRUD-----------------------------------------------------------
def add_order(customer_id, order_date, order_status):
    new_order = Orders(customer_id=customer_id, order_date=order_date, order_status=order_status)
    session.add(new_order)
    session.commit()



# -------------------------------------------------------Order_items CRUD------------------------------------------------------
def add_order_item(order_id, product_id, quantity):
    new_order_item = Order_items(order_id=order_id, product_id=product_id, quantity=quantity)
    session.add(new_order_item)
    session.commit()