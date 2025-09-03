import click

from crud import (
    # --------------Suppliers---------------
    add_supplier, get_suppliers, delete_supplier,

    # --------------Suppy Orders---------------
    add_supply_order, get_all_supply_orders, update_supply_order_status, delete_supply_order,

    # --------------Product Categories---------------
    add_product_category, get_product_categories, delete_product_category,

    # --------------Product---------------
    add_product, get_all_products, delete_product,

    # --------------Customers---------------
    add_customer, get_customers, delete_customer,

    # --------------Customer Orders---------------
    add_order, get_orders, delete_order, update_order_status,

    # --------------Order Items---------------
    add_order_item, get_order_items, delete_order_item
)

# -------------------- Menu Structures --------------------
main_menu = {
    1: "Suppliers",
    2: "Supply Orders",
    3: "Product Categories",
    4: "Products",
    5: "Customers",
    6: "Customer Orders",
    7: "Customer Order Items"
}

supplier_menu = {
    1: "Add New Supplier",
    2: "View Company Suppliers",
    3: "Delete Supplier"
}

supply_order_menu = {
    1: "Add New Supply Order",
    2: "View Supply Orders",
    3: "Update Order Status",
    4: "Delete Supply Order"
}

product_category_menu = {
    1: "Add Product Category",
    2: "View all Product Categories",
    3: "Delete Category Product"
}

product_menu = {
    1: "Add Product",
    2: "View all Products",
    3: "Delete Product"
}

customer_menu = {
    1: "Add Customer",
    2: "View Customers",
    3: "Delete Customer"
}

order_menu = {
    1: "Add Order",
    2: "View Orders",
    3: "Delete Order",
    4: "Update Order Status"
}

order_item_menu = {
    1: "Add Order Item",
    2: "View Order Items",
    3: "Delete Order Item"
}


def show_menu(title, menu_dict):
    click.secho(f"------ {title} ------", dim=True, fg="green", bold=True)
    for key, val in menu_dict.items():
        click.secho(f"{key}. {val}", fg="cyan")
    return click.prompt("Option", type=int)


while True:
    click.secho("-------------Welcome to the Electrical Appliances Database System------------", bold=True, fg='green')
    click.secho("Select an Option by number", dim=True, fg='cyan')

    user_input = show_menu("Main Menu", main_menu)
    if user_input == 1:
        supplier_option = show_menu("Suppliers' Options", supplier_menu)
        if supplier_option == 1:
            name = click.prompt("Enter name")
            email = click.prompt("Enter email")
            phone = click.prompt("Enter phone")
            address = click.prompt("Enter Address")
            add_supplier(name, email, phone, address)

        elif supplier_option == 2:
            suppliers = get_suppliers()
            print("Supplier Id |     Name     |      Email      |    Phone    |  Address")
            for s in suppliers:    
                print(f"      {s.id}      | {s.name} | {s.email} | {s.phone} | {s.address}")

        elif supplier_option == 3:
            supplier_name = click.prompt("Enter the name of supplier")
            delete_supplier(supplier_name)


    elif user_input == 2:
        supply_order_option = show_menu("Supply Orders' Options", supply_order_menu)
        if supply_order_option == 1:
            prod_id = click.prompt("Enter Product ID")
            quantity = click.prompt("Enter Quantity")
            supplier = click.prompt("Enter Supplier ID")
            add_supply_order(prod_id, quantity, supplier, status="Not Delivered")

        elif supply_order_option == 2:
            print("Supply Order ID |   Quantity    | Supplier ID      | Order status")
            for so in get_all_supply_orders():    
                print(f"       {so.id}       | {so.quantity} | {so.supplier_id} | {so.status}")

        elif supply_order_option == 3:
            supply_order_id = click.prompt("Enter Supply Order Id")
            update_supply_order_status(supply_order_id, "Delivered")

        elif supply_order_option == 4:
            supply_order_id = click.prompt("Enter Supply Order ID")
            delete_supply_order(supply_order_id)


    elif user_input == 3:
        category_option = show_menu("Product Categories", product_category_menu)
        if category_option == 1:
            name = click.prompt("Enter category name")
            quantity_in_stock = click.prompt("Enter Stock Quantity")
            description = click.prompt("Describe the Category")
            add_product_category(name, quantity_in_stock, description)

        elif category_option == 2:
            print("Category ID  |    Name    |  Quantity in stock  |  Description")
            for pc in get_product_categories():
                print(f"     {pc.id}      | {pc.name} | {pc.quantity_in_stock} | {pc.description}")

        elif category_option == 3:
            name = click.prompt("Enter Existing Category Name")
            delete_product_category(name)


    elif user_input == 4:
        product_option = show_menu("Products", product_menu)
        if product_option == 1:
            name = click.prompt("Enter Product Name")
            brand = click.prompt("Enter Brand Name")
            price = click.prompt("Enter product price")
            availability = click.confirm("Is the product available?", default=True)
            category_id = click.prompt("Enter Category ID (Optional)")
            description = click.prompt("Enter Description (Optional)")
            add_product(name, brand, price, availability, category_id, description)

        elif product_option == 2:
            print("Prod_ID |    Name    |  Brand  |   Price   | Availability | Category ID | Description")
            for p in get_all_products():
                print(f"   {p.id}    | {p.name} | {p.brand} | {p.price} | {p.availability} | {p.category_id} | {p.description}")

        elif product_option == 3:
            product_name = click.prompt("Enter Product Name")
            delete_product(product_name)


    elif user_input == 5:
        customer_option = show_menu("Customers", customer_menu)
        if customer_option == 1:
            first_name = click.prompt("Enter first name")
            last_name = click.prompt("Enter last name")
            email = click.prompt("Enter email")
            phone = click.prompt("Enter phone number(Optional)")
            address = click.prompt("Enter Address(Optional)")
            add_customer(first_name, last_name, email, phone, address)

        elif customer_option == 2:
            print("Customer ID | First Name | Last Name | Email | Phone | Address")
            for c in get_customers():
                print(f"    {c.id}     | {c.first_name} | {c.last_name} | {c.email} | {c.phone} | {c.address}")

        elif customer_option == 3:
            customer_first_name = click.prompt("Enter Customer's First Name")
            delete_customer(customer_first_name)


    elif user_input == 6:
        order_option = show_menu("Orders", order_menu)
        if order_option == 1:
            customer_id = click.prompt("Enter Customer ID")
            order_datetime = click.prompt("Enter Order Date (YYYY-MM-DD)", type=click.DateTime(formats=['%Y-%m-%d']))
            order_date = order_datetime.date()
            add_order(customer_id, order_date, order_status="Not Delivered")

        elif order_option == 2:
            print("Order ID | Customer ID |  Order Date  | Order Status")
            for o in get_orders():
                print(f"    {o.id}    | {o.customer_id} | {o.order_date} | {o.order_status}")

        elif order_option == 3:
            order_id = click.prompt("Enter Order ID")
            delete_order(order_id)

        elif order_option == 4:
            order_id = click.prompt("Enter Order ID")
            update_order_status(order_id, "Delivered")


    elif user_input == 7:
        item_option = show_menu("Order Items", order_item_menu)
        if item_option == 1:
            order_id = click.prompt("Enter Order ID")
            product_id = click.prompt("Enter Product ID")
            quantity = click.prompt("Enter quantity")
            add_order_item(order_id, product_id, quantity)

        elif item_option == 2:
            print("Order Item ID | Order ID | Product ID | Quantity")
            for oi in get_order_items():
                print(f"        {oi.id}         | {oi.order_id} | {oi.product_id} | {oi.quantity}")

        elif item_option == 3:
            item_id = click.prompt("Enter Order Item ID")
            delete_order_item(item_id)
