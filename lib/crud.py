from db.models import Supply_orders, Suppliers, Product_category, Product, Customers, Orders, Order_items, session

# -------------------------------------------------Supply_orders CRUD-----------------------------------------------------------

def add_supply_order (product_id, quantity, supplier_id, status ):
    new_supply_order = Supply_orders(product_id = product_id, quantity=quantity, supplier_id=supplier_id, status=status)
    session.add(new_supply_order)
    session.commit()

def get_all_supply_orders():
    return session.query(Supply_orders).all()

def update_supply_order_status(supply_order_id, new_order_status):
    order = session.query(Supply_orders).filter_by(id=supply_order_id).first()

    if not order:
        print(f"Supply order with ID {supply_order_id} not found.")
        return

    if order.status == "Delivered":
        print(f"Order with ID {supply_order_id} is already 'Delivered'. No update needed.")
        return

    order.status = new_order_status
    session.commit()
    print(f"Order status for supply order ID {supply_order_id} has been updated to '{new_order_status}'.")

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
    print(f"{new_supplier.name} has been added successfully")

def get_suppliers():
    return session.query(Suppliers).all()

def delete_supplier(supplier_name):
    supplier = session.query(Suppliers).filter_by(name=supplier_name).first()

    if supplier:
        session.delete(supplier)
        session.commit()
        print(f"Supplier ({supplier_name}) has been deleted successfully")
    else:
        print(f"Supplier has not been deleted. Ensure ID is valid")



# ---------------------------------------------------Product_category CRUD-----------------------------------------------------
def add_product_category(name, quantity_in_stock, description):
    new_product_category = Product_category(name=name, quantity_in_stock=quantity_in_stock, description=description)
    session.add(new_product_category)
    session.commit()
    print(f"{new_product_category.name} has been added successfully")

def get_product_categories():
    return session.query(Product_category).all()

def delete_product_category(product_category_name):
    category = session.query(Product_category).filter_by(name=product_category_name).first()

    if category:
        session.delete(category)
        session.commit()
        print(f"Category with ID {product_category_name} has been deleted successfully")
    else:
        print(f"Category has not been deleted. Ensure ID is valid")



# ----------------------------------------------------Product CRUD-------------------------------------------------------------
def add_product(name, brand, price, availability, category_id, description):
    new_product = Product(name=name, brand=brand, price=price, availability=availability, category_id=category_id, description=description)
    session.add(new_product)
    session.commit()
    print(f"{new_product.name} has been added successfully")

def get_all_products():
    return session.query(Product).all()

def delete_product(product_name):
    product = session.query(Product).filter_by(name=product_name).first()

    if product:
        session.delete(product)
        session.commit()
        print(f"Product with ID {product_name} has been deleted successfully")
    else:
        print(f"Product has not been deleted. Ensure ID is valid")



# ------------------------------------------------------Customers CRUD---------------------------------------------------------
def add_customer(first_name, last_name, email, phone, address):
    new_customer = Customers(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address)
    session.add(new_customer)
    session.commit()
    print(f"{new_customer.first_name} {new_customer.last_name} has been added successfully")

def get_customers():
    return session.query(Customers).all()

def delete_customer(customer_first_name):
    customer = session.query(Customers).filter_by(first_name=customer_first_name).first()

    if customer:
        session.delete(customer)
        session.commit()
        print(f"Customer with ID {customer_first_name} has been deleted successfully")
    else:
        print(f"Customer has not been deleted. Ensure ID is valid")



# -------------------------------------------------------Orders CRUD-----------------------------------------------------------
def add_order(customer_id, order_date, order_status):
    new_order = Orders(customer_id=customer_id, order_date=order_date, order_status=order_status)
    session.add(new_order)
    session.commit()
    print(f"{new_order.id} has been added successfully")

def get_orders():
    return session.query(Orders).all()

def update_order_status(order_id, new_order_status):
    order = session.query(Orders).filter_by(id=order_id).first()

    if order:
        order.status = new_order_status
        session.commit()
        print(f"Order status of order with ID {order_id} has been updated successfully.")
    else:
        print(f"Order with ID {order_id} has not been updated. Ensure ID is correct")

def delete_order(order_id):
    order = session.query(Orders).filter_by(id=order_id).first()

    if order:
        session.delete(order)
        session.commit()
        print(f"Order with ID {order_id} has been deleted successfully")
    else:
        print(f"Order has not been deleted. Ensure ID is valid")


# -------------------------------------------------------Order_items CRUD------------------------------------------------------
def add_order_item(order_id, product_id, quantity):
    new_order_item = Order_items(order_id=order_id, product_id=product_id, quantity=quantity)
    session.add(new_order_item)
    session.commit()
    print(f"{new_order_item.id} has been added successfully")

def get_order_items():
    return session.query(Order_items).all()

def delete_order_item(item_id):
    item = session.query(Order_items).filter_by(id=item_id).first()

    if item:
        session.delete(item)
        session.commit()
        print(f"Order item with ID {item_id} has been deleted successfully")
    else:
        print(f"Order item has not been deleted. Ensure ID is valid")
